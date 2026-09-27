#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


Stats = Dict[str, Union[str, int, float]]


class DataStream(ABC):
    """structural base"""
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self._stats: Stats = {"stream_id": stream_id}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Stats:
        return self._stats


class SensorStream(DataStream):
    """sensor stream methods"""
    def process_batch(self, data_batch: List[Any]) -> str:
        temp_vals: List[float] = []
        readings = 0

        for item in data_batch:
            if not isinstance(item, str) or ":" not in item:
                continue
            key, value = item.split(":", 1)
            readings += 1
            if key == "temp":
                try:
                    temp_vals.append(float(value))
                except ValueError:
                    pass

        avg_temp = (sum(temp_vals) / len(temp_vals)) if len(temp_vals) else 0.0
        self._stats = {
            "stream_id": self.stream_id,
            "type": "sensor",
            "readings": readings,
            "avg_temp": avg_temp,
        }
        return (f"Sensor analysis: \33[36m{readings}\33[37m readings processed"
                f", avg temp: \33[36m{avg_temp:.1f}\33[37m°C")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high":
            return [x for x in data_batch if isinstance(x, str)
                    and x.startswith("critical:")]
        return data_batch


class TransactionStream(DataStream):
    """transaction stream methods"""
    def process_batch(self, data_batch: List[Any]) -> str:
        # attend "buy:100" / "sell:150"
        ops = 0
        net = 0

        for item in data_batch:
            if not isinstance(item, str) or ":" not in item:
                continue
            op, value = item.split(":", 1)
            try:
                amount = int(value)
            except ValueError:
                continue

            ops += 1
            if op == "buy":
                net += amount
            elif op == "sell":
                net -= amount

        self._stats = {
            "stream_id": self.stream_id,
            "type": "transaction",
            "operations": ops,
            "net_flow": net,
        }
        sign = "+" if net >= 0 else "-"
        return (f"Transaction analysis: \33[36m{ops}\33[37m operations, net "
                f"flow: \33[36m{sign}{abs(net)}\33[37m units")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high":
            # "large transaction" = abs(amount) >= 1000
            out: List[str] = []
            for item in data_batch:
                if not isinstance(item, str) or ":" not in item:
                    continue
                _, value = item.split(":", 1)
                try:
                    amount = int(value)
                except ValueError:
                    continue
                if abs(amount) >= 1000:
                    out.append(item)
            return out
        return data_batch


class EventStream(DataStream):
    """event stream methods"""
    def process_batch(self, data_batch: List[Any]) -> str:
        events = [x for x in data_batch if isinstance(x, str)]
        errors = len([e for e in events if e == "error"])

        self._stats = {
            "stream_id": self.stream_id,
            "type": "event",
            "events": len(events),
            "errors": errors,
        }
        return (f"Event analysis: \33[36m{len(events)}\33[37m events, "
                f"\33[36m{errors}\33[37m error detected")

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "high":
            return [x for x in data_batch if isinstance(x, str)
                    and x == "error"]
        return data_batch


class StreamProcessor:
    """global processor methods"""
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_all(self, batches: List[List[Any]]) -> None:
        for stream, batch in zip(self.streams, batches):
            stream.process_batch(batch)

    def print_batch_results(self) -> None:
        sensor_readings = 0
        trans_ops = 0
        event_count = 0

        for stream in self.streams:
            stats = stream.get_stats()
            if stats.get("type") == "sensor":
                sensor_readings = int(stats.get("readings", 0))
            elif stats.get("type") == "transaction":
                trans_ops = int(stats.get("operations", 0))
            elif stats.get("type") == "event":
                event_count = int(stats.get("events", 0))

        print(f"- Sensor data: \33[36m{sensor_readings}\33[37m "
              "readings processed")
        print(f"- Transaction data: \33[36m{trans_ops}\33[37m operations "
              "processed")
        print(f"- Event data: \33[36m{event_count}\33[37m events processed")

    def filter_summary(self, sensor_batch: List[Any],
                       trans_batch: List[Any]) -> None:
        sensor_stream = None
        trans_stream = None
        for s in self.streams:
            stats = s.get_stats()
            if stats.get("type") == "sensor":
                sensor_stream = s
            elif stats.get("type") == "transaction":
                trans_stream = s
        if sensor_stream is None or trans_stream is None:
            print("Filtered results: \33[32m0\33[37m critical sensor alerts, "
                  "\33[32m0\33[37m large transaction")
            return
        critical = sensor_stream.filter_data(sensor_batch, "high")
        large = trans_stream.filter_data(trans_batch, "high")
        print(f"Filtered results: \33[36m{len(critical)}\33[37m critical "
              f"sensor alerts, \33[36m{len(large)}\33[37m large transaction")


def main() -> None:
    print("\n\33[1m=====\33[35m CODE NEXUS - "
          "POLYMORPHIC STREAM SYSTEM \33[37m=====")
    print("\nInitializing \33[35mSensor Stream\33[37m...")
    stream = "SENSOR_001"
    sensor = SensorStream(stream)
    print(f"Stream ID: \33[36m{stream}\33[37m, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))
    print("\nInitializing \33[35mTransaction Stream\33[37m...")
    stream = "TRANS_001"
    trans = TransactionStream(stream)
    print(f"Stream ID: \33[36m{stream}\33[37m, Type: Financial Data")
    print("Processing transaction batch: [buy:100, sell:150, buy:75]")
    print(trans.process_batch(["buy:100", "sell:150", "buy:75"]))
    print("\nInitializing \33[35mEvent Stream\33[37m...")
    stream = "EVENT_001"
    event = EventStream(stream)
    print(f"Stream ID: \33[36m{stream}\33[37m, Type: System Events")
    print("Processing event batch: [login, error, logout]")
    print(event.process_batch(["login", "error", "logout"]))
    print("\n===\33[35m Polymorphic Stream Processing \33[37m===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    processor = StreamProcessor([sensor, trans, event])
    batch_sensor = ["temp:20.0", "humidity:40"]
    batch_trans = ["buy:10", "sell:5", "buy:7", "sell:3"]
    batch_event = ["login", "error", "logout"]
    processor.process_all([batch_sensor, batch_trans, batch_event])
    processor.print_batch_results()
    print("\nStream filtering active: High-priority data only")
    sens_filter = ["critical:temp_high", "critical:pressure_drop", "temp:22.5"]
    trans_filter = ["buy:50", "sell:1200", "buy:75"]
    processor.filter_summary(sens_filter, trans_filter)
    print("\nAll streams processed \33[32msuccessfully\33[37m. "
          "Nexus throughput \33[32moptimal\33[37m.\n\33[0m")


if __name__ == "__main__":
    main()
