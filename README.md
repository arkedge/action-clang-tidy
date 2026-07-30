# GitHub Actions: Run clang-tidy with reviewdog

This action runs [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) with [reviewdog](https://github.com/reviewdog/reviewdog).

## Example Usage

```yaml
name: Build & clang-tidy
on: [pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: CMake
      env:
        CC: clang
      run: cmake -B ./build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    - name: reviewdog with clang-tidy
      uses: arkedge/action-clang-tidy
      with:
        workdir: ./build
    - name: Build
     run: cmake --build ./build
```

## clang-tidy version

`clang-tidy` is installed from the runner's apt repositories, so the available
versions depend on the Ubuntu release:

| | Ubuntu 22.04 | Ubuntu 24.04 |
|---|---|---|
| `clang-tidy-11` | ✅ | ❌ not packaged |
| `clang-tidy-14` | ✅ | ✅ |
| `clang-tidy-18` | ❌ not packaged | ✅ |

`clang_tidy_version` defaults to `14`, the only version packaged by both, so
the action works on `ubuntu-22.04`, `ubuntu-24.04` and `ubuntu-latest`.
Override it to pick a different one:

```yaml
    - uses: arkedge/action-clang-tidy
      with:
        workdir: ./build
        clang_tidy_version: '18'   # ubuntu-24.04 only
```
