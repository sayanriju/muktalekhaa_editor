#/usr/bin/env python
# coding: utf-8
## keymaps.py


###############################################################################################
##		Copyright 2007 Sayan "Riju" Chakrabarti <sayan.marchlinux@gmail.com>
##
##		This file is part of Muktalekhaa : A Bangla Phonetic Text Editor for GNU/Linux Systems
##
##      Muktalekhaa is FREE software; you can redistribute it and/or modify
##      it under the terms of the GNU General Public License as published by
##      the Free Software Foundation; either version 3 of the License, or
##      (at your option) any later version.
##       
##      This program is distributed in the hope that it will be useful,
##      but WITHOUT ANY WARRANTY; without even the implied warranty of
##      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##      GNU General Public License for more details.
##       
##      You should have received a copy of the GNU General Public License
##      along with Muktalekhaa. If not, see <http://www.gnu.org/licenses/>.
###############################################################################################


''' Keymaps: Lists the keymaps for use with engine.py '''


keymap = {}

keymap['0'] = '০';
keymap['1'] = '১';
keymap['2'] = '২';
keymap['3'] = '৩';
keymap['4'] = '৪';
keymap['5'] = '৫';
keymap['6'] = '৬';
keymap['7'] = '৭';
keymap['8'] = '৮';
keymap['9'] = '৯';

keymap['a'] = 'অ';
keymap['A'] = 'আ';
keymap['i'] = 'ই';
keymap['I'] = 'ঈ';
keymap['u'] = 'উ';
keymap['U'] = 'ঊ';
keymap['e'] = 'এ';
keymap['E'] = 'ঐ';
keymap['o'] = 'ও';
keymap['O'] = 'ঔ';
keymap['X'] = 'ঋ'; 


keymap['amatra'] = '';
keymap['Amatra'] = 'া';
keymap['imatra'] = 'ি';
keymap['Imatra'] = 'ী';
keymap['umatra'] = 'ু';
keymap['Umatra'] = 'ূ';
keymap['ematra'] = 'ে';
keymap['Ematra'] = 'ৈ';
keymap['omatra'] = 'ো';
keymap['Omatra'] = 'ৌ';
keymap['Xmatra'] = 'ৃ';


keymap['hasanta'] = '্';

keymap['k'] = 'ক';
keymap['kh'] = 'খ';
keymap['g'] = 'গ';
keymap['gh'] = 'ঘ';
keymap['G'] = 'ঙ';
keymap['c'] = 'চ';
keymap['ch'] = 'ছ';
keymap['j'] = 'জ';
keymap['jh'] = 'ঝ';
keymap['J'] = 'ঞ';
keymap['t'] = 'ত';
keymap['th'] = 'থ';
keymap['d'] = 'দ';
keymap['dh'] = 'ধ';
keymap['n'] = 'ন';
keymap['T'] = 'ট';
keymap['Th'] = 'ঠ';
keymap['D'] = 'ড';
keymap['Dh'] = 'ঢ';
keymap['N'] = 'ণ';
keymap['p'] = 'প';
keymap['ph'] = 'ফ';
keymap['b'] = 'ব';
keymap['bh'] = 'ভ';
keymap['m'] = 'ম';
keymap['Y'] = 'য';
keymap['r'] = 'র';
keymap['l'] = 'ল';
keymap['sh'] = 'শ';
keymap['S'] = 'ষ';
keymap['s'] = 'স';
keymap['h'] = 'হ';

keymap['H'] = 'ঃ';
keymap['M'] = 'ং';
keymap['C'] = 'ঁ';


keymap['W'] = 'ৎ'


keymap['y'] = 'য়';
keymap['R'] = 'ড়';
keymap['Z'] = 'ঢ়';

keymap['|'] = '।'; # daanri
#keymap['.'] = '।'; # daanri
keymap['#'] = '‌'; # zero-width non-joiner ?
keymap['`'] = '‌'; # <same> Useful to 'force' a hasanta between letters
