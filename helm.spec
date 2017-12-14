# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 0
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 0

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         kubernetes
%global repo            helm
# https://github.com/kubernetes/helm
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     k8s.io/helm

%define _disable_source_fetch 0

Name:           helm
Version:        2.7.2
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/v%{version}.zip

BuildRequires:  glide
BuildRequires:  git

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
Helm is a tool for managing Kubernetes charts.
Charts are packages of pre-configured Kubernetes
resources.

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/BurntSushi/toml)
BuildRequires: golang(github.com/Masterminds/semver)
BuildRequires: golang(github.com/Masterminds/sprig)
BuildRequires: golang(github.com/Masterminds/vcs)
BuildRequires: golang(github.com/asaskevich/govalidator)
BuildRequires: golang(github.com/evanphx/json-patch)
BuildRequires: golang(github.com/ghodss/yaml)
BuildRequires: golang(github.com/gobwas/glob)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/ptypes/any)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/technosophos/moniker)
BuildRequires: golang(golang.org/x/crypto/openpgp)
BuildRequires: golang(golang.org/x/crypto/openpgp/clearsign)
BuildRequires: golang(golang.org/x/crypto/openpgp/packet)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/keepalive)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(k8s.io/api/apps/v1beta1)
BuildRequires: golang(k8s.io/api/apps/v1beta2)
BuildRequires: golang(k8s.io/api/batch/v1)
BuildRequires: golang(k8s.io/api/core/v1)
BuildRequires: golang(k8s.io/api/extensions/v1beta1)
BuildRequires: golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires: golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires: golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires: golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires: golang(k8s.io/apimachinery/pkg/fields)
BuildRequires: golang(k8s.io/apimachinery/pkg/labels)
BuildRequires: golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires: golang(k8s.io/apimachinery/pkg/types)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires: golang(k8s.io/apimachinery/pkg/version)
BuildRequires: golang(k8s.io/apimachinery/pkg/watch)
BuildRequires: golang(k8s.io/client-go/discovery)
BuildRequires: golang(k8s.io/client-go/kubernetes)
BuildRequires: golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires: golang(k8s.io/client-go/kubernetes/typed/extensions/v1beta1)
BuildRequires: golang(k8s.io/client-go/rest)
BuildRequires: golang(k8s.io/client-go/tools/clientcmd)
BuildRequires: golang(k8s.io/client-go/tools/portforward)
BuildRequires: golang(k8s.io/client-go/transport/spdy)
BuildRequires: golang(k8s.io/client-go/util/homedir)
BuildRequires: golang(k8s.io/helm/pkg/chartutil)
BuildRequires: golang(k8s.io/helm/pkg/engine)
BuildRequires: golang(k8s.io/helm/pkg/getter)
BuildRequires: golang(k8s.io/helm/pkg/helm/environment)
BuildRequires: golang(k8s.io/helm/pkg/helm/helmpath)
BuildRequires: golang(k8s.io/helm/pkg/hooks)
BuildRequires: golang(k8s.io/helm/pkg/ignore)
BuildRequires: golang(k8s.io/helm/pkg/kube)
BuildRequires: golang(k8s.io/helm/pkg/lint/rules)
BuildRequires: golang(k8s.io/helm/pkg/lint/support)
BuildRequires: golang(k8s.io/helm/pkg/plugin)
BuildRequires: golang(k8s.io/helm/pkg/plugin/cache)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/chart)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/release)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/rudder)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/services)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/version)
BuildRequires: golang(k8s.io/helm/pkg/provenance)
BuildRequires: golang(k8s.io/helm/pkg/releasetesting)
BuildRequires: golang(k8s.io/helm/pkg/releaseutil)
BuildRequires: golang(k8s.io/helm/pkg/repo)
BuildRequires: golang(k8s.io/helm/pkg/resolver)
BuildRequires: golang(k8s.io/helm/pkg/rudder)
BuildRequires: golang(k8s.io/helm/pkg/storage)
BuildRequires: golang(k8s.io/helm/pkg/storage/driver)
BuildRequires: golang(k8s.io/helm/pkg/strvals)
BuildRequires: golang(k8s.io/helm/pkg/tiller/environment)
BuildRequires: golang(k8s.io/helm/pkg/timeconv)
BuildRequires: golang(k8s.io/helm/pkg/tlsutil)
BuildRequires: golang(k8s.io/helm/pkg/urlutil)
BuildRequires: golang(k8s.io/helm/pkg/version)
BuildRequires: golang(k8s.io/kubernetes/pkg/api)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/helper)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/v1/helper)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/v1/pod)
BuildRequires: golang(k8s.io/kubernetes/pkg/apis/batch)
BuildRequires: golang(k8s.io/kubernetes/pkg/apis/extensions)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset/typed/core/internalversion)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/unversioned)
BuildRequires: golang(k8s.io/kubernetes/pkg/controller/deployment/util)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/cmd/util)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/resource)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/validation)
BuildRequires: golang(k8s.io/kubernetes/pkg/printers)
%endif

