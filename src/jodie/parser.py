import struct
import typing

from jodie.version import Version
from jodie.constant_pool import *
from jodie.structures import *


# u8 in jezebel
U1 = struct.Struct(">B")
# u16 in jezebel code
U2 = struct.Struct(">H")
U2Pair = struct.Struct(">2H")
# u32 in jezebel code
U4 = struct.Struct(">I")
U4Pair = struct.Struct(">2I")

U1U2 = struct.Struct(">BH")


def parse_magic(cf: typing.BinaryIO) -> None:
    header = cf.read(4)
    if header != b'\xca\xfe\xba\xbe':
        raise ValueError("Expected magic header")


def parse_version(cf: typing.BinaryIO) -> Version:
    version_info = cf.read(4)
    minor, major = struct.unpack(">HH", version_info)
    return Version(major=major, minor=minor)


def parse_pool_class_info(cf: typing.BinaryIO) -> ClassInfo:
    byts = cf.read(2)
    name_index, = U2.unpack(byts)
    return ClassInfo(name_index=name_index)


def parse_pool_fieldref_info(cf: typing.BinaryIO) -> FieldRefInfo:
    byts = cf.read(4)
    class_index, name_and_type_index = U2Pair.unpack(byts)
    return FieldRefInfo(
        class_index=class_index,
        name_and_type_index=name_and_type_index
    )


def parse_pool_methodref_info(cf: typing.BinaryIO) -> MethodRefInfo:
    byts = cf.read(4)
    class_index, name_and_type_index = U2Pair.unpack(byts)
    return MethodRefInfo(
        class_index=class_index,
        name_and_type_index=name_and_type_index
    )


def parse_pool_interfacemethodref_info(cf: typing.BinaryIO) -> InterfaceMethodRefInfo:
    byts = cf.read(4)
    class_index, name_and_type_index = U2Pair.unpack(byts)
    return InterfaceMethodRefInfo(
        class_index=class_index,
        name_and_type_index=name_and_type_index
    )


def parse_pool_string_info(cf: typing.BinaryIO) -> StringInfo:
    byts = cf.read(2)
    string_index, = U2.unpack(byts)
    return StringInfo(string_index=string_index)


def parse_pool_integer_info(cf: typing.BinaryIO) -> IntegerInfo:
    byts = cf.read(4)
    bytes = U4.unpack(byts)
    return IntegerInfo(bytes=bytes)


def parse_pool_float_info(cf: typing.BinaryIO) -> FloatInfo:
    byts = cf.read(4)
    bytes = U4.unpack(byts)
    return FloatInfo(bytes=bytes)


def parse_pool_long_info(cf: typing.BinaryIO) -> LongInfo:
    byts = cf.read(8)
    high_bytes, low_bytes = U4Pair.unpack(byts)
    return LongInfo(
        high_bytes=high_bytes,
        low_bytes=low_bytes
    )


def parse_pool_double_info(cf: typing.BinaryIO) -> DoubleInfo:
    byts = cf.read(8)
    high_bytes, low_bytes = U4Pair.unpack(byts)
    return DoubleInfo(
        high_bytes=high_bytes,
        low_bytes=low_bytes
    )


def parse_pool_nameandtype_info(cf: typing.BinaryIO) -> NameAndTypeInfo:
    byts = cf.read(4)
    name_index, descriptor_index = U2Pair.unpack(byts)
    return NameAndTypeInfo(
        name_index=name_index,
        descriptor_index=descriptor_index
    )


def parse_pool_utf_info(cf: typing.BinaryIO) -> Utf8Info:
    byts = cf.read(2)
    length, = U2.unpack(byts)
    byte_content = cf.read(length)
    return Utf8Info(
        length=length,
        bytes=byte_content
    )


def parse_pool_methodhandle_info(cf: typing.BinaryIO) -> MethodHandleInfo:
    byts = cf.read(3)
    reference_kind, reference_index = U1U2.unpack(byts)
    return MethodHandleInfo(
        reference_kind=reference_kind,
        reference_index=reference_index
    )


def parse_pool_methodtype_info(cf: typing.BinaryIO) -> MethodTypeInfo:
    byts = cf.read(2)
    descriptor_index, = U2.unpack(byts)
    return MethodTypeInfo(descriptor_index=descriptor_index)


