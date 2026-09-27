#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    """Abstract base class for all data processors"""

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: \33[36m{result}\33[37m"


class NumericProcessor(DataProcessor):
    """NumericProcessor class"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\33[31mInvalid numeric data\33[37m]")
        total = sum(data)
        avg = total / len(data)
        return (f"Processed \33[36m{len(data)}\33[37m numeric values, sum="
                f"\33[36m{total}\33[37m, avg=\33[36m{avg}\33[37m")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        for item in data:
            if not isinstance(item, (int, float)):
                return False
        return True


class TextProcessor(DataProcessor):
    """TextProcessor class"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\33[31mInvalid text data\33[37m")
        length = len(data)
        words = len(data.split())
        return (f"Processed text: \33[36m{length}\33[37m characters, "
                f"\33[36m{words}\33[37m words")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    """LogProcessor class"""
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("\33[31mInvalid log entry\33[37m")
        level, _, message = data.partition(": ")
        if level == "ERROR":
            title = "\33[31mALERT\33[37m"
        else:
            title = "\33[33mINFO\33[37m"
        return (f"[{title}] \33[36m{level}\33[37m level "
                f"detected: \33[36m{message}\33[37m")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return ":" in data


def main() -> None:
    print("\n\33[1m=====\33[35m CODE NEXUS - "
          "DATA PROCESSOR FOUNDATION \33[37m=====")
    print("\nInitializing\33[35m Numeric Processor\33[37m...")
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: \33[36m{num_data}\33[37m")
    num_valid = NumericProcessor().validate(num_data)
    if num_valid is True:
        num_valid_msg = "\33[32mverified\33[37m"
    else:
        num_valid_msg = "\33[31minvalid\33[37m"
    print("Validation: Numeric data "
          f"{num_valid_msg}")
    print(f"Output: {NumericProcessor().process(num_data)}")
    print("\nInitializing\33[35m Text Processor\33[37m...")
    txt_data = "Hello Nexus World"
    print(f"Processing data: \33[36m{txt_data}\33[37m")
    txt_valid = TextProcessor().validate(txt_data)
    if txt_valid is True:
        txt_valid_msg = "\33[32mverified\33[37m"
    else:
        txt_valid_msg = "\33[31minvalid\33[37m"
    print("Validation: Numeric data "
          f"{txt_valid_msg}")
    print(f"Output: {TextProcessor().process(txt_data)}")
    print("\nInitializing\33[35m Log Processor\33[37m...")
    log_data = "ERROR: Connection timeout"
    print(f"Processing data: \33[36m{log_data}\33[37m")
    log_valid = LogProcessor().validate(log_data)
    if log_valid is True:
        log_valid_msg = "\33[32mverified\33[37m"
    else:
        log_valid_msg = "\33[31minvalid\33[37m"
    print("Validation: Log entry "
          f"{log_valid_msg}")
    print(f"Output: {LogProcessor().process(log_data)}")
    print("\n===\33[35m Polymorphic Processing Demo \33[37m===")
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    samples = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]
    for i in range(len(processors)):
        try:
            result = processors[i].process(samples[i])
            print(f"Result \33[36m{i + 1}\33[37m: {result}")
        except Exception as e:
            print(f"Processing error: \33[31m{e}\33[37m")

    print("\nFoundation systems \33[32monline\33[37m. "
          "Nexus \33[32mready\33[37m for advanced streams.")
    print("\33[0m")


if __name__ == "__main__":
    main()
