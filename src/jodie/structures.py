from enum import IntFlag
from dataclasses import dataclass
from jodie.version import Version
from jodie.constant_pool import ConstantPoolInfo


class AccessFlags(IntFlag):
    PUBLIC = 0x0001
    FINAL = 0x0010
    SUPER = 0x0020
    INTERFACE = 0x0200
    ABSTRACT = 0x0400
    SYNTHETIC = 0x1000
    ANNOTATION = 0x2000
    ENUM = 0x4000
    MODULE = 0x8000

    def __str__(self):
        return f"0x{self:0>4X}"


@dataclass
class ClassFile:
    version: Version
    constant_pool: list[ConstantPoolInfo]
    access_flags: AccessFlags
    this_class: int
    super_class: int
    interfaces: list[int]
