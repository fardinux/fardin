#!/usr/bin/env python
# coding: utf-8
__author__ = 'fardin'
"""TQDK bal hesablama proqramı. Çox əlverişsiz şəkildə kodlaşdırılıb, bilirəm. \
Yaxın zamanda yenidən əldən keçiriləcək."""

qrup = float(raw_input("Qrupunuzu daxil edin(1,2,3 ya da 4): "))

if qrup == 1:
    # 1ci qrup
    print " "
    fiz_bir_sehv = float(raw_input("Fizika fənnindən olan səhvlərin sayı: "))
    fiz_bir_bos = float(raw_input("Fizika fənnindən olan boşların sayı: "))
    fiz_bir_net = float(200 - (fiz_bir_sehv * 10) - fiz_bir_bos * 8)
    fiz_bir_faiz = (fiz_bir_net * 50) / 100
    print "Fizika fənni üzrə faiziniz:", fiz_bir_faiz
    print" "
    riy_bir_sehv = float(raw_input("Riyaziyyat fənnindən olan səhvlərin sayı: "))
    riy_bir_bos = float(raw_input("Riyaziyyat fənnindən olan boşların sayı: "))
    riy_bir_net = float(200 - (riy_bir_sehv * 10) - riy_bir_bos * 8)
    riy_bir_faiz = (riy_bir_net * 50) / 100
    print "Riyaziyyat fənni üzrə faiziniz:", riy_bir_faiz
    print" "
    az_bir_sehv = float(raw_input("Ana dili fənnindən olan səhvlərin sayı: "))
    az_bir_bos = float(raw_input("Ana dili fənnindən olan boşların sayı: "))
    az_bir_net = float(100 - (az_bir_sehv * 5) - az_bir_bos * 4)
    az_bir_faiz = az_bir_net
    print "Ana dili fənni üzrə faiziniz:", az_bir_faiz
    print" "
    kim_bir_sehv = float(raw_input("Kimya fənnindən olan səhvlərin sayı: "))
    kim_bir_bos = float(raw_input("Kimya fənnindən olan boşların sayı: "))
    kim_bir_net = float(100 - (kim_bir_sehv * 5) - kim_bir_bos * 4)
    kim_bir_faiz = kim_bir_net
    print "Kimya fənni üzrə faiziniz:", kim_bir_faiz
    print" "
    xar_bir_sehv = float(raw_input("Xarici dil fənnindən olan səhvlərin sayı: "))
    xar_bir_bos = float(raw_input("Xarici dil fənnindən olan boşların sayı: "))
    xar_bir_net = float(100 - (xar_bir_sehv * 5) - xar_bir_bos * 4)
    xar_bir_faiz = xar_bir_net
    sehv_bir = fiz_bir_sehv + riy_bir_sehv + az_bir_sehv + kim_bir_sehv + xar_bir_sehv
    bos_bir = xar_bir_bos + kim_bir_bos + az_bir_bos + riy_bir_bos + fiz_bir_bos
    print "Xarici dil fənni üzrə faiziniz:", xar_bir_faiz
    print " "
    print "Nəticəniz:", fiz_bir_net + riy_bir_net + az_bir_net + xar_bir_net + \
                        kim_bir_net, "bal"
    print "Düzgün cavabların sayı:", 125 - (sehv_bir + bos_bir)
    print "Səhv cavabların sayı:", sehv_bir, ", boşların sayı:", bos_bir

if qrup == 2:
    # 2ci qrup 
    print " "
    cog_iki_sehv = float(raw_input("Coğrafiya fənnindən olan səhvlərin sayı: "))
    cog_iki_bos = float(raw_input("Coğrafiya fənnindən olan boşların sayı: "))
    cog_iki_net = float(200 - (cog_iki_sehv * 10) - cog_iki_bos * 8)
    cog_iki_faiz = (cog_iki_net * 50) / 100
    print "Coğrafiya fənni üzrə faiziniz:", cog_iki_faiz
    print" "
    riy_iki_sehv = float(raw_input("Riyaziyyat fənnindən olan səhvlərin sayı: "))
    riy_iki_bos = float(raw_input("Riyaziyyat fənnindən olan boşların sayı: "))
    riy_iki_net = float(200 - (riy_iki_sehv * 10) - riy_iki_bos * 8)
    riy_iki_faiz = (riy_iki_net * 50) / 100
    print "Riyaziyyat fənni üzrə faiziniz:", riy_iki_faiz
    print" "
    az_iki_sehv = float(raw_input("Ana dili fənnindən olan səhvlərin sayı: "))
    az_iki_bos = float(raw_input("Ana dili fənnindən olan boşların sayı: "))
    az_iki_net = float(100 - (az_iki_sehv * 5) - az_iki_bos * 4)
    az_iki_faiz = az_iki_net
    print "Ana dili fənni üzrə faiziniz:", az_iki_faiz
    print" "
    tar_iki_sehv = float(raw_input("Azərbaycan tarixi fənnindən olan səhvlərin sayı: "))
    tar_iki_bos = float(raw_input("Azərbaycan tarixi fənnindən olan boşların sayı: "))
    tar_iki_net = float(100 - (tar_iki_sehv * 5) - tar_iki_bos * 4)
    tar_iki_faiz = tar_iki_net
    print "Azərbaycan tarixi fənni üzrə faiziniz:", tar_iki_faiz
    print" "
    xar_iki_sehv = float(raw_input("Xarici dil fənnindən olan səhvlərin sayı: "))
    xar_iki_bos = float(raw_input("Xarici dil fənnindən olan boşların sayı: "))
    xar_iki_net = float(100 - (xar_iki_sehv * 5) - xar_iki_bos * 4)
    xar_iki_faiz = xar_iki_net
    sehv_iki = cog_iki_sehv + riy_iki_sehv + az_iki_sehv + tar_iki_sehv + xar_iki_sehv
    bos_iki = xar_iki_bos + tar_iki_bos + az_iki_bos + riy_iki_bos + cog_iki_bos
    print "Xarici dil fənni üzrə faiziniz:", xar_iki_faiz
    print " "
    print "Nəticəniz:", cog_iki_net + riy_iki_net + az_iki_net + xar_iki_net + \
                        tar_iki_net, "bal"
    print "Düzgün cavabların sayı:", 125 - (sehv_iki + bos_iki)
    print "Səhv cavabların sayı:", sehv_iki, ", boşların sayı:", bos_iki

if qrup == 3:
    # 3cü qrup
    print " "
    edeb_uc_sehv = float(raw_input("Ədəbiyyat fənnindən olan səhvlərin sayı: "))
    edeb_uc_bos = float(raw_input("Ədəbiyyat fənnindən olan boşların sayı: "))
    edeb_uc_net = float(100 - (edeb_uc_sehv * 5) - edeb_uc_bos * 4)
    edeb_uc_faiz = edeb_uc_net
    print "Ədəbiyyat fənni üzrə faiziniz:", edeb_uc_faiz
    print" "
    riy_uc_sehv = float(raw_input("Riyaziyyat fənnindən olan səhvlərin sayı: "))
    riy_uc_bos = float(raw_input("Riyaziyyat fənnindən olan boşların sayı: "))
    riy_uc_net = float(100 - (riy_uc_sehv * 5) - riy_uc_bos * 4)
    riy_uc_faiz = riy_uc_net
    print "Riyaziyyat fənni üzrə faiziniz:", riy_uc_faiz
    print" "
    az_uc_sehv = float(raw_input("Ana dili fənnindən olan səhvlərin sayı: "))
    az_uc_bos = float(raw_input("Ana dili fənnindən olan boşların sayı: "))
    az_uc_net = float(200 - (az_uc_sehv * 10) - az_uc_bos * 8)
    az_uc_faiz = (az_uc_net * 50) / 100
    print "Ana dili fənni üzrə faiziniz:", az_uc_faiz
    print" "
    tar_uc_sehv = float(raw_input("Azərbaycan tarixi fənnindən olan səhvlərin sayı: "))
    tar_uc_bos = float(raw_input("Azərbaycan tarixi fənnindən olan boşların sayı: "))
    tar_uc_net = float(200 - (tar_uc_sehv * 10) - tar_uc_bos * 8)
    tar_uc_faiz = (tar_uc_net * 50) / 100
    print "Tarix fənni üzrə faiziniz:", tar_uc_faiz
    print" "
    xar_uc_sehv = float(raw_input("Xarici dil fənnindən olan səhvlərin sayı: "))
    xar_uc_bos = float(raw_input("Xarici dil fənnindən olan boşların sayı: "))
    xar_uc_net = float(100 - (xar_uc_sehv * 5) - xar_uc_bos * 4)
    xar_uc_faiz = xar_uc_net
    sehv_uc = edeb_uc_sehv + riy_uc_sehv + az_uc_sehv + tar_uc_sehv + xar_uc_sehv
    bos_uc = xar_uc_bos + tar_uc_bos + az_uc_bos + riy_uc_bos + edeb_uc_bos
    print "Xarici dil fənni üzrə faiziniz:", xar_uc_faiz
    print " "
    print "Nəticəniz:", edeb_uc_net + riy_uc_net + az_uc_net + xar_uc_net + \
                        tar_uc_net, "bal"
    print "Düzgün cavabların sayı:", 125 - (sehv_uc + bos_uc)
    print "Səhv cavabların sayı:", sehv_uc, ", boşların sayı:", bos_uc

if qrup == 4:
    # 4cü qrup
    print " "
    riy_dord_sehv = float(raw_input("Riyaziyyat fənnindən olan səhvlərin sayı: "))
    riy_dord_bos = float(raw_input("Riyaziyyat fənnindən olan boşların sayı: "))
    riy_dord_net = float(100 - (riy_dord_sehv * 5) - riy_dord_bos * 4)
    riy_dord_faiz = riy_dord_net
    print "Riyaziyyat fənni üzrə faiziniz:", riy_dord_faiz
    print" "
    az_dord_sehv = float(raw_input("Ana dili fənnindən olan səhvlərin sayı: "))
    az_dord_bos = float(raw_input("Ana dili fənnindən olan boşların sayı: "))
    az_dord_net = float(100 - (az_dord_sehv * 5) - az_dord_bos * 4)
    az_dord_faiz = az_dord_net
    print "Ana dili fənni üzrə faiziniz:", az_dord_faiz
    print" "
    bio_dord_sehv = float(raw_input("Biologiya fənnindən olan səhvlərin sayı: "))
    bio_dord_bos = float(raw_input("Biologiya fənnindən olan boşların sayı: "))
    bio_dord_net = float(200 - (bio_dord_sehv * 10) - bio_dord_bos * 8)
    bio_dord_faiz = (bio_dord_net * 50) / 100
    print "Biologiya fənni üzrə faiziniz:", bio_dord_faiz
    print" "
    kim_dord_sehv = float(raw_input("Kimya fənnindən olan səhvlərin sayı: "))
    kim_dord_bos = float(raw_input("Kimya fənnindən olan boşların sayı: "))
    kim_dord_net = float(200 - (kim_dord_sehv * 10) - kim_dord_bos * 8)
    kim_dord_faiz = (kim_dord_net * 50) / 100
    print "Kimya fənni üzrə faiziniz:", kim_dord_faiz
    print" "
    fiz_dord_sehv = float(raw_input("Fizika fənnindən olan səhvlərin sayı: "))
    fiz_dord_bos = float(raw_input("Fizika fənnindən olan boşların sayı: "))
    fiz_dord_net = float(100 - (fiz_dord_sehv * 5) - fiz_dord_bos * 4)
    fiz_dord_faiz = fiz_dord_net
    sehv_dord = riy_dord_sehv + kim_dord_sehv + az_dord_sehv + bio_dord_sehv + fiz_dord_sehv
    bos_dord = fiz_dord_bos + kim_dord_bos + az_dord_bos + riy_dord_bos + bio_dord_bos
    print "Fizika fənni üzrə faiziniz:", fiz_dord_faiz
    print " "
    print "Nəticəniz:", riy_dord_net + bio_dord_net + az_dord_net + kim_dord_net + \
                        fiz_dord_net, "bal"
    print "Düzgün cavabların sayı:", 125 - (sehv_dord + bos_dord)
    print "Səhv cavabların sayı:", sehv_dord, ", boşların sayı:", bos_dord
