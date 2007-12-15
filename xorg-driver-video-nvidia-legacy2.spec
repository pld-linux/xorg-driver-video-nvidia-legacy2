#
# Conditional build:
%bcond_without	dist_kernel	# without distribution kernel
%bcond_without	kernel		# without kernel packages
%bcond_without	incall		# include all tarballs
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)
#
%define		no_install_post_strip 1
#
%define		_nv_ver		96
%define		_nv_rel		43.01
%define		_min_x11	6.7.0
%define		_rel		7
#
%define		need_x86	0
%define		need_x8664	0
%if %{with incall}
%define		need_x86	1
%define		need_x8664	1
%else
%ifarch %{ix86}
%define		need_x86	1
%endif
%ifarch %{x8664}
%define		need_x8664	1
%endif
%endif
#
Summary:	Linux Drivers for older nVidia GeForce/Quadro Chips
Summary(pl.UTF-8):	Sterowniki do starszych kart graficznych nVidia GeForce/Quadro
Name:		xorg-driver-video-nvidia-legacy2
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}
License:	nVidia Binary
Group:		X11
%if %{need_x86}
Source0:	http://download.nvidia.com/XFree86/Linux-x86/%{_nv_ver}.%{_nv_rel}/NVIDIA-Linux-x86-%{_nv_ver}.%{_nv_rel}-pkg1.run
# Source0-md5:	66f8b5e243aad22162e40d0f05f0bf1e
%endif
%if %{need_x8664}
Source1:	http://download.nvidia.com/XFree86/Linux-x86_64/%{_nv_ver}.%{_nv_rel}/NVIDIA-Linux-x86_64-%{_nv_ver}.%{_nv_rel}-pkg2.run
# Source1-md5:	a908a02dc58ddec526184dda18bf4ea5
%endif
Patch0:		X11-driver-nvidia-GL.patch
Patch1:		X11-driver-nvidia-desktop.patch
URL:		http://www.nvidia.com/object/unix.html
BuildRequires:	%{kgcc_package}
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2}
%endif
BuildRequires:	rpmbuild(macros) >= 1.379
BuildConflicts:	XFree86-nvidia
Requires:	xorg-xserver-server
Requires:	xorg-xserver-server(videodrv-abi) = 2.0
Provides:	OpenGL = 2.1
Provides:	OpenGL-GLX = 1.4
Provides:	xorg-xserver-libglx
Obsoletes:	Mesa
Obsoletes:	X11-OpenGL-core < 1:7.0.0
Obsoletes:	X11-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-OpenGL-core < 1:7.0.0
Obsoletes:	XFree86-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-driver-nvidia
Obsoletes:	XFree86-nvidia
Conflicts:	Mesa-libGL
Conflicts:	XFree86-OpenGL-devel <= 4.2.0-3
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreqdep   libGL.so.1 libGLcore.so.1

%description
This driver set adds improved 2D functionality to the Xorg/XFree86 X
server as well as high performance OpenGL acceleration, AGP support,
support for most flat panels, and 2D multiple monitor support.

This driver version supports the following nVidia adapters: 
GeForce 6100/6150/6150LE/6200/6200TurboCache(TM)/6500/6600/6600GT/6600LE/6600VE/6610XL/6800/6800GS/6800GT/6800LE/6800Ultra/6800XE/6800XT/7300GS/7300LE/7600GS/7600GT/7800GS/7800GT/7800GTX/7900GT/7900GTX
GeForce FX 5100/5200/5200LE/5500/5600/5600XT/5700/5700LE/5700VE/5800/5900/5900XT/5900ZT/5950/Go5100/Go5200/Go5250/Go53xx/Go5600/Go5650/Go5700
GeForce Go 6200/6400/6600/6800/7300/7400/7600/7800/7900 
GeForce PCX 4300/5750/5900 GeForce2 Go/Integrated GPU/MX(100/200/400)
GeForce3/GeForce3 Ti(200/500) GeForce4 410Go/420Go/4200Go/440Go/460Go
GeForce4 MX 4000/420/440/440SE/440-SE/460/Integrated 
GeForce4 Ti 4200/4400/4600/4800 
Quadro DCC 
Quadro FX 1000/1100/1300/1400/1500/1500M/2000/2500M/3000/330/3400/4400/3450/350/3500/350M/4000/4500/500/600/540/550/5500/560/700/Go1000/Go1400/Go700
Quadro NVS 110M/120M/280/285/440/50 Quadro NVSA Quadro2 MXR/EX/Go
Quadro4 380XGL/500GoGL/550XGL/580XGL/700GoGL/700XGL/750XGL/780XGL/900XGL/980XGL

Older TNT/GeForce/Quadro adapters are supported by driver from
xorg-driver-video-nvidia-legacy package, not this one.

%description -l pl.UTF-8
Usprawnione sterowniki dla kart graficznych nVidia do serwera
Xorg/XFree86, dające wysokowydajną akcelerację OpenGL, obsługę AGP i
wielu monitorów 2D.

Ta wersja sterowników obsługuje następujące karty nVidia: 
GeForce 6100/6150/6150LE/6200/6200TurboCache(TM)/6500/6600/6600GT/6600LE/6600VE/6610XL/6800/6800GS/6800GT/6800LE/6800Ultra/6800XE/6800XT/7300GS/7300LE/7600GS/7600GT/7800GS/7800GT/7800GTX/7900GT/7900GTX
GeForce FX 5100/5200/5200LE/5500/5600/5600XT/5700/5700LE/5700VE/5800/5900/5900XT/5900ZT/5950/Go5100/Go5200/Go5250/Go53xx/Go5600/Go5650/Go5700
GeForce Go 6200/6400/6600/6800/7300/7400/7600/7800/7900 
GeForce PCX 4300/5750/5900 GeForce2 Go/Integrated GPU/MX(100/200/400)
GeForce3/GeForce3 Ti(200/500) GeForce4 410Go/420Go/4200Go/440Go/460Go
GeForce4 MX 4000/420/440/440SE/440-SE/460/Integrated 
GeForce4 Ti 4200/4400/4600/4800 
Quadro DCC 
Quadro FX 1000/1100/1300/1400/1500/1500M/2000/2500M/3000/330/3400/4400/3450/350/3500/350M/4000/4500/500/600/540/550/5500/560/700/Go1000/Go1400/Go700
Quadro NVS 110M/120M/280/285/440/50 Quadro NVSA Quadro2 MXR/EX/Go
Quadro4 380XGL/500GoGL/550XGL/580XGL/700GoGL/700XGL/750XGL/780XGL/900XGL/980XGL

Starsze karty TNT/GeForce/Quadro są obsługiwane przez sterownik z
pakietu xorg-driver-video-nvidia-legacy.

%package devel
Summary:	OpenGL (GL and GLX) header files
Summary(pl.UTF-8):	Pliki nagłówkowe OpenGL (GL i GLX)
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	OpenGL-GLX-devel = 1.4
Provides:	OpenGL-devel = 2.1
Obsoletes:	X11-OpenGL-devel-base
Obsoletes:	XFree86-OpenGL-devel-base
Obsoletes:	XFree86-driver-nvidia-devel
Conflicts:	XFree86-OpenGL-devel < 4.3.99.902-0.3

%description devel
OpenGL header files (GL and GLX only) for NVIDIA OpenGL
implementation.

%description devel -l pl.UTF-8
Pliki nagłówkowe OpenGL (tylko GL i GLX) dla implementacji OpenGL
firmy NVIDIA.

%package static
Summary:	Static XvMCNVIDIA library
Summary(pl.UTF-8):	Statyczna biblioteka XvMCNVIDIA
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XvMCNVIDIA library.

%description static -l pl.UTF-8
Statyczna biblioteka XvMCNVIDIA.

%package progs
Summary:	Tools for advanced control of nVidia graphic cards
Summary(pl.UTF-8):	Narzędzia do zarządzania kartami graficznymi nVidia
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	XFree86-driver-nvidia-progs

%description progs
Tools for advanced control of nVidia graphic cards.

%description progs -l pl.UTF-8
Narzędzia do zarządzania kartami graficznymi nVidia.

%package -n kernel%{_alt_kernel}-video-nvidia-legacy2
Summary:	nVidia kernel module for nVidia Architecture support
Summary(de.UTF-8):	Das nVidia-Kern-Modul für die nVidia-Architektur-Unterstützung
Summary(pl.UTF-8):	Moduł jądra dla obsługi kart graficznych nVidia
Version:	%{_nv_ver}.%{_nv_rel}
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
Requires:	dev >= 2.7.7-10
%{?with_dist_kernel:%requires_releq_kernel}
Provides:	X11-driver-nvidia(kernel)
Obsoletes:	XFree86-nvidia-kernel

%description -n kernel%{_alt_kernel}-video-nvidia-legacy2
nVidia Architecture support for Linux kernel.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy2 -l de.UTF-8
Die nVidia-Architektur-Unterstützung für den Linux-Kern.

