# routes.py
from fastapi import APIRouter
from controller import create_generic_routes

# Models & Schemas
from models.cpu import CPU
from schemas.cpu import CPUBase, CPUResponse

from models.user import User
from schemas.user import UserCreate, UserUpdate, UserResponse

from models.laptop import Laptop
from schemas.laptop import LaptopBase, LaptopResponse

from models.case import Case
from schemas.case import CaseBase, CaseResponse

from models.wifi_card import WifiCard
from schemas.wifi_card import WifiCardBase, WifiCardResponse

from models.external_drive import ExternalDrive
from schemas.external_drive import ExternalDriveBase, ExternalDriveResponse

from models.wired_card import PciCard
from schemas.wired_card import PciCardBase, PciCardResponse

from models.webcam import Webcam
from schemas.webcam import WebcamBase, WebcamResponse

from models.video_card import GPU
from schemas.video_card import GPUBase, GPUResponse

from models.ups import UPS
from schemas.ups import UPSBase, UPSResponse

from models.headphones import Headphones
from schemas.headphones import HeadphonesBase, HeadphonesResponse

from models.internal_harddrive import InternalHardDrive
from schemas.internal_harddrive import InternalHardDriveBase, InternalHardDriveResponse

# Eksik olanlar:
from models.keyboard import Keyboard
from schemas.keyboard import KeyboardBase, KeyboardResponse

from models.memory import Memory
from schemas.memory import MemoryBase, MemoryResponse

from models.monitor import Monitor
from schemas.monitor import MonitorBase, MonitorResponse

from models.motherboard import Motherboard
from schemas.motherboard import MotherboardBase, MotherboardResponse

from models.mouse import Mouse
from schemas.mouse import MouseBase, MouseResponse


api_router = APIRouter()

# User endpoints
user_router = create_generic_routes(User, UserCreate, UserUpdate, UserResponse, "users")
api_router.include_router(user_router, prefix="/users", tags=["Users"])

# Laptop
laptop_router = create_generic_routes(Laptop, LaptopBase, LaptopBase, LaptopResponse, "laptops")
api_router.include_router(laptop_router, prefix="/laptops", tags=["Laptops"])

# Case
case_router = create_generic_routes(Case, CaseBase, CaseBase, CaseResponse, "cases")
api_router.include_router(case_router, prefix="/cases", tags=["Cases"])

# Wi-Fi card
wifi_card_router = create_generic_routes(WifiCard, WifiCardBase, WifiCardBase, WifiCardResponse, "wifi_cards")
api_router.include_router(wifi_card_router, prefix="/wifi-cards", tags=["Wi-Fi Cards"])

# External drive
external_drive_router = create_generic_routes(ExternalDrive, ExternalDriveBase, ExternalDriveBase, ExternalDriveResponse, "external_harddrives")
api_router.include_router(external_drive_router, prefix="/external-harddrives", tags=["External Hard Drives"])

# PCI card
pci_card_router = create_generic_routes(PciCard, PciCardBase, PciCardBase, PciCardResponse, "pci_cards")
api_router.include_router(pci_card_router, prefix="/pci-cards", tags=["PCI Cards"])

# Webcam
webcam_router = create_generic_routes(Webcam, WebcamBase, WebcamBase, WebcamResponse, "webcams")
api_router.include_router(webcam_router, prefix="/webcams", tags=["Webcams"])

# GPU
gpu_router = create_generic_routes(GPU, GPUBase, GPUBase, GPUResponse, "video_cards")
api_router.include_router(gpu_router, prefix="/video-cards", tags=["Video Cards"])

# UPS
ups_router = create_generic_routes(UPS, UPSBase, UPSBase, UPSResponse, "ups_devices")
api_router.include_router(ups_router, prefix="/ups", tags=["UPS"])

# CPU
cpu_router = create_generic_routes(CPU, CPUBase, CPUBase, CPUResponse, "cpus")
api_router.include_router(cpu_router, prefix="/cpus", tags=["CPUs"])

# Headphones
headphones_router = create_generic_routes(Headphones, HeadphonesBase, HeadphonesBase, HeadphonesResponse, "headphones")
api_router.include_router(headphones_router, prefix="/headphones", tags=["Headphones"])

# Internal hard drive
internal_harddrive_router = create_generic_routes(InternalHardDrive, InternalHardDriveBase, InternalHardDriveBase, InternalHardDriveResponse, "internal-harddrives")
api_router.include_router(internal_harddrive_router, prefix="/internal-harddrives", tags=["Internal Hard Drives"])

# Keyboard
keyboard_router = create_generic_routes(Keyboard, KeyboardBase, KeyboardBase, KeyboardResponse, "keyboards")
api_router.include_router(keyboard_router, prefix="/keyboards", tags=["Keyboards"])

# Memory
memory_router = create_generic_routes(Memory, MemoryBase, MemoryBase, MemoryResponse, "memories")
api_router.include_router(memory_router, prefix="/memories", tags=["Memories"])

# Monitor
monitor_router = create_generic_routes(Monitor, MonitorBase, MonitorBase, MonitorResponse, "monitors")
api_router.include_router(monitor_router, prefix="/monitors", tags=["Monitors"])

# Motherboard
motherboard_router = create_generic_routes(Motherboard, MotherboardBase, MotherboardBase, MotherboardResponse, "motherboards")
api_router.include_router(motherboard_router, prefix="/motherboards", tags=["Motherboards"])

# Mouse
mouse_router = create_generic_routes(Mouse, MouseBase, MouseBase, MouseResponse, "mouses")
api_router.include_router(mouse_router, prefix="/mouses", tags=["Mouses"])


from models.optical_drive import OpticalDrive
from schemas.optical_drive import OpticalDriveBase, OpticalDriveResponse

optical_drive_router = create_generic_routes(OpticalDrive, OpticalDriveBase, OpticalDriveBase, OpticalDriveResponse, "optical_drives")
api_router.include_router(optical_drive_router, prefix="/optical-drives", tags=["Optical Drives"])


# router ekleme
from models.operating_system import OperatingSystem
from schemas.operating_system import OperatingSystemBase, OperatingSystemResponse

os_router = create_generic_routes(OperatingSystem, OperatingSystemBase, OperatingSystemBase, OperatingSystemResponse, "os")
api_router.include_router(os_router, prefix="/os", tags=["Operating Systems"])

# router ekleme
from models.power_supply import PSU
from schemas.power_supply import PSUBase, PSUResponse

psu_router = create_generic_routes(PSU, PSUBase, PSUBase, PSUResponse, "power-supplies")
api_router.include_router(psu_router, prefix="/power-supplies", tags=["Power Supplies"])

# router ekleme
from models.sound_card import SoundCard
from schemas.sound_card import SoundCardBase, SoundCardResponse

sound_card_router = create_generic_routes(SoundCard, SoundCardBase, SoundCardBase, SoundCardResponse, "sound_cards")
api_router.include_router(sound_card_router, prefix="/sound-cards", tags=["Sound Cards"])


from models.speaker import Speaker
from schemas.speaker import SpeakerBase, SpeakerResponse
speaker_router = create_generic_routes(Speaker, SpeakerBase, SpeakerBase, SpeakerResponse, "speakers")
api_router.include_router(speaker_router, prefix="/speakers", tags=["Speakers"])


from models.tablet import Tablet
from schemas.tablet import TabletBase, TabletResponse
tablet_router = create_generic_routes(Tablet, TabletBase, TabletBase, TabletResponse, "tablets")
api_router.include_router(tablet_router, prefix="/tablets", tags=["Tablets"])
