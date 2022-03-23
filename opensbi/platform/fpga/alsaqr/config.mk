#
# SPDX-License-Identifier: BSD-2-Clause
#
# Copyright (C) 2019 FORTH-ICS/CARV
#		Panagiotis Peristerakis <perister@ics.forth.gr>
#

#for more infos, check out /platform/template/config.mk

PLATFORM_RISCV_XLEN = 64

# Blobs to build
FW_TEXT_START=0x80000000

FW_DYNAMIC = n

FW_JUMP=n


# Firmware with payload configuration.
FW_PAYLOAD=y
# This needs to be 2MB aligned for 64-bit support
FW_PAYLOAD_OFFSET=0x200000
# Let's put the dtb in the L3! 
FW_PAYLOAD_FDT_ADDR=0x82200000
FW_PAYLOAD_ALIGN=0x1000

