### Generate Linux Image

Use the forked [cva6-sdk](https://github.com/AlSaqr-platform/cva6). Generate the image and copy it in the opensbi folder.

Path to the Image is `cva6-sdk/buildroot/output/build/linux-v5.10.7/arch/riscv/boot/Image``

### Link against opensbi
```
make PLATFORM=fpga/alsaqr install

make PLATFORM=fpga/alsaqr FW_PAYLOAD_PATH=./Image

```