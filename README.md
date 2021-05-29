![](https://cdn-images-1.medium.com/max/800/1*MXlAZ9fzOBiBvjEErVn3Fw.png)
<br><center><span class="figcaption_hack">SOLUTIONS’21</span></center>

<h1>### ByPass CTF 2021 Write-up ###</h1>

#### <The quieter you become, the more you are able to hear/>

You can find the homepage for this CTF
[here](https://bypassctf.solutions21.in/).

### WEB

1.  **FBIescape(100 | Easy)**

    FBI is looking for you so don’t get tracked buddy I know you can use your head and run away. Link → 

Add Do Not Track Header and use HEAD request by following:

    Linux: curl -X HEAD 
     -H “DNT:1”

    Windows: curl head 
     -H “DNT:1”

![](https://cdn-images-1.medium.com/max/800/1*DcsPHKA90MbJidNmlRaF3w.png)
<br><span class="figcaption_hack">HEADER Content</span>

**2. BlackClover(250 | Medium)**

    Welcome to clover kingdom :) visit here : 

By enumerating the directory using tools like dirsearch, you’ll get a
security.txt as *.well-known/security.txt *giving a hint as **devil **indicating
that we can do an LFI attack on this parameter using this:

    curl -X POST 
     -d "devil=php://filter/resource=/flag”

![](https://cdn-images-1.medium.com/max/800/1*-biwOG8dli9U_qFZV7XLMg.png)
<br><span class="figcaption_hack">FLAG</span>

**3. SHAttered(500 | Hard)**

    Prove me that you can shatter my page and get the flag. 

1. This challenge is based on broken sha1 algo. <br> 2. You need to pass first
500 bytes from pdf of shattered or make your own then pass them in name and
password parameters.

    curl -X POST http://168.63.250.254/ -d "name=%25PDF-1.3%0A%25%E2%E3%CF%D3%0A%0A%0A1%20%0A%3C%3C/Width%202%200%20R/Height%203%200%20R/Type%204%200%20R/Subtype%205%200%20R/Filter%206%200%20R/ColorSpace%207%200%20R/Length%208%200%20R/BitsPerComponent%208%3E%3E%0Astream%0A%FF%D8%FF%FE%00%24SHA-1%20is%20dead%21%21%21%21%21%85/%EC%09%239u%9C9%B1%A1%C6%3CL%97%E1%FF%FE%01%7FF%DC%93%A6%B6%7E%01%3B%02%9A%AA%1D%B2V%0BE%CAg%D6%88%C7%F8K%8CLy%1F%E0%2B%3D%F6%14%F8m%B1i%09%01%C5kE%C1S%0A%FE%DF%B7%608%E9rr/%E7%ADr%8F%0EI%04%E0F%C20W%0F%E9%D4%13%98%AB%E1.%F5%BC%94%2B%E35B%A4%80-%98%B5%D7%0F%2A3.%C3%7F%AC5%14%E7M%DC%0F%2C%C1%A8t%CD%0Cx0Z%21Vda0%97%89%60k%D0%BF%3F%98%CD%A8%04F%29%A1&password=%25PDF-1.3%0A%25%E2%E3%CF%D3%0A%0A%0A1%200%20obj%0A%3C%3C/Width%202%200%20R/Height%203%200%20R/Type%204%200%20R/Subtype%205%200%20R/Filter%206%200%20R/ColorSpace%207%200%20R/Length%208%200%20R/BitsPerComponent%208%3E%3E%0Astream%0A%FF%D8%FF%FE%00%24SHA-1%20is%20dead%21%21%21%21%21%85/%EC%09%239u%9C9%B1%A1%C6%3CL%97%E1%FF%FE%01sF%DC%91f%B6%7E%11%8F%02%9A%B6%21%B2V%0F%F9%CAg%CC%A8%C7%F8%5B%A8Ly%03%0C%2B%3D%E2%18%F8m%B3%A9%09%01%D5%DFE%C1O%26%FE%DF%B3%DC8%E9j%C2/%E7%BDr%8F%0EE%BC%E0F%D2%3CW%0F%EB%14%13%98%BBU.%F5%A0%A8%2B%E31%FE%A4%807%B8%B5%D7%1F%0E3.%DF%93%AC5%00%EBM%DC%0D%EC%C1%A8dy%0Cx%2Cv%21V%60%DD0%97%91%D0k%D0%AF%3F%98%CD%A4%BCF%29%B1"

Note: Try on Linux if doesn’t works on Windows.

![](https://cdn-images-1.medium.com/max/800/1*FazmL-XlBGjrzLL43PUaLw.png)
<br><span class="figcaption_hack">FLAG</span>

### CRYPTO

1.  **RSA 1.0(100 | Easy)**

    I use RSA to encrypt my important secret for my Friend SinText. But I wrote the modulus and it’s factor information on the paper, it got damaged and last 3 digit of modulus is destroyed. can you help me get it back?

    N = 82072959455291134430563846735070417499964928796236988322554005385529891380454429820523001982189930383032515888996968014624392597103513494998868953162343211815354731296297261483197603923999547977295270517234626139219302306781866644678661575761618700545242197533298123803493373168687939328408337464956713770???

    p = 10360184456717574681896651194799048522521497531075966964675714395201430858140056615057039697058381933640865435287871899192220478151593121946193481408306881

    C = 6292644989386796193348492370545740273664058837038634745612645174532766902483284019555228550093470957822473132152865230847185710465249785765142987472021602906043306826153132401262351131589976399086573748065754319695439588189721375438144967964513379281001634528629508904527213906356657761404930106587935568625

This challenge is simple RSA just you have to brute-force all the last three
combination for n and divide it by p to get q and also verify if q which we’ve
got is prime or not, if it is prime then try to decode the encrypted flag.
Here’s the Python script for the above mentioned process.

![](https://cdn-images-1.medium.com/max/800/1*faYPrJawSAWqUiVPLFvZKw.png)
<br><span class="figcaption_hack">FLAG</span>

**2. Little_Information_Leaks_A_Lot(250 | Medium)**

    I xored my secret file and I noted the time when I did this. This is what I have for you 

    Files: 
     & 

In this challenge we are given the date and time and I am also using that as
seed but *time.time()* return seconds, so we have to convert the given date into
seconds and use them as seed and then we can reverse the* xor* to get the flag.

![](https://cdn-images-1.medium.com/max/800/1*wu4OY7aNaZP7vqhyx9admQ.png)
<br><span class="figcaption_hack">FLAG</span>

**3. RSA_2.0(250 | Medium)**

    Here Is All You Need :) 
    q = 1169308535661061883601718278029178532579893961637917450548194874621120325272747502265038337302712391206860744418050104380433672959311510965459536075063414053713275712737274655301765208851528047724259083132308147284798886790387046467

    n = 1767851792031133258573149211223576840441233598393441179519250830258605567528134015177783867628408692079657509361643483662648484501591944265647164942872514453941170557837893989751799954174597385323282012066851803047110357212185487261691006796587502670372456690659491464066659209766793559901274788318647671714770060946980834724197455408294440520057269719542155445889380960096135755321320294463647409757608982664026167368917409077948250361723616746877263784067416733

    e = 11

    cipher= 615332628098121990257094267579984234186316426970751200414291770742561222271952895055382292827995311599720567991200438337119382775978093548491043712718918341740035477730488306911007119815207141452582938720656729278253606047862033614417029232678768962758723323890638709795816659740821477420399375013921920608081034122641588051012524064474710072639887787437000774014399029632191451914505873328610615417619901837630299136028205045962643296204723945945959770551698068

In this challenge we are given the cipher, N, Q and e so it seems to be easy to
use any random RSA decryption script to decode it and get the flag. But as I
promised you have to think not be a script kiddie. When you use any script (
given below ) to decode this RSA you get an error as below:

So if you google about this error you’ll find that python throw this error when
e and phi are not *co-primes*. This time we have to modify our scripts to get
flag.

![](https://cdn-images-1.medium.com/max/800/1*Ar2UiohGvK4sQmNrcvUNuw.png)
<br><span class="figcaption_hack">FLAG</span>

**4. I_will_never_Stop(500 | Hard)**

    You always bully me because of my week encryption algorithm but this time you all will cry :)

    Files: 
     & 

We’re given a zip file and a python code which performs the following
operations:
<ul>
    <li>Creates *zip_name* of random length(1–10) character</li><br> 
    <li>Every character of the flag is encrypted via md5 and stored in *flag_hash*</li><br> 
    <li>*zip_name*’s md5 encrypted string is stored in *zip_pass*</li>

So inside every zip folder, the files in format: (num).(2char) is something to
be looked upon as concatenating their char in sorted order of their respective
num we get a string which is a md5 hash representing a single char of the flag.

The process can be automated using the Python script as given below:

![](https://cdn-images-1.medium.com/max/800/1*xVfnCCS2CkEnboYKL8Pv5Q.png)
<br><span class="figcaption_hack">FLAG</span>

### MISC

1.  **Why we all are fighting :/ (250 | Medium)**

    In todays world everyone is fighting with each other. Some people want to stop this therefore they using technology to stop these riots. But politicians doesn’t want the fights to be stopped therefore they forced us to investigate the system for those persons who want to stop riots. Politicians are saying we will find something serious. Can you help us to prove them wrong?
    FILE: 

In this we are given a pcap file, if we check what type of protocols it has,
we’ll find that it has HTTPS ( TCP ), Telnet, FTP. Now as we know that Telnet
and FTP traffic is unencrypted so we can check what is passing through it. So if
you check the FTP traffic you will know that one image is transferred. Now
convert the image to its *hexdump* from the option in the protocol analyser of
*Wireshark* and copy that hexdump to *cyberchef* you will get your flag.

![](https://cdn-images-1.medium.com/max/800/1*eO7g8r5qjPjZVBfYY4m3Og.png)
<br><span class="figcaption_hack">FLAG</span>

**2. Investigation(500 | Hard)**

    While investigating the solar wind attack we reached to one of the hacker and got something on his system but we are not able to get what this file is or is something more than file that can help us to login into there server.

    FILE: 

1. Use command ‘*binwalk -e file.bin*’ <br> 2. Use unshadow and then crack the
shadow and passwd file. <br> 3. Brute force using *JohnTheRipper* to get
password which is the flag.

![](https://cdn-images-1.medium.com/max/800/1*yyMMnfXGGwGOeZi7TmalaA.png)
<br><span class="figcaption_hack">FLAG</span>

### MEM FORENSIC

    File: 

Before doing anything we have to find the profile for the image, you can use
command: *vol.py iamgeinfo -f dump.raw*

1.  **What he executed :/ (100 | Easy)**

    Me and My friend SinText started a company named H4x0r Pvt Ltd. But someone from our company had deals with the APT Group and leaked our Internal information even our Red Team Tools Details and lot more passwords for our servers. Now you have to investigate and find all the clues in series So sit with the coffee start the investigation, first thing we got is that he executed something before he did anything . Can you help us?

Check the console as anything we execute get listed on the console thus we can
check the command executed via console plugin by:

> vol.py -f dump.raw — profile=Win81U1x64 consoles

You will find a base64 string, decode it to get your flag.

![](https://cdn-images-1.medium.com/max/800/1*4i5DkwOCmiAKhlkwSg033Q.png)
<br><span class="figcaption_hack">FLAG</span>

**2. N3v3r C0py M3(250 | Medium)**

    We Only found that before the threat ins1d3r copied something that APT-33 provided him and then he used that for hacking the internal servers but we can’t find what was that, now it’s all on you. file : same from previous problem

In this challenge as description says, insider copied something which we don’t
know. Copy get stored to the clipboard, check the clipboard using clipboard
plugin by:

> vol.py -f dump.raw — profile=Win81U1x64 clipboard

![](https://cdn-images-1.medium.com/max/800/1*zdGqlkqRxu9EpbUBhCwdew.png)
<br><span class="figcaption_hack">FLAG</span>

**3. my_advice(250 | Medium)**

    I always asked the ins1d3r to not use the same password for everything but he has never taken my advice seriously. Now this will put him in problem HAHA :)

Challenge description is sufficient to find the flag. This time we have to find
the password of the insider using hashdump command in the *vol.py*

> vol.py -f dump.raw — profile=Win81U1x64 hashdump

you will get the NT Hash of the password:

> l3v1ath4n:1001:aad3b435b51404eeaad3b435b51404ee:31e8aa4d81712d3c5f0b0b271206041e:::

Now that we have password hash, copy that and decode from the crackstation to
get the password as “*hacked*”.

> decode this: 31e8aa4d81712d3c5f0b0b271206041e

![](https://cdn-images-1.medium.com/max/800/1*psxg1htLaCwcVno-F1snvw.png)
<br><span class="figcaption_hack">FLAG</span>

**4. How he Login to APT site ???(500 | Hard)**

    I am wrong this time that he reused the password, this time he logged in to APT site but that was password protected, how did he logged in I am not getting that. Save the H4x0rs Pvt. Ltd. this time also.

In this, I said he always use the password but this time to login the apt he use
something different so we have to find something via which we can find the
password of that. If you check the process using pslist

> vol.py -f dump.raw — profile=Win81U1x64 pslist

You will find that there is the process of kdbx that means it can store the
password in the keepass. We can find the kdbx database file using filescan
command

> vol.py -f dump.raw — profile=Win81U1x64 filescan | grep kdbx

Now we have the kdbx file *secret.kdbx*, we can dump that file and try to open
using kdbx but twist here is, it asking for the master password for that we have
to read the challenge, he uses same password every where and as we already have
the password from previous we can use that to login and get our flag in the
internet entries.

> vol.py -f dump.raw — profile=Win81U1x64 dumpfiles -D . -Q 0x00000000266b05f0

![](https://cdn-images-1.medium.com/max/800/1*uXT1dNsrH4K4_AZqk-jyKw.png)
<br><span class="figcaption_hack">FLAG</span>

### DISK FORENSIC

    File: 

As we got the .EO1 we can open it using FTK Imager Tool and when we add it as
evidence into the tool we got all the directory and contents.

1.  **What he deleted :/**

    We got the Disk of the Insid3r but before we got to him he deleted something can you help us?

As description says we have to find something which he deleted that means there
will be something in the recycle bin when you check the bin you get file named
*R74SPM.txt* it has the flag.

![](https://cdn-images-1.medium.com/max/800/1*pZkONMXVqBLstZRddSrjnQ.png)
<br><span class="figcaption_hack">FLAG</span>

**2. FIREeye Why ?(250 | Medium)**

    After interrogating him we only got that he logged into the site which helps APT to trigger the attack. Can you help us to find the credential so that we can stop it? (same file)

If you see the name of the challenge carefully, you get FIRE and then as
description says we have to find the login creds. Check if there’s a browser
installed on the system. Yes it has the Firefox so if we have the *Logins.json*
file as in Firefox, all logins details are stored in it but encrypted, we can
use [cracker](https://github.com/pradeep1288/ffpasscracker) to crack the
password and we will got our flag.

![](https://cdn-images-1.medium.com/max/800/1*c_sTL8SsQLib45Rw6nalmQ.png)
<br><span class="figcaption_hack">FLAG</span>

**3. Self Mistakes(500 | Hard)**

    I think luck is in our hand we got that when he was doing everything on the network everything gets captured but what does it have :{

In this description says all what he has done on network got captured so we have
to find the pcap file. If we check the keepass folder in the
*l3v1ath4n/AppData/Roaming/keePass* it has one file named “How this happened”,
we export that file and open in the Wireshark. It have lots of HTTP traffic it
means we can dump those files. So When we dump all that we found, it have lots
of JS & CSS files when we check these files then in the jquery.max.js we have
one code which have xored flag.

Just reverse the code to get the flag

![](https://cdn-images-1.medium.com/max/800/1*pxZJPUt83wU2hUtBjSqi-Q.png)
<br><span class="figcaption_hack">FLAG</span>

**4. Oh! He is too smart(500 | Hard)**

    We came to know that the old system backup are hidden somewhere which contains all details about the attacks we have got every details available on portal of APT. But after analyzing for more than 2 days got nothing nowits onto you :/

In this as description says, he hide the backup of previous somewhere when we
check the favorite folder it contain the nested directories, when we go to the
end it contains the [mega
link](https://mega.nz/folder/dgUCjTIC#IAuDKymKxiKmxEifLfTi8g). When we go to
that mega link we got a vhd file, when we try to import the vhd it is protected
by bitlocker but we have one more note in that folder which contained some text
but not understandable. If you reverse the text you will get the bitlocker
password *l33tsupah4x0r*.

Now description also says he got all things on the portal of APT, it means he
definitely used one of the browser to access the portal which is Firefox but
this time logins.json is empty it means we have to check something else. Twist
here is as we know website also store cookies so we have to check the
cookies.sqlite but there are lot of cookies we have to first find the url of the
apt we have to enumerate the vhd more so on the desktop directory we have one
file named as secret_url, when we check we find one
[url](https://apt-login.vulnfreak.org/) so it means we have to check the cookies
of the vulnfreak. Now when we check we get the creds

> admin: L33T_4sl0_Gr4B_C00k13s

Just login and you will get your flag

![](https://cdn-images-1.medium.com/max/800/1*ghJEYRvEuzHFU_9vowoa6g.png)
<br><span class="figcaption_hack">FLAG</span>

### OSINT

1.  **GhostsEverywhere(100 | Easy)**

    All I have is This image 
    .

Check the metadata of the image you will find ***something is waiting for you at
qZdp4***. Now read the name carefully it says “Ghost are every where” when you
google if there is something like pastebin, you will find ghostbin. Now you have
to access the [qZdp4](https://ghostbin.com/paste/qZdp4), you will find a message
there but main points are “*social media*”, “*ban*” and “*using alternatives*”.
These words are important and you also find a username *cord cy. N*ow if you
know or you can google that from last few months there’s trend to ban twitter in
India because some people are not liking it. Therefore an alternative tooter
started. Then if you go to the tooter and search for the *cord cy* you will find
the account, it has the flag in the toots.

![](https://cdn-images-1.medium.com/max/800/1*oehe4-9WFEqlLl_YyjTSyA.png)
<br><span class="figcaption_hack">FLAG</span>

**2. Ilovemusic(250 | Medium)**

    Hey My Friend SinText love music we also have secret information at some place but he only told me that his habits can take you to the flag

SinText being the event moderator as on event’s discord channel, the only place
where you can find music on discord is on his profile. There you can get his
twitter account which has 1st half of the flag and a Spotify link which leads us
to its left half.

![](https://cdn-images-1.medium.com/max/800/1*IeY6S-xNDEILqKrtkKj9Pw.png)
<br><span class="figcaption_hack">FLAG</span>

### FORENSIC

1.  **Is_Th3s3_IMp0rt4nt(250 | Medium)**

    Our organization lost his Red Team Tools. Our Incident Response team have doubt that this attack is only because of some insider. As we have logs of all of our employees can you help us to reach the person who helped them.

In this challenge, you’ve to look into logs and find a suspicious URL. I you go
down you will find a url:

> /persistant_threat.org/log.in?uS3r=k1nG&p4S=**QnlQYXNzQ1RGe0wwR1NfNHIzXzFtUDBSdDRuVF9QNHJUXzFuX0YwcjNuU2ljNX0K**

Password is in base64 decode that and get your flag.

![](https://cdn-images-1.medium.com/max/800/1*z8N7gptSfkQSSiZTuYkboQ.png)
<br><span class="figcaption_hack">FLAG</span>

<br> 
