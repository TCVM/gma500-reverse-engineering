# GMA500 Reverse Engineering Project

## Objetivo

Desarrollar un driver Linux moderno para la Intel GMA500 (PowerVR SGX545)
mediante ingeniería inversa del driver EMGD existente.

## Hardware objetivo

- **Máquina:** Coradir ES10IS5
- **GPU:** Intel GMA500 / PowerVR SGX545
- **CPU:** Intel Atom N2600 @ 1.60GHz
- **RAM:** 4GB DDR3
- **Kernel actual:** 3.13.0-24-generic (Ubuntu 14.04)

## Problema

El driver EMGD solo es compatible con Xserver ABI 8 y kernels hasta ~4.x.
El objetivo es portar la funcionalidad a kernels modernos (6.x+).

## Stack de trabajo

- Análisis estático: Ghidra
- Análisis dinámico: MMIO tracing
- Documentación: Este repo
- IA asistente: Ollama + Qwen (local) + Claude (decisiones complejas)

## Estado actual

- [x] Ubuntu 14.04 instalado con kernel 3.13
- [x] Módulo emgd.ko compilado y cargando
- [x] gma500_gfx blacklisteado
- [x] Xserver 1.9.5 compilado
- [ ] EMGD funcionando en Xorg
- [ ] Análisis con Ghidra iniciado
- [ ] Documentación de registros de hardware

## Links útiles

- [EMGD Community](https://github.com/EMGD-Community/intel-binaries-linux)
- [DRM subsystem docs](https://dri.freedesktop.org/docs/drm/)
