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