Requires:      golang(github.com/BurntSushi/toml)
Requires:      golang(github.com/Masterminds/semver)
Requires:      golang(github.com/Masterminds/sprig)
Requires:      golang(github.com/Masterminds/vcs)
Requires:      golang(github.com/asaskevich/govalidator)
Requires:      golang(github.com/evanphx/json-patch)
Requires:      golang(github.com/ghodss/yaml)
Requires:      golang(github.com/gobwas/glob)
Requires:      golang(github.com/golang/protobuf/proto)
Requires:      golang(github.com/golang/protobuf/ptypes/any)
Requires:      golang(github.com/golang/protobuf/ptypes/timestamp)
Requires:      golang(github.com/grpc-ecosystem/go-grpc-prometheus)
Requires:      golang(github.com/spf13/pflag)
Requires:      golang(github.com/technosophos/moniker)
Requires:      golang(golang.org/x/crypto/openpgp)
Requires:      golang(golang.org/x/crypto/openpgp/clearsign)
Requires:      golang(golang.org/x/crypto/openpgp/packet)
Requires:      golang(golang.org/x/net/context)
Requires:      golang(google.golang.org/grpc)
Requires:      golang(google.golang.org/grpc/credentials)
Requires:      golang(google.golang.org/grpc/keepalive)
Requires:      golang(google.golang.org/grpc/metadata)
Requires:      golang(k8s.io/api/apps/v1beta1)
Requires:      golang(k8s.io/api/apps/v1beta2)
Requires:      golang(k8s.io/api/batch/v1)
Requires:      golang(k8s.io/api/core/v1)
Requires:      golang(k8s.io/api/extensions/v1beta1)
Requires:      golang(k8s.io/apimachinery/pkg/api/errors)
Requires:      golang(k8s.io/apimachinery/pkg/api/meta)
Requires:      golang(k8s.io/apimachinery/pkg/apis/meta/v1)
Requires:      golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
Requires:      golang(k8s.io/apimachinery/pkg/fields)
Requires:      golang(k8s.io/apimachinery/pkg/labels)
Requires:      golang(k8s.io/apimachinery/pkg/runtime)
Requires:      golang(k8s.io/apimachinery/pkg/types)
Requires:      golang(k8s.io/apimachinery/pkg/util/intstr)
Requires:      golang(k8s.io/apimachinery/pkg/util/strategicpatch)
Requires:      golang(k8s.io/apimachinery/pkg/util/validation)
Requires:      golang(k8s.io/apimachinery/pkg/util/wait)
Requires:      golang(k8s.io/apimachinery/pkg/version)
Requires:      golang(k8s.io/apimachinery/pkg/watch)
Requires:      golang(k8s.io/client-go/discovery)
Requires:      golang(k8s.io/client-go/kubernetes)
Requires:      golang(k8s.io/client-go/kubernetes/typed/core/v1)
Requires:      golang(k8s.io/client-go/kubernetes/typed/extensions/v1beta1)
Requires:      golang(k8s.io/client-go/rest)
Requires:      golang(k8s.io/client-go/tools/clientcmd)
Requires:      golang(k8s.io/client-go/tools/portforward)
Requires:      golang(k8s.io/client-go/transport/spdy)
Requires:      golang(k8s.io/client-go/util/homedir)
Requires:      golang(k8s.io/helm/pkg/chartutil)
Requires:      golang(k8s.io/helm/pkg/engine)
Requires:      golang(k8s.io/helm/pkg/getter)
Requires:      golang(k8s.io/helm/pkg/helm/environment)
Requires:      golang(k8s.io/helm/pkg/helm/helmpath)
Requires:      golang(k8s.io/helm/pkg/hooks)
Requires:      golang(k8s.io/helm/pkg/ignore)
Requires:      golang(k8s.io/helm/pkg/kube)
Requires:      golang(k8s.io/helm/pkg/lint/rules)
Requires:      golang(k8s.io/helm/pkg/lint/support)
Requires:      golang(k8s.io/helm/pkg/plugin)
Requires:      golang(k8s.io/helm/pkg/plugin/cache)
Requires:      golang(k8s.io/helm/pkg/proto/hapi/chart)
Requires:      golang(k8s.io/helm/pkg/proto/hapi/release)
Requires:      golang(k8s.io/helm/pkg/proto/hapi/rudder)
Requires:      golang(k8s.io/helm/pkg/proto/hapi/services)
Requires:      golang(k8s.io/helm/pkg/proto/hapi/version)
Requires:      golang(k8s.io/helm/pkg/provenance)
Requires:      golang(k8s.io/helm/pkg/releasetesting)
Requires:      golang(k8s.io/helm/pkg/releaseutil)
Requires:      golang(k8s.io/helm/pkg/repo)
Requires:      golang(k8s.io/helm/pkg/resolver)
Requires:      golang(k8s.io/helm/pkg/rudder)
Requires:      golang(k8s.io/helm/pkg/storage)
Requires:      golang(k8s.io/helm/pkg/storage/driver)
Requires:      golang(k8s.io/helm/pkg/strvals)
Requires:      golang(k8s.io/helm/pkg/tiller/environment)
Requires:      golang(k8s.io/helm/pkg/timeconv)
Requires:      golang(k8s.io/helm/pkg/tlsutil)
Requires:      golang(k8s.io/helm/pkg/urlutil)
Requires:      golang(k8s.io/helm/pkg/version)
Requires:      golang(k8s.io/kubernetes/pkg/api)
Requires:      golang(k8s.io/kubernetes/pkg/api/helper)
Requires:      golang(k8s.io/kubernetes/pkg/api/v1/helper)
Requires:      golang(k8s.io/kubernetes/pkg/api/v1/pod)
Requires:      golang(k8s.io/kubernetes/pkg/apis/batch)
Requires:      golang(k8s.io/kubernetes/pkg/apis/extensions)
Requires:      golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset)
Requires:      golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset/typed/core/internalversion)
Requires:      golang(k8s.io/kubernetes/pkg/client/unversioned)
Requires:      golang(k8s.io/kubernetes/pkg/controller/deployment/util)
Requires:      golang(k8s.io/kubernetes/pkg/kubectl)
Requires:      golang(k8s.io/kubernetes/pkg/kubectl/cmd/util)
Requires:      golang(k8s.io/kubernetes/pkg/kubectl/resource)
Requires:      golang(k8s.io/kubernetes/pkg/kubectl/validation)
Requires:      golang(k8s.io/kubernetes/pkg/printers)