%description -n kernel%{_alt_kernel}-video-nvidia-legacy2 -l pl.UTF-8
Obsługa architektury nVidia dla jądra Linuksa. Pakiet wymagany przez
sterownik nVidii dla Xorg/XFree86.

%prep
cd %{_builddir}
rm -rf NVIDIA-Linux-x86*-%{_nv_ver}.%{_nv_rel}-pkg*
%ifarch %{ix86}
/bin/sh %{SOURCE0} --extract-only
%setup -qDT -n NVIDIA-Linux-x86-%{_nv_ver}.%{_nv_rel}-pkg1
%else
/bin/sh %{SOURCE1} --extract-only
%setup -qDT -n NVIDIA-Linux-x86_64-%{_nv_ver}.%{_nv_rel}-pkg2
%endif
%patch0 -p1
%patch1 -p1
echo 'EXTRA_CFLAGS += -Wno-pointer-arith -Wno-sign-compare -Wno-unused' >> usr/src/nv/Makefile.kbuild

%build
%if %{with kernel}
cd usr/src/nv/
ln -sf Makefile.kbuild Makefile
cat >> Makefile <<'EOF'

$(obj)/nv-kernel.o: $(src)/nv-kernel.o.bin
	cp $< $@
EOF
mv nv-kernel.o{,.bin}
%build_kernel_modules -m nvidia
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}
install -d $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,extensions} \
        $RPM_BUILD_ROOT{%{_includedir}/GL,%{_libdir},%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/etc/X11/xinit/xinitrc.d}

install usr/bin/nvidia-{settings,xconfig,bug-report.sh} $RPM_BUILD_ROOT%{_bindir}
install usr/share/man/man1/nvidia-{settings,xconfig}.* $RPM_BUILD_ROOT%{_mandir}/man1
install usr/share/applications/nvidia-settings.desktop $RPM_BUILD_ROOT%{_desktopdir}
install usr/share/pixmaps/nvidia-settings.png $RPM_BUILD_ROOT%{_pixmapsdir}

for f in \
        usr/lib/tls/libnvidia-tls.so.%{version}         \
        usr/lib/libnvidia-cfg.so.%{version}             \
        usr/lib/libGL{,core}.so.%{version}              \
        usr/X11R6/lib/libXvMCNVIDIA.so.%{version}       \
        usr/X11R6/lib/libXvMCNVIDIA.a                   \
; do
        install $f $RPM_BUILD_ROOT%{_libdir}
done

install usr/X11R6/lib/modules/extensions/libglx.so.%{version} \
        $RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions
install usr/X11R6/lib/modules/drivers/nvidia_drv.so \
        $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers

install usr/include/GL/*.h $RPM_BUILD_ROOT%{_includedir}/GL

ln -sf libglx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/extensions/libglx.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA.so
ln -sf libXvMCNVIDIA.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libXvMCNVIDIA_dynamic.so.1

# OpenGL ABI for Linux compatibility
ln -sf libGL.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libGL.so.1
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
%endif

%if %{with kernel}
%install_kernel_modules -m usr/src/nv/nvidia -d misc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cat << EOF
NOTE: You must install:
kernel-video-nvidia-legacy2-%{version}
for this driver to work
EOF

%postun	-p /sbin/ldconfig

%post	-n kernel%{_alt_kernel}-video-nvidia-legacy2
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-video-nvidia-legacy2
%depmod %{_kernel_ver}

%if %{with userspace}
%files
%defattr(644,root,root,755)
%doc LICENSE
%doc usr/share/doc/{README.txt,NVIDIA_Changelog,XF86Config.sample,html}
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libGL.so.1
# symlink for binary apps which fail to conform Linux OpenGL ABI
# (and dlopen libGL.so instead of libGL.so.1)
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/libGLcore.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so.*.*
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA_dynamic.so.1
%attr(755,root,root) %{_libdir}/libnvidia-cfg.so.*.*.*
%attr(755,root,root) %{_libdir}/libnvidia-tls.so.*.*.*
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/nvidia_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libglx.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMCNVIDIA.so
%dir %{_includedir}/GL
%{_includedir}/GL/gl.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glxext.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libXvMCNVIDIA.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nvidia-settings
%attr(755,root,root) %{_bindir}/nvidia-xconfig
%attr(755,root,root) %{_bindir}/nvidia-bug-report.sh
%{_desktopdir}/nvidia-settings.desktop
%{_mandir}/man1/nvidia-*
%{_pixmapsdir}/nvidia-settings.png
%endif

%if %{with kernel}
%files -n kernel%{_alt_kernel}-video-nvidia-legacy2
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/misc/*.ko*
%endif
