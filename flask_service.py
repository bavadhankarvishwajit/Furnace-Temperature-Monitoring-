import win32serviceutil
import win32service
import win32event
import servicemanager
from waitress import serve
from app import app  # your Flask app

class FlaskWindowsService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FlaskFurnaceService"
    _svc_display_name_ = "Flask API Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        # Serve Flask using Waitress (production WSGI server)
        serve(app, host='0.0.0.0', port=8000)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(FlaskWindowsService)