Provides:      golang(%{import_path}/cmd/helm/installer) = %{version}-%{release}
Provides:      golang(%{import_path}/cmd/helm/search) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/chartutil) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/downloader) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/engine) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/getter) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/helm) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/helm/environment) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/helm/helmpath) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/helm/portforwarder) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/hooks) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/ignore) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/kube) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/lint) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/lint/rules) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/lint/support) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/plugin) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/plugin/cache) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/plugin/installer) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/proto/hapi/chart) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/proto/hapi/release) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/proto/hapi/rudder) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/proto/hapi/services) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/proto/hapi/version) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/provenance) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/releasetesting) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/releaseutil) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/repo) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/repo/repotest) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/resolver) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/rudder) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/storage) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/storage/driver) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/strvals) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/tiller) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/tiller/environment) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/timeconv) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/tlsutil) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/urlutil) = %{version}-%{release}
Provides:      golang(%{import_path}/pkg/version) = %{version}-%{release}

%description devel
Helm is a tool for managing Kubernetes charts.
Charts are packages of pre-configured Kubernetes
resources.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Summary:         Unit tests for %{name} package
%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(golang.org/x/crypto/openpgp/errors)
BuildRequires: golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires: golang(k8s.io/client-go/dynamic)
BuildRequires: golang(k8s.io/client-go/kubernetes/fake)
BuildRequires: golang(k8s.io/client-go/rest/fake)
BuildRequires: golang(k8s.io/client-go/testing)
BuildRequires: golang(k8s.io/helm/cmd/helm/installer)
BuildRequires: golang(k8s.io/helm/pkg/helm)
BuildRequires: golang(k8s.io/helm/pkg/repo/repotest)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/testapi)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset/fake)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/cmd/testing)
BuildRequires: golang(k8s.io/kubernetes/pkg/watch/json)
%endif

