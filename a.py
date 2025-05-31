#!/usr/bin/env python3
import ctypes
import sys
from OpenGL import GL, GLX  # 系统自带的 OpenGL 绑定

# 检查 OpenGL 版本
def get_opengl_version():
    try:
        # 初始化 X11 显示连接
        display = GLX.glXOpenDisplay(None)
        if not display:
            raise RuntimeError("无法打开 X11 显示")
        
        # 获取可用的帧缓冲区配置
        fbcount = ctypes.c_int(0)
        visual_info = GLX.glXChooseVisual(display, 0, [GLX.GLX_RGBA, GLX.GLX_DEPTH_SIZE, 24, GLX.GLX_DOUBLEBUFFER, 0], fbcount)
        
        if not visual_info:
            raise RuntimeError("无法获取合适的视觉配置")
        
        # 创建上下文
        context = GLX.glXCreateContext(display, visual_info, None, True)
        if not context:
            raise RuntimeError("无法创建 OpenGL 上下文")
        
        # 使上下文成为当前上下文
        GLX.glXMakeCurrent(display, GLX.glXCreateWindow(display, visual_info, None, None), context)
        
        # 获取 OpenGL 版本和渲染器信息
        version = GL.glGetString(GL.GL_VERSION).decode('utf-8')
        renderer = GL.glGetString(GL.GL_RENDERER).decode('utf-8')
        
        # 清理资源
        GLX.glXMakeCurrent(display, None, None)
        GLX.glXDestroyContext(display, context)
        GLX.glXCloseDisplay(display)
        
        return version, renderer
    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    version, renderer = get_opengl_version()
    if version:
        print(f"OpenGL 版本: {version}")
        print(f"渲染器: {renderer}")
        print("✅ OpenGL 环境正常工作")
    else:
        print(f"❌ 无法获取 OpenGL 信息: {renderer}")
        print("可能原因:")
        print("  1. 系统缺少 OpenGL 驱动")
        print("  2. 无图形界面环境（需启用 X11 转发或使用 EGL）")
        print("  3. Python OpenGL 绑定未正确安装")