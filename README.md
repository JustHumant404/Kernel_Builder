# Generic Kernel Image Manual

> Please read this manual carefully and use it with guidance from Google.

**【Kernel Name】**

    Common Name: Generic Kernel Image
    English Name: Generic Kernel Image
    Chinese Pinyin: Tongyong Neihe Yingxiang

**【Components】**

https://kernel.org/

https://kernelsu.org/

**【Form】**

This product is a compressed archive within another archive file. SHA256 checksum is noted beside the download link.

**【Supported Devices】**

Phones compatible with GKI.

**【Adverse Reactions】**

    Common: overheating
    Occasional: system crashes
    Rare: device bricking

**【Precautions】**

This kernel’s security patch level is based on the latest KernelSU workflow settings.

Before installing this kernel, make sure to boot once into the official or 5ec1cff version of KernelSU. After entering the system, open the KernelSU Manager, go to settings, and **disable global umount**. This is to prevent susfs’s handling of umount from affecting system apps. Possible symptoms include but are not limited to：

- Black screen after boot (SystemUI fails to load)
- Wi-Fi inaccessible
- Baseband-related communications unavailable

**【Pharmacokinetics (Kinetics of the Kernel)】**

Kinetics of the Generic Kernel Image have been studied on Pixel 8. It can boot successfully.

> **Software Interaction**
>
> Material Cleaner: When used together with SUSFS, there are interactions in both kinetics and dynamics. After SUSFS was released, users reported that using Material Cleaner caused the “umount app” to show 0B of free space. Additionally, side effects included WeChat Mini Programs failing to launch.

**【Storage】**

No specific condition required.

**【Packaging】**

Archive file.
