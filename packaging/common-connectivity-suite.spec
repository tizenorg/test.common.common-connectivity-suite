%define _unpackaged_files_terminate_build 0

Name: common-connectivity-suite
Summary: common-connectivity-suite
Version: 0.1.0
Release: 1
License: GPLv2
Group: Development/Testing
Source0: %{name}-%{version}.tar.gz


%description
This package is IVI common connectivity test suite

%package -n tts-bluez-tests
Summary: Bluez test suit   
Group:   Development/Testing

%description -n tts-bluez-tests
%{summary}.


%package -n tts-connman-tests
Summary: Connman test suit   
Group:   Development/Testing

%description -n tts-connman-tests
%{summary}.

%prep
%setup -q

%build

%install

install -d %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests
install -d %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests/data
install -d %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests/data/server

install -m 0755 ivi/tts-bluez-tests/src/* %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests
install -m 0755 ivi/tts-bluez-tests/tests.xml %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests
install -m 0755 ivi/tts-bluez-tests/README %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests
install -m 0755 ivi/tts-bluez-tests/data/client/* %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests/data
cp -fr ivi/tts-bluez-tests/data/server/* %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests/data/server
install LICENSE %{buildroot}/%{_datadir}/tests/%{name}/tts-bluez-tests


install -d %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests

install -m 0755 ivi/tts-connman-tests/src/3G/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/BM/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/BT/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/common/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/Ethernet/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/Flight/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/Launch/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/MBT/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/Profile/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/Property/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/Signal/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/State/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/Stress/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/
install -m 0755 ivi/tts-connman-tests/src/WiFi/* %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/

install -d %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/data
install -m 0755 ivi/tts-connman-tests/data/apset.tgz %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests/data

install -m 0755 ivi/tts-connman-tests/network.jpg %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests

install -m 0755 ivi/tts-connman-tests/bisect.sh %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/tests.xml %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/README %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests
install LICENSE %{buildroot}/%{_datadir}/tests/%{name}/tts-connman-tests



%clean
rm -rf $RPM_BUILD_ROOT


%files -n tts-bluez-tests
%defattr(-,root,root)
%{_datadir}/tests/%{name}/tts-bluez-tests
%license LICENSE

%files -n tts-connman-tests
%defattr(-,root,root)
%{_datadir}/tests/%{name}/tts-connman-tests
%license LICENSE

%changelog
* Fri May 23 2014 Wu dawei<daweix.wu@intel.com> 0.1.0-1
 - Initial common connectivity suite test

