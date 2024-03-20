<div align="center">

[![Visit Sync. labs](./header.png)](https://synclabs.so)

# Sync. labs<a id="sync-labs"></a>

Synchronize API allows you to lipsync a video to any audio in any language.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`synclabs.animate.animate`](#synclabsanimateanimate)
  * [`synclabs.animate.animate_cost`](#synclabsanimateanimate_cost)
  * [`synclabs.animate.get_animation`](#synclabsanimateget_animation)
  * [`synclabs.lipsync.get_lipsync`](#synclabslipsyncget_lipsync)
  * [`synclabs.lipsync.lip_sync`](#synclabslipsynclip_sync)
  * [`synclabs.lipsync.lipsync_cost`](#synclabslipsynclipsync_cost)
  * [`synclabs.speak.get_speech`](#synclabsspeakget_speech)
  * [`synclabs.speak.speak`](#synclabsspeakspeak)
  * [`synclabs.speak.speak_cost`](#synclabsspeakspeak_cost)
  * [`synclabs.translate.get_translation`](#synclabstranslateget_translation)
  * [`synclabs.translate.translate`](#synclabstranslatetranslate)
  * [`synclabs.translate.translation_cost`](#synclabstranslatetranslation_cost)
  * [`synclabs.video.cost`](#synclabsvideocost)
  * [`synclabs.video.get_lip_sync_job`](#synclabsvideoget_lip_sync_job)
  * [`synclabs.video.lip_sync`](#synclabsvideolip_sync)
  * [`synclabs.voices.voices`](#synclabsvoicesvoices)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=sync.%20labs&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from sync_labs_python_sdk import SyncLabs, ApiException

synclabs = SyncLabs(
    api_key="YOUR_API_KEY",
)

try:
    animate_response = synclabs.animate.animate(
        video_url="string_example",
        transcript="string_example",
        voice_id="string_example",
        model="sync-1.5.0",
        max_credits=3.14,
        webhook_url="string_example",
    )
    print(animate_response)
except ApiException as e:
    print("Exception when calling AnimateApi.animate: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from sync_labs_python_sdk import SyncLabs, ApiException

synclabs = SyncLabs(
    api_key="YOUR_API_KEY",
)


async def main():
    try:
        animate_response = await synclabs.animate.aanimate(
            video_url="string_example",
            transcript="string_example",
            voice_id="string_example",
            model="sync-1.5.0",
            max_credits=3.14,
            webhook_url="string_example",
        )
        print(animate_response)
    except ApiException as e:
        print("Exception when calling AnimateApi.animate: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from sync_labs_python_sdk import SyncLabs, ApiException

synclabs = SyncLabs(
    api_key="YOUR_API_KEY",
)

try:
    animate_response = synclabs.animate.raw.animate(
        video_url="string_example",
        transcript="string_example",
        voice_id="string_example",
        model="sync-1.5.0",
        max_credits=3.14,
        webhook_url="string_example",
    )
    pprint(animate_response.body)
    pprint(animate_response.body["id"])
    pprint(animate_response.body["transcript_url"])
    pprint(animate_response.body["status"])
    pprint(animate_response.body["video_url"])
    pprint(animate_response.body["audio_url"])
    pprint(animate_response.headers)
    pprint(animate_response.status)
    pprint(animate_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AnimateApi.animate: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `synclabs.animate.animate`<a id="synclabsanimateanimate"></a>

Generates audio given inputted text and voice and synchronizes with the given video.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
animate_response = synclabs.animate.animate(
    video_url="string_example",
    transcript="string_example",
    voice_id="string_example",
    model="sync-1.5.0",
    max_credits=3.14,
    webhook_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_url: `str`<a id="video_url-str"></a>

A url to the video file to be synchronized -- must be publicly accessible

##### transcript: `str`<a id="transcript-str"></a>

A string of text to be spoken by the AI

##### voice_id: `str`<a id="voice_id-str"></a>

The voice to use for audio generation

##### model: `str`<a id="model-str"></a>

The model to use for video generation

##### max_credits: `Union[int, float]`<a id="max_credits-unionint-float"></a>

Maximum number of credits to use for audio generation. If job exceeds this value, the job will be aborted

##### webhook_url: `str`<a id="webhook_url-str"></a>

A url to send a notification to upon completion of audio generation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AnimateDto`](./sync_labs_python_sdk/type/animate_dto.py)
Required data for animating video. Includes video URL, transcript, voice, and optional parameters for webhook integration and credit limits.

#### 🔄 Return<a id="🔄-return"></a>

[`AnimateInitial`](./sync_labs_python_sdk/pydantic/animate_initial.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/animate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.animate.animate_cost`<a id="synclabsanimateanimate_cost"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synclabs.animate.animate_cost(
    transcript="string_example",
    transcript_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transcript: `str`<a id="transcript-str"></a>

A string of text to be spoken by the AI

##### transcript_url: `str`<a id="transcript_url-str"></a>

A url pointing to a file of text to be spoken by the AI

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/animate/cost` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.animate.get_animation`<a id="synclabsanimateget_animation"></a>

Use the ID from the POST request to check status. Keep checking until status is 'completed' and a download URL is provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_animation_response = synclabs.animate.get_animation(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AnimateExtended`](./sync_labs_python_sdk/pydantic/animate_extended.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/animate/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.lipsync.get_lipsync`<a id="synclabslipsyncget_lipsync"></a>

Use the video ID from the POST request to check video status. Keep checking until status is 'completed' and a download URL is provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_lipsync_response = synclabs.lipsync.get_lipsync(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`LipSyncExtended`](./sync_labs_python_sdk/pydantic/lip_sync_extended.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lipsync/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.lipsync.lip_sync`<a id="synclabslipsynclip_sync"></a>

Submit a set of urls to publically hosted audio and video files or to YouTube videos. Our synchronizer will sync the video's lip movements to match the audio and return the synced video.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lip_sync_response = synclabs.lipsync.lip_sync(
    audio_url="string_example",
    video_url="string_example",
    synergize=True,
    max_credits=3.14,
    webhook_url="string_example",
    model="sync-1.5.0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audio_url: `str`<a id="audio_url-str"></a>

A url to the audio file to be synchronized -- must be publicly accessible

##### video_url: `str`<a id="video_url-str"></a>

A url to the video file to be synchronized -- must be publicly accessible

##### synergize: `bool`<a id="synergize-bool"></a>

A flag to enable / disable post-processing

##### max_credits: `Union[int, float]`<a id="max_credits-unionint-float"></a>

Maximum number of credits to use for video generation. If job exceeds this value, the job will be aborted

##### webhook_url: `str`<a id="webhook_url-str"></a>

A url to send a notification to upon completion of video generation

##### model: `str`<a id="model-str"></a>

The model to use for video generation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LipsyncDto`](./sync_labs_python_sdk/type/lipsync_dto.py)
The audio + video data to be synced. Set synergize = false to skip our synergizer post-processor for a 10x speedup, but w/ a degredation in output quality.

#### 🔄 Return<a id="🔄-return"></a>

[`LipSyncInitial`](./sync_labs_python_sdk/pydantic/lip_sync_initial.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lipsync` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.lipsync.lipsync_cost`<a id="synclabslipsynclipsync_cost"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synclabs.lipsync.lipsync_cost(
    audio_url="audioUrl_example",
    video_url="videoUrl_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audio_url: `str`<a id="audio_url-str"></a>

A url to the audio file to be synchronized -- must be publicly accessible

##### video_url: `str`<a id="video_url-str"></a>

A url to the video file to be synchronized -- must be publicly accessible

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lipsync/cost` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.speak.get_speech`<a id="synclabsspeakget_speech"></a>

Use the video ID from the POST request to check video status. Keep checking until status is 'completed' and a download URL is provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_speech_response = synclabs.speak.get_speech(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SpeakExtended`](./sync_labs_python_sdk/pydantic/speak_extended.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/speak/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.speak.speak`<a id="synclabsspeakspeak"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
speak_response = synclabs.speak.speak(
    transcript="string_example",
    voice_id="string_example",
    max_credits=3.14,
    webhook_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transcript: `str`<a id="transcript-str"></a>

A string of text to be spoken by the AI

##### voice_id: `str`<a id="voice_id-str"></a>

The voice to use for audio generation

##### max_credits: `Union[int, float]`<a id="max_credits-unionint-float"></a>

Maximum number of credits to use for audio generation. If job exceeds this value, the job will be aborted

##### webhook_url: `str`<a id="webhook_url-str"></a>

A url to send a notification to upon completion of audio generation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SpeakDto`](./sync_labs_python_sdk/type/speak_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SpeakInitial`](./sync_labs_python_sdk/pydantic/speak_initial.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/speak` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.speak.speak_cost`<a id="synclabsspeakspeak_cost"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synclabs.speak.speak_cost(
    transcript="string_example",
    transcript_url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transcript: `str`<a id="transcript-str"></a>

A string of text to be spoken by the AI

##### transcript_url: `str`<a id="transcript_url-str"></a>

A url pointing to a file of text to be spoken by the AI

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/speak/cost` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.translate.get_translation`<a id="synclabstranslateget_translation"></a>

Use the video ID from the POST request to check video status. Keep checking until status is 'completed' and a download URL is provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_translation_response = synclabs.translate.get_translation(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TranslationJobExtended`](./sync_labs_python_sdk/pydantic/translation_job_extended.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/translate/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.translate.translate`<a id="synclabstranslatetranslate"></a>

Translates and synchronizes the given video to the specified target language.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
translate_response = synclabs.translate.translate(
    video_url="string_example",
    target_language="string_example",
    max_credits=3.14,
    webhook_url="string_example",
    model="sync-1.5.0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_url: `str`<a id="video_url-str"></a>

A url to the video file to be translated and synchronized -- must be publicly accessible

##### target_language: `str`<a id="target_language-str"></a>

Target language to translate the video to

##### max_credits: `Union[int, float]`<a id="max_credits-unionint-float"></a>

Maximum number of credits to use for video generation. If job exceeds this value, the job will be aborted

##### webhook_url: `str`<a id="webhook_url-str"></a>

A url to send a notification to upon completion of video generation

##### model: `str`<a id="model-str"></a>

The model to use for video generation.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TranslateDto`](./sync_labs_python_sdk/type/translate_dto.py)
Required data for translating and synchronizing video. Includes video URL, target language, and optional parameters for model selection, webhook integration, and credit limits.

#### 🔄 Return<a id="🔄-return"></a>

[`TranslationJobInitial`](./sync_labs_python_sdk/pydantic/translation_job_initial.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/translate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.translate.translation_cost`<a id="synclabstranslatetranslation_cost"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synclabs.translate.translation_cost(
    video_url="videoUrl_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### video_url: `str`<a id="video_url-str"></a>

A url to the video file to be synchronized -- must be publicly accessible

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/translate/cost` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.video.cost`<a id="synclabsvideocost"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synclabs.video.cost(
    audio_url="audioUrl_example",
    video_url="videoUrl_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audio_url: `str`<a id="audio_url-str"></a>

A url to the audio file to be synchronized -- must be publicly accessible

##### video_url: `str`<a id="video_url-str"></a>

A url to the video file to be synchronized -- must be publicly accessible

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/video/cost` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.video.get_lip_sync_job`<a id="synclabsvideoget_lip_sync_job"></a>

[Deprecated] Use the video ID from the POST request to check video status. Keep checking until status is 'completed' and a download URL is provided.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_lip_sync_job_response = synclabs.video.get_lip_sync_job(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`VideoExtended`](./sync_labs_python_sdk/pydantic/video_extended.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/video/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.video.lip_sync`<a id="synclabsvideolip_sync"></a>

[Deprecated] Submit a set of urls to publically hosted audio and video files or to YouTube videos. Our synchronizer will sync the video's lip movements to match the audio and return the synced video.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lip_sync_response = synclabs.video.lip_sync(
    audio_url="string_example",
    video_url="string_example",
    synergize=True,
    max_credits=3.14,
    webhook_url="string_example",
    model="sync-1.5.0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### audio_url: `str`<a id="audio_url-str"></a>

A url to the audio file to be synchronized -- must be publicly accessible

##### video_url: `str`<a id="video_url-str"></a>

A url to the video file to be synchronized -- must be publicly accessible

##### synergize: `bool`<a id="synergize-bool"></a>

A flag to enable / disable post-processing

##### max_credits: `Union[int, float]`<a id="max_credits-unionint-float"></a>

Maximum number of credits to use for video generation. If job exceeds this value, the job will be aborted

##### webhook_url: `str`<a id="webhook_url-str"></a>

A url to send a notification to upon completion of video generation

##### model: `str`<a id="model-str"></a>

The model to use for video generation

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateVideoDto`](./sync_labs_python_sdk/type/create_video_dto.py)
The audio + video data to be synced. Set synergize = false to skip our synergizer post-processor for a 10x speedup, but w/ a degredation in output quality.

#### 🔄 Return<a id="🔄-return"></a>

[`VideoInitial`](./sync_labs_python_sdk/pydantic/video_initial.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/video` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `synclabs.voices.voices`<a id="synclabsvoicesvoices"></a>

Get all voices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
synclabs.voices.voices()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/voices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
