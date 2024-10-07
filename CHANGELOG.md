# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.7] - 2024-10-09
### Added
- 2 new programs
	1. `mate`
	2. `french-press`
- 9 new tones
### Changed
- `README.md` updated
## [1.6] - 2024-08-30
### Added
- 2 new programs
	1. `puer-tea`
	2. `purple-tea`
- `--set-on` argument
### Changed
- Default mode changed from `count-up` to `countdown`
- `white-tea` program duration changed from `10` minutes to `3` minutes
## [1.5] - 2024-08-12
### Added
- 2 new programs
	1. `rooibos-tea`
	2. `yellow-tea`
- `--keep-on` argument
### Changed
- `README.md` updated
- Programs message updated
## [1.4] - 2024-07-15
### Added
- 1 new program
	1. `mid-break`
- `--repeat` argument
- `--sign` argument
### Changed
- `long-break` program duration changed from `15` minutes to `30` minutes
- `README.md` updated
## [1.3] - 2024-05-23
### Added
- 1 new program
	1. `animedoro`
- `two_step_timer` function
- `print_message` function
- `SECURITY.md`
### Changed
- Test system modified
- `nava` added to `requirements.txt`
- Sound playing system updated
- Python 3.5 dropped
- `short-break` program duration changed from `10` minutes to `5` minutes
- `long-break` program duration changed from `30` minutes to `15` minutes
- `pomodoro` program updated
- `pomodoro_timer` function modified
- `load_params` function modified
- `README.md` updated
### Removed
- `animedoro_timer` function
- `_112_26_timer` function
- `_52_17_timer` function
## [1.2] - 2024-02-05
### Added
- `feature_request.yml` template
- `config.yml` for issue template
- 2 new programs
	1. `52-17`
	2. `112-26`
### Changed
- Bug report template modified
- `run_timer` function modified
## [1.1] - 2023-12-20
### Added
- 1 new program
	1. `pomodoro`
### Changed
- `TIME_PRINT_TEMPLATE` changed
- `KeyboardInterrupt` exit handling updated
- `ADDITIONAL_INFO` added to argparser epilog
- `Python 3.12` added to `test.yml`
## [1.0] - 2023-11-08
### Added
- `--programs-list` argument
- `--faces-list` argument
- `--v-shift` argument
- `--h-shift` argument
- `DEFAULT_PARAMS` parameter
- `PROGRAMS_DEFAULTS` parameter
- `load_program_params` function
### Changed
- `japanese-green-tea` program bug fixed
- `README.md` updated
## [0.9] - 2023-10-04
### Added
- 4 new faces
- 4 new programs
	1. `work`
	2. `short-break`
	3. `long-break`
	4. `noodle`
### Changed
- `PROGRAMS.md` updated
## [0.8] - 2023-08-07
### Added
- Logo
- `--alarm-repeat` argument
### Changed
- Tones length modified
- `README.md` updated
## [0.7] - 2023-07-23
### Added
- `--tone` argument
- `TONES.md`
- 9 new tones
### Changed
- Test system modified
- `input_check` decorator renamed to `input_handler`
- `countup_timer` function inputs modified
- `countdown_timer` function inputs modified
- `PROGRAMS.md` updated
- `FACES.md` updated
## [0.6] - 2023-07-04
### Added
- `--program` argument
- `PROGRAMS.md`
- `run_timer` function
### Changed
- Inputs type changed to `int`
- `README.md` updated
- `WRONG_INPUT_ERROR` renamed to `INPUT_ERROR_MESSAGE`
- Alarm tone changed
## [0.5] - 2023-05-25
### Added
- 5 new faces
- `--message` argument
### Changed
- `play_sound` function modified
- `playsound` removed from `requirements.txt`
- `README.md` updated
## [0.4] - 2023-02-10
### Added
- 4 new faces
- Infinite timer mode
### Changed
- `README.md` updated
- Parameters moved to `params.py`
## [0.3] - 2022-11-25
### Added
- `--face` argument
- `FACES.md`
### Changed
- `README.md` updated
- Minimum `art` library version changed from `1.8` to `2.9`
## [0.2] - 2022-11-03
### Added
- `--version` flag
### Changed
- Test system modified
- `countdown_timer` function modified
- `countup_timer` function modified
## [0.1] - 2022-10-18
### Added
- Countdown mode
- Count-up mode
- Alarm

[Unreleased]: https://github.com/sepandhaghighi/mytimer/compare/v1.7...dev
[1.7]: https://github.com/sepandhaghighi/mytimer/compare/v1.6...v1.7
[1.6]: https://github.com/sepandhaghighi/mytimer/compare/v1.5...v1.6
[1.5]: https://github.com/sepandhaghighi/mytimer/compare/v1.4...v1.5
[1.4]: https://github.com/sepandhaghighi/mytimer/compare/v1.3...v1.4
[1.3]: https://github.com/sepandhaghighi/mytimer/compare/v1.2...v1.3
[1.2]: https://github.com/sepandhaghighi/mytimer/compare/v1.1...v1.2
[1.1]: https://github.com/sepandhaghighi/mytimer/compare/v1.0...v1.1
[1.0]: https://github.com/sepandhaghighi/mytimer/compare/v0.9...v1.0
[0.9]: https://github.com/sepandhaghighi/mytimer/compare/v0.8...v0.9
[0.8]: https://github.com/sepandhaghighi/mytimer/compare/v0.7...v0.8
[0.7]: https://github.com/sepandhaghighi/mytimer/compare/v0.6...v0.7
[0.6]: https://github.com/sepandhaghighi/mytimer/compare/v0.5...v0.6
[0.5]: https://github.com/sepandhaghighi/mytimer/compare/v0.4...v0.5
[0.4]: https://github.com/sepandhaghighi/mytimer/compare/v0.3...v0.4
[0.3]: https://github.com/sepandhaghighi/mytimer/compare/v0.2...v0.3
[0.2]: https://github.com/sepandhaghighi/mytimer/compare/v0.1...v0.2
[0.1]: https://github.com/sepandhaghighi/mytimer/compare/daa2be6...v0.1