def parse_pool_dynamic_info(cf: typing.BinaryIO) -> DynamicInfo:
    byts = cf.read(4)
    bootstrap_method_attr_index, name_and_type_index = U2Pair.unpack(byts)
    return DynamicInfo(
        bootstrap_method_attr_index=bootstrap_method_attr_index,
        name_and_type_index=name_and_type_index
    )


def parse_pool_invokedynamic_info(cf: typing.BinaryIO) -> InvokeDynamicInfo:
    byts = cf.read(4)
    bootstrap_method_attr_index, name_and_type_index = U2Pair.unpack(byts)
    return InvokeDynamicInfo(
        bootstrap_method_attr_index=bootstrap_method_attr_index,
        name_and_type_index=name_and_type_index
    )


def parse_pool_module_info(cf: typing.BinaryIO) -> ModuleInfo:
    byts = cf.read(2)
    name_index, = U2.unpack(byts)
    return ModuleInfo(name_index=name_index)


def parse_pool_package_info(cf: typing.BinaryIO) -> PackageInfo:
    byts = cf.read(2)
    name_index, = U2.unpack(byts)
    return PackageInfo(name_index=name_index)


def parse_constant_pool_info(cf: typing.BinaryIO) -> ConstantPoolInfo:
    byts = cf.read(1)
    tag, = U1.unpack(byts)

    match tag:
        case 1:
            return parse_pool_utf_info(cf)
        case 3:
            return parse_pool_integer_info(cf)
        case 4:
            return parse_pool_float_info(cf)
        case 5:
            return parse_pool_long_info(cf)
        case 6:
            return parse_pool_double_info(cf)
        case 7:
            return parse_pool_class_info(cf)
        case 8:
            return parse_pool_string_info(cf)
        case 9:
            return parse_pool_fieldref_info(cf)
        case 10:
            return parse_pool_methodref_info(cf)
        case 11:
            return parse_pool_interfacemethodref_info(cf)
        case 12:
            return parse_pool_nameandtype_info(cf)
        case 15:
            return parse_pool_methodhandle_info(cf)
        case 16:
            return parse_pool_methodtype_info(cf)
        case 17:
            return parse_pool_dynamic_info(cf)
        case 18:
            return parse_pool_invokedynamic_info(cf)
        case 19:
            return parse_pool_module_info(cf)
        case 20:
            return parse_pool_package_info(cf)


def parse_constant_pool(cf: typing.BinaryIO) -> list[ConstantPoolInfo]:
    count_byts = cf.read(2)
    count, = U2.unpack(count_byts)

    pool = []
    for _ in range(count - 1):
        pool_item = parse_constant_pool_info(cf)
        pool.append(pool_item)

    return pool


def parse_access_flags(cf: typing.BinaryIO) -> AccessFlags:
    byts = cf.read(2)
    flags, = U2.unpack(byts)
    return AccessFlags(flags)


def parse_this_class(cf: typing.BinaryIO) -> int:
    byts = cf.read(2)
    this_class, = U2.unpack(byts)
    return this_class


def parse_super_class(cf: typing.BinaryIO) -> int:
    byts = cf.read(2)
    super_class, = U2.unpack(byts)
    return super_class


def parse_interfaces(cf: typing.BinaryIO) -> list[int]:
    byts = cf.read(2)
    interface_count, = U2.unpack(byts)

    interfaces = []
    for _ in range(interface_count):
        ibyts = cf.read(2)
        interface_idx, = U2.unpack(ibyts)
        interfaces.append(interface_idx)

    return interfaces


def parse(file_path: str) -> ClassFile:
    with open(file_path, 'rb') as class_file:
        parse_magic(class_file)
        cf_version = parse_version(class_file)
        pool = parse_constant_pool(class_file)
        access_flags = parse_access_flags(class_file)
        this_class = parse_this_class(class_file)
        super_class = parse_super_class(class_file)
        interfaces = parse_interfaces(class_file)

        print(interfaces)

        return ClassFile(
            version=cf_version,
            constant_pool=pool,
            access_flags=access_flags,
            this_class=this_class,
            super_class=super_class,
            interfaces=interfaces
        )
