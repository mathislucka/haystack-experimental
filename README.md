[![PyPI - Version](https://img.shields.io/pypi/v/haystack-experimental.svg)](https://pypi.org/project/haystack-experimental)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/haystack-experimental.svg)](https://pypi.org/project/haystack-experimental)
[![Tests](https://github.com/deepset-ai/haystack-experimental/actions/workflows/tests.yml/badge.svg)](https://github.com/deepset-ai/haystack-experimental/actions/workflows/tests.yml)
[![Project release on PyPi](https://github.com/deepset-ai/haystack-experimental/actions/workflows/pypi_release.yml/badge.svg)](https://github.com/deepset-ai/haystack-experimental/actions/workflows/pypi_release.yml)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

# Haystack experimental package

The `haystack-experimental` package provides Haystack users with access to experimental features without immediately
committing to their official release. The main goal is to gather user feedback and iterate on new features quickly.

## Installation

For simplicity, every release of `haystack-experimental` will ship all the available experiments at that time. To
install the latest experimental features, run:

```sh
$ pip install -U haystack-experimental
```

> [!IMPORTANT]
> The latest version of the experimental package is only tested against the latest version of Haystack. Compatibility
> with older versions of Haystack is not guaranteed.

## Experiments lifecycle

Each experimental feature has a default lifespan of 3 months starting from the date of the first non-pre-release build
that includes it. Once it reaches the end of its lifespan, the experiment will be either:

- Merged into Haystack core and published in the next minor release, or
- Released as a Core Integration, or
- Dropped.

## Experiments catalog

### Active experiments

| Name                                                                                                                                                                                                                                                                                         | Type                                     | Expected End Date | Dependencies | Cookbook                                                                                                                                                                                                                                             | Discussion                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [`EvaluationHarness`][1]                                                                                                                                                                                                                                                                     | Evaluation orchestrator                  | October 2024      | None         | <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/rag_eval_harness.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>            | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/74)  |
| Support for Tools: [refactored `ChatMessage` dataclass][10], [`Tool` dataclass][4], [refactored `OpenAIChatGenerator`][11], [refactored `OllamaChatGenerator`][14], [refactored `HuggingFaceAPIChatGenerator`][15], [refactored `AnthropicChatGenerator`][16], [`ToolInvoker` component][12] | Tool Calling support                     | November 2024     | jsonschema   | <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/tools_support.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>                   | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/98)  |
| [`ChatMessageWriter`][5]                                                                                                                                                                                                                                                                     | Memory Component                         | December 2024     | None         | <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/conversational_rag_using_memory.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/75)  |
| [`ChatMessageRetriever`][6]                                                                                                                                                                                                                                                                  | Memory Component                         | December 2024     | None         | <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/conversational_rag_using_memory.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/75)  |
| [`InMemoryChatMessageStore`][7]                                                                                                                                                                                                                                                              | Memory Store                             | December 2024     | None         | <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/conversational_rag_using_memory.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/> | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/75)  |
| [`Auto-Merging Retriever`][8] & [`HierarchicalDocumentSplitter`][9]                                                                                                                                                                                                                          | Document Splitting & Retrieval Technique | December 2024     | None         | <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/auto_merging_retriever.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>          | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/78)  |
| [`LLMMetadataExtractor`][13]                                                                                                                                                                                                                                                                 | Metadata extraction with LLM             | December 2024     | None         | 🔜                                                                                                                                                                                                                                                   | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/130) |
| [`AsyncPipeline`][17]                                                                                                                                                                                                                                                                 | Async Pipeline & Components | February 2024     | None         | <a href="https://colab.research.google.com/github/deepset-ai/haystack-experimental/blob/main/examples/async_pipeline.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>                                                                                                                                                                                                                                                   | [Discuss](https://github.com/deepset-ai/haystack-experimental/discussions/152) |

[1]: https://github.com/deepset-ai/haystack-experimental/tree/main/haystack_experimental/evaluation/harness
[2]: https://github.com/deepset-ai/haystack-experimental/tree/fe20b69b31243f8a3976e4661d9aa8c88a2847d2/haystack_experimental/components/tools/openai
[3]: https://github.com/deepset-ai/haystack-experimental/tree/fe20b69b31243f8a3976e4661d9aa8c88a2847d2/haystack_experimental/components/tools/openapi
[4]: https://github.com/deepset-ai/haystack-experimental/tree/main/haystack_experimental/dataclasses/tool.py
[5]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/writers/chat_message_writer.py
[6]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/retrievers/chat_message_retriever.py
[7]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/chat_message_stores/in_memory.py
[8]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/retrievers/auto_merging_retriever.py
[9]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/splitters/hierarchical_doc_splitter.py
[10]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/dataclasses/chat_message.py
[11]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/generators/chat/openai.py
[12]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/tools/tool_invoker.py
[13]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/extractors/llm_metadata_extractor.py
[14]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/generators/ollama/chat/chat_generator.py
[15]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/generators/chat/hugging_face_api.py
[16]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/components/generators/anthropic/chat/chat_generator.py
[17]: https://github.com/deepset-ai/haystack-experimental/blob/main/haystack_experimental/core/pipeline/async_pipeline.py

### Discontinued experiments

| Name                        | Type                       | Final release | Cookbook                                                                                                                                 |
| --------------------------- | -------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [`OpenAIFunctionCaller`][2] | Function Calling Component | 0.3.0         | None                                                                                                                                     |
| [`OpenAPITool`][3]          | OpenAPITool component      | 0.3.0         | [Notebook](https://github.com/deepset-ai/haystack-experimental/blob/fe20b69b31243f8a3976e4661d9aa8c88a2847d2/examples/openapitool.ipynb) |

## Usage

Experimental new features can be imported like any other Haystack integration package:

```python
from haystack.dataclasses import ChatMessage
from haystack_experimental.components.generators import FoobarGenerator

c = FoobarGenerator()
c.run([ChatMessage.from_user("What's an experiment? Be brief.")])
```

Experiments can also override existing Haystack features. For example, users can opt into an experimental type of
`Pipeline` by just changing the usual import:

```python
# from haystack import Pipeline
from haystack_experimental import Pipeline

pipe = Pipeline()
# ...
pipe.run(...)
```

Some experimental features come with example notebooks and resources that can be found in the [`examples` folder](https://github.com/deepset-ai/haystack-experimental/tree/main/examples).

## Documentation

Documentation for `haystack-experimental` can be found [here](https://docs.haystack.deepset.ai/reference/experimental-data-classes-api).

## Implementation

Experiments should replicate the namespace of the core package. For example, a new generator:

```python
# in haystack_experimental/components/generators/foobar.py

from haystack import component


@component
class FoobarGenerator:
    ...

```

When the experiment overrides an existing feature, the new symbol should be created at the same path in the experimental
package. This new symbol will override the original in `haystack-ai`: for classes, with a subclass and for bare
functions, with a wrapper. For example:

```python
# in haystack_experiment/src/haystack_experiment/core/pipeline/pipeline.py

from haystack.core.pipeline import Pipeline as HaystackPipeline


class Pipeline(HaystackPipeline):
    # Any new experimental method that doesn't exist in the original class
    def run_async(self, inputs) -> Dict[str, Dict[str, Any]]:
        ...

    # Existing methods with breaking changes to their signature, like adding a new mandatory param
    def to_dict(new_param: str) -> Dict[str, Any]:
        # do something with the new parameter
        print(new_param)
        # call the original method
        return super().to_dict()

```

## Contributing

Direct contributions to `haystack-experimental` are not expected, but Haystack maintainers might ask contributors to move pull requests that target the [core repository](https://github.com/deepset-ai/haystack) to this repository.

## Telemetry

As with the Haystack core package, we rely on anonymous usage statistics to determine the impact and usefulness of the experimental features. For more information on what we collect and how we use the data, as well as instructions to opt-out, please refer to our [documentation](https://docs.haystack.deepset.ai/docs/telemetry).
