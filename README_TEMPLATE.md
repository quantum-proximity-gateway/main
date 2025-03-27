# IBM+UCL - Quantum Proximity Gateway

This is a container github repository that links to all the other necessary repos required to setup and run this project in its entirety. Since we created a github org for this project, we had multiple repos, but we figured that creating a single access point which links to all of the other repos would be more convenient for everyone.

<details>
  <summary><strong>Table of Contents</strong></summary>

- [Summary](#summary)
- [Setup/Installation](#setupinstallation)
- [Server](#server)
  - [Purpose](#purpose)
  - [Setup](#setup)
  - [README](#readme)
- [Registration Website](#registration-website)
  - [Purpose](#purpose-1)
  - [Setup](#setup-1)
  - [README](#readme-1)
- [ESP32 Code](#esp32-code)
  - [Purpose](#purpose-2)
  - [Setup](#setup-2)
  - [README](#readme-2)
- [Raspberry Pi Code](#raspberry-pi-code)
  - [Purpose](#purpose-3)
  - [Setup](#setup-3)
  - [README](#readme-3)
- [Desktop Application](#desktop-application)
  - [Purpose](#purpose-4)
  - [Setup](#setup-4)
  - [README](#readme-4)
- [Contributors](#contributors)

</details>

## Summary

The goal of this project was to be able to walk up to any hot-desking computer and, simply by being near the computer, automatically get logged in and have your profile preferences loaded up onto the device. In the end, this project ended up combining a wide variety of functionalities together, from Bluetooth Low Energy signals for communication between an ESP32 and a Raspberry Pi, to USB HID keyboard simulation with a Raspberry Pi Pico, as well as using an LLM such as IBM Granite to seamlessly allow the user to let the computer know which preferences need to be changes (and saved), amongst other technologies.

This README file will cover what each of the 5 main parts of the project generally are for, as well as how to set them up (they will have links to the READMEs in their respective repos, but also collapsible copies of those READMEs).

## Setup/Installation

Since all of the submodules in this project have different requirements, we have decided to write what are essentially separate READMEs for each of them (each of which can be accessed from this file itself).

Below is the command to clone this entire repository (and its submodules) together. However, note that some of the repositories (such as the `rpi-code` repo) need to be cloned and used on a different hardware device (i.e. the Raspberry Pi 5).

To clone all of the code for this project, run the following command:

```bash
git clone --recurse-submodules https://github.com/quantum-proximity-gateway/main.git
```

## Server

### Purpose

The server is where we handle all of the requests that the other components of the project make, as well as store our data. In our case, this means handling how to register an ESP32 device with a user (and their account details), as well as storing a user's accessibility preferences which can be retrieved. This also handles the majority of the encryption aspect of the project, ensuring that we use a quantum-secure encryption standard such as [CRYSTALS-Kyber](https://pq-crystals.org/kyber/).

### Setup

The server has already been deployed and is currently being hosted on IBM Cloud, but if you want to run it locally anyways, refer to [server/README.md](server/README.md) for more information.

Alternatively, you can open the following collapsible section to view the contents of this submodule's README. We do, however, recommend looking at the linked README instead, as this one can quickly get quite cluttered.

### README

<details>
    <summary><strong>Server README</strong></summary>

---

{{SERVER_README}}

---

</details>

## Registration Website

### Purpose

TODO

### Setup

TODO

### README

<details>
    <summary><strong>Registration Website README</strong></summary>

---

{{REGISTRATION_README}}

---

</details>

## ESP32 Code

### Purpose

TODO

### Setup

TODO

### README

<details>
    <summary><strong>ESP32 Code README</strong></summary>

---

{{ESP32_README}}

---

</details>

## Raspberry Pi Code

### Purpose

TODO

### Setup

TODO

### README

<details>
    <summary><strong>Raspberry Pi Code README</strong></summary>

---

{{RPI_README}}

---

</details>

## Desktop Application

### Purpose

TODO

### Setup

TODO

### README

<details>
    <summary><strong>Desktop Application README</strong></summary>

---

{{DESKTOP_README}}

---

</details>

## Contributors

- [Raghav Awasthi](https://github.com/raghav2005)
- [Marwan Yassini Chairi El Kamel](https://github.com/marwan141)
- [Abdulhamid Abayomi](https://github.com/248abdul)
- [Abdul Muhaymin Abdul Hafiz](https://github.com/abmu)
