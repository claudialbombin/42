from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    """Common interface shared by every specialized data processor."""

    name: str = "Data Processor"

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._next_rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Return True if data can be ingested by this processor."""

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process data and store it, or raise if data is invalid."""

    def output(self) -> tuple[int, str]:
        """Remove and return the oldest stored (rank, value) pair."""
        return self._storage.pop(0)

    def _store(self, value: str) -> None:
        self._storage.append((self._next_rank, value))
        self._next_rank += 1

    @property
    def total_processed(self) -> int:
        return self._next_rank

    def __len__(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):
    """Ingests int, float, or lists mixing both."""

    name = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    """Ingests str or lists of str."""

    name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    """Ingests dict[str, str] log entries, or lists of them."""

    name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if self._is_log_entry(data):
            return True
        if isinstance(data, list):
            return all(self._is_log_entry(item) for item in data)
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        entries = data if isinstance(data, list) else [data]
        for entry in entries:
            level = entry.get("log_level", "")
            message = entry.get("log_message", "")
            self._store(f"{level}: {message}")

    @staticmethod
    def _is_log_entry(data: Any) -> bool:
        if not isinstance(data, dict):
            return False
        for key, value in data.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True


class ExportPlugin(Protocol):
    """Structural contract every export plugin must satisfy."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    """Exports a batch of (rank, value) pairs as one CSV line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    """Exports a batch of (rank, value) pairs as a JSON object."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = [f'"item_{rank}": "{value}"' for rank, value in data]
        print("JSON Output:")
        print("{" + ", ".join(pairs) + "}")


class DataStream:
    """Routes stream elements to processors, and their output to
    export plugins."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            self._dispatch(element)

    def _dispatch(self, element: Any) -> None:
        for proc in self._processors:
            if proc.validate(element):
                proc.ingest(element)
                return
        print(
            f"DataStream error - Can't process element in stream: "
            f"{element}"
        )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if len(proc) == 0:
                    break
                collected.append(proc.output())
            if collected:
                plugin.process_output(collected)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.name}: total {proc.total_processed} items "
                f"processed, remaining {len(proc)} on processor"
            )


def build_batch_one() -> list[Any]:
    return [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]


def build_batch_two() -> list[Any]:
    return [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    stream = DataStream()
    print("Initialize Data Stream...\n")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch = build_batch_one()
    print(f"\nSend first batch of data on stream: {batch}\n")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    batch = build_batch_two()
    print(f"\nSend another batch of data: {batch}\n")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
