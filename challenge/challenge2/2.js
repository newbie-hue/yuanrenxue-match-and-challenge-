

function get_cookie() {

    var _$oa = ['TkdQTU4=', 'UVFnZGY=', 'Skl4Vlk=', 'QkVhTnc=', 'XCtcKyAqKD86W2EtekEtWl8kXVswLTlhLXpBLVpfJF0qKQ==', 'Qndsa0g=', 'U0tjTXE=', 'a2ZUWGk=', 'Wm12bGs=', 'dnV5bEU=', 'YnRvYQ==', 'dmNSY2w=', 'dGVzdA==', 'eU9zYWg=', 'ZmtSZXc=', 'QnlIeUI=', 'WVNIUkI=', 'YXNyR3g=', 'S0JTSXU=', 'VnJrUlU=', 'YWlkaW5nX3dpbg==', 'TFpKUUM=', 'U3NIWmw=', 'Y29uc3RydWN0b3I=', 'bmJETG0=', 'RFlQeVM=', 'aFF0Q2Y=', 'ZnVuY3Rpb24gKlwoICpcKQ==', 'TmhPQ2o=', 'ZVRoSHU=', 'ZFpsaGs=', 'bHRXaXM=', 'SVphcko=', 'VmNJRVQ=', 'QWpPZ0I=', 'UENGaHU=', 'c3RhdGVPYmplY3Q=', 'SWdCdkQ=', 'ZG1HSmQ=', 'Z0lTQno=', 'cEt6b3I=', 'Y2hhaW4=', 'aUNnckk=', 'ZUZUV0I=', 'dU9abGY=', 'RnJyUVA=', 'Q3hOaWw=', 'dmFsdWVPZg==', 'YXBwbHk=', 'SmNnSG0=', 'ZnBCS04=', 'cm5ET3I=', 'UUlEYnQ=', 'eEhFb20=', 'emNJR3E=', 'cm91bmQ=', 'UGVzdVY=', 'Z0JubkE=', 'b01icW8=', 'TWZDTEc=', 'dUtuUE4=', 'b0NyeEw=', 'bVBSWmg=', 'RGVDeFI=', 'ZGVidQ==', 'SVRWRFg=', 'VGtybkk=', 'dW1heFI=', 'bG9n', 'VHBRcno=', 'c2lnbj0=', 'Y291bnRlcg==', 'eFJvRFA=', 'cE13ZnI=', 'Z1pCb0Y=', 'b25qd2k=', 'Y2FsbA==', 'Y29va2ll', 'dkVaUGY=', 'dmpSTHg=', 'aU9Xa1A=', 'eVROZlU=', 'T2thaGg=', 'SGVNSUI=', 'c2JXSG4=', 'bXpDZ3o=', 'cmVsb2Fk', 'aW5wdXQ=', 'a2d6d2c=', 'YWN0aW9u', 'Z0lZVWE=', 'Rkl1SWc=', 'aUdtTmo=', 'Z1RsR2Y=', 'SVhPVWg=', 'eG5Fcmk=', 'Z2dlcg==', 'eEZOUEc=', 'TmRzS20=', 'S0NSdFE='];
    (function (a, b) {
        var c = function (f) {
            while (--f) {
                a['push'](a['shift']());
            }
        };
        c(++b);
    }(_$oa, 0x1d2));


    var _$ob = function (a, b) {
        a = a - 0x0;
        var c = _$oa[a];
        if (_$ob['ChLEzk'] === undefined) {
            (function () {
                var e = function () {
                    var h;
                    try {
                        h = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');')();
                    } catch (i) {
                        h = window;
                    }
                    return h;
                };
                var f = e();
                var g = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
                f['atob'] || (f['atob'] = function (h) {
                        var i = String(h)['replace'](/=+$/, '');
                        var j = '';
                        for (var k = 0x0, l, m, n = 0x0; m = i['charAt'](n++); ~m && (l = k % 0x4 ? l * 0x40 + m : m,
                        k++ % 0x4) ? j += String['fromCharCode'](0xff & l >> (-0x2 * k & 0x6)) : 0x0) {
                            m = g['indexOf'](m);
                        }
                        return j;
                    }
                );
            }());
            _$ob['lEFtsO'] = function (e) {
                var f = atob(e);
                var g = [];
                for (var h = 0x0, j = f['length']; h < j; h++) {
                    g += '%' + ('00' + f['charCodeAt'](h)['toString'](0x10))['slice'](-0x2);
                }
                return decodeURIComponent(g);
            }
            ;
            _$ob['vztbtz'] = {};
            _$ob['ChLEzk'] = !![];
        }
        var d = _$ob['vztbtz'][a];
        if (d === undefined) {
            c = _$ob['lEFtsO'](c);
            _$ob['vztbtz'][a] = c;
        } else {
            c = d;
        }
        return c;
    };


    var a = {
        'gZBoF': function (d, e) {
            return d + e;
        },
        'IZarJ': _$ob('0x62'),
        'VcIET': _$ob('0x1e'),
        'eFTWB': _$ob('0x46'),
        'mPRZh': function (d, e) {
            return d === e;
        },
        'rZmJI': _$ob('0x1c'),
        'dZlhk': _$ob('0x37'),
        'KCRtQ': _$ob('0x17'),
        'QIXGz': 'function\x20*\x5c(\x20*\x5c)',
        'pMwfr': _$ob('0x26'),
        'umaxR': function (d, e) {
            return d(e);
        },
        'eThHu': 'init',
        'ITVDX': function (d, e) {
            return d + e;
        },
        'BwlkH': _$ob('0x4b'),
        'gBnnA': function (d, e) {
            return d + e;
        },
        'PCFhu': 'input',
        'MfCLG': _$ob('0x4e'),
        'cjzAT': function (d, e) {
            return d === e;
        },
        'yTNfU': _$ob('0x11'),
        'gTlGf': function (d) {
            return d();
        },
        'hQtCf': function (d, e) {
            return d(e);
        },
        'uKnPN': function (d, e, f) {
            return d(e, f);
        },
        'yOsah': '此网页受【爱锭云盾\x20V1.0\x20动态版】保护',
        'JcgHm': function (d, e) {
            return d + e;
        },
        'SsHZl': _$ob('0x36'),
        'iOWkP': function (d, e) {
            return d(e);
        },
        'MXudn': function (d, e) {
            return d / e;
        },
        'SKcMq': function (d, e) {
            return d + e;
        },
        'NGPMN': function (d, e) {
            return d + e;
        },
        'vEZPf': function (d, e) {
            return d + e;
        },
        'iCgrI': function (d, e) {
            return d + e;
        },
        'xRoDP': _$ob('0x4'),
        'oMbqo': function (d, e) {
            return d / e;
        },
        'xnEri': ';\x20path=/'
    };

    var hexcase = 0;  /* hex output format. 0 - lowercase; 1 - uppercase        */
    var b64pad = ""; /* base-64 pad character. "=" for strict RFC compliance   */
    var chrsz = 8;  /* bits per input character. 8 - ASCII; 16 - Unicode      */


    function hex_md5(s) {
        return binl2hex(core_md5(str2binl(s), s.length * chrsz));
    }

    function binl2hex(binarray) {
        var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
        var str = "";
        for (var i = 0; i < binarray.length * 4; i++) {
            str += hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8 + 4)) & 0xF) +
                hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8)) & 0xF);
        }
        return str;
    }

    function core_md5(x, len) {
        /* append padding */
        x[len >> 5] |= 0x80 << ((len) % 32);
        x[(((len + 64) >>> 9) << 4) + 14] = len;

        var a = 1732584193;
        var b = -271733879;
        var c = -1732584194;
        var d = 271733878;

        for (var i = 0; i < x.length; i += 16) {
            var olda = a;
            var oldb = b;
            var oldc = c;
            var oldd = d;

            a = md5_ff(a, b, c, d, x[i + 0], 7, -680876936);
            d = md5_ff(d, a, b, c, x[i + 1], 12, -389564586);
            c = md5_ff(c, d, a, b, x[i + 2], 17, 606105819);
            b = md5_ff(b, c, d, a, x[i + 3], 22, -1044525330);
            a = md5_ff(a, b, c, d, x[i + 4], 7, -176418897);
            d = md5_ff(d, a, b, c, x[i + 5], 12, 1200080426);
            c = md5_ff(c, d, a, b, x[i + 6], 17, -1473231341);
            b = md5_ff(b, c, d, a, x[i + 7], 22, -45705983);
            a = md5_ff(a, b, c, d, x[i + 8], 7, 1770035416);
            d = md5_ff(d, a, b, c, x[i + 9], 12, -1958414417);
            c = md5_ff(c, d, a, b, x[i + 10], 17, -42063);
            b = md5_ff(b, c, d, a, x[i + 11], 22, -1990404162);
            a = md5_ff(a, b, c, d, x[i + 12], 7, 1804603682);
            d = md5_ff(d, a, b, c, x[i + 13], 12, -40341101);
            c = md5_ff(c, d, a, b, x[i + 14], 17, -1502002290);
            b = md5_ff(b, c, d, a, x[i + 15], 22, 1236535329);

            a = md5_gg(a, b, c, d, x[i + 1], 5, -165796510);
            d = md5_gg(d, a, b, c, x[i + 6], 9, -1069501632);
            c = md5_gg(c, d, a, b, x[i + 11], 14, 643717713);
            b = md5_gg(b, c, d, a, x[i + 0], 20, -373897302);
            a = md5_gg(a, b, c, d, x[i + 5], 5, -701558691);
            d = md5_gg(d, a, b, c, x[i + 10], 9, 38016083);
            c = md5_gg(c, d, a, b, x[i + 15], 14, -660478335);
            b = md5_gg(b, c, d, a, x[i + 4], 20, -405537848);
            a = md5_gg(a, b, c, d, x[i + 9], 5, 568446438);
            d = md5_gg(d, a, b, c, x[i + 14], 9, -1019803690);
            c = md5_gg(c, d, a, b, x[i + 3], 14, -187363961);
            b = md5_gg(b, c, d, a, x[i + 8], 20, 1163531501);
            a = md5_gg(a, b, c, d, x[i + 13], 5, -1444681467);
            d = md5_gg(d, a, b, c, x[i + 2], 9, -51403784);
            c = md5_gg(c, d, a, b, x[i + 7], 14, 1735328473);
            b = md5_gg(b, c, d, a, x[i + 12], 20, -1926607734);

            a = md5_hh(a, b, c, d, x[i + 5], 4, -378558);
            d = md5_hh(d, a, b, c, x[i + 8], 11, -2022574463);
            c = md5_hh(c, d, a, b, x[i + 11], 16, 1839030562);
            b = md5_hh(b, c, d, a, x[i + 14], 23, -35309556);
            a = md5_hh(a, b, c, d, x[i + 1], 4, -1530992060);
            d = md5_hh(d, a, b, c, x[i + 4], 11, 1272893353);
            c = md5_hh(c, d, a, b, x[i + 7], 16, -155497632);
            b = md5_hh(b, c, d, a, x[i + 10], 23, -1094730640);
            a = md5_hh(a, b, c, d, x[i + 13], 4, 681279174);
            d = md5_hh(d, a, b, c, x[i + 0], 11, -358537222);
            c = md5_hh(c, d, a, b, x[i + 3], 16, -722521979);
            b = md5_hh(b, c, d, a, x[i + 6], 23, 76029189);
            a = md5_hh(a, b, c, d, x[i + 9], 4, -640364487);
            d = md5_hh(d, a, b, c, x[i + 12], 11, -421815835);
            c = md5_hh(c, d, a, b, x[i + 15], 16, 530742520);
            b = md5_hh(b, c, d, a, x[i + 2], 23, -995338651);

            a = md5_ii(a, b, c, d, x[i + 0], 6, -198630844);
            d = md5_ii(d, a, b, c, x[i + 7], 10, 1126891415);
            c = md5_ii(c, d, a, b, x[i + 14], 15, -1416354905);
            b = md5_ii(b, c, d, a, x[i + 5], 21, -57434055);
            a = md5_ii(a, b, c, d, x[i + 12], 6, 1700485571);
            d = md5_ii(d, a, b, c, x[i + 3], 10, -1894986606);
            c = md5_ii(c, d, a, b, x[i + 10], 15, -1051523);
            b = md5_ii(b, c, d, a, x[i + 1], 21, -2054922799);
            a = md5_ii(a, b, c, d, x[i + 8], 6, 1873313359);
            d = md5_ii(d, a, b, c, x[i + 15], 10, -30611744);
            c = md5_ii(c, d, a, b, x[i + 6], 15, -1560198380);
            b = md5_ii(b, c, d, a, x[i + 13], 21, 1309151649);
            a = md5_ii(a, b, c, d, x[i + 4], 6, -145523070);
            d = md5_ii(d, a, b, c, x[i + 11], 10, -1120210379);
            c = md5_ii(c, d, a, b, x[i + 2], 15, 718787259);
            b = md5_ii(b, c, d, a, x[i + 9], 21, -343485551);

            a = safe_add(a, olda);
            b = safe_add(b, oldb);
            c = safe_add(c, oldc);
            d = safe_add(d, oldd);
        }
        return Array(a, b, c, d);

    }

    function md5_cmn(q, a, b, x, s, t) {
        return safe_add(bit_rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b);
    }

    function md5_ff(a, b, c, d, x, s, t) {
        return md5_cmn((b & c) | ((~b) & d), a, b, x, s, t);
    }

    function md5_gg(a, b, c, d, x, s, t) {
        return md5_cmn((b & d) | (c & (~d)), a, b, x, s, t);
    }

    function md5_hh(a, b, c, d, x, s, t) {
        return md5_cmn(b ^ c ^ d, a, b, x, s, t);
    }

    function md5_ii(a, b, c, d, x, s, t) {
        return md5_cmn(c ^ (b | (~d)), a, b, x, s, t);
    }

    /*
     * Calculate the HMAC-MD5, of a key and some data
     */


    function str2binl(str) {
        var bin = Array();
        var mask = (1 << chrsz) - 1;
        for (var i = 0; i < str.length * chrsz; i += chrsz)
            bin[i >> 5] |= (str.charCodeAt(i / chrsz) & mask) << (i % 32);
        return bin;
    }

    function safe_add(x, y) {
        var lsw = (x & 0xFFFF) + (y & 0xFFFF);
        var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
        return (msw << 16) | (lsw & 0xFFFF);
    }

    function bit_rol(num, cnt) {
        return (num << cnt) | (num >>> (32 - cnt));
    }


    window = this;
    window.btoa = function (val) {
        base64 = new Buffer.from(val).toString("base64")
        return base64
    }
    var c = new Date()[_$ob('0x51')]();
    console.log(c)
    c=1587102734000
    token = window[_$ob('0x2c')](a[_$ob('0x53')](a[_$ob('0x38')], a[_$ob('0x3c')](String, c)));
    md = a['hQtCf'](hex_md5, window[_$ob('0x2c')](a['JcgHm'](a[_$ob('0x38')], a[_$ob('0xe')](String, Math['round'](a['MXudn'](c, 0x3e8))))));
    cookie = a[_$ob('0x28')](a[_$ob('0x22')](a[_$ob('0xc')](a['iCgrI'](a[_$ob('0x4c')](a[_$ob('0x4c')](a[_$ob('0x6')], Math[_$ob('0x59')](a[_$ob('0x5c')](c, 0x3e8))), '~'), token), '|'), md), a[_$ob('0x1d')])
    console.log(cookie)
    return cookie

}
get_cookie()