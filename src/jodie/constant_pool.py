from dataclasses import dataclass
from enum import IntEnum


# Tags for each pool info
#     Utf8 = 1
#     Integer = 3
#     Float = 4
#     Long = 5
#     Double = 6
#     Class = 7
#     String = 8
#     FieldRef = 9
#     MethodRef = 10
#     InterfaceMethodRef = 11
#     NameAndType = 12
#     MethodHandle = 15
#     MethodType = 16
#     Dynamic = 17
#     InvokeDynamic = 18
#     Module = 19
#     Package = 20


@dataclass
class ClassInfo:
    name_index: int


@dataclass
class FieldRefInfo:
    class_index: int
    name_and_type_index: int


@dataclass
class MethodRefInfo:
    class_index: int
    name_and_type_index: int


@dataclass
class InterfaceMethodRefInfo:
    class_index: int
    name_and_type_index: int


@dataclass
class StringInfo:
    string_index: int


@dataclass
class IntegerInfo:
    bytes: int


@dataclass
class FloatInfo:
    bytes: int


@dataclass
class LongInfo:
    high_bytes: int
    low_bytes: int


@dataclass
class DoubleInfo:
    high_bytes: int
    low_bytes: int


@dataclass
class NameAndTypeInfo:
    name_index: int
    descriptor_index: int


@dataclass
class Utf8Info:
    length: int
    bytes: bytes


@dataclass
class MethodHandleInfo:
    reference_kind: int
    reference_index: int


@dataclass
class MethodTypeInfo:
    descriptor_index: int


@dataclass
class DynamicInfo:
    bootstrap_method_attr_index: int
    name_and_type_index: int


@dataclass
class InvokeDynamicInfo:
    bootstrap_method_attr_index: int
    name_and_type_index: int


@dataclass
class ModuleInfo:
    name_index: int


@dataclass
class PackageInfo:
    name_index: int


ConstantPoolInfo = (ClassInfo
                    | FieldRefInfo
                    | MethodRefInfo
                    | InterfaceMethodRefInfo
                    | StringInfo
                    | IntegerInfo
                    | FloatInfo
                    | LongInfo
                    | DoubleInfo
                    | NameAndTypeInfo
                    | Utf8Info
                    | MethodHandleInfo
                    | MethodTypeInfo
                    | DynamicInfo
                    | InvokeDynamicInfo
                    | ModuleInfo
                    | PackageInfo)
