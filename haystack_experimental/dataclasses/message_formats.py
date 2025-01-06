# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

from typing import Any, Dict, List

from .chat_message import ChatMessage, ChatRole, MediaContent, TextContent


def message_to_openai_format(message: ChatMessage) -> Dict[str, Any]:
    """
    Convert a ChatMessage to OpenAI's format.

    :param message: The ChatMessage to convert
    :returns: A dictionary in OpenAI's message format
    """
    result = {"role": message.role.value}
    
    # Handle multimodal content
    content: List[Any] = []
    
    for part in message._content:
        if isinstance(part, TextContent):
            if len(message._content) == 1:
                # If only text, use string format
                return {"role": message.role.value, "content": part.text}
            content.append({"type": "text", "text": part.text})
        elif isinstance(part, MediaContent):
            content.append({
                "type": "image" if part.data.mime_type.startswith("image/") else "file",
                "media_type": part.data.mime_type,
                "data": part.data.to_base64()
            })
    
    if content:
        result["content"] = content
    
    # Include any tool calls from assistant
    if message.is_from(ChatRole.ASSISTANT) and message.tool_calls:
        result["tool_calls"] = [
            {
                "id": call.id,
                "type": "function",
                "function": {
                    "name": call.tool_name,
                    "arguments": call.arguments
                }
            }
            for call in message.tool_calls
        ]
    
    # Include tool results
    if message.is_from(ChatRole.TOOL):
        result["tool_call_id"] = message.tool_call_result.origin.id
    
    return result


def message_to_anthropic_format(message: ChatMessage) -> str:
    """
    Convert a ChatMessage to Anthropic's format.

    :param message: The ChatMessage to convert
    :returns: A string in Anthropic's message format
    """
    role_map = {
        ChatRole.USER: "Human",
        ChatRole.ASSISTANT: "Assistant",
        ChatRole.SYSTEM: "System",
    }
    
    if message.is_from(ChatRole.TOOL):
        raise ValueError("Anthropic format does not support tool messages")
    
    parts = []
    for part in message._content:
        if isinstance(part, TextContent):
            parts.append(part.text)
        elif isinstance(part, MediaContent):
            if part.data.mime_type.startswith("image/"):
                parts.append(f"<image>{part.data.to_base64()}</image>")
            else:
                # Currently Anthropic only supports images
                raise ValueError(
                    f"Anthropic format does not support media type: {part.data.mime_type}"
                )
    
    content = "\n".join(parts)
    return f"{role_map[message.role]}: {content}"