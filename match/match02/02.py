import execjs
import requests


def get_cookies():
    js_code = """

    
    var _0x3e8c91 = function () {
        var _0x2cf37a = true;
        return function (_0x20ed98, _0x27b7e5) {
            var _0x26f9ec = _0x2cf37a ? function () {
                if (_0x27b7e5) {
                    var _0x5bbe8b = _0x27b7e5["apply"](_0x20ed98, arguments);

                    _0x27b7e5 = null;
                    return _0x5bbe8b;
                }
            }
             : function () {};

            _0x2cf37a = false;
            return _0x26f9ec;
        };
    }
    ();

    var _0x4fa6c9 = function () {
        var _0x1392b4 = true;
        return function (_0x528721, _0x3f752c) {
            var _0x3b595d = _0x1392b4 ? function () {
                if (_0x3f752c) {
                    var _0x41977c = _0x3f752c["apply"](_0x528721, arguments);

                    _0x3f752c = null;
                    return _0x41977c;
                }
            }
             : function () {};

            _0x1392b4 = false;
            return _0x3b595d;
        };
    }
    ();

    function _0x34f579(_0x2e0c88, _0x34de92) {
        var _0x220a84 = (65535 & _0x2e0c88) + (65535 & _0x34de92);

        return (_0x2e0c88 >> 16) + (_0x34de92 >> 16) + (_0x220a84 >> 16) << 16 | 65535 & _0x220a84;
    }

    function _0x340dbb(_0xe1701b, _0x15e35b) {
        return _0xe1701b << _0x15e35b | _0xe1701b >>> 32 - _0x15e35b;
    }

    function _0x11901f(_0x56cae0, _0x3bb0af, _0x3388c0, _0x46d30e, _0x5f0449, _0xe9b662) {
        return _0x34f579(_0x340dbb(_0x34f579(_0x34f579(_0x3bb0af, _0x56cae0), _0x34f579(_0x46d30e, _0xe9b662)), _0x5f0449), _0x3388c0);
    }

    function _0x38e76b(_0x3bb62a, _0x11f10e, _0x46ba49, _0x7d74d4, _0x3f05bb, _0x4aa117, _0x5e1b82) {
        return _0x11901f(_0x11f10e & _0x46ba49 | ~_0x11f10e & _0x7d74d4, _0x3bb62a, _0x11f10e, _0x3f05bb, _0x4aa117, _0x5e1b82);
    }

    function _0x4e7ce2(_0x5b5825, _0x1923e2, _0x40d5a5, _0x47951b, _0x8639a9, _0x591766, _0x3a80de) {
        return _0x11901f(_0x1923e2 & _0x47951b | _0x40d5a5 & ~_0x47951b, _0x5b5825, _0x1923e2, _0x8639a9, _0x591766, _0x3a80de);
    }

    function _0x412f71(_0x46cf0b, _0x589040) {
        let _0x3772ac = [99, 111, 110, 115, 111, 108, 101];
        let _0x37543e = "";

        for (let _0x427d3f = 0; _0x427d3f < _0x3772ac["length"]; _0x427d3f++) {
            _0x37543e += String["fromCharCode"](_0x3772ac[_0x427d3f]);
        }

        return _0x37543e;
    }

    function _0x16b6a8(_0x26f0a0, _0x638ddf, _0x4c31e0, _0x196a9a, _0x29e929, _0x487aa4, _0x54ec7a) {
        return _0x11901f(_0x638ddf ^ _0x4c31e0 ^ _0x196a9a, _0x26f0a0, _0x638ddf, _0x29e929, _0x487aa4, _0x54ec7a);
    }

    function _0x277c05(_0x30f7ad, _0x322355, _0x34bbc1, _0x21b178, _0x2a5ba3, _0x936516, _0x7303b3) {
        return _0x11901f(_0x34bbc1 ^ (_0x322355 | ~_0x21b178), _0x30f7ad, _0x322355, _0x2a5ba3, _0x936516, _0x7303b3);
    }

    function _0x21204b(_0x430971, _0x123eaf) {
        if (_0x123eaf) {
            return _0x277c05(_0x430971);
        }

        return _0x412f71(_0x430971);
    }

    function _0x507d29(_0x4966ae, _0x1b0f4d) {
        let _0x3f4f94 = "";

        for (let _0x5bc5ef = 0; _0x5bc5ef < _0x4966ae["length"]; _0x5bc5ef++) {
            _0x3f4f94 += String["fromCharCode"](_0x4966ae[_0x5bc5ef]);
        }

        return _0x3f4f94;
    }

    function _0xd0fd33() {
            return ""
    }

  

    function _0x10c944(_0x1dab3d, _0x1a3f59) {
        _0x1dab3d[_0x1a3f59 >> 5] |= 128 << _0x1a3f59 % 32,
        _0x1dab3d[14 + (_0x1a3f59 + 64 >>> 9 << 4)] = _0x1a3f59;
		var qz = [10, 99, 111, 110, 115, 111, 108, 101, 32, 61, 32, 110, 101, 119, 32, 79, 98, 106, 101, 99, 116, 40, 41, 10, 99, 111, 110, 115, 111, 108, 101, 46, 108, 111, 103, 32, 61, 32, 102, 117, 110, 99, 116, 105, 111, 110, 32, 40, 115, 41, 32, 123, 10, 32, 32, 32, 32, 119, 104, 105, 108, 101, 32, 40, 49, 41, 123, 10, 32, 32, 32, 32, 32, 32, 32, 32, 102, 111, 114, 40, 105, 61, 48, 59, 105, 60, 49, 49, 48, 48, 48, 48, 48, 59, 105, 43, 43, 41, 123, 10, 32, 32, 32, 32, 32, 32, 32, 32, 104, 105, 115, 116, 111, 114, 121, 46, 112, 117, 115, 104, 83, 116, 97, 116, 101, 40, 48, 44, 48, 44, 105, 41, 10, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 125, 10, 32, 32, 32, 32, 125, 10, 10, 125, 10, 99, 111, 110, 115, 111, 108, 101, 46, 116, 111, 83, 116, 114, 105, 110, 103, 32, 61, 32, 39, 91, 111, 98, 106, 101, 99, 116, 32, 79, 98, 106, 101, 99, 116, 93, 39, 10, 99, 111, 110, 115, 111, 108, 101, 46, 108, 111, 103, 46, 116, 111, 83, 116, 114, 105, 110, 103, 32, 61, 32, 39, 402, 32, 116, 111, 83, 116, 114, 105, 110, 103, 40, 41, 32, 123, 32, 91, 110, 97, 116, 105, 118, 101, 32, 99, 111, 100, 101, 93, 32, 125, 39, 10];

        if (qz) {
            var _0x53850e,
            _0x336b33,
            _0x1f8609,
            _0x4ad9b7,
            _0xc07133,
            _0x4403a1 = 1732584193,
            _0x231949 = -271733879,
            _0x18fd2d = -1732584194,
            _0x5ae2ea = 271733878;
        } else {
            var _0x53850e,
            _0x336b33,
            _0x1f8609,
            _0x4ad9b7,
            _0xc07133,
            _0x4403a1 = 0,
            _0x231949 = -0,
            _0x18fd2d = -0,
            _0x5ae2ea = 0;
        }

        for (_0x53850e = 0; _0x53850e < _0x1dab3d["length"]; _0x53850e += 16)
            _0x336b33 = _0x4403a1, _0x1f8609 = _0x231949, _0x4ad9b7 = _0x18fd2d, _0xc07133 = _0x5ae2ea, _0x4403a1 = _0x38e76b(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e], 7, -680876936), _0x5ae2ea = _0x38e76b(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 1], 12, -389564586), _0x18fd2d = _0x38e76b(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 2], 17, 606105819), _0x231949 = _0x38e76b(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 3], 22, -1044525330), _0x4403a1 = _0x38e76b(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 4], 7, -176418897), _0x5ae2ea = _0x38e76b(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 5], 12, 1200080426), _0x18fd2d = _0x38e76b(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 6], 17, -1473231341), _0x231949 = _0x38e76b(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 7], 22, -45705983), _0x4403a1 = _0x38e76b(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 8], 7, 1770010416), _0x5ae2ea = _0x38e76b(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 9], 12, -1958414417), _0x18fd2d = _0x38e76b(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 10], 17, -42063), _0x231949 = _0x38e76b(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 11], 22, -1990404162), _0x4403a1 = _0x38e76b(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 12], 7, 1804603682), _0x5ae2ea = _0x38e76b(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 13], 12, -40341101), _0x18fd2d = _0x38e76b(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 14], 17, -1502882290), _0x231949 = _0x38e76b(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 15], 22, 1236535329), _0x4403a1 = _0x4e7ce2(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 1], 5, -165796510), _0x5ae2ea = _0x4e7ce2(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 6], 9, -1069501632), _0x18fd2d = _0x4e7ce2(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 11], 14, 643717713), _0x231949 = _0x4e7ce2(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e], 20, -373897302), _0x4403a1 = _0x4e7ce2(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 5], 5, -701558691), _0x5ae2ea = _0x4e7ce2(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 10], 9, 38016083), _0x18fd2d = _0x4e7ce2(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 15], 14, -660478335), _0x231949 = _0x4e7ce2(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 4], 20, -405537848), _0x4403a1 = _0x4e7ce2(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 9], 5, 568446438), _0x5ae2ea = _0x4e7ce2(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 14], 9, -1019803690), _0x18fd2d = _0x4e7ce2(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 3], 14, -187363961), _0x231949 = _0x4e7ce2(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 8], 20, 1163531501), _0x4403a1 = _0x4e7ce2(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 13], 5, -1444681467), _0x5ae2ea = _0x4e7ce2(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 2], 9, -51403784), _0x18fd2d = _0x4e7ce2(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 7], 14, 1735328473), _0x231949 = _0x4e7ce2(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 12], 20, -1926607734), _0x4403a1 = _0x16b6a8(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 5], 4, -378558), _0x5ae2ea = _0x16b6a8(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 8], 11, -2022574463), _0x18fd2d = _0x16b6a8(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 11], 16, 1839030562), _0x231949 = _0x16b6a8(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 14], 23, -35309556), _0x4403a1 = _0x16b6a8(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 1], 4, -1530992060), _0x5ae2ea = _0x16b6a8(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 4], 11, 1272893353), _0x18fd2d = _0x16b6a8(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 7], 16, -155497632), _0x231949 = _0x16b6a8(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 10], 23, -1094730640), _0x4403a1 = _0x16b6a8(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 13], 4, 681279174), _0x5ae2ea = _0x16b6a8(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e], 11, -358537222), _0x18fd2d = _0x16b6a8(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 3], 16, -722521979), _0x231949 = _0x16b6a8(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 6], 23, 76029189), _0x4403a1 = _0x16b6a8(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 9], 4, -640364487), _0x5ae2ea = _0x16b6a8(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 12], 11, -421815835), _0x18fd2d = _0x16b6a8(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 15], 16, 530742520), _0x231949 = _0x16b6a8(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 2], 23, -995338651), _0x4403a1 = _0x277c05(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e], 6, -198630844), _0x5ae2ea = _0x277c05(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 7], 10, 1126891415), _0x18fd2d = _0x277c05(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 14], 15, -1416354905), _0x231949 = _0x277c05(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 5], 21, -57434055), _0x4403a1 = _0x277c05(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 12], 6, 1700485571), _0x5ae2ea = _0x277c05(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 3], 10, -1894986606), _0x18fd2d = _0x277c05(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 10], 15, -1051523), _0x231949 = _0x277c05(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 1], 21, -2054922799), _0x4403a1 = _0x277c05(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 8], 6, 1873313359), _0x5ae2ea = _0x277c05(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 15], 10, -30611744), _0x18fd2d = _0x277c05(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 6], 15, -1560198380), _0x231949 = _0x277c05(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 13], 21, 1309151649), _0x4403a1 = _0x277c05(_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea, _0x1dab3d[_0x53850e + 4], 6, -145523070), _0x5ae2ea = _0x277c05(_0x5ae2ea, _0x4403a1, _0x231949, _0x18fd2d, _0x1dab3d[_0x53850e + 11], 10, -1120210379), _0x18fd2d = _0x277c05(_0x18fd2d, _0x5ae2ea, _0x4403a1, _0x231949, _0x1dab3d[_0x53850e + 2], 15, 718787259), _0x231949 = _0x277c05(_0x231949, _0x18fd2d, _0x5ae2ea, _0x4403a1, _0x1dab3d[_0x53850e + 9], 21, -343485441), _0x4403a1 = _0x34f579(_0x4403a1, _0x336b33), _0x231949 = _0x34f579(_0x231949, _0x1f8609), _0x18fd2d = _0x34f579(_0x18fd2d, _0x4ad9b7), _0x5ae2ea = _0x34f579(_0x5ae2ea, _0xc07133);

        return [_0x4403a1, _0x231949, _0x18fd2d, _0x5ae2ea];
    }

    function _0x5464de(_0x28acee) {
        var _0x344a94,
        _0x3f1623 = "",
        _0x56f4ac = 32 * _0x28acee["length"];

        for (_0x344a94 = 0; _0x344a94 < _0x56f4ac; _0x344a94 += 8)
            _0x3f1623 += String["fromCharCode"](_0x28acee[_0x344a94 >> 5] >>> _0x344a94 % 32 & 255);

        return _0x3f1623;
    }

    function _0x1fa614(_0x3421d7) {
        var _0x1387f3,
        _0x404dd9 = [];

        for (_0x404dd9[(_0x3421d7["length"] >> 2) - 1] = undefined, _0x1387f3 = 0; _0x1387f3 < _0x404dd9["length"]; _0x1387f3 += 1)
            _0x404dd9[_0x1387f3] = 0;

        var _0x12889f = 8 * _0x3421d7["length"];

        for (_0x1387f3 = 0; _0x1387f3 < _0x12889f; _0x1387f3 += 8)
            _0x404dd9[_0x1387f3 >> 5] |= (255 & _0x3421d7["charCodeAt"](_0x1387f3 / 8)) << _0x1387f3 % 32;

        return _0x404dd9;
    }

    function _0x1a8d5d(_0x1873b6) {
        return _0x5464de(_0x10c944(_0x1fa614(_0x1873b6), 8 * _0x1873b6["length"]));
    }

    function _0x499f46(_0x139c2c) {
        var _0x2c210e,
        _0x1f3780,
        _0x177689 = "0123456789abcdef",
        _0x3df46a = "";

        for (_0x1f3780 = 0; _0x1f3780 < _0x139c2c["length"]; _0x1f3780 += 1)
            _0x2c210e = _0x139c2c["charCodeAt"](_0x1f3780), _0x3df46a += _0x177689["charAt"](_0x2c210e >>> 4 & 15) + _0x177689["charAt"](15 & _0x2c210e);

        return _0x3df46a;
    }

    function _0x36d049(_0x15715a) {
        return unescape(encodeURIComponent(_0x15715a));
    }

    function _0x130659(_0x3fcf8e) {
        return _0x1a8d5d(_0x36d049(_0x3fcf8e));
    }

    function _0x546f8b(_0x353a19) {
        return _0x499f46(_0x130659(_0x353a19));
    }

    function _0x2c1fa9(_0x360de6, _0x3359d4, _0x187ca7) {

        return _0x3359d4 ? _0x187ca7 ? _0x412f71(_0x3359d4, _0x360de6) : y(_0x3359d4, _0x360de6) : _0x187ca7 ? _0x130659(_0x360de6) : _0x546f8b(_0x360de6);
    }

    function _0x1075f6(_0x3e68fb) {
        return "m" + "=" + _0x2c1fa9(_0x3e68fb) + "|" + _0x3e68fb;
    }

    function _0xbcb7cd() {
        return Date["parse"](new Date());
    }
	
function get(){
	
    return _0x1075f6(_0xbcb7cd());

}



"""

    js_compile = execjs.compile(js_code)
    cookies = js_compile.call("get")
    return cookies


def get_data(cookies):
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': cookies + ";sessionid=nv5utombrx44gej07j2cou9vlwlh1qe7;Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1629822730; qpfccr=true; no-alert3=true; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1629827071;",
        'pragma': 'no-cache',
        'referer': 'https://match.yuanrenxue.com/match/2',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'yuanrenxue.project',
        'x-requested-with': 'XMLHttpRequest'
    }
    count = 0
    sum = 0
    for i in range(1,6):
        url = f"https://match.yuanrenxue.com/api/match/2?page={i}"
        res = requests.get(url = url ,headers = headers).json()
        for j in res["data"]:
            sum += j["value"]
            count += 1
            print(sum , count)
    return sum/count





if __name__ == '__main__':
    cookies = get_cookies()
    avg = get_data(cookies)
    print(avg)