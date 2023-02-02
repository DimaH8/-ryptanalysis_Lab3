import datetime as dt
import math
import gmpy2 as GMP

print("SE Input: 10 variant")

C1 = 0x2ed84d90aeba92a2e5a7c62c9a34b41e769132178b746f0415bc1975a8b6387c32a090e629d1af07377e0a55ea81349e27f8da57ef6bd1723294789e07fcede89ebaefae2c929adae7596b3c34c052e0dcc5fa8694c4a7ab73f93872c8f27c2aab4167d1d7291b90a90d6030eda1e82eb95461424a70679e9049e46e3e9e0919
N1 = 0xC7CD2AED56B246AF0C64DF1C10E1C5B896100A1E469FD72B663BC7B00E421E05FA1BB9F4E322A33CB1272CD668F95F512587A5F66C63B4E0B5A7A1639A5D9DABFD06002EFC15411B4C358CABA45CD47E35CF0F15562380E14C1B4FEA1F28F5676DB8F8844A0E1AA7573944C507D2D2E08A412A62FC7904C78A061D14B71BC757
C2 = 0x005a45762541ca9e45ea6e46ad66e256ed90b1e7dbdba84bcfcf6a949f37e9dc163007a9bace06ac2525c84223ee1b8cf1b0c4a37f50875764a417a52dcff1784c92a7f6ab0bc5f396b99ef6aeadeb00821d581bbeb68f08eba82f60c0256121cec97928ddcd64bc49961718d13344b2018a474392b164718a89561fe0f9f47a
N2 = 0xD56BA42833DC6CB1C77A023CDC94614914C7BCE469732A59280D3D5BBB9F740B8DC2D282EAFA8CAA23A40F09A5CAF336B0D831DC3FF3F3FF1A3817EF98AAE253BA74C9D9192ACC4740E57961266CFD1DA07CF2CF984731347DCE302EB0719DD9DBB01A249FEBCE01CE9D3DD9456AC1E0D48280A505156E371119CD067DB9CC2B
C3 = 0xc2f5e809a43b2cf5e1c2ff59f474624ea778b42f75b9c220c319c90d30baa760e1aa5b878037ea0235c2d8b2bd3e39484b337a5a12b69172653c89c9e007e322f646b340deaf115fbb513b55b3151d59397876efc213a2549c3a1df3c2882dbfa22da22a8d0e7bc2c7bf65069e0844c230829e6c38701e95ea50dabf49b7d2b9
N3 = 0xE15809AEA8921F144B5C6183765388A22B9EF18409DB00DE223DEF41236AEF3B9F5B9A55D240708EF41479A213BFDD681C6C04E37D8001B6FF53930628A086829535E9A1D86EE2BECAF53AEC32D936F4FF54FA5B09D2AF841BBDD8D362BA90EA57FD623CA28211D2EDEDC4B66C3C4082A60C0316ACEDB150855419F465090C47
C4 = 0x6d989046456b04804b95f210ec71bec92a4e1f989e54cbd004973dad1f8088a70a614a6c9978f7520fc8472e9e6bd1f4bc1826fe0e1a4cdfea8d8b4d9a93e8f23601dfb72c1130d51abb7b640bd3fb182ba026d1c30d847df63648ebc54e5863ee55c61de4a9c7e0a2fa459afbeab7727bf8e053e10d860ba66b5cb224f9802e
N4 = 0xB0FA0B64C68CA73668E795CEA789255AB862540F749DE17DFDB6C7FEB862F3092D1241851606ACC5F0073A96192578EB552828397F40F04C255C61D60297C77C387C8FE8EB6FD3DF34F2EC4F3D61E6BF68E5C33268B5DB64DD09C90C976B33AA346D5B986BAC4330E89D41E971E314C0DABF38C17E8DC3516F3101DCD9DCD1C7
C5 = 0x0fdd469b99841163a43ec0600faf8b9ef4c743237640db5545ea32bd2200fdba6fc43115a07c0ff8bd77d4ac19d439ac65160fe5bd4cbe20013d54166760c24f08ce7acc6010cfe8ffaf409d4fd13f852656cbf2d07a5574a3c1556a1a9a24cddc9d60de4180d3c150969326253e613e8de5b61f983abf802d813c13e469d89a
N5 = 0xEDD4710A6B1EF3902921841EB9DB2F21EF6ED8DE310633EEDD74BDF2FDE9CFDEF27E4D2C08E23BAE08777793115498A8D12BF1E85B5406D0225F957D70C1067B08545C20320CEB553E6A64F651B20684CE45A7AD131A1D16496B7F0EC4606643D7C1683072E06A107C7704D68182239DB050EC706246FD0405EA35A1CDB6380D

