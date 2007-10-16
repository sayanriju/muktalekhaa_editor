#/usr/bin/env python
# coding: utf-8
## engine.py


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



''' Engine: This is where the conversion get's done! '''


import string
from keymaps import keymap  ## load the keymaps



def mreplace(s, prv, nxt):
	if prv in s:
		s = s.replace(prv, nxt)
		return s
	else:
		return s
	

def roman2beng(intext):
		
	ans = ''
	
	## formating the input string to a suitable form for internal use!
	
	intext = mreplace(intext, 'aaY', 'w'); ## SPECIAL !! 'অ্যা' (No Specific Keymap for this!)

	
#	intext = mreplace(intext, 'tw', 'W');  ## khandyot twa
	intext = mreplace(intext, 'ng', 'M');  ## ং
	intext = mreplace(intext, 'nG', 'G'); ## ঙ
	intext = mreplace(intext, 'NG', 'J');  ## ঞ
	intext = mreplace(intext, 'NJ', 'J')   ## " "
	intext = mreplace(intext, 'z', 'Y');   ## য
	intext = mreplace(intext, 'wri', 'X'); #### ঋ
	intext = mreplace(intext, 'wr', 'X');  ## " "
	intext = mreplace(intext, '^', 'C');   ## ঁ
	intext = mreplace(intext, 't`', 'W');  ## khandyot twa
	intext = mreplace(intext, 'Rh', 'Z');  ## 'ঢ়'
	
	intext = mreplace(intext, '`', '`#');	
	
	intext = mreplace(intext, 'b ', 'ba ');
	intext = mreplace(intext, 'c ', 'ca ');
	intext = mreplace(intext, 'd ', 'da ');
	intext = mreplace(intext, 'f ', 'fa ');
	intext = mreplace(intext, 'g ', 'ga ');
	intext = mreplace(intext, 'h ', 'ha ');
	intext = mreplace(intext, 'j ', 'ja ');
	intext = mreplace(intext, 'k ', 'ka ');
	intext = mreplace(intext, 'l ', 'la ');
	intext = mreplace(intext, 'm ', 'ma ');
	intext = mreplace(intext, 'n ', 'na ');
	intext = mreplace(intext, 'p ', 'pa ');
	intext = mreplace(intext, 'r ', 'ra ');
	intext = mreplace(intext, 's ', 'sa ');
	intext = mreplace(intext, 't ', 'ta ');
	intext = mreplace(intext, 'v ', 'va ');
	intext = mreplace(intext, 'Y ', 'Ya ');
	
	intext = mreplace(intext, 'Z ', 'Za ');
	intext = mreplace(intext, 'R ', 'Ra ');
	

	intext = mreplace(intext, 'D ', 'Da ');
	intext = mreplace(intext, 'G ', 'Ga ');
	intext = mreplace(intext, 'J ', 'Ja ');
	intext = mreplace(intext, 'N ', 'Na ');
	intext = mreplace(intext, 'S ', 'Sa ');
	intext = mreplace(intext, 'T ', 'Ta ');
	intext = mreplace(intext, 'y ', 'ya ');
	intext = mreplace(intext, 'W', 'W`');
	

	#intext = mreplace(intext, '. ', '.a ');
	

	
	
	if '|' in intext:
		intext = mreplace(intext, 'b|', 'ba|');
		intext = mreplace(intext, 'c|', 'ca|');
		intext = mreplace(intext, 'd|', 'da|');
		intext = mreplace(intext, 'f|', 'fa|');
		intext = mreplace(intext, 'g|', 'ga|');
		intext = mreplace(intext, 'h|', 'ha|');
		intext = mreplace(intext, 'j|', 'ja|');
		intext = mreplace(intext, 'k|', 'ka|');
		intext = mreplace(intext, 'l|', 'la|');
		intext = mreplace(intext, 'm|', 'ma|');
		intext = mreplace(intext, 'n|', 'na|');
		intext = mreplace(intext, 'p|', 'pa|');
		intext = mreplace(intext, 'r|', 'ra|');
		intext = mreplace(intext, 's|', 'sa|');
		intext = mreplace(intext, 't|', 'ta|');
		intext = mreplace(intext, 'v|', 'va|');
		intext = mreplace(intext, 'Y|', 'Ya|');

		intext = mreplace(intext, 'D|', 'Da|');
		intext = mreplace(intext, 'G|', 'Ga|');
		intext = mreplace(intext, 'J|', 'Ja|');
		intext = mreplace(intext, 'N|', 'Na|');
		intext = mreplace(intext, 'S|', 'Sa|');
		intext = mreplace(intext, 'T|', 'Ta|');
		intext = mreplace(intext, 'y|', 'ya|');

		intext = mreplace(intext, '.|', '.a|');
		
	intext = mreplace(intext, 'aa', 'A');
	intext = mreplace(intext, 'ii', 'I');
	intext = mreplace(intext, 'ee', 'I');
	intext = mreplace(intext, 'uu', 'U');
	intext = mreplace(intext, 'ai', 'E');
	intext = mreplace(intext, 'au', 'O');
	#intext = mreplace(intext, 'Ri', 'R');   ## needed ?

	intext = mreplace(intext, 'chh', 'TMPUNIKSTR');
	intext = mreplace(intext, 'ch', 'c');
	intext = mreplace(intext, 'TMPUNIKSTR', 'ch');
	intext = mreplace(intext, 'GN', 'G');
	intext = mreplace(intext, 'JN', 'J');
	
	intext = mreplace(intext, 'Sh', 'S');
	
	
	intext = mreplace(intext, '.n', 'M');
	intext = mreplace(intext, '.N', 'C');
	intext = mreplace(intext, '.Y', 'y');
	intext = mreplace(intext, '.Dh', 'Z');
	#intext = mreplace(intext, '.D', 'X');
	#intext = mreplace(intext, 'Dh.', 'Z');
	#intext = mreplace(intext, 'D.', 'X');
	#intext = mreplace(intext, ':', 'H');

	intext = mreplace(intext, 'f', 'ph');
	intext = mreplace(intext, 'v', 'bh');

	intext = mreplace(intext, '_', '');
	
	
	
	## Main conversion to bengali begins!
	i = 0
	#global len
	intext_len = len(intext)
	
	while i < intext_len:
		cur = intext[i]
		if i+1 < intext_len:
			next = intext[i+1]
		else:
			next = ''
			
		comb = cur + next
	
	## mainly the 'vowels'  list (first 12 are swarabarna which also acts as matra)
		list1 = ['a','A','i','I','u','U','e','E','o','O','X','M','H','C','^','|','#','W','`'] 
		## mainly the 'consonants' list
		list2 = ['k','g','G','c','j','J','t','d','n','T','D','N','p','b','m','s','h','Y','r','I','R','y','Z','S','l'] 


		if cur in list1 or (cur >= '0' and cur <= '9'):
			ans += keymap[cur]
			i += 1
		
		elif cur in list2:
			## more consonants list
			list3 = ['kh','gh','ch','jh','th','dh','Th','Dh','ph','bh','sh']

			if comb in list3:
				cur =  comb
				i +=1
				if i+1 < intext_len:
					next  = intext[i+1]
				else:
					next  = ''
	
			if next in list1[:11]: ## this lists the swarabarna / matra
				ans += (keymap[cur] + keymap[next+'matra'])
				i += 2
			elif next != '':
				ans += (keymap[cur] + keymap['hasanta'])
				i += 1
			###### trying to remove trailing hasanta for words ending with 'a kaar' 
			else :
				ans += keymap[cur]
				i += 1
		elif cur == 'w': ## SPECIAL !!!  'অ্যা'
			ans += 'অ্যা'
			i += 1
		
		else:
			ans += cur
			i += 1

	
	return ans 
