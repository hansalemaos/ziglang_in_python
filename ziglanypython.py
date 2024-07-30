import numpy as np
import os 
import ctypes 

zigdll = "ziglangpythoncolor.dll"
dllpath = os.path.normpath(os.path.join(os.path.dirname(__file__), zigdll))
cta = ctypes.cdll.LoadLibrary(dllpath)
colorsearch = cta.colorsearch

def search_colors(pic, colors):
    if not pic.flags["C_CONTIGUOUS"]:
        pic = np.ascontiguousarray(pic)
    if not isinstance(colors, np.ndarray):
        colors = np.array(colors, dtype=np.uint8)
    if not colors.flags["C_CONTIGUOUS"]:
        colors = np.ascontiguousarray(colors)
    totallengthcolor = (colors.shape[0] * colors.shape[1]) - 1
    totallenghtpic = (pic.shape[0] * pic.shape[1] * pic.shape[2]) - 1
    outputx = np.zeros(totallenghtpic, dtype=np.int32)
    outputy = np.zeros(totallenghtpic, dtype=np.int32)
    endresults = np.zeros(1, dtype=np.int32)
    width = pic.shape[1]

    picb = pic.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
    colorsb = colors.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
    totallengthpicb = ctypes.c_uint(totallenghtpic)
    totallengthcolorcb = ctypes.c_uint(totallengthcolor)
    outputxb = outputx.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    outputyb = outputy.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    endresultsb = endresults.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
    widthb = ctypes.c_int(width)

    colorsearch(
        picb,
        colorsb,
        widthb,
        totallengthpicb,
        totallengthcolorcb,
        outputxb,
        outputyb,
        endresultsb,
    )
    return np.dstack([outputx[: endresults[0] + 1], outputy[: endresults[0] + 1]])[0]