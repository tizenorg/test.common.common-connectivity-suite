Name:		common-connectivity-suite
Summary:	Connectivity suite for Tizen Common
Version:	1.0.0
Release:	1
License:	GPL-2.0
Group:		Development/Testing
Source0:	%{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:	fdupes
Requires:	bluez
Requires:	bluez-test
Requires:	common-suite-launcher
Requires:	connman
Requires:	connman-test
Requires:	testkit-lite
BuildArch:	noarch

%description
The common-connectivity-suite validates the connectivity features of the Tizen Common image : core connman, wifi, bluetooth


%package -n ivi-connectivity-tests
Summary:	Bluez test suite   
Group:		Development/Testing
Requires:	bluez
Requires:	connman
Requires:	connman-test
Requires:	testkit-lite

%description -n ivi-connectivity-tests
IVI multimedia test suite. Validates connectivity features 


%prep
%setup -q
cp %{SOURCE1001} .

%build


%install
# common-connectivity-suite package
install -d %{buildroot}/%{_datadir}/tests/%{name}
install -m 0644 common/TODO %{buildroot}/%{_datadir}/tests/%{name}

# ivi-connectivity-tests package
install -d %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-bluez-tests
install -d %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0644 LICENSE %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests

install -m 0644 ivi/tts-bluez-tests/tests.xml %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-bluez-tests
install -m 0755 ivi/tts-bluez-tests/src/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-bluez-tests
cp -r ivi/tts-bluez-tests/data %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-bluez-tests

install -m 0755 ivi/tts-connman-tests/bisect.sh %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0644 ivi/tts-connman-tests/network.jpg %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0644 ivi/tts-connman-tests/tests.xml %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0644 ivi/tts-connman-tests/README %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/3G/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/BM/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/BT/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/common/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/Ethernet/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/Flight/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/Launch/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/MBT/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/Profile/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/Property/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/Signal/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/State/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/Stress/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
install -m 0755 ivi/tts-connman-tests/src/WiFi/* %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests
cp -r ivi/tts-connman-tests/data %{buildroot}/%{_datadir}/tests/ivi-connectivity-tests/tts-connman-tests

%fdupes %{buildroot}


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_datadir}/tests/%{name}


%files -n ivi-connectivity-tests
%defattr(-,root,root)
%{_datadir}/tests/ivi-connectivity-tests