Requires:      golang(github.com/gogo/protobuf/proto)
Requires:      golang(github.com/spf13/cobra)
Requires:      golang(github.com/stretchr/testify/assert)
Requires:      golang(golang.org/x/crypto/openpgp/errors)
Requires:      golang(k8s.io/apimachinery/pkg/runtime/schema)
Requires:      golang(k8s.io/client-go/dynamic)
Requires:      golang(k8s.io/client-go/kubernetes/fake)
Requires:      golang(k8s.io/client-go/rest/fake)
Requires:      golang(k8s.io/client-go/testing)
Requires:      golang(k8s.io/helm/cmd/helm/installer)
Requires:      golang(k8s.io/helm/pkg/helm)
Requires:      golang(k8s.io/helm/pkg/repo/repotest)
Requires:      golang(k8s.io/kubernetes/pkg/api/testapi)
Requires:      golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset/fake)
Requires:      golang(k8s.io/kubernetes/pkg/kubectl/cmd/testing)
Requires:      golang(k8s.io/kubernetes/pkg/watch/json)

%description unit-test-devel
Helm is a tool for managing Kubernetes charts.
Charts are packages of pre-configured Kubernetes
resources.

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%autosetup -n %{name}-%{version}

%build

export GOPATH=$(pwd):%{gopath}
mkdir -p src/k8s.io
ln -s ../../ src/k8s.io/helm
pushd src/k8s.io/helm

glide install --strip-vendor
scripts/setup-apimachinery.sh

go install ./cmd/...
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp -pav bin/helm bin/tiller $RPM_BUILD_ROOT%{_bindir}/

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test-devel.file-list
for file in $(find . -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
# No dependency directories so far

export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/cmd/helm
%gotest %{import_path}/cmd/helm/installer
%gotest %{import_path}/cmd/helm/search
%gotest %{import_path}/cmd/tiller
%gotest %{import_path}/pkg/chartutil
%gotest %{import_path}/pkg/downloader
%gotest %{import_path}/pkg/engine
%gotest %{import_path}/pkg/getter
%gotest %{import_path}/pkg/helm
%gotest %{import_path}/pkg/helm/environment
%gotest %{import_path}/pkg/helm/helmpath
%gotest %{import_path}/pkg/helm/portforwarder
%gotest %{import_path}/pkg/ignore
%gotest %{import_path}/pkg/kube
%gotest %{import_path}/pkg/lint
%gotest %{import_path}/pkg/lint/rules
%gotest %{import_path}/pkg/lint/support
%gotest %{import_path}/pkg/plugin
%gotest %{import_path}/pkg/plugin/installer
%gotest %{import_path}/pkg/provenance
%gotest %{import_path}/pkg/releasetesting
%gotest %{import_path}/pkg/releaseutil
%gotest %{import_path}/pkg/repo
%gotest %{import_path}/pkg/repo/repotest
%gotest %{import_path}/pkg/resolver
%gotest %{import_path}/pkg/storage
%gotest %{import_path}/pkg/storage/driver
%gotest %{import_path}/pkg/strvals
%gotest %{import_path}/pkg/tiller
%gotest %{import_path}/pkg/tiller/environment
%gotest %{import_path}/pkg/timeconv
%gotest %{import_path}/pkg/tlsutil
%gotest %{import_path}/pkg/urlutil
%gotest %{import_path}/pkg/version
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%{_bindir}/helm
%{_bindir}/tiller

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%license LICENSE
%doc README.md code-of-conduct.md CONTRIBUTING.md
%endif

%changelog
* Wed Dec 14 2017 Jonh Wendell <jonh.wendell@redhat.com> - 2.7.2-1
- First package for Fedora

