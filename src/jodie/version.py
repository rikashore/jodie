from dataclasses import dataclass


@dataclass
class Version:
    major: int
    minor: int

    def __get_major_string(self):
        match self.major:
            case 45:
                return "JDK 1.1"
            case 46:
                return "JDK 1.2"
            case 47:
                return "JDK 1.3"
            case 48:
                return "JDK 1.4"
            case 49:
                return "SE 5"
            case 50:
                return "SE 6"
            case 51:
                return "SE 7"
            case 52:
                return "SE 8"
            case 53:
                return "SE 9"
            case 54:
                return "SE 10"
            case 55:
                return "SE 11"
            case 56:
                return "SE 12"
            case 57:
                return "SE 13"
            case 58:
                return "SE 14"
            case 59:
                return "SE 15"
            case 60:
                return "SE 16"
            case 61:
                return "SE 17"
            case 62:
                return "SE 18"
            case 63:
                return "SE 19"
            case 64:
                return "SE 20"
            case 65:
                return "SE 21"
            case _:
                return "unknown"

    def __str__(self):
        return f"major: {self.major} ({self.__get_major_string()}) minor: {self.minor}"
