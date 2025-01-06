# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

import base64
import mimetypes
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

@dataclass
class ByteStream:
    """
    Represents a binary data stream with its associated MIME type.
    Used for handling multimedia content like images, audio files, and PDFs.

    :param data: The binary data as bytes
    :param mime_type: The MIME type of the data (e.g., 'image/jpeg', 'audio/mp3', 'application/pdf')
    """
    data: bytes
    mime_type: str

    @classmethod
    def from_file(cls, file_path: Union[str, Path]) -> "ByteStream":
        """
        Create a ByteStream from a file path. The MIME type is automatically detected.

        :param file_path: Path to the file
        :returns: A new ByteStream instance
        """
        path = Path(file_path)
        mime_type = mimetypes.guess_type(path)[0]
        if mime_type is None:
            raise ValueError(f"Could not determine MIME type for file: {file_path}")

        with open(path, "rb") as f:
            data = f.read()
        return cls(data=data, mime_type=mime_type)

    def to_base64(self) -> str:
        """
        Convert the binary data to a base64 encoded string.

        :returns: Base64 encoded string
        """
        return base64.b64encode(self.data).decode("utf-8")

    @classmethod
    def from_base64(cls, base64_str: str, mime_type: str) -> "ByteStream":
        """
        Create a ByteStream from a base64 encoded string.

        :param base64_str: The base64 encoded data
        :param mime_type: The MIME type of the data
        :returns: A new ByteStream instance
        """
        data = base64.b64decode(base64_str)
        return cls(data=data, mime_type=mime_type)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ByteStream):
            return NotImplemented
        return self.data == other.data and self.mime_type == other.mime_type