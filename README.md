# Home Assistant - Door and window integration __(work in progress...)__

<!--
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)--> 
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/laszlojakab/homeassistant-door-and-window?include_prereleases) ![GitHub](https://img.shields.io/github/license/laszlojakab/homeassistant-door-and-window?)
![GitHub all releases](https://img.shields.io/github/downloads/laszlojakab/homeassistant-door-and-window/total) [![HA integration usage](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=integration%20usage&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.door_and_window.total)](https://analytics.home-assistant.io/custom_integrations.json) [![codecov](https://codecov.io/gh/laszlojakab/homeassistant-door-and-window/branch/develop/graph/badge.svg?token=WG3NJGR2XM)](https://codecov.io/gh/laszlojakab/homeassistant-door-and-window) [![Donate](https://img.shields.io/badge/donate-Coffee-yellow.svg)](https://www.buymeacoffee.com/laszlojakab)

-----

With the integration you can create devices for your doors or windows in [Home Assistant](https://www.home-assistant.io/).

## Installation

You can install this integration <!--via [HACS](#hacs) or -->[manually](#manual).

<!--### HACS installation

This integration is included in HACS. Search for the `Door and window` integration and choose install. Reboot Home Assistant and configure the 'Door and window' integration via the integrations page or press the blue button below.

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=door_and_window)-->

### Manual installation

Copy the `custom_components/door_and_window` to your `custom_components` folder. Reboot Home Assistant and configure the 'Door and window' integration via the integrations page or press the blue button below.

## Features
The integration adds some static diagnostic sensors (door and window dimensions, orientation, etc..) and some dynamically changing diagnostic sensors:

- __angle of incidence__: the angle between the direct sun ray incident on the glazing and the line perpendicular to the glazing at the point of incidence
- __sunny glazing area__: the area of the glazing covered by direct sunlight
- __sunny glazing area percentage__: the percentage of the glazing area receives sunlight.

Beside the diagnostic sensors it also adds some more useful sensors to Home Assistant:

- __glazing has direct sunlight__: the binary sensor shows if the window glazing receives direct sunlight

## ___Important notes___
_The integration is work in progress so adding breaking changes to the integration could happen anytime! Use it at your own risk!_ 