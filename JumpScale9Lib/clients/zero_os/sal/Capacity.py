import io
from js9 import j

class Capacity:

    def __init__(self, node):
        self._node = node
        self._hw_info = None
        self._disk_info = None

    @property
    def hw_info(self):
        if self._hw_info is None:
            out = io.StringIO()

            def cb(level, msg, flag):
                out.write(msg)
                out.write('\n')
            self._node.client.system('dmidecode', stream=True).stream(cb)
            self._hw_info = j.tools.capacityparser.hw_info_from_dmi(out.getvalue())
        return self._hw_info

    @property
    def disk_info(self):
        if self._disk_info is None:
            self._disk_info = {}
            for disk in self._node.disks.list():
                out = io.StringIO()

                def cb(level, msg, flag):
                    out.write(msg)
                    out.write('\n')
                self._node.client.system('smartctl -i %s' % disk.devicename, stream=True).stream(cb)
                self._disk_info[disk.devicename] = j.tools.capacityparser.disk_info_from_smartctl(
                    out.getvalue(),
                    disk.size,
                    disk.type.name,
                )
        return self._disk_info

    def report(self):
        """
        create a report of the hardware capacity for
        processor, memory, motherboard and disks
        """
        return j.tools.capacityparser.get_report(self._node.client.info.mem()['total'], self.hw_info, self.disk_info)
