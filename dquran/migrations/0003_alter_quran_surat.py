# Generated by Django 4.1.5 on 2023-01-09 07:27
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("dquran", "0002_alter_quran_surat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quran",
            name="surat",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Al-Fātiḥah (7)"),
                    (2, "Al-Baqarah (286)"),
                    (3, "Āli 'Imrān (200)"),
                    (4, "An-Nisā' (176)"),
                    (5, "Al-Mā'idah (120)"),
                    (6, "Al-An'ām (165)"),
                    (7, "Al-A'rāf (206)"),
                    (8, "Al-Anfāl (75)"),
                    (9, "At-Taubah (129)"),
                    (10, "Yūnus (109)"),
                    (11, "Hūd (123)"),
                    (12, "Yūsuf (111)"),
                    (13, "Ar-Ra'd (43)"),
                    (14, "Ibrāhīm (52)"),
                    (15, "Al-Ḥijr (99)"),
                    (16, "An-Naḥl (128)"),
                    (19, "Al-Isrā' (111)"),
                    (18, "Al-Kahf (110)"),
                    (17, "Maryam (98)"),
                    (20, "Ṭāhā (135)"),
                    (21, "Al-Anbiyā' (112)"),
                    (22, "Al-Ḥajj (78)"),
                    (23, "Al-Mu'minūn (118)"),
                    (24, "An-Nūr (64)"),
                    (25, "Al-Furqān (77)"),
                    (26, "Asy-Syu'arā' (227)"),
                    (27, "An-Naml (93)"),
                    (28, "Al-Qaṣaṣ (88)"),
                    (29, "Al-'Ankabūt (69)"),
                    (30, "Ar-Rūm (60)"),
                    (31, "Luqmān (34)"),
                    (32, "As-Sajdah (30)"),
                    (33, "Al-Aḥzāb (73)"),
                    (34, "Saba' (54)"),
                    (35, "Fāṭir (45)"),
                    (36, "Yāsīn (83)"),
                    (37, "Aṣ-Ṣāffāt (182)"),
                    (38, "Ṣād (88)"),
                    (39, "Az-Zumar (75)"),
                    (40, "Gāfir (85)"),
                    (41, "Fuṣṣilat (54)"),
                    (42, "Asy-Syūrā (53)"),
                    (43, "Az-Zukhruf (89)"),
                    (44, "Ad-Dukhān (59)"),
                    (45, "Al-Jāṡiyah (37)"),
                    (46, "Al-Aḥqāf (35)"),
                    (47, "Muḥammad (38)"),
                    (48, "Al-Fatḥ (29)"),
                    (49, "Al-Ḥujurāt (18)"),
                    (50, "Qāf (45)"),
                    (51, "Aż-Żāriyāt (60)"),
                    (52, "At-Ṭūr (49)"),
                    (53, "An-Najm (62)"),
                    (54, "Al-Qamar (55)"),
                    (55, "Ar-Raḥmān (78)"),
                    (56, "Al-Wāqi'ah (96)"),
                    (57, "Al-Ḥadīd (29)"),
                    (58, "Al-Mujādalah (22)"),
                    (59, "Al-Ḥasyr (24)"),
                    (60, "Al-Mumtaḥanah (13)"),
                    (61, "Aṣ-Ṣaff (14)"),
                    (62, "Al-Jumu'ah (11)"),
                    (63, "Al-Munāfiqūn (11)"),
                    (64, "At-Tagābun (18)"),
                    (65, "At-Talāq (12)"),
                    (66, "At-Taḥrīm (12)"),
                    (67, "Al-Mulk (30)"),
                    (68, "Al-Qalam (52)"),
                    (69, "Al-Ḥāqqah (52)"),
                    (70, "Al-Ma'ārij (44)"),
                    (71, "Nūḥ (28)"),
                    (72, "Al-Jinn (28)"),
                    (73, "Al-Muzzammil (20)"),
                    (74, "Al-Muddaṡṡir (56)"),
                    (75, "Al-Qiyāmah (40)"),
                    (76, "Al-Insān (31)"),
                    (77, "Al-Mursalāt (50)"),
                    (78, "An-Naba' (40)"),
                    (79, "An-Nāzi'āt (46)"),
                    (80, "'Abasa (42)"),
                    (81, "At-Takwīr (29)"),
                    (82, "Al-Infiṭār (19)"),
                    (83, "Al-Muṭaffifīn (36)"),
                    (84, "Al-Insyiqāq (25)"),
                    (85, "Al-Burūj (22)"),
                    (86, "At-Ṭāriq (17)"),
                    (87, "Al-A'lā (19)"),
                    (88, "Al-Gāsyiyah (26)"),
                    (89, "Al-Fajr (30)"),
                    (90, "Al-Balad (20)"),
                    (91, "Asy-Syams (15)"),
                    (92, "Al-Lail (21)"),
                    (93, "Ad-Duḥā (11)"),
                    (94, "Asy-Syarḥ (8)"),
                    (95, "At-Tīn (8)"),
                    (96, "Al-'Alaq (19)"),
                    (97, "Al-Qadr (5)"),
                    (98, "Al-Bayyinah (8)"),
                    (99, "Az-Zalzalah (8)"),
                    (100, "Al-'Adiyāt (11)"),
                    (101, "Al-Qāri'ah (11)"),
                    (102, "At-Takāṡur (8)"),
                    (103, "Al-'Aṣr (3)"),
                    (104, "Al-Humazah (9)"),
                    (105, "Al-Fīl (5)"),
                    (106, "Quraisy (4)"),
                    (107, "Al-Mā'ūn (7)"),
                    (108, "Al-Kauṡar (3)"),
                    (109, "Al-Kāfirūn (6)"),
                    (110, "An-Naṣr (3)"),
                    (111, "Al-Lahab (5)"),
                    (112, "Al-Ikhlāṣ (4)"),
                    (113, "Al-Falaq (5)"),
                    (114, "An-Nās (6)"),
                ]
            ),
        ),
    ]