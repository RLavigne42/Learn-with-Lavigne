# Flood-Tuber: The Lightweight OBS Avatar Solution

## Overview

Adding a dynamic visual presence to an audio-only input shouldn't come at the cost of your system's performance. While robust software like Adobe Character Animator is incredibly powerful, running a full physics and facial-tracking engine alongside your broadcast software often consumes excessive CPU overhead.

**Flood-Tuber** is an open-source, native OBS Studio plugin (`.dll`) that completely streamlines the digital avatar workflow. Operating entirely within OBS, it translates your microphone input into lip-syncing, blinking, and reactive movements with near-zero latency and no external desktop applications required.

## Core Benefits

* **Native Integration:** Bypasses the need for window-capturing external software. Everything is managed within the OBS source properties.
* **Massive CPU Savings:** Eliminates the background processing overhead of standalone 2D/3D avatar engines.
* **Instant Persona Swapping:** Build a native library of characters (e.g., Captain Diana Morrow, Louie, Rigel) and switch between them with a single click or hotkey, without loading new project files.
* **Animated Format Support:** Supports static PNGs as well as animated formats like GIF, APNG, and WebP for retaining fluid, pre-rendered motion.

---

## Phase 1: Asset Preparation & Folder Structure

Flood-Tuber relies on a strict file-naming convention to automatically trigger states based on your microphone input.

For each character or persona, create a dedicated folder. Inside that folder, your image files (PNG, GIF, or WebP) must be named exactly as follows:

* `idle` *(Required)*: The baseline, quiet state (mouth closed).
* `talk_a` *(Required)*: The primary speaking state (mouth open).
* `talk_b` & `talk_c` *(Optional)*: Secondary speaking frames. If included, the plugin cycles through them for smoother mouth movement.
* `blink` *(Optional)*: A frame with the avatar's eyes closed, utilized by the auto-blink engine.
* `action` *(Optional)*: A random emote or pose that triggers automatically during silences to keep the avatar feeling alive.

*Example Directory:*

```text
/Avatars/
  ├── /Louie/
  │    ├── idle.png
  │    ├── talk_a.png
  │    └── blink.png
  └── /Rigel/
       ├── idle.gif
       ├── talk_a.gif
       └── settings.ini

```

---

## Phase 2: Installation & Setup Guide

### 1. Install the Plugin

1. Navigate to the official [justflood/flood-tuber GitHub Releases page](https://github.com/justflood/flood-tuber/releases).
2. Download the latest `FloodTuber-Installer.exe`.
3. Run the installer. *(Note: Windows SmartScreen may flag it as an "Unknown Publisher." Click **More Info** -> **Run Anyway**).*
4. Follow the setup wizard to install the files directly into your OBS directory, then restart OBS Studio.

### 2. Build Your Library in OBS

1. In your OBS Scene, click the **+** button under the **Sources** dock and select **Flood Tuber Avatar**.
2. Name the source (e.g., "Active Persona") and click **OK**.
3. In the plugin properties window, click the **Open Library Folder** button.
4. Drag and drop your prepared character folders directly into this newly opened directory.

### 3. Route Audio and Apply

1. Back in the OBS properties window for your Flood-Tuber source, locate the **Audio Source** dropdown and select your active microphone.
2. Under the **Avatar Library** dropdown, select your desired character's folder.
3. Click **Load & Apply Avatar**. Your baseline `idle` image will appear on the canvas.

### 4. Fine-Tune the Reaction

* **Audio Threshold:** Speak into your microphone at a normal volume. Adjust the **Threshold** slider until the avatar only triggers the talking frames when you speak, ensuring it ignores background noise or keyboard clicks.
* **Motion Effects:** Use the **Motion Type** dropdown to apply a built-in **Shake** or **Bounce** effect. This forces the avatar to physically react to your voice volume, adding weight and energy.

---

## Phase 3: Advanced Customization (`settings.ini`)

You can assign unique physics and blink rates to individual avatars by placing a text file named `settings.ini` inside their specific character folder. This allows one persona to have a hyperactive bounce while another remains completely static, bypassing the global OBS settings.

Create a standard text file, name it `settings.ini`, and configure the following parameters:

```ini
[Animation]
; All values are in milliseconds (1000ms = 1 second)
BlinkMin=2000
BlinkMax=5000
BlinkDuration=130
ActionInterval=15000

[Motion]
; Adjust physical reactions to audio input
BounceAmount=15
ShakeAmount=2
Threshold=-40.0

```

### Parameter Breakdown

* **`BlinkMin` / `BlinkMax`:** The avatar will blink randomly between these two timeframes.
* **`BlinkDuration`:** How long the eyes remain closed (150ms is a natural human blink).
* **`ActionInterval`:** How often the `action` frame triggers during silence.
* **`BounceAmount` / `ShakeAmount`:** The intensity of the vertical jump or horizontal vibration when the audio threshold is crossed. Set to `0` to disable.
* **`Threshold`:** The specific audio gate (in dB) required to trigger this specific character's talking animation.

*(Note: If you edit the `settings.ini` file while OBS is open, you must switch to a different avatar and back, or restart OBS, for the new values to take effect).*

---