Cs = [C1, C2, C3, C4, C5]
Ns = [N1, N2, N3, N4, N5]


def gcd(x, y):
    if x == 0:
        return y, 0, 1
    res, u_temp, v_temp = gcd(y % x, x)
    return res, (v_temp - (y // x) * u_temp), u_temp


def attack_chinese_remainder_theorem():
    print()
    print("chinese remainder theorem attack starts")
    start_attack = dt.datetime.now()

    mod = math.prod(Ns)
    mods = []
    for n in Ns:
        mods.append(mod // n)

    MpowE = 0
    count = len(Ns)
    for i in range(count):
        _, _, v = gcd(Ns[i], mods[i])
        MpowE += v * mods[i] * Cs[i]

    MpowE = MpowE % mod
    roots = GMP.iroot(MpowE, 5)
    M = roots[0]
    print("M =", hex(M))
    print("Verification: M^E == C :", M ** 5 == MpowE)

    end_attack = dt.datetime.now()
    diff_attack = end_attack - start_attack
    print("chinese remainder theorem attack time is", diff_attack.total_seconds(), "seconds")


print("MitM Input: 10 variant")
E = 65537
L = 20

C = 0x61ea7c551d6f4fed72d57013e8853ad5ae72e664066a20e34fbba1c4ed86f5fd61374be7aa69b5abe3106a299c9d729ece42b647c115ec061fb84a144f130cb0ad815f758358d6ffdd2a99bb1dd7aac8bc12b2f40d802c6d376a89bb70bc098a6db4b137128d8960f34d5b783e7fea5e3d3ac294b4a0f6cef17856f70656cc8a80f5e40c6a763960e51bc297f316254a86d0e64324e65184c5456bcdcab07e5d9e833f6eb2de4ee15d19ea639e54c37af0538f81347f64ff0e03659f6c3e9f0be4f3c1bf3824ca55085997bd59de8c02f4c22ed668cdf795146a2b05a5b9105a5d029a704bdbb92e619a5b9bfc4fc3c39c5be12b5697684e535d4f18f4348cda
N = 0xC68D3351791940055D7CABF1CA24764DDDA34933985F6F822FFD52B18C1746B0B79D4B0FAE00CB0D26487F3AF2E292D6319C653F9855A720E4DA5EC7E653AD00047925F3651A80B42ECEF4530EEDA1D8DB3724E6EC779DFF1506D7D98272D57CD51BBD2BBA23C2868FB3FC1690EA851C46904161AA61A66258C33EB9F4EC8A0666447D61F3A03E5D4FFC7584DCD6CB15145CDE09A77CEEBCB33617780DC02049078AB36A7D80CA4DB2CC263E36DA437723AAA45CB9943720FD9B69B73A52D52637F2C6750D616F7E43106C26E4698DB07B62D4896E1B44F4BB51D4773F194C11DA7DE0C9B65C54EC800223EEF36B14546A8F1A7ADE015414E04F87A187494613


def attack_brute_force():
    print()
    print("Brute force attack starts")
    start_attack = dt.datetime.now()
    loop_end = range(N)
    res = -1
    for x in loop_end:
        res = GMP.powmod(x, E, N)
        if res == C:
            print("brute force result:", hex(x))
            break
    else:
        print("attack_brute_force: Not found!")

    end_attack = dt.datetime.now()
    diff_attack = end_attack - start_attack
    print("Brute force attack time is", diff_attack.total_seconds(), "seconds")


def attack_meet_in_the_middle():
    print()
    print("Meet in the Middle attack starts")
    start_attack = dt.datetime.now()

    loop_end = 1 << (L >> 1)
    Ts = [GMP.powmod(x + 1, E, N) for x in range(loop_end)]

    found = False
    t = 0
    s = 0
    for x in range(loop_end):
        inv = GMP.invert(Ts[x], N)
        C_mul_inv = GMP.mul(C, inv)
        res = GMP.f_mod(C_mul_inv, N)

        for i in range(loop_end):
            if Ts[i] == res:
                found = True
                t = x + 1
                s = i + 1
                break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break

    if found:
        print("Meet in the Middle attack result: (t*s) mod N =", hex(t * s % N))
        print("Verification: (t*s)^E mod N == C :", GMP.powmod(t * s, E, N) == C)
    else:
        print("attack_meet_in_the_middle: Not found!")

    end_attack = dt.datetime.now()
    diff_attack = end_attack - start_attack
    print("MitM attack time is", diff_attack.total_seconds(), "seconds")


attack_chinese_remainder_theorem()
attack_meet_in_the_middle()
attack_brute_force()