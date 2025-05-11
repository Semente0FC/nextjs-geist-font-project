import pynvml
from loguru import logger

class GPUMonitor:
    def __init__(self):
        pynvml.nvmlInit()
        self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # Assuming single GPU

    def get_usage(self):
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(self.handle)
        util = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
        temp = pynvml.nvmlDeviceGetTemperature(self.handle, pynvml.NVML_TEMPERATURE_GPU)
        return {
            "memory_total": mem_info.total / (1024 ** 2),  # MB
            "memory_used": mem_info.used / (1024 ** 2),    # MB
            "memory_free": mem_info.free / (1024 ** 2),    # MB
            "gpu_util": util.gpu,
            "memory_util": util.memory,
            "temperature": temp
        }

    def close(self):
        pynvml.nvmlShutdown()
