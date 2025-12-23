const courseData = [
    {
        id: "theme-1",
        title: "Tema 1: Mengenal Allah",
        description: "Pembahasan mendalam tentang nama dan sifat Allah",
        subjects: [
            {
                id: "subject-1",
                title: "Pokok Bahasan 1: Sifat Wajib & Asmaul Husna",
                topics: [
                    {
                        id: 1,
                        title: "Persaksian Tauhid & Nama-Nama Allah",
                        file: "topic_1.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Tidak Ada Tuhan Selain Allah</li>
                <li>Allah Pemelihara/Pengatur Semesta Alam (Rabb)</li>
                <li>Allah Memiliki Al Asma Al Husna (Nama-nama Yang Baik)</li>
                <li>Perintah Menyeru Allah dengan Al Asma Al Husna</li>
            </ul>

            <hr class="divider">

            <h2>Isi Materi</h2>
            <p>Materi ini membahas tentang persaksian tauhid, yang menekankan bahwa tidak ada Tuhan yang berhak
                disembah selain Allah, serta menjelaskan nama-nama dan sifat-sifat Allah yang agung (Al Asma Al
                Husna). Pembahasan ini didasarkan pada dalil-dalil dari Al-Qur'an yang menjelaskan keesaan
                Allah, kekuasaan-Nya dalam mengatur alam semesta, dan perintah untuk berdoa dengan menyebut
                nama-nama-Nya yang terbaik.</p>

            <hr class="divider">

            <!-- CONTENT SECTIONS -->
            <div class="content-section">
                <h3>Tidak Ada Tuhan Selain Allah</h3>

                <div class="quran-quote">
                    
                    <p class="translation">Allah menyatakan bahwasanya tidak ada Tuhan selain Dia, yang
                        menegakkan keadilan. Para malaikat dan orang-orang yang berilmu (juga menyatakan yang
                        demikian itu). Tidak ada Tuhan selain Dia, Yang Maha Perkasa lagi Maha Bijaksana.</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 18</span>
                </div>
                <p>Ayat ini menjelaskan martabat orang-orang berilmu yang turut bersaksi atas keesaan Allah.</p>

                <div class="quran-quote">
                    
                    <p class="translation">Atau siapakah yang telah menciptakan langit dan bumi dan yang
                        menurunkan air untukmu dari langit, lalu Kami tumbuhkan dengan air itu kebun-kebun yang
                        berpemandangan indah, yang kamu sekali-kali tidak mampu menumbuhkan pohon-pohonnya?.
                        Apakah di samping Allah ada Tuhan (yang lain)?. Bahkan (sebenarnya) mereka adalah
                        orang-orang yang menyimpang (dari kebenaran).</p>
                    
                    <p class="translation">Atau siapakah yang telah menjadikan bumi sebagai tempat berdiam, dan
                        yang menjadikan sungai-sungai di celah-celahnya, dan yang menjadikan gunung-gunung untuk
                        (mengokohkan)-nya, dan men-jadikan suatu pemisah antara dua laut. Apakah di samping
                        Allah ada Tuhan (yang lain)?. Bahkan (sebenarnya) kebanyakan dari mereka tidak
                        mengetahui.</p>

                    
                    <p class="translation">Atau siapakah yang memperkenankan (doa) orang yang dalam kesulitan
                        apabila ia berdoa kepada-Nya, dan yang menghilangkan kesusahan dan yang menjadikan kamu
                        (manusia) sebagai khalifah di bumi?. Apakah di samping Allah ada Tuhan (yang lain)?.
                        Amat sedikitlah kamu mengingati(Nya).</p>
                    
                    <p class="translation">Atau siapakah yang memimpin kamu dalam kegelapan di daratan dan
                        lautan dan siapa (pula)-kah yang mendatangkan angin sebagai kabar gembira sebelum
                        (kedatangan) rahmat-Nya?. Apakah di samping Allah ada Tuhan (yang lain)?. Maha Tinggi
                        Allah terhadap apa yang mereka persekutukan (dengan-Nya).</p>
                    
                    <p class="translation">Atau siapakah yang menciptakan (manusia dari permulaannya), kemudian
                        mengulanginya (lagi), dan siapa (pula) yang memberikan rezeki kepadamu dari langit dan
                        bumi?. Apakah di samping Allah ada Tuhan (yang lain)?. Katakanlah: "Unjukkanlah bukti
                        kebenaranmu, jika kamu memang orang-orang yang benar".</p>
                    <span class="source">Surat An Naml Ayat: 60 – 64</span>
                </div>

                <div class="note-box">
                    <strong>Catatan:</strong>
                    <ul>
                        <li><strong>"Dua laut"</strong> di sini ialah laut yang asin dan sungai besar bermuara
                            ke laut. Sungai yang tawar itu setelah sampai di muara tidak langsung menjadi asin.
                        </li>
                        <li><strong>"Menjadikan manusia sebagai khalifah"</strong> ialah menjadikannya berkuasa
                            di bumi.</li>
                        <li><strong>"Rahmat Tuhan"</strong> di sini: hujan yang menyebabkan suburnya
                            tumbuh-tumbuhan.</li>
                    </ul>
                </div>

                <div class="quran-quote">
                    
                    <p class="translation">Dialah Allah yang tiada Tuhan selain Dia, yang mengetahui yang ghaib
                        dan yang nyata, Dialah Yang Maha Pemurah lagi Maha Penyayang.</p>
                    <span class="source">Surat Al Hasyr Ayat: 22</span>
                </div>

                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Aku ini adalah Allah, tidak ada Tuhan selain Aku. Maka
                        hambakanlah dirimu (ibadah) kepada-Ku dan dirikanlah shalat untuk mengingat-Ku.</p>
                    <span class="source">Surat Thaahaa Ayat: 14</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Pemelihara/Pengatur Semesta Alam (Rabb)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tuhan langit dan bumi dan apa yang berada di antara keduanya dan
                        Tuhan tempat-tempat terbit matahari.</p>
                    
                    <p class="translation">Sesungguhnya Kami telah menghias langit yang terdekat dengan hiasan,
                        yaitu bintang-bintang,</p>
                    
                    <p class="translation">Dan telah memeliharanya dari setiap setan yang sangat durhaka,</p>
                    
                    <p class="translation">Setan-setan itu tidak dapat mendengar-dengarkan (pembicaraan) para
                        malaikat dan mereka dilempari dari segala penjuru.</p>
                    
                    <p class="translation">Untuk mengusir mereka dan bagi mereka siksaan yang kekal,</p>
                    
                    <p class="translation">Tetapi siapa (di antara mereka) yang mencuri-curi (pembicaraan); maka
                        ia dikejar oleh suluh api yang cemerlang.</p>
                    <span class="source">Surat Ash Shaaffaat Ayat: 5 – 10</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Memiliki Al Asma Al Husna (Nama-nama Yang Baik)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dialah Allah, tidak ada Tuhan (yang berhak disembah) selain Dia. Dia
                        mempunyai al Asma al Husna (nama-nama yang terbaik),</p>
                    <span class="source">Surat Thaahaa Ayat: 8</span>
                </div>
                <p><br></p>
            </div>

            <div class="content-section">
                <h3>Perintah Menyeru Allah dengan Al Asma Al Husna</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hanya milik Allah al Asma al Husna (nama-nama yang terbaik), maka
                        bermohonlah kepada-Nya dengan menyebut al Asmaa al Husna (nama-nama yang terbaik) itu
                        dan tinggalkanlah orang-orang yang menyimpang dari kebenaran dalam (menyebut)
                        nama-nama-Nya. Nanti mereka akan mendapat balasan atas apa yang telah mereka kerjakan.
                    </p>
                    <span class="source">Surat Al A'raaf Ayat: 180</span>
                </div>

                <div class="note-box">
                    <strong>Penjelasan:</strong>
                    <p></p>
                </div>

                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Serulah Allah atau serulah Ar-Rahman. Dengan nama yang
                        mana saja kamu seru, Dia mempunyai Al asmaa al Husna (nama-nama terbaik) dan janganlah
                        kamu mengeraskan suaramu dalam shalatmu dan janganlah pula merendahkannya dan carilah
                        jalan tengah di antara kedua itu".</p>
                    <span class="source">Surat Al Israa' Ayat: 110</span>
                </div>
                <p class="note-simple"></p>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Demikianlah materi tentang Nama dan Sifat Allah, yang mencakup keesaan-Nya, peran-Nya sebagai
                Rabb semesta alam, dan kemuliaan nama-nama-Nya (Al Asma Al Husna) yang wajib kita imani dan
                gunakan dalam berdoa.</p>`,

                        quiz: [
                            {
                                question: "Siapakah yang bersaksi bahwa tidak ada Tuhan selain Allah menurut Surat Ali ‘Imraan ayat 18?",
                                options: ["Hanya Para Malaikat", "Allah, Para Malaikat, dan orang berilmu", "Hanya orang-orang berilmu", "Seluruh makhluk di bumi"],
                                correct: 2,
                                explanation: "Tuhan yang menyekutukan Allah dianggap menyamakan makhluk dengan Khaliq, padahal hanya Allah yang berhak disembah."
                            },
                            {
                                question: "Apa yang dimaksud dengan \"Rahmat Tuhan\" dalam konteks Surat An Naml ayat 63 menurut catatan kaki?",
                                options: ["Kasih sayang", "Ampunan dosa", "Hujan yang menyuburkan tanaman", "Pahala yang besar"],
                                correct: 3,
                                explanation: "Dalam catatan kaki materi, dijelaskan bahwa Rahmat Tuhan di sini bermakna hujan yang menyuburkan tanaman."
                            },
                            {
                                question: "Dalam Surat An Naml ayat 62, siapakah yang memperkenankan doa orang yang kesulitan?",
                                options: ["Nabi", "Malaikat", "Allah", "Para Wali"],
                                correct: 3,
                                explanation: "Hanya Allah yang memperkenankan doa orang yang dalam kesulitan dan menghilangkan kesusahan."
                            },
                            {
                                question: "Apa alasan setan-setan dilempari dari segala penjuru menurut Surat Ash Shaaffaat?",
                                options: ["Karena mereka mencuri-curi pembicaraan malaikat", "Karena mereka tidak mau bersujud", "Karena mereka menggoda manusia", "Karena mereka masuk surga"],
                                correct: 1,
                                explanation: "Setan-setan dilempari karena mereka mencoba mencuri-curi dengar pembicaraan para malaikat di langit."
                            },
                            {
                                question: "Apa yang diperintahkan dalam Surat Al A'raaf ayat 180 terkait Al Asma Al Husna?",
                                options: ["Menghafalnya saja", "Menulisnya di dinding", "Bermohonlah kepada-Nya dengan menyebutnya", "Mengabaikannya"],
                                correct: 3,
                                explanation: "Allah memerintahkan kita untuk bermohon kepada-Nya dengan menyebut Asmaul Husna tersebut."
                            },
                            {
                                question: "Menurut Surat Al Israa' ayat 110, bagaimana sebaiknya suara dalam shalat?",
                                options: ["Sangat keras", "Sangat pelan (berbisik)", "Diam dalam hati", "Jalan tengah (tidak terlalu keras dan tidak terlalu pelan)"],
                                correct: 4,
                                explanation: "Allah berfirman: Janganlah kamu mengeraskan suaramu dalam shalatmu dan jangan pula merendahkannya, tetapi carilah jalan tengah."
                            },
                            {
                                question: "Apa arti dari \"Al Aziz\" yang terdapat dalam Surat Ali 'Imraan ayat 18?",
                                options: ["Yang Maha Pengampun", "Yang Maha Perkasa", "Yang Maha Mengetahui", "Yang Maha Bijaksana"],
                                correct: 2,
                                explanation: "Al Aziz artinya Yang Maha Perkasa, sering digandingkan dengan Al Hakim (Yang Maha Bijaksana)."
                            }
                        ]
                    },
                    {
                        id: 2,
                        title: "Al Waahid, Al Ahad, dan Al Shamad",
                        file: "topic_2.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Esa dan Tempat Bergantung</li>
                <li>Allah Bersih dari Sekutu dan Anak</li>
                <li>Larangan Menyekutukan Allah (Syirik)</li>
                <li>Syirik Merupakan Kepercayaan Yahudi dan Nashrani</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan sifat Allah sebagai Al Waahid (Maha Esa) dan Al Ahad (Maha Satu), serta Ash Shamad (Tempat Bergantung). Dijelaskan pula dalil-dalil yang membantah anggapan bahwa Allah memiliki anak atau sekutu, serta peringatan keras terhadap perbuatan syirik yang menjadi kepercayaan kaum terdahulu.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Esa dan Tempat Bergantung</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Dia-lah Allah, Yang Maha Esa. Allah adalah Tuhan yang bergantung kepada-Nya segala sesuatu. Dia tiada beranak dan tidak pula diperanakkan, dan tidak ada seorangpun yang setara dengan Dia."</p>
                    <span class="source">Surat Al Ikhlaash Ayat: 1 – 4</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Tuhanmu benar-benar Esa. Tuhan langit dan bumi dan apa yang berada di antara keduanya dan Tuhan tempat-tempat terbit matahari.</p>
                    <span class="source">Surat Ash Shaaffaat Ayat: 4 – 5</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Bersih dari Sekutu dan Anak</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kalau sekiranya Allah hendak mengambil anak, tentu Dia akan memilih apa yang dikehendaki-Nya di antara ciptaan-ciptaan yang telah diciptakan-Nya. Maha Suci Allah. Dialah Allah Yang Maha Esa lagi Maha Mengalahkan.</p>
                    <span class="source">Surat Az Zumar Ayat: 4</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan katakanlah: "Segala puji bagi Allah Yang tidak mempunyai anak dan tidak mempunyai sekutu dalam kerajaan-Nya dan Dia bukan pula hina yang memerlukan penolong dan agungkanlah Dia dengan pengagungan yang sebesar-besarnya".</p>
                    <span class="source">Surat Al Israa' Ayat: 111</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Larangan Menyekutukan Allah (Syirik)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah tidak akan mengampuni dosa syirik, dan Dia mengampuni segala dosa yang selain dari (syirik) itu, bagi siapa yang dikehendaki-Nya. Barangsiapa yang mempersekutukan Allah, maka sungguh ia telah berbuat dosa yang besar.</p>
                    <span class="source">Surat An Nisaa' Ayat: 48</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Syirik Merupakan Kepercayaan Yahudi dan Nashrani</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Orang-orang Yahudi berkata: "Uzair itu putera Allah" dan orang-orang Nasrani berkata: "Al Masih itu putera Allah". Demikianlah itu ucapan mereka dengan mulut mereka, mereka meniru perkataan orang-orang kafir yang terdahulu. Dilaknati Allah mereka , bagaimana mereka sampai berpaling.</p>
                    <span class="source">Surat At Taubah Ayat: 30</span>
                </div>
            </div>
            <hr class="divider">
            <h2>Penutup</h2>
            <p>Mengesakan Allah (Tauhid) adalah inti ajaran Islam. Kita wajib meyakini bahwa Allah Maha Esa, tidak beranak, tidak diperanakkan, dan tidak ada sekutu bagi-Nya. Menyekutukan Allah adalah dosa besar yang tidak akan diampuni.</p>
        `,

                        quiz: [
                            {
                                question: "Apa arti dari 'Ash Shamad' dalam Surat Al Ikhlas?",
                                options: ["Maha Esa", "Tempat bergantung segala sesuatu", "Maha Perkasa", "Maha Mengetahui"],
                                correct: 2,
                                explanation: "Ash Shamad artinya Tuhan yang bergantung kepada-Nya segala sesuatu, tempat meminta dan memohon."
                            },
                            {
                                question: "Dalam Surat Al An'aam ayat 19 (konteks materi), siapakah yang menjadi saksi?",
                                options: ["Malaikat", "Nabi Muhammad", "Allah", "Manusia"],
                                correct: 3,
                                explanation: "Katakanlah: 'Siapakah yang lebih kuat persaksiannya?'. Katakanlah: 'Allah'. Allah menjadi saksi antara aku (Rasul) dan kamu."
                            },
                            {
                                question: "Siapakah yang disebut 'Rombongan yang bershaf-shaf' dalam tafsir materi ini?",
                                options: ["Para tentara", "Malaikat (atau makhluk lain)", "Orang yang shalat", "Para Nabi"],
                                correct: 2,
                                explanation: "Dalam Surat Ash Shaaffaat ayat 1, yang dimaksud bershaf-shaf adalah para malaikat."
                            },
                            {
                                question: "Menurut Surat An Nisaa' ayat 48, dosa apakah yang tidak akan diampuni Allah?",
                                options: ["Mencuri", "Berzina", "Membunuh", "Syirik (Mempersekutukan Allah)"],
                                correct: 4,
                                explanation: "Sesungguhnya Allah tidak akan mengampuni dosa syirik, dan Dia mengampuni dosa selain itu bagi siapa yang Dia kehendaki."
                            },
                            {
                                question: "Siapakah yang dianggap sebagai anak Allah oleh kaum Yahudi menurut Surat At Taubah ayat 30?",
                                options: ["Isa (Al Masih)", "Uzair", "Musa", "Daud"],
                                correct: 2,
                                explanation: "Orang-orang Yahudi berkata: 'Uzair itu putera Allah', sedangkan Nasrani berkata 'Al Masih itu putera Allah'."
                            }
                        ]
                    },
                    {
                        id: 3,
                        title: "Al Dhaarr dan Al Naafi'",
                        file: "topic_3.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Hanya Allah yang Memiliki Manfaat dan Madharat</li>
                <li>Larangan Menyeru yang tak Memiliki Manfaat/Madharat</li>
                <li>Tidak Ada yang Dapat Memberi Madharat Kepada Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah sebagai Al Dhaarr (Yang Menimpakan Mudharat) dan Al Naafi' (Yang Memberi Manfaat). Segala kebaikan dan keburukan berada di tangan Allah. Makhluk, termasuk berhala yang disembah, tidak memiliki kuasa sedikitpun untuk mendatangkan manfaat atau menolak bahaya tanpa izin Allah.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Hanya Allah yang Memiliki Manfaat dan Madharat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Jika Allah menimpakan suatu mudharat kepadamu, maka tak ada yang dapat menghilangkannya kecuali Dia. Dan jika Allah menghendaki kebaikan bagimu, maka tak ada yang dapat menolak kurnia-Nya. Dia memberi kebaikan kepada siapa yang Dia kehendaki di antara hamba-hamba-Nya dan Dia Maha Pengampun lagi Maha Penyayang.</p>
                    <span class="source">Surat Yuunus Ayat: 107</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka mengambil tuhan-tuhan selain-Nya (untuk diibadahi), yang tuhan-tuhan itu tidak menciptakan apapun, bahkan mereka sendiri diciptakan dan tidak kuasa untuk (menolak) suatu mudharat dari dirinya dan tidak (pula untuk mengambil) suatu manfaat pun dan tidak kuasa mematikan, menghidupkan, dan tidak membangkitkan.</p>
                    <span class="source">Surat Al Furqaan Ayat: 3</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Larangan Menyeru yang tak Memiliki Manfaat/Madharat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Mengapa kamu mengabdi kepada selain Allah, sesuatu yang tidak dapat memudharatkanmu dan tidak memberi manfaat?", dan Allahlah Yang Maha Mendengar lagi Maha Mengetahui.</p>
                    <span class="source">Surat Al Maaidah Ayat: 76</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Hai manusia, telah dibuat perumpamaan, maka dengarkanlah olehmu perumpamaan itu. Sesungguhnya segala yang kamu seru selain Allah sekali-kali tidak dapat menciptakan seekor lalatpun, walaupun mereka bersatu menciptakannya.</p>
                    <span class="source">Surat Al Hajj Ayat: 73</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tidak Ada yang Dapat Memberi Madharat Kepada Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Janganlah kamu disedihkan oleh orang-orang yang segera menjadi kafir; sesungguhnya mereka tidak dapat memudharatkan Allah sedikitpun.</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 176</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Hanya Allah yang berkuasa memberikan manfaat atau menimpakan mudharat. Segala sesembahan selain Allah adalah lemah, bahkan tidak mampu menciptakan seekor lalat. Oleh karena itu, kita dilarang keras memohon atau bergantung kepada selain Allah.</p>
        `,

                        quiz: [
                            {
                                question: "Jika Allah menimpakan kemudharatan, siapakah yang dapat menghilangkannya menurut Surat Yuunus ayat 107?",
                                options: ["Para Malaikat", "Hanya Allah", "Orang Sholeh", "Dukun"],
                                correct: 2,
                                explanation: "Hanya Allah yang dapat menimpakan mudharat dan memberi manfaat. Sesembahan selain Allah tidak memiliki kuasa sedikitpun akan hal tersebut."
                            },
                            {
                                question: "Apa kelemahan berhala yang disebutkan dalam Surat Al Furqaan ayat 3?",
                                options: ["Tidak bisa bicara", "Tidak bisa melihat", "Tidak bisa mematikan, menghidupkan, atau membangkitkan", "Tidak bisa mendengar doa"],
                                correct: 3,
                                explanation: "Berhala tidak bisa mematikan, menghidupkan, maupun membangkitkan. Mereka sendiri diciptakan."
                            },
                            {
                                question: "Dalam Surat Al Hajj ayat 73, apa perumpamaan kelemahan sesembahan selain Allah?",
                                options: ["Tidak bisa membuat langit", "Tidak bisa membelah laut", "Tidak bisa menciptakan seekor lalat pun", "Tidak bisa menurunkan hujan"],
                                correct: 3,
                                explanation: "Sesembahan selain Allah tidak dapat menciptakan seekor lalatpun, walaupun mereka bersatu untuk menciptakannya."
                            },
                            {
                                question: "Mengapa kita dilarang menyembah selain Allah menurut Surat Al Maaidah ayat 76?",
                                options: ["Karena mereka jelek", "Karena mereka tidak dapat memberi mudharat maupun manfaat", "Karena mereka mahal harganya", "Karena mereka terbuat dari batu"],
                                correct: 2,
                                explanation: "Allah berfirman: 'Mengapa kamu mengabdi kepada selain Allah, sesuatu yang tidak dapat memudharatkanmu dan tidak memberi manfaat?'."
                            },
                            {
                                question: "Apakah orang-orang kafir dapat memberi mudharat kepada Allah (Surat Ali 'Imraan 176)?",
                                options: ["Ya, sangat besar", "Ya, sedikit", "Tidak dapat memudharatkan sedikitpun", "Tergantung kekuatan mereka"],
                                correct: 3,
                                explanation: "Sesungguhnya mereka (orang-orang kafir) tidak dapat memudharatkan Allah sedikitpun."
                            }
                        ]
                    },
                    {
                        id: 4,
                        title: "Allah Maha Pencipta",
                        file: "topic_4.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pencipta (Al Khaaliq)</li>
                <li>Tidak Ada Pencipta Selain Allah</li>
                <li>Allah Maha Pencipta (Faathir & Al Badii')</li>
                <li>Allah Maha Pembentuk Rupa (Al Mushawwir)</li>
                <li>Allah Memulai & Mengulangi Penciptaan (Al Mubdi' - Al Mu'iid)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas Al Asma Al Husna yang berkaitan dengan perbuatan Allah (Af'al) dalam menciptakan, mengadakan, dan membentuk alam semesta beserta isinya. Allah adalah Al Khaaliq (Pencipta), Al Baari' (Yang Mengadakan), dan Al Mushawwir (Yang Membentuk Rupa).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Pencipta (Al Khaaliq)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah Pencipta segala sesuatu dan Dia Pemelihara segala sesuatu.</p>
                    <span class="source">Surat Az Zumar Ayat: 62</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Yang demikian itu adalah Allah, Tuhanmu, Pencipta segala sesuatu, tiada Tuhan (yang berhak diibadahi) kecuali Dia; Maka bagaimana kamu dapat dipalingkan?</p>
                    <span class="source">Surat Al Mu'min Ayat: 62</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tidak Ada Pencipta Selain Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dia menciptakan langit tanpa tiang yang kamu melihatnya dan Dia meletakkan gunung-gunung (di permukaan) bumi supaya bumi itu tidak menggoyangkan kamu.</p>
                    <span class="source">Surat Luqmaan Ayat: 10</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Inilah ciptaan Allah, maka perlihatkan olehmu kepadaku apa yang telah diciptakan oleh sembahan-sembahan-(mu) selain Allah.</p>
                    <span class="source">Surat Luqmaan Ayat: 11</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Pencipta (Faathir & Al Badii')</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Pencipta langit dan bumi...</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 11</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Allah pencipta langit dan bumi, dan bila Dia berkehendak (untuk menciptakan) sesuatu, maka (cukuplah) Dia hanya mengatakan kepadanya: "Jadilah!" lalu jadilah ia.</p>
                    <span class="source">Surat Al Baqarah Ayat: 117</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Pembentuk Rupa (Al Mushawwir)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dialah Allah yang menciptakan, yang mengadakan, yang membentuk rupa, yang memiliki al Asma al Husna.</p>
                    <span class="source">Surat Al Hasyr Ayat: 24</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dia menciptakan langit dan bumi dengan haq. Dia membentuk rupamu dan Dia baguskan rupamu dan hanya kepada Allah tempat kembali.</p>
                    <span class="source">Surat At Taghaabun Ayat: 3</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Memulai & Mengulangi Penciptaan (Al Mubdi' - Al Mu'iid)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Allah-lah yang memulai penciptaan makhluk, lalu mengulanginya (menghidupkannya) kembali".</p>
                    <span class="source">Surat Yuunus Ayat: 34</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Allah adalah satu-satunya Pencipta. Tidak ada sekutu bagi-Nya dalam penciptaan. Dia yang memulai penciptaan dari tiada, membentuknya dengan indah, dan Dia pula yang berkuasa mengulangi penciptaan (membangkitkan) manusia setelah kematian.</p>
        `,

                        quiz: [
                            {
                                question: "Apa arti dari Al Khaaliq?",
                                options: ["Maha Pengampun", "Maha Pencipta", "Maha Melihat", "Maha Mendengar"],
                                correct: 2,
                                explanation: "Al Khaaliq artinya Maha Pencipta, yang mengadakan segala sesuatu dari ketiadaan."
                            },
                            {
                                question: "Menurut Surat Luqmaan ayat 10, bagaimana Allah menciptakan langit?",
                                options: ["Dengan tiang besi", "Tanpa tiang yang kamu melihatnya", "Dari asap", "Dari air"],
                                correct: 2,
                                explanation: "Dalam Surat Luqmaan ayat 10 disebutkan: 'Dia menciptakan langit tanpa tiang yang kamu melihatnya'."
                            },
                            {
                                question: "Apa yang dimaksud dengan Al Mu'iid?",
                                options: ["Yang Memulai Penciptaan", "Yang Mengulangi Penciptaan", "Yang Mematikan", "Yang Menghancurkan"],
                                correct: 2,
                                explanation: "Al Mu'iid artinya Yang Mengulangi (menghidupkan kembali makhluk setelah mati) pada hari kebangkitan."
                            },
                            {
                                question: "Siapakah yang membentuk rupa manusia (Al Mushawwir)?",
                                options: ["Malaikat", "Orang tua", "Allah", "Alam semesta"],
                                correct: 3,
                                explanation: "Dialah Allah Yang Menciptakan, Yang Mengadakan, Yang Membentuk Rupa (Al Mushawwir)."
                            },
                            {
                                question: "Kalimat 'Kun Fayakun' terdapat dalam pembahasan sifat Allah yang mana?",
                                options: ["Al Badii'", "Al Malik", "Al Quddus", "Al Salaam"],
                                correct: 1,
                                explanation: "Kalimat 'Jadilah! Maka jadilah ia' berkaitan dengan sifat Al Badii' (Pencipta yang Inovatif dan Maha Kuasa)."
                            }
                        ]
                    },
                    {
                        id: 5,
                        title: "Al Rahmaan, Al Rahiim, Al Ra'uuf & Al Waduud",
                        file: "topic_5.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Al Rahmaan (Maha Pemurah)</li>
                <li>Al Rahiim (Maha Penyayang)</li>
                <li>Al Ra'uuf (Maha Penyantun)</li>
                <li>Al Waduud (Maha Pecinta)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas luasnya rahmat Allah yang meliputi segala sesuatu. Ar Rahmaan menunjukkan rahmat yang luas di dunia bagi seluruh makhluk, sedangkan Ar Rahiim adalah kasih sayang khusus di akhirat bagi orang-orang beriman. Juga dibahas sifat Al Ra'uuf (Penyantun) dan Al Waduud (Yang Mencintai).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Al Rahmaan (Maha Pemurah)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">(Tuhan) Yang Maha Pemurah, Yang telah mengajarkan Alquran. Dia menciptakan manusia. Mengajarnya pandai berbicara.</p>
                    <span class="source">Surat Ar Rahmaan Ayat: 1 – 4</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Dia-lah Allah Yang Maha Penyayang, kami beriman kepada-Nya dan kepada-Nya-lah kami bertawakkal".</p>
                    <span class="source">Surat Al Mulk Ayat: 29</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Al Rahiim (Maha Penyayang)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah benar-benar Maha Pengasih lagi Maha Penyayang kepada manusia.</p>
                    <span class="source">Surat Al Hajj Ayat: 65</span>
                </div>
                <p>Juga disebutkan dalam banyak ayat bahwa Allah Maha Pengampun lagi Maha Penyayang (Ghafuurur Rahiim), menunjukkan kasih sayang-Nya kepada hamba yang bertaubat.</p>
            </div>

            <div class="content-section">
                <h3>Al Ra'uuf (Maha Penyantun)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan di antara manusia ada orang yang mengorbankan dirinya karena mencari keridhaan Allah; dan Allah Maha Penyantun kepada hamba-hamba-Nya.</p>
                    <span class="source">Surat Al Baqarah Ayat: 207</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Rahmat Allah mendahului murka-Nya. Kita diperintahkan untuk memohon rahmat-Nya dan meneladani sifat kasih sayang dalam kehidupan sehari-hari. Namun, kita juga harus takut akan azab-Nya yang pedih bagi mereka yang ingkar.</p>
        `,

                        quiz: [
                            {
                                question: "Siapakah yang mengajarkan Al Qur'an menurut awal Surat Ar Rahmaan?",
                                options: ["Jibril", "Nabi Muhammad", "Ar Rahmaan (Allah)", "Ulama"],
                                correct: 3,
                                explanation: "Surat Ar Rahmaan dimulai dengan: (Tuhan) Yang Maha Pemurah. Yang telah mengajarkan Alquran."
                            },
                            {
                                question: "Sifat Ar Rahiim biasanya identik dengan kasih sayang yang diberikan di?",
                                options: ["Dunia saja", "Akhirat (untuk orang beriman)", "Neraka", "Alam Kubur"],
                                correct: 2,
                                explanation: "Ar Rahiim adalah kasih sayang khusus yang Allah berikan kepada orang-orang beriman, terutama di akhirat."
                            },
                            {
                                question: "Apa arti Al Ra'uuf?",
                                options: ["Maha Keras", "Maha Penyantun/Belas Kasih", "Maha Kaya", "Maha Adil"],
                                correct: 2,
                                explanation: "Al Ra'uuf memiliki arti Maha Penyantun atau Maha Belas Kasih (lebih halus dari Rahmat)."
                            },
                            {
                                question: "Menurut Surat Al Hajj ayat 65, kenapa langit tidak jatuh ke bumi?",
                                options: ["Karena gravitasi", "Karena tiang penyangga", "Karena izin Allah (Rahmat-Nya)", "Karena kebetulan"],
                                correct: 3,
                                explanation: "Langit tidak jatuh ke bumi melainkan dengan izin-Nya. Sesungguhnya Allah benar-benar Maha Pengasih lagi Maha Penyayang."
                            },
                            {
                                question: "Lanjutan ayat 'In nallaaha binnaasi la...'",
                                options: ["Ghafuurur Rahiim", "Ra'uufur Rahiim", "Sami'un 'Aliim", "Azizun Hakim"],
                                correct: 2,
                                explanation: "Lanjutan ayatnya adalah '...la Ra'uufur Rahiim' (Sesungguhnya Allah benar-benar Maha Penyantun lagi Maha Penyayang)."
                            }
                        ]
                    },
                    {
                        id: 6,
                        title: "Al Malik & Al Maliik",
                        file: "topic_6.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Al Malik (Maha Raja)</li>
                <li>Al Maliik (Penguasa Yang Sempurna)</li>
                <li>Tempat Orang Bertakwa</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas kekuasaan mutlak Allah sebagai Raja (Al Malik) yang menguasai hari pembalasan dan seluruh alam semesta. Tidak ada sekutu bagi-Nya dalam kerajaan-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Al Malik (Maha Raja)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka Maha Tinggi Allah, Raja yang sebenarnya; tidak ada Tuhan selain Dia, Tuhan (yang mempunyai) 'Arsy yang mulia.</p>
                    <span class="source">Surat Al Mu’minuun Ayat: 116</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tempat Orang Bertakwa di Sisi Sang Raja</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya orang-orang yang bertakwa itu di dalam taman-taman dan sungai-sungai, Di tempat yang disenangi di sisi Tuhan yang berkuasa.</p>
                    <span class="source">Surat Al Qamar Ayat: 54 – 55</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Allah adalah Raja Yang Sebenarnya (Al Malik Al Haq). Kepemimpinan dan kekuasaan manusia hanyalah pinjaman dan sementara. Kelak di hari kiamat, hanya kerajaan Allah yang nampak nyata dan kekal.</p>
        `,

                        quiz: [
                            {
                                question: "Apa arti dari Al Malik?",
                                options: ["Maha Pencipta", "Maha Raja", "Maha Suci", "Maha Besar"],
                                correct: 2,
                                explanation: "Al Malik artinya Maha Raja atau Penguasa mutlak seluruh alam semesta."
                            },
                            {
                                question: "Dimana tempat orang bertakwa menurut Surat Al Qamar ayat 54?",
                                options: ["Di dalam taman-taman dan sungai-sungai", "Di istana emas", "Di atas awan", "Di gunung tinggi"],
                                correct: 1,
                                explanation: "Sesungguhnya orang-orang yang bertakwa itu di dalam taman-taman dan sungai-sungai."
                            },
                            {
                                question: "Apa kelanjutan ayat 'Fata'aalallaahul Malikul...'",
                                options: ["Quddus", "Haqq", "Mubin", "Karim"],
                                correct: 2,
                                explanation: "Lanjutannya adalah '...Malikul Haqq' (Maka Maha Tinggi Allah, Raja yang sebenarnya/Haq)."
                            },
                            {
                                question: "Siapakah Tuhan pemilik Arsy yang Mulia (Rabbul 'Arsyil Kariim)?",
                                options: ["Malaikat Pemikul Arsy", "Allah", "Manusia Pilihan", "Nabi"],
                                correct: 2,
                                explanation: "Dalam Surat Al Mu’minuun ayat 116 disebutkan bahwa Dia (Allah) adalah Tuhan yang mempunyai 'Arsy yang mulia."
                            },
                            {
                                question: "Kata 'Muqtadir' dalam surat Al Qamar ayat 55 merujuk pada sifat Allah yang...",
                                options: ["Maha Berkuasa", "Maha Mengetahui", "Maha Mendengar", "Maha Melihat"],
                                correct: 1,
                                explanation: "Muqtadir bermakna Yang Maha Berkuasa (Menentukan segala sesuatu)."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-2",
                title: "Pokok Bahasan 2: Sifat Allah Bagian 2",
                topics: [
                    {
                        id: 7,
                        title: "Al Maalik Al Mulki & Al Mu'izz Al Mudzill",
                        file: "topic_7.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Pemilik Kerajaan (Al Maalik Al Mulki)</li>
                <li>Allah Memuliakan dan Menghinakan (Al Mu'izz - Al Mudzill)</li>
                <li>Allah Pemilik Langit, Bumi, dan Isinya</li>
                <li>Allah Pemilik Dunia dan Akhirat</li>
                <li>Kunci-kunci Alam Gaib</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah sebagai Pemilik Mutlak Kerajaan (Maalik Al Mulki). Dia berkuasa memberikan kekuasaan kepada siapa yang Dia kehendaki dan mencabutnya dari siapa yang Dia kehendaki. Dia juga Al Mu'izz (Yang Memuliakan) dan Al Mudzill (Yang Menghinakan). Segala sesuatu di langit, bumi, dunia, dan akhirat adalah milik-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Pemilik Kerajaan, Memuliakan dan Menghinakan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Ya Allah Maha Pemilik kerajaan, Engkau berikan kerajaan kepada orang yang Engkau kehendaki dan Engkau cabut kerajaan dari orang yang Engkau kehendaki. Engkau muliakan orang yang Engkau kehendaki dan Engkau hinakan orang yang Engkau kehendaki. Di tangan-Mulah segala kebajikan. Sesungguhnya Engkau Maha Kuasa atas segala sesuatu.</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 26</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Pemilik Langit dan Bumi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tidakkah kamu mengetahui bahwa kerajaan langit dan bumi adalah kepunyaan Allah? Dan tiada bagimu selain Allah seorang pelindung maupun seorang penolong.</p>
                    <span class="source">Surat Al Baqarah Ayat: 107</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan kepunyaan Allah-lah kerajaan langit dan bumi dan kepada Allah-lah kembali (semua makhluk).</p>
                    <span class="source">Surat An Nuur Ayat: 42</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Pemilik (Penguasa) Dunia dan Akhirat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka hanya bagi Allah kehidupan akhirat dan dunia.</p>
                    <span class="source">Surat An Najm Ayat: 25</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">(Lalu Allah berfirman): "Kepunyaan siapakah kerajaan pada hari ini?" Kepunyaan Allah Yang Maha Esa lagi Maha Mengalahkan.</p>
                    <span class="source">Surat Al Mu'min Ayat: 16</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Pemilik Kunci Alam Gaib</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan pada sisi Allah-lah kunci-kunci semua yang ghaib; tidak ada yang mengetahuinya kecuali Dia, dan Dia mengetahui apa yang di daratan dan di lautan.</p>
                    <span class="source">Surat Al An'aam Ayat: 59</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Penguasa sejati adalah Allah. Jabatan dan kekuasaan di dunia adalah titipan yang bisa diambil kapan saja. Kita harus menyadari bahwa kemuliaan dan kehinaan ada di tangan Allah, dan hanya kepada-Nya kita kembali.</p>
                        `,
                        quiz: [
                            {
                                question: "Siapakah yang berhak memberikan dan mencabut kerajaan menurut Surat Ali 'Imraan ayat 26?",
                                options: ["Raja-raja dunia", "Allah", "Malaikat", "Pemenang perang"],
                                correct: 2,
                                explanation: "Katakanlah: 'Ya Allah Maha Pemilik kerajaan, Engkau berikan kerajaan kepada orang yang Engkau kehendaki dan Engkau cabut kerajaan dari orang yang Engkau kehendaki'."
                            },
                            {
                                question: "Apa arti dari 'Maalik Al Mulki'?",
                                options: ["Pemilik Kerajaan", "Pencipta Alam", "Pemberi Rezeki", "Pengampun Dosa"],
                                correct: 1,
                                explanation: "Maalik Al Mulki artinya Maha Pemilik Kerajaan atau Penguasa Kekuasaan."
                            },
                            {
                                question: "Dalam Surat Al An'aam ayat 59, apa yang berada di sisi Allah?",
                                options: ["Kunci-kunci rezeki", "Kunci-kunci surga", "Kunci-kunci semua yang ghaib", "Kunci-kunci dunia"],
                                correct: 3,
                                explanation: "Dan pada sisi Allah-lah kunci-kunci semua yang ghaib; tidak ada yang mengetahuinya kecuali Dia."
                            },
                            {
                                question: "Kepunyaan siapakah kerajaan langit dan bumi menurut Surat Al Baqarah ayat 107?",
                                options: ["Manusia", "Jin dan Manusia", "Allah", "Malaikat"],
                                correct: 3,
                                explanation: "Tidakkah kamu mengetahui bahwa kerajaan langit dan bumi adalah kepunyaan Allah?"
                            },
                            {
                                question: "Apa makna dari sifat Allah Al Mu'izz?",
                                options: ["Yang Maha Menghinakan", "Yang Maha Memuliakan", "Yang Maha Kaya", "Yang Maha Adil"],
                                correct: 2,
                                explanation: "Al Mu'izz artinya Yang Memuliakan, sedangkan Al Mudzill artinya Yang Menghinakan."
                            }
                        ]
                    },
                    {
                        id: 8,
                        title: "Al Waliy, Al Maulaa & An Nashiir",
                        file: "topic_8.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Pelindung (Al Waliy/Al Maulaa)</li>
                <li>Allah Penolong (An Nashiir)</li>
                <li>Pertolongan Allah Itu Dekat</li>
                <li>Allah Menolong Orang Beriman</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah sebagai Pelindung (Al Waliy/Al Maulaa) dan Penolong (An Nashiir). Tidak ada pelindung dan penolong yang sebenarnya selain Allah. Pertolongan Allah sangat dekat bagi orang-orang yang beriman dan menyadari kelemahan dirinya di hadapan Allah.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Adalah Pelindung dan Penolong yang Sebenarnya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka Allah, Dia pelindung (yang sebenarnya) dan Dia menghidupkan orang-orang yang mati, dan Dia Maha Kuasa atas segala sesuatu.</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 9</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Tetapi, Allahlah pelindungmu, dan Dia-lah sebaik-baik penolong.</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 150</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Menolong Siapa yang Dia Kehendaki</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Jika Allah menolong kamu, maka tidak ada orang yang dapat mengalahkanmu; jika Allah membiarkanmu (tidak menolongmu), maka siapakah gerangan yang dapat menolong kamu (selain dari) Allah sesudah itu?</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 160</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Pertolongan Allah Itu Dekat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Ingatlah, sesungguhnya pertolongan Allah itu sangat dekat.</p>
                    <span class="source">Surat Al Baqarah Ayat: 214</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Adalah Pelindung Orang-orang yang Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah pelindung orang-orang beriman; Dia mengeluarkan mereka dari kegelapan (kekafiran) kepada cahaya (iman). Dan orang-orang kafir, pelindung-pelindungnya ialah setan.</p>
                    <span class="source">Surat Al Baqarah Ayat: 257</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Hanya Allah sebaik-baik pelindung dan penolong. Jika Allah menolong kita, tidak ada yang bisa mengalahkan kita. Kuncinya adalah keimanan dan tawakkal kepada-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari An Nashiir?",
                                options: ["Maha Pelindung", "Maha Penolong", "Maha Melihat", "Maha Mendengar"],
                                correct: 2,
                                explanation: "An Nashiir artinya Maha Penolong. Allah adalah sebaik-baik penolong."
                            },
                            {
                                question: "Jika Allah menolong kita, apa yang akan terjadi menurut Surat Ali 'Imraan ayat 160?",
                                options: ["Kita akan kaya", "Kita akan terkenal", "Tidak ada yang dapat mengalahkan kita", "Kita tidak akan mati"],
                                correct: 3,
                                explanation: "Jika Allah menolong kamu, maka tidak ada orang yang dapat mengalahkanmu."
                            },
                            {
                                question: "Siapakah pelindung orang-orang kafir menurut Surat Al Baqarah ayat 257?",
                                options: ["Allah", "Malaikat", "Thaghut (Setan)", "Manusia kuat"],
                                correct: 3,
                                explanation: "Dan orang-orang kafir, pelindung-pelindungnya ialah thaghut (setan)."
                            },
                            {
                                question: "Bagaimanakah sifat pertolongan Allah menurut Surat Al Baqarah ayat 214?",
                                options: ["Sangat jauh", "Mustahil", "Sangat dekat", "Tertunda"],
                                correct: 3,
                                explanation: "Ingatlah, sesungguhnya pertolongan Allah itu sangat dekat."
                            },
                            {
                                question: "Apa yang dilakukan Allah kepada orang beriman menurut Surat Al Baqarah 257?",
                                options: ["Membiarkan dalam kegelapan", "Mengeluarkan dari cahaya ke kegelapan", "Mengeluarkan dari kegelapan kepada cahaya", "Menghukum mereka"],
                                correct: 3,
                                explanation: "Dia mengeluarkan mereka dari kegelapan (kekafiran) kepada cahaya (iman)."
                            }
                        ]
                    },
                    {
                        id: 9,
                        title: "Al Wakil",
                        file: "topic_9.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pemelihara (Al Wakil)</li>
                <li>Cukuplah Allah Sebagai Pemelihara</li>
                <li>Tidak Ada Pelindung Selain Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah sebagai Al Wakil (Maha Pemelihara/Tempat Berserah Diri). Allah mengurus segala urusan hamba-Nya. Cukuplah Allah sebagai pelindung dan tempat bergantung dari segala bahaya dan siksa.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Pemelihara Segala Sesuatu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Allah pemelihara segala sesuatu.</p>
                    <span class="source">Surat Huud Ayat: 12</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Cukuplah Allah Sebagai Pemelihara</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan kepunyaan Allah-lah apa yang di langit dan apa yang di bumi. Dan cukuplah Allah sebagai pemelihara.</p>
                    <span class="source">Surat An Nisaa' Ayat: 132</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan bertawakkallah kepada Allah. Dan cukuplah Allah sebagai pelindung.</p>
                    <span class="source">Surat Al Ahzaab Ayat: 48</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tidak Ada yang Dapat Memelihara Diri dari Siksa Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan jika kamu ditimpa bahaya di lautan, niscaya hilanglah siapa yang kamu seru kecuali Dia, maka tatkala Dia menyelamatkanmu ke darat, kamu berpaling. Dan ternyata manusia selalu tidak berterima kasih.</p>
                    <span class="source">Surat Al Israa' Ayat: 67</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Hanya Allah tempat kita menyerahkan segala urusan (tawakkal). Dia-lah Al Wakil yang menjamin dan memelihara hamba-Nya. Tidak ada tempat berlindung dari azab Allah selain kembali kepada-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Wakil?",
                                options: ["Maha Mengetahui", "Maha Pemelihara/Tempat Berserah Diri", "Maha Kaya", "Maha Bijaksana"],
                                correct: 2,
                                explanation: "Al Wakil artinya Maha Pemelihara, yang mengurusi segala urusan hamba-Nya."
                            },
                            {
                                question: "Dalam Surat An Nisaa' ayat 132, apa yang dikatakan tentang Allah?",
                                options: ["Allah Maha Keras Azabnya", "Cukuplah Allah sebagai pemelihara", "Allah memiliki anak", "Allah tidur"],
                                correct: 2,
                                explanation: "Dan cukuplah Allah sebagai pemelihara (Wakil)."
                            },
                            {
                                question: "Apa perintah Allah dalam Surat Al Ahzaab ayat 48?",
                                options: ["Lari dari musuh", "Bertawakkallah kepada Allah", "Kumpulkan harta", "Balas dendam"],
                                correct: 2,
                                explanation: "Dan bertawakkallah kepada Allah. Dan cukuplah Allah sebagai pelindung."
                            },
                            {
                                question: "Menurut Surat Huud ayat 12, Allah adalah wakil atas?",
                                options: ["Orang beriman saja", "Segala sesuatu", "Langit saja", "Bumi saja"],
                                correct: 2,
                                explanation: "Dan Allah pemelihara (Wakil) segala sesuatu."
                            },
                            {
                                question: "Bagaimana sifat manusia menurut Surat Al Israa' ayat 67 ketika diselamatkan ke darat?",
                                options: ["Bersyukur", "Berpaling dan tidak berterima kasih", "Semakin taat", "Memberi sedekah"],
                                correct: 2,
                                explanation: "Maka tatkala Dia menyelamatkanmu ke darat, kamu berpaling. Dan ternyata manusia selalu tidak berterima kasih."
                            }
                        ]
                    },
                    {
                        id: 10,
                        title: "Al Razzaaq, Al Baasith & Al Qaabidh",
                        file: "topic_10.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pemberi Rezeki (Ar Razzaaq)</li>
                <li>Rezeki Seluruh Makhluk Dijamin Allah</li>
                <li>Allah Memberi Rezeki Tanpa Batas</li>
                <li>Allah Melapangkan dan Menyempitkan Rezeki (Al Baasith - Al Qaabidh)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah sebagai Ar Razzaaq (Maha Pemberi Rezeki). Allah menjamin rezeki seluruh makhluk-Nya, mulai dari manusia hingga binatang melata. Dia juga Al Baasith (Yang Melapangkan Rezeki) dan Al Qaabidh (Yang Menyempitkan Rezeki) sesuai kehendak dan hikmah-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Pemberi Rezeki</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah Dialah Maha Pemberi rezeki yang mempunyai kekuatan lagi sangat kokoh.</p>
                    <span class="source">Surat Adz Dzaariyaat Ayat: 58</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Rezeki Seluruh Makhluk Ada dalam Jaminan Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tidak ada suatu binatang melata pun di bumi melainkan Allah-lah yang memberi rezkinya, dan Dia mengetahui tempat berdiam binatang itu dan tempat penyimpanannya. Semuanya tertulis dalam Kitab yang nyata (Lauh Mahfuzh).</p>
                    <span class="source">Surat Huud Ayat: 6</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan berapa banyak binatang yang tidak (dapat) membawa (mengurus) rezekinya sendiri. Allah-lah yang memberi rezeki kepadanya dan kepadamu dan Dia Maha Mendengar lagi Maha Mengetahui.</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 60</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Memberi Rezeki Tanpa Batas</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Engkau beri rezeki siapa yang Engkau kehendaki tanpa hisab (batas).</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 27</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Melapangkan dan Menyempitkan Rezeki (Al Baasith & Al Qaabidh)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah meluaskan rezeki dan menyempitkannya bagi siapa yang Dia kehendaki. Mereka bergembira dengan kehidupan di dunia, padahal kehidupan dunia itu (dibanding dengan) kehidupan akhirat, hanyalah kesenangan (yang sedikit).</p>
                    <span class="source">Surat Ar Ra’d Ayat: 26</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apakah mereka tidak memperhatikan bahwa sesungguhnya Allah melapangkan rezeki bagi siapa yang dikehendaki-Nya dan Dia (pula) yang menyempitkan-(nya). Sesungguhnya pada yang demikian itu benar-benar terdapat tanda-tanda (kekuasaan Allah) bagi kaum yang beriman.</p>
                    <span class="source">Surat Ar Ruum Ayat: 37</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Rezeki adalah urusan Allah. Tugas kita adalah berusaha dan berdoa, namun hasil dan pembagiannya adalah hak prerogatif Allah Yang Maha Mengetahui apa yang terbaik bagi hamba-Nya. Kita harus mensyukuri kelapangan dan bersabar dalam kesempitan.</p>
                        `,
                        quiz: [
                            {
                                question: "Siapakah yang menanggung rezeki setiap binatang melata di bumi menurut Surat Huud ayat 6?",
                                options: ["Manusia", "Alam Semesta", "Allah", "Malaikat Mikail"],
                                correct: 3,
                                explanation: "Dan tidak ada suatu binatang melata pun di bumi melainkan Allah-lah yang memberi rezkinya."
                            },
                            {
                                question: "Apa arti dari Al Razzaaq?",
                                options: ["Maha Pemberi Rezeki", "Maha Mengetahui", "Maha Kaya", "Maha Kuat"],
                                correct: 1,
                                explanation: "Al Razzaaq artinya Maha Pemberi Rezeki."
                            },
                            {
                                question: "Dalam Surat Adz Dzaariyaat ayat 58, Allah disebut memiliki sifat apa selain Pemberi Rezeki?",
                                options: ["Yang Maha Lembut", "Yang mempunyai kekuatan lagi sangat kokoh", "Yang Maha Cepat hisab-Nya", "Yang Maha Tinggi"],
                                correct: 2,
                                explanation: "Sesungguhnya Allah Dialah Maha Pemberi rezeki yang mempunyai kekuatan lagi sangat kokoh."
                            },
                            {
                                question: "Apa arti dari Al Baasith?",
                                options: ["Yang Menyempitkan Rezeki", "Yang Memberi Kehidupan", "Yang Melapangkan/Meluaskan Rezeki", "Yang Mematikan"],
                                correct: 3,
                                explanation: "Al Baasith adalah Yang Melapangkan atau Meluaskan Rezeki."
                            },
                            {
                                question: "Mengapa Allah meyempitkan rezeki sebagian hamba-Nya?",
                                options: ["Karena Allah benci", "Karena kebetulan", "Sesuai kehendak dan hikmah-Nya (ujian)", "Karena mereka malas"],
                                correct: 3,
                                explanation: "Allah melapangkan dan menyempitkan rezeki bagi siapa yang Dia kehendaki (sebagai ujian dan hikmah)."
                            }
                        ]
                    },
                    {
                        id: 11,
                        title: "Al Wahhaab, Dzu al Thawl & Al Barr",
                        file: "topic_11.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pemberi Karunia (Al Wahhaab)</li>
                <li>Allah Pemilik Anugerah (Dzu al Thawl/Fadhl)</li>
                <li>Allah Maha Melimpahkan Kebaikan (Al Barr)</li>
                <li>Perintah Mencari Karunia Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas kemurahan Allah dalam memberi karunia tanpa mengharap balasan. Dia adalah Al Wahhaab (Maha Pemberi), Dzu Al Fadhl (Pemilik Karunia Besar), dan Al Barr (Maha Melimpahkan Kebaikan). Segala fasilitas hidup yang kita nikmati adalah anugerah-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Pemberi Karunia (Al Wahhaab)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">"Ya Tuhan kami, janganlah Engkau jadikan hati kami condong kepada kesesatan sesudah Engkau beri petunjuk kepada kami, dan karuniakanlah kepada kami rahmat dari sisi Engkau; sesungguhnya Engkau-lah Maha Pemberi (karunia)".</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 8</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Melimpahkan Kebaikan (Al Barr)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya kami dahulu menyeru-Nya. Sesungguhnya Dia-lah Yang Maha Melimpahkan kebaikan lagi Maha Penyayang.</p>
                    <span class="source">Surat Ath Thuur Ayat: 28</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Pemberi Karunia (Dzu Al Fadhl)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah benar-benar mempunyai karunia yang dilimpahkan atas manusia, akan tetapi kebanyakan manusia tidak bersyukur.</p>
                    <span class="source">Surat Al Mu'min Ayat: 61</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Perintah Mencari Karunia Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tuhan-mu adalah yang melayarkan kapal-kapal di lautan untukmu, agar kamu mencari sebagian dari karunia-Nya. Sesungguhnya Dia adalah Maha Penyayang terhadapmu.</p>
                    <span class="source">Surat Al Israa' Ayat: 66</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Allah memberi tanpa diminta dan tanpa pamrih. Sebagai hamba, kita harus sadar bahwa semua nikmat berasal dari-Nya, Dzat Yang Maha Baik (Al Barr) dan Maha Pemberi (Al Wahhaab), dan kita wajib mensyukurinya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Wahhaab?",
                                options: ["Maha Kaya", "Maha Pemberi (Karunia)", "Maha Sombong", "Maha Memaksa"],
                                correct: 2,
                                explanation: "Al Wahhaab artinya Maha Pemberi Karunia (tanpa mengharap balasan)."
                            },
                            {
                                question: "Dalam Surat Ali 'Imraan ayat 8, apa yang diminta dalam doa tersebut?",
                                options: ["Harta kekayaan", "Kekuasaan dunia", "Rahmat dari sisi-Nya dan keteguhan hati", "Umur panjang"],
                                correct: 3,
                                explanation: "Janganlah Engkau jadikan hati kami condong kepada kesesatan... dan karuniakanlah kepada kami rahmat."
                            },
                            {
                                question: "Apa arti dari Al Barr dalam Surat Ath Thuur ayat 28?",
                                options: ["Maha Benar", "Maha Melimpahkan Kebaikan", "Maha Suci", "Maha Agung"],
                                correct: 2,
                                explanation: "Al Barr artinya Yang Maha Melimpahkan Kebaikan atau Maha Dermawan."
                            },
                            {
                                question: "Mengapa manusia disebut tidak bersyukur dalam Surat Al Mu'min ayat 61?",
                                options: ["Karena mereka miskin", "Karena mereka lupa ibadah", "Padahal Allah melimpahkan karunia kepada mereka", "Karena mereka sakit"],
                                correct: 3,
                                explanation: "Allah mempunyai karunia atas manusia, akan tetapi kebanyakan manusia tidak bersyukur."
                            },
                            {
                                question: "Untuk apa Allah melayarkan kapal-kapal di lautan (Surat Al Israa' 66)?",
                                options: ["Untuk berperang", "Untuk berwisata", "Agar kamu mencari sebagian dari karunia-Nya", "Untuk pamer kekuatan"],
                                correct: 3,
                                explanation: "Agar kamu mencari sebagian dari karunia-Nya (seperti berdagang, mencari ikan, dll)."
                            }
                        ]
                    },
                    {
                        id: 12,
                        title: "Al Hayy, Al Qayyuum & Al Muhyii Al Mumiit",
                        file: "topic_12.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Hidup (Al Hayy)</li>
                <li>Allah Maha Berdiri Sendiri (Al Qayyuum)</li>
                <li>Allah Menghidupkan dan Mematikan (Al Muhyii - Al Mumiit)</li>
                <li>Menghidupkan Bumi Sesudah Mati</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas tentang kehidupan Allah yang kekal abadi (Al Hayy) dan sifat-Nya yang terus menerus mengurus makhluk-Nya (Al Qayyuum). Allah juga satu-satunya Dzat yang mampu menghidupkan yang mati (Al Muhyii) dan mematikan yang hidup (Al Mumiit).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Hidup dan Maha Berdiri Sendiri</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah, tidak ada Tuhan (yang berhak diibadahi) selain Dia. Yang Maha Hidup kekal lagi Maha Berdiri sendiri (terus menerus mengurus makhluk-Nya).</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 2</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Menghidupkan dan Maha Mematikan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tidak ada Tuhan (yang berhak disembah) melainkan Dia, yang menghidupkan dan yang mematikan, (Dialah) Tuhanmu dan Tuhan bapak-bapakmu yang terdahulu.</p>
                    <span class="source">Surat Ad Dukhaan Ayat: 8</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">.</p>
                    <span class="source">Referensi: Al Baqarah Ayat 28</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Menghidupkan Bumi Sesudah Mati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dia mengeluarkan yang hidup dari yang mati dan mengeluarkan yang mati dari yang hidup dan menghidupkan bumi sesudah matinya. Dan seperti itulah kamu akan dikeluarkan (dari kubur).</p>
                    <span class="source">Surat Ar Ruum Ayat: 19</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kehidupan hakiki hanyalah milik Allah. Semua makhluk akan mati (fana), namun Allah Al Hayy Al Qayyuum akan tetap kekal. Dia-lah yang berkuasa membangkitkan manusia dari liang kubur sebagaimana Dia menghidupkan tanah yang tandus dengan air hujan.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Hayy?",
                                options: ["Maha Berdiri Sendiri", "Maha Hidup Kekal", "Maha Mematikan", "Maha Kaya"],
                                correct: 2,
                                explanation: "Al Hayy artinya Yang Maha Hidup Kekal, tidak pernah mati dan tidak mengantuk."
                            },
                            {
                                question: "Apa arti dari Al Qayyuum?",
                                options: ["Yang Maha Tidur", "Yang Tergantung pada makhluk", "Yang Maha Berdiri Sendiri / Mengurus Makhluk", "Yang Maha Lembut"],
                                correct: 3,
                                explanation: "Al Qayyuum artinya Maha Berdiri Sendiri dan terus menerus mengurus makhluk-Nya."
                            },
                            {
                                question: "Siapakah yang menghidupkan dan mematikan menurut Surat Ad Dukhaan ayat 8?",
                                options: ["Malaikat Izrail", "Allah", "Dokter", "Alam"],
                                correct: 2,
                                explanation: "Tidak ada Tuhan melainkan Dia, yang menghidupkan dan yang mematikan."
                            },
                            {
                                question: "Bagaimana Allah membuktikan kekuasaan-Nya membangkitkan yang mati di Surat Ar Ruum 19?",
                                options: ["Dengan menghidupkan orang mati langsung", "Dengan sihir", "Dengan menghidupkan bumi sesudah matinya (tandus)", "Dengan menciptakan robot"],
                                correct: 3,
                                explanation: "Dia menghidupkan bumi sesudah matinya (tandus) dengan menurunkan hujan. Seperti itulah kamu akan dikeluarkan dari kubur."
                            },
                            {
                                question: "Apa yang dikeluarkan Allah dari yang mati menurut Surat Ar Ruum ayat 19?",
                                options: ["Emas", "Yang Hidup", "Api", "Air"],
                                correct: 2,
                                explanation: "Dia mengeluarkan yang hidup dari yang mati dan mengeluarkan yang mati dari yang hidup."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-3",
                title: "Pokok Bahasan 3: Sifat Allah Bagian 3",
                topics: [
                    {
                        id: 13,
                        title: "Mukhaalafah li al Hawaadits",
                        file: "topic_13.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Berbeda dengan Makhluk-Nya (Mukhaalafah li al Hawaadits)</li>
                <li>Allah Bersemayam di Atas Arasy</li>
                <li>Allah Tidak Dapat Dilihat di Dunia</li>
                <li>Allah Maha Berkehendak</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah yang Maha Berbeda dengan segala makhluk-Nya (Mukhaalafah li al Hawaadits). Tidak ada sesuatupun yang serupa dengan Dia. Allah bersemayam di atas 'Arsy sesuai keagungan-Nya, dan Dia tidak dapat dilihat oleh mata di dunia, namun orang mukmin akan melihat-Nya di akhirat.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Berbeda dengan Makhluk-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tidak ada sesuatupun yang serupa dengan Dia, dan Dia-lah Yang Maha Mendengar dan melihat.</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 11</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Bersemayam di Atas Arasy</h3>
                <div class="quran-quote">
                    
                    <p class="translation">(Yaitu) Tuhan Yang Maha Pemurah, Yang bersemayam di atas 'Arsy.</p>
                    <span class="source">Surat Thaahaa Ayat: 5</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Tidak Dapat Dilihat di Dunia tapi Dapat Dilihat di Surga</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dia tidak dapat dicapai oleh penglihatan mata, sedang Dia dapat melihat segala yang kelihatan.</p>
                    <span class="source">Surat Al An'aam Ayat: 103</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Wajah-wajah (orang-orang mukmin) pada hari itu berseri-seri. Kepada Tuhannyalah mereka melihat.</p>
                    <span class="source">Surat Al Qiyaamah Ayat: 22-23</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Berkehendak (Kun Fayakun)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya keadaan-Nya apabila Dia menghendaki sesuatu hanyalah berkata kepadanya: "Kun (jadilah)!", maka jadilah ia.</p>
                    <span class="source">Surat Yaasiin Ayat: 82</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kita wajib mengimani bahwa Allah berbeda dengan makhluk-Nya. Sifat-sifat seperti bersemayam, tangan, wajah, atau mata bagi Allah harus diimani sesuai dengan kebesaran-Nya tanpa menyerupakan dengan makhluk (tasybih) dan tanpa menolak maknanya (ta'thil).</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Mukhaalafah li al Hawaadits?",
                                options: ["Sama dengan makhluk", "Berbeda dengan makhluk/baharu", "Maha Mengetahui", "Maha Mendengar"],
                                correct: 1,
                                explanation: "Mukhaalafah li al Hawaadits artinya Allah berbeda dengan segala sesuatu yang baharu (makhluk)."
                            },
                            {
                                question: "Potongan ayat 'Laisa kamitslihi syai'un' (Asy Syuuraa: 11) bermakna?",
                                options: ["Allah Maha Besar", "Allah Maha Pengampun", "Tidak ada sesuatupun yang serupa dengan Dia", "Allah Maha melihat"],
                                correct: 2,
                                explanation: "Laisa kamitslihi syai'un artinya Tidak ada sesuatupun yang serupa dengan Dia."
                            },
                            {
                                question: "Di manakah Allah bersemayam menurut Surat Thaahaa ayat 5?",
                                options: ["Di Bumi", "Di Langit ke-7", "Di atas 'Arsy", "Di Baitullah"],
                                correct: 2,
                                explanation: "(Yaitu) Tuhan Yang Maha Pemurah, Yang bersemayam di atas 'Arsy."
                            },
                            {
                                question: "Apa yang terjadi apabila Allah menghendaki sesuatu (Surat Yaasiin 82)?",
                                options: ["Dia butuh bantuan", "Dia berkata 'Kun' (Jadilah), maka jadilah ia", "Dia beristirahat", "Dia berpikir dulu"],
                                correct: 1,
                                explanation: "Dia hanya berkata kepadanya: 'Kun (jadilah)!', maka jadilah ia."
                            },
                            {
                                question: "Kapan wajah orang mukmin bisa melihat Tuhannya menurut Surat Al Qiyaamah 22-23?",
                                options: ["Di dunia", "Di dalam mimpi", "Pada hari kiamat/di surga", "Tidak bisa melihat sama sekali"],
                                correct: 2,
                                explanation: "Wajah-wajah (orang-orang mukmin) pada hari itu berseri-seri. Kepada Tuhannyalah mereka melihat."
                            }
                        ]
                    },
                    {
                        id: 14,
                        title: "Al Ghaniy & Al Mughniy",
                        file: "topic_14.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Kaya (Al Ghaniy)</li>
                <li>Allah Maha Memberikan Kekayaan (Al Mughniy)</li>
                <li>Allah Tidak Membutuhkan Makhluk-Nya</li>
                <li>Harta Milik Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Ghaniy (Maha Kaya) yang tidak membutuhkan apapun dari makhluk-Nya. Sebaliknya, makhluklah yang membutuhkan Dia. Allah juga Al Mughniy (Maha Memberi Kekayaan) kepada siapa yang Dia kehendaki.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Kaya dan Tidak Membutuhkan Makhluk</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hai manusia, kamulah yang membutuhkan Allah; dan Allah Dialah Yang Maha Kaya (tidak memerlukan sesuatu) lagi Maha Terpuji.</p>
                    <span class="source">Surat Faathir Ayat: 15</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Memberikan Kekayaan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan bahwasanya Dialah yang memberikan kekayaan dan memberikan kecukupan.</p>
                    <span class="source">Surat An Najm Ayat: 48</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Segala yang di Langit dan Bumi Milik Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan kepunyaan Allah-lah apa yang di langit dan apa yang di bumi... dan Allah Maha Kaya dan Maha Terpuji.</p>
                    <span class="source">Surat An Nisaa' Ayat: 131</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kekayaan sejati adalah merasa cukup (qana'ah) dengan pemberian Allah. Allah Maha Kaya secara mutlak, sedangkan kekayaan manusia adalah titipan. Jangan sampai harta membuat kita sombong dan lupa bahwa kita sangat miskin di hadapan Allah.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Ghaniy?",
                                options: ["Maha Kuasa", "Maha Kaya / Tidak Membutuhkan Sesuatu", "Maha Bijaksana", "Maha Melihat"],
                                correct: 1,
                                explanation: "Al Ghaniy artinya Maha Kaya dan tidak memerlukan sesuatu dari makhluk-Nya."
                            },
                            {
                                question: "Apa arti dari Al Mughniy?",
                                options: ["Yang Maha Meminta", "Yang Maha Memberi Kekayaan/Kecukupan", "Yang Maha Mengambil", "Yang Maha Menghitung"],
                                correct: 1,
                                explanation: "Al Mughniy artinya Yang Memberikan Kekayaan dan Kecukupan."
                            },
                            {
                                question: "Siapakah yang membutuhkan Allah menurut Surat Faathir ayat 15?",
                                options: ["Hanya orang miskin", "Hanya orang sakit", "Semua manusia (Antumul fuqara')", "Malaikat saja"],
                                correct: 2,
                                explanation: "Hai manusia, kamulah yang membutuhkan Allah (antumul fuqara')."
                            },
                            {
                                question: "Apa yang dikatakan Surat An Nisaa' ayat 131 tentang kepemilikan langit dan bumi?",
                                options: ["Milik manusia", "Milik raja-raja", "Milik Allah", "Milik bersama"],
                                correct: 2,
                                explanation: "Dan kepunyaan Allah-lah apa yang di langit dan apa yang di bumi."
                            },
                            {
                                question: "Jika Allah mau, apa yang bisa Dia lakukan kepada manusia (Surat Al An'aam 133)?",
                                options: ["Menambah rezekinya", "Memusnahkan dan mengganti dengan kaum lain", "Membiarkan saja", "Menghukum di dunia saja"],
                                correct: 1,
                                explanation: "Apabila Dia menghendaki niscaya Dia memusnahkanmu dan menggantimu dengan siapa yang Dia kehendaki."
                            }
                        ]
                    },
                    {
                        id: 15,
                        title: "Al Hamiid",
                        file: "topic_15.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Terpuji (Al Hamiid)</li>
                <li>Segala Puji Milik Allah</li>
                <li>Pujian di Dunia dan Akhirat</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Hamiid (Maha Terpuji). Segala puji, baik di langit maupun di bumi, di dunia maupun di akhirat, hanyalah milik Allah. Semua ciptaan-Nya memuji-Nya, dan Dia berhak atas segala pujian karena kesempurnaan sifat-sifat-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Terpuji</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah Yang Maha Pelindung lagi Maha Terpuji.</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 28</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Segala Puji Bagi Allah Pencipta Langit dan Bumi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Segala puji bagi Allah yang telah menciptakan langit dan bumi.</p>
                    <span class="source">Surat Al An'aam Ayat: 1</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Maka bagi Allah-lah segala puji, Tuhan langit dan Tuhan bumi, Tuhan semesta alam.</p>
                    <span class="source">Surat Al Jaatsiyah Ayat: 36</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Pujian di Dunia dan Akhirat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Segala puji bagi Allah yang memiliki apa yang di langit dan apa yang di bumi dan bagi-Nya (pula) segala puji di akhirat. Dan Dia-lah Yang Maha Bijaksana lagi Maha Mengetahui.</p>
                    <span class="source">Surat Saba' Ayat: 1</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Mengucapkan 'Alhamdulillah' (Segala puji bagi Allah) adalah bentuk pengakuan bahwa segala kebaikan dan kesempurnaan hanya milik-Nya. Kita memuji Allah dalam setiap keadaan, baik lapang maupun sempit.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Hamiid?",
                                options: ["Maha Kuasa", "Maha Melihat", "Maha Terpuji", "Maha Mendengar"],
                                correct: 2,
                                explanation: "Al Hamiid artinya Yang Maha Terpuji."
                            },
                            {
                                question: "Menurut Surat Al Jaatsiyah ayat 36, bagi siapa segala puji?",
                                options: ["Bagi Nabi", "Bagi Allah Tuhan semesta alam", "Bagi Malaikat", "Bagi orang tua"],
                                correct: 1,
                                explanation: "Maka bagi Allah-lah segala puji, Tuhan langit dan Tuhan bumi, Tuhan semesta alam."
                            },
                            {
                                question: "Dalam Surat Saba' ayat 1, di mana segala puji bagi Allah berlaku?",
                                options: ["Hanya di bumi", "Hanya di langit", "Di dunia dan di akhirat", "Hanya hari Jum'at"],
                                correct: 2,
                                explanation: "Dan bagi-Nya (pula) segala puji di akhirat."
                            },
                            {
                                question: "Apa sifat yang digandengkan dengan Al Waliy dalam Surat Asy Syuuraa ayat 28?",
                                options: ["Al Hamiid (Maha Terpuji)", "Al Qawiy (Maha Kuat)", "Al Aziz (Maha Perkasa)", "Al Ghafur (Maha Pengampun)"],
                                correct: 0,
                                explanation: "Dan Dialah Yang Maha Pelindung (Al Waliy) lagi Maha Terpuji (Al Hamiid)."
                            },
                            {
                                question: "Apa kalimat yang diucapkan untuk memuji Allah?",
                                options: ["Subhanallah", "Allahu Akbar", "Alhamdulillah", "Astaghfirullah"],
                                correct: 2,
                                explanation: "Alhamdulillah artinya Segala puji bagi Allah."
                            }
                        ]
                    },
                    {
                        id: 16,
                        title: "An Nuur & Al Latiif",
                        file: "topic_16.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Pemberi Cahaya (An Nuur)</li>
                <li>Cahaya di Atas Cahaya</li>
                <li>Allah Maha Lembut/Halus (Al Latiif)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah An Nuur (Pemberi Cahaya). Allah adalah cahaya langit dan bumi. Perumpamaan cahaya-Nya sangat indah dan berlapis-lapis. Dia juga Al Latiif (Maha Halus/Lembut), mengetahui segala sesuatu yang tersembunyi dan memberikan rezeki dengan cara yang halus.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Pemberi Cahaya Langit dan Bumi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah (Pemberi) cahaya (kepada) langit dan bumi. Perumpamaan cahaya Allah, adalah seperti sebuah lubang yang tidak tembus, yang di dalamnya ada pelita besar.</p>
                    <span class="source">Surat An Nuur Ayat: 35</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Cahaya di Atas Cahaya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Cahaya di atas cahaya (berlapis-lapis), Allah membimbing kepada cahaya-Nya siapa yang Dia kehendaki.</p>
                    <span class="source">Surat An Nuur Ayat: 35</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Halus (Al Latiif)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Apakah kamu tidak melihat, bahwasanya Allah menurunkan air dari langit, lalu jadilah bumi itu hijau? Sesungguhnya Allah Maha Halus lagi Maha Mengetahui.</p>
                    <span class="source">Surat Al Hajj Ayat: 63</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kita memohon kepada Allah agar hati kita diterangi dengan cahaya hidayah-Nya. Sifat Al Latiif mengajarkan kita bahwa Allah mengurus hamba-Nya dengan kelembutan yang seringkali tidak kita sadari, seperti tumbuhnya tanaman dari air hujan yang turun dari langit.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari An Nuur?",
                                options: ["Maha Besar", "Maha Pemberi Cahaya", "Maha Gelap", "Maha Tinggi"],
                                correct: 1,
                                explanation: "An Nuur artinya Allah adalah (Pemberi) cahaya bagi langit dan bumi."
                            },
                            {
                                question: "Dalam Surat An Nuur ayat 35, cahaya Allah diumpamakan sebagai?",
                                options: ["Matahari", "Bulan", "Lubang tak tembus yang di dalamnya ada pelita besar", "Api unggun"],
                                correct: 2,
                                explanation: "Perumpamaan cahaya Allah, adalah seperti sebuah lubang yang tidak tembus, yang di dalamnya ada pelita besar."
                            },
                            {
                                question: "Apa arti dari Al Latiif?",
                                options: ["Maha Keras", "Maha Halus/Lembut", "Maha Cepat", "Maha Lambat"],
                                correct: 1,
                                explanation: "Al Latiif artinya Yang Maha Halus atau Maha Lembut."
                            },
                            {
                                question: "Menurut Surat Al Hajj ayat 63, bukti sifat Al Latiif Allah adalah?",
                                options: ["Terjadinya gempa", "Turunnya hujan yang membuat bumi hijau", "Meletusnya gunung", "Terbitnya matahari"],
                                correct: 1,
                                explanation: "Allah menurunkan air dari langit, lalu jadilah bumi itu hijau. Sesungguhnya Allah Maha Halus."
                            },
                            {
                                question: "Siapakah yang dibimbing Allah kepada cahaya-Nya (An Nuur: 35)?",
                                options: ["Semua manusia", "Hanya Malaikat", "Siapa yang Dia kehendaki", "Orang kaya saja"],
                                correct: 2,
                                explanation: "Allah membimbing kepada cahaya-Nya siapa yang Dia kehendaki."
                            }
                        ]
                    },
                    {
                        id: 17,
                        title: "Al Qudduss, As Salaam & Al Mukmin",
                        file: "topic_17.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Suci (Al Qudduss)</li>
                <li>Allah Maha Sejahtera (As Salaam)</li>
                <li>Allah Pemberi Keamanan (Al Mukmin)</li>
                <li>Nama-Nama Indah di Surat Al Hasyr</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas tiga sifat mulia Allah yang sering disebut bersamaan: Al Qudduss (Maha Suci dari segala kekurangan), As Salaam (Maha Sejahtera/Pemberi Keselamatan), dan Al Mukmin (Yang Mengaruniakan Keamanan). Ketiganya menunjukkan kesempurnaan Allah yang mutlak.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Rangkaian Nama Indah dalam Surat Al Hasyr</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dialah Allah yang tiada Tuhan selain Dia, Raja, Yang Maha Suci, Yang Maha Sejahtera, Yang Mengaruniakan keamanan, Yang Maha Memelihara, Yang Maha Perkasa, Yang Maha Kuasa, Yang Memiliki segala keagungan, Maha Suci Allah dari apa yang mereka persekutukan.</p>
                    <span class="source">Surat Al Hasyr Ayat: 23</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Hanya Allah yang Mahasuci (Al Qudduss) dari segala aib. Dia sumber segala keselamatan (As Salaam) dan rasa aman (Al Mukmin). Kita menyucikan Allah dengan bertasbih dan memohon keselamatan serta perlindungan hanya kepada-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Qudduss?",
                                options: ["Maha Raja", "Maha Suci", "Maha Melihat", "Maha Mendengar"],
                                correct: 1,
                                explanation: "Al Qudduss artinya Yang Maha Suci (dari segala kekurangan)."
                            },
                            {
                                question: "Apa arti dari As Salaam?",
                                options: ["Maha Pemberi Rezeki", "Maha Sejahtera / Pemberi Keselamatan", "Maha Menghukum", "Maha Mematikan"],
                                correct: 1,
                                explanation: "As Salaam artinya Yang Maha Sejahtera atau Yang Memberi Keselamatan."
                            },
                            {
                                question: "Apa arti dari Al Mukmin dalam konteks Asmaul Husna?",
                                options: ["Orang beriman", "Yang Mengaruniakan Keamanan", "Yang Mempercayai", "Yang Menjaga"],
                                correct: 1,
                                explanation: "Al Mukmin artinya Yang Mengaruniakan keamanan."
                            },
                            {
                                question: "Di surat manakah ketiga nama ini (Al Qudduss, As Salaam, Al Mukmin) disebutkan berurutan?",
                                options: ["Al Ikhlas", "Al Baqarah", "Al Hasyr ayat 23", "An Naas"],
                                correct: 2,
                                explanation: "Terdapat dalam Surat Al Hasyr ayat 23."
                            },
                            {
                                question: "Apa sebutan Allah sebagai Raja dalam ayat tersebut?",
                                options: ["Al Malik", "Al Aziz", "Al Jabbar", "Al Mutakabbir"],
                                correct: 0,
                                explanation: "Dialah Allah... Al Malik (Raja), Al Qudduss, As Salaam..."
                            }
                        ]
                    },
                    {
                        id: 18,
                        title: "Al Qariib & Al Mujib",
                        file: "topic_18.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Dekat (Al Qariib)</li>
                <li>Allah Maha Mengabulkan Doa (Al Mujib)</li>
                <li>Berhala Tidak Bisa Menolong</li>
                <li>Hanya Allah Tempat Meminta</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Qariib (Maha Dekat) dan Al Mujib (Maha Memperkenankan Doa). Allah sangat dekat dengan hamba-Nya dan menjamin akan mengabulkan doa orang yang memohon kepada-Nya. Sebaliknya, berhala dan sesembahan selain Allah tidak bisa mendengar apalagi mengabulkan doa.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Dekat dan Maha Mengabulkan Doa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Tuhanku Maha Dekat (rahmat-Nya) lagi Maha Memperkenankan (doa).</p>
                    <span class="source">Surat Huud Ayat: 61</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Mengabulkan Doa Orang Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dia memperkenankan (doa) orang-orang beriman serta beramal yang saleh, dan menambah (pahala) mereka dari karunia-Nya.</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 26</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Hanya Allah yang Berhak Disembah dan Dimintai Pertolongan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hanya bagi Allah (hak mengabulkan) doa yang benar. Dan berhala-berhala yang mereka seru selain Allah tidak dapat mengabulkan sesuatupun bagi mereka.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 14</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Jangan pernah merasa sendiri karena Allah itu Al Qariib (Dekat). Jangan ragu untuk berdoa karena Dia Al Mujib (Pengabul Doa). Tinggalkanlah segala bentuk permohonan kepada selain Allah karena itu adalah kesesatan yang nyata.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Qariib?",
                                options: ["Maha Jauh", "Maha Dekat", "Maha Tinggi", "Maha Besar"],
                                correct: 1,
                                explanation: "Al Qariib artinya Maha Dekat."
                            },
                            {
                                question: "Apa arti dari Al Mujib?",
                                options: ["Maha Menolak", "Maha Memperkenankan/Mengabulkan Doa", "Maha Memuliakan", "Maha Menghinakan"],
                                correct: 1,
                                explanation: "Al Mujib artinya Maha Memperkenankan atau Mengabulkan doa."
                            },
                            {
                                question: "Menurut Surat Huud ayat 61, Nabi siapakah yang berkata bahwa Tuhanku Maha Dekat?",
                                options: ["Nabi Musa", "Nabi Nuh", "Nabi Shaleh", "Nabi Ibrahim"],
                                correct: 2,
                                explanation: "Dan kepada Tsamud (kami utus) saudara mereka Shaleh... Shaleh berkata: ... sesungguhnya Tuhanku Maha Dekat."
                            },
                            {
                                question: "Dalam Surat Ar Ra'd ayat 14, bagaikan apakah orang yang berdoa kepada berhala?",
                                options: ["Orang yang tidur", "Orang yang membukakan kedua telapak tangannya ke air agar air sampai ke mulutnya", "Orang yang berteriak di hutan", "Orang yang bisu"],
                                correct: 1,
                                explanation: "Melainkan seperti orang yang membukakan kedua telapak tangannya ke dalam air agar sampai air ke mulutnya, padahal air itu tidak dapat sampai."
                            },
                            {
                                question: "Siapakah yang doanya diperkenankan Allah menurut Surat Asy Syuuraa ayat 26?",
                                options: ["Orang-orang kaya", "Orang-orang beriman serta beramal saleh", "Orang-orang yang berteriak keras", "Hanya para Nabi"],
                                correct: 1,
                                explanation: "Dan Dia memperkenankan (doa) orang-orang beriman serta beramal yang saleh."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-4",
                title: "Pokok Bahasan 4: Sifat Allah Bagian 4",
                topics: [
                    {
                        id: 19,
                        title: "Al Waasi'",
                        file: "topic_19.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Luas (Al Waasi')</li>
                <li>Maha Luas Ampunan-Nya</li>
                <li>Maha Luas Rahmat-Nya</li>
                <li>Kursi Allah Meliputi Langit dan Bumi</li>
                <li>Ilmu Allah Meliputi Segala Sesuatu</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Waasi' (Maha Luas). Kekuasaan, ilmu, rahmat, dan ampunan Allah sangat luas dan tidak terbatas. Wajah Allah ada di timur dan barat, dan kursi-Nya meliputi langit dan bumi.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Luas dan Mengetahui</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan kepunyaan Allah-lah timur dan barat... Sesungguhnya Allah Maha Luas lagi Maha Mengetahui.</p>
                    <span class="source">Surat Al Baqarah Ayat: 115</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Maha Luas Ampunan-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Tuhanmu Maha Luas ampunan-Nya.</p>
                    <span class="source">Surat An Najm Ayat: 32</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Rahmat Allah Meliputi Segala Sesuatu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan rahmat-Ku meliputi segala sesuatu.</p>
                    <span class="source">Surat Al A'raaf Ayat: 156</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kursi Allah Meliputi Langit dan Bumi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kursi Allah meliputi langit dan bumi.</p>
                    <span class="source">Surat Al Baqarah Ayat: 255 (Ayat Kursi)</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Luasnya rahmat dan ampunan Allah memberi harapan bagi kita untuk selalu bertaubat dan memohon karunia-Nya. Namun, kita juga harus ingat bahwa ilmu Allah meliputi segala gerak-gerik kita, tidak ada yang tersembunyi bagi-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Waasi'?",
                                options: ["Maha Sempit", "Maha Luas", "Maha Tinggi", "Maha Jauh"],
                                correct: 1,
                                explanation: "Al Waasi' artinya Allah Maha Luas (kekuasaan, rahmat, ilmu, dan ampunan-Nya)."
                            },
                            {
                                question: "Dalam Surat Al Baqarah ayat 115, kepunyaan siapakah timur dan barat?",
                                options: ["Milik manusia", "Milik raja", "Milik Allah", "Tidak ada yang punya"],
                                correct: 2,
                                explanation: "Dan kepunyaan Allah-lah timur dan barat."
                            },
                            {
                                question: "Apa yang dikatakan tentang ampunan Allah dalam Surat An Najm ayat 32?",
                                options: ["Ampunan-Nya sedikit", "Ampunan-Nya terbatas", "Tuhanmu Maha Luas ampunan-Nya", "Tidak ada ampunan"],
                                correct: 2,
                                explanation: "Sesungguhnya Tuhanmu Maha Luas ampunan-Nya."
                            },
                            {
                                question: "Dalam Ayat Kursi (Al Baqarah: 255), apa yang meliputi langit dan bumi?",
                                options: ["Singgasana manusia", "Kursi Allah", "Awan", "Bintang"],
                                correct: 1,
                                explanation: "Kursi Allah meliputi langit dan bumi."
                            },
                            {
                                question: "Kepada siapakah rahmat Allah yang luas ditetapkan (Al A'raaf: 156)?",
                                options: ["Orang yang bertakwa, menunaikan zakat, dan beriman", "Orang kafir", "Semua orang tanpa terkecuali", "Hanya para pejabat"],
                                correct: 1,
                                explanation: "Maka akan Aku tetapkan rahmat-Ku untuk orang-orang yang bertakwa, yang menunaikan zakat, dan orang-orang yang beriman kepada ayat-ayat Kami."
                            }
                        ]
                    },
                    {
                        id: 20,
                        title: "Al Haqq & Maha Menepati Janji",
                        file: "topic_20.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Benar (Al Haqq)</li>
                <li>Tuhan Selain Allah adalah Batil</li>
                <li>Allah Maha Menepati Janji</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Haqq (Maha Benar). Allah adalah Tuhan yang sebenarnya, sedangkan sesembahan selain Dia adalah batil (salah/palsu). Allah juga Maha Menepati Janji, janji-Nya kepada para Rasul dan orang beriman adalah benar dan pasti terjadi.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Adalah Al Haqq (Maha Benar)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Yang demikian itu, karena sesungguhnya Allah, Dialah yang haq dan sesungguhnya Dialah yang menghidupkan segala yang mati.</p>
                    <span class="source">Surat Al Hajj Ayat: 6</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Sesembahan Selain Allah Adalah Batil</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya apa saja yang mereka seru selain dari Allah itulah yang batil.</p>
                    <span class="source">Surat Al Hajj Ayat: 62</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Menepati Janji</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka janganlah sekali-kali kamu mengira Allah akan menyalahi janji-Nya kepada rasul-rasul-Nya; sesungguhnya Allah Maha Perkasa lagi Maha Mempunyai pembalasan.</p>
                    <span class="source">Surat Ibraahiim Ayat: 47</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kebenaran mutlak hanya milik Allah. Segala janji Allah tentang surga, neraka, dan kebangkitan adalah benar adanya (Haqq). Kita harus meyakini hal ini dan menjauhi segala kebatilan.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Haqq?",
                                options: ["Maha Kuat", "Maha Benar/Haq", "Maha Indah", "Maha Pemurah"],
                                correct: 1,
                                explanation: "Al Haqq artinya Yang Maha Benar."
                            },
                            {
                                question: "Menurut Surat Al Hajj ayat 62, apa status sesembahan selain Allah?",
                                options: ["Benar", "Suci", "Batil (Salah/Palsu)", "Mulia"],
                                correct: 2,
                                explanation: "Dan sesungguhnya apa saja yang mereka seru selain dari Allah itulah yang batil."
                            },
                            {
                                question: "Siapakah yang menghidupkan segala yang mati menurut Surat Al Hajj ayat 6?",
                                options: ["Dokter", "Alam Semesta", "Allah Yang Maha Haqq", "Tidak ada"],
                                correct: 2,
                                explanation: "Sesungguhnya Allah, Dialah yang haq dan sesungguhnya Dialah yang menghidupkan segala yang mati."
                            },
                            {
                                question: "Apakah Allah akan menyalahi janji-Nya kepada Rasul-rasul-Nya (Surat Ibraahiim: 47)?",
                                options: ["Ya, mungkin saja", "Tidak, jangan sekali-kali mengira demikian", "Tidak tahu", "Tergantung keadaan"],
                                correct: 1,
                                explanation: "Maka janganlah sekali-kali kamu mengira Allah akan menyalahi janji-Nya kepada rasul-rasul-Nya."
                            },
                            {
                                question: "Apa sifat Allah yang disebut di akhir Surat Ibraahiim ayat 47?",
                                options: ["Maha Pengampun", "Maha Perkasa lagi Maha Mempunyai pembalasan", "Maha Lembut", "Maha Kaya"],
                                correct: 1,
                                explanation: "Sesungguhnya Allah Maha Perkasa lagi Maha Mempunyai pembalasan."
                            }
                        ]
                    },
                    {
                        id: 21,
                        title: "Al Haliim & Al Syakuur",
                        file: "topic_21.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Penyantun (Al Haliim)</li>
                <li>Allah Maha Mensyukuri (Al Syakuur)</li>
                <li>Segala Puji Bagi Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Haliim (Maha Penyantun), yang tidak tergesa-gesa menghukum hamba-Nya yang berbuat dosa. Allah juga Al Syakuur (Maha Mensyukuri), yang memberi balasan berlipat ganda atas amal soleh yang sedikit dan menghargai usaha hamba-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Mengetahui dan Maha Penyantun</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya Allah Maha Mengetahui lagi Maha Penyantun.</p>
                    <span class="source">Surat Al Hajj Ayat: 59</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Pengampun dan Maha Mensyukuri</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Tuhan Kami benar-benar Maha Pengampun lagi Maha Mensyukuri.</p>
                    <span class="source">Surat Faathir Ayat: 34</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Jika bukan karena sifat Al Haliim Allah, niscaya kita sudah binasa karena dosa-dosa kita yang langsung dibalas. Kita harus bersyukur kepada Allah yang Al Syakuur, yang menghargai setiap kebaikan kita meski kecil.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Haliim?",
                                options: ["Maha Cepat Siksanya", "Maha Penyantun (Tidak tergesa-gesa menghukum)", "Maha Kaya", "Maha Bijaksana"],
                                correct: 1,
                                explanation: "Al Haliim artinya Maha Penyantun, tidak segera menyiksa orang yang durhaka meski Dia mampu."
                            },
                            {
                                question: "Apa arti dari Al Syakuur?",
                                options: ["Maha Meminta Terima Kasih", "Maha Mensyukuri (Memberi balasan besar untuk amal sedikit)", "Maha Melupakan", "Maha Menghitung"],
                                correct: 1,
                                explanation: "Al Syakuur artinya Maha Mensyukuri atau Menerima syukur hamba-Nya dengan memberi pahala berlipat."
                            },
                            {
                                question: "Dalam Surat Al Hajj ayat 59, kemana Allah akan memasukkan orang-orang (mukmin)?",
                                options: ["Ke neraka", "Ke tempat yang mereka menyukainya (surga)", "Ke hutan", "Ke laut"],
                                correct: 1,
                                explanation: "Sesungguhnya Allah akan memasukkan mereka ke dalam suatu tempat (surga) yang mereka menyukainya."
                            },
                            {
                                question: "Apa ucapan penghuni surga dalam Surat Faathir ayat 34?",
                                options: ["Duhai celakanya kami", "Segala puji bagi Allah yang telah menghilangkan duka cita dari kami", "Kembalikan kami ke dunia", "Kami ingin tidur"],
                                correct: 1,
                                explanation: "Segala puji bagi Allah yang telah menghilangkan duka cita dari kami."
                            },
                            {
                                question: "Sifat apa yang bergandengan dengan Al Syakuur dalam Surat Faathir ayat 34?",
                                options: ["Al Ghafur (Maha Pengampun)", "Al Aziz (Maha Perkasa)", "Al Qawiy (Maha Kuat)", "Al Jabbar (Maha Kuasa)"],
                                correct: 1,
                                explanation: "Sesungguhnya Tuhan Kami benar-benar Maha Pengampun (Al Ghafur) lagi Maha Mensyukuri (Al Syakuur)."
                            }
                        ]
                    },
                    {
                        id: 22,
                        title: "Al Waarits",
                        file: "topic_22.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Mewarisi (Al Waarits)</li>
                <li>Mewarisi Bumi dan Isinya</li>
                <li>Pewaris Negeri yang Binasa</li>
                <li>Mewariskan Surga kepada Orang Bertakwa</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Waarits (Maha Mewarisi). Setelah alam semesta hancur, segala sesuatu kembali kepada Allah. Allah juga yang mewariskan bumi kepada hamba-hamba-Nya yang saleh dan mewariskan surga kepada orang yang bertakwa.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Menghidupkan dan Mewarisi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya benar-benar Kami-lah yang menghidupkan dan mematikan dan Kami (pula) yang mewarisi.</p>
                    <span class="source">Surat Al Hijr Ayat: 23</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Mewarisi Bumi dan Isinya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami mewarisi bumi dan semua orang-orang yang ada di atasnya, dan hanya kepada Kamilah mereka dikembalikan.</p>
                    <span class="source">Surat Maryam Ayat: 40</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Bumi Dipusakai Hamba yang Saleh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Bahwasanya bumi ini dipusakai hamba-hamba-Ku yang saleh.</p>
                    <span class="source">Surat Al Anbiyaa' Ayat: 105</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Surga Diwariskan kepada Orang Bertakwa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Itulah surga yang akan Kami wariskan kepada hamba-hamba Kami yang selalu bertakwa.</p>
                    <span class="source">Surat Maryam Ayat: 63</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Segala kepemilikan kita di dunia hanyalah titipan sementara. Pemilik sejati dan pewaris mutlak adalah Allah. Maka gunakanlah titipan itu untuk ketaatan agar kita diwarisi surga-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Waarits?",
                                options: ["Maha Kaya", "Maha Mewarisi", "Maha Memberi", "Maha Mengambil"],
                                correct: 1,
                                explanation: "Al Waarits artinya Yang Maha Mewarisi segalanya setelah semua makhluk binasa."
                            },
                            {
                                question: "Menurut Surat Maryam ayat 40, siapa yang mewarisi bumi dan isinya?",
                                options: ["Raja-raja dunia", "Manusia", "Allah (Kami)", "Malaikat"],
                                correct: 2,
                                explanation: "Sesungguhnya Kami (Allah) mewarisi bumi dan semua orang-orang yang ada di atasnya."
                            },
                            {
                                question: "Siapakah yang akan mempusakai bumi menurut Surat Al Anbiyaa' ayat 105?",
                                options: ["Orang yang kuat", "Hamba-hamba-Ku yang saleh", "Orang yang kaya", "Para pemimpin"],
                                correct: 1,
                                explanation: "Bahwasanya bumi ini dipusakai hamba-hamba-Ku yang saleh."
                            },
                            {
                                question: "Kepada siapakah surga diwariskan menurut Surat Maryam ayat 63?",
                                options: ["Hamba yang selalu bertakwa", "Hamba yang berdosa", "Semua manusia", "Orang yang berilmu saja"],
                                correct: 0,
                                explanation: "Itulah surga yang akan Kami wariskan kepada hamba-hamba Kami yang selalu bertakwa."
                            },
                            {
                                question: "Apa yang terjadi pada negeri yang penduduknya bersenang-senang (dalam dosa) di Al Qashash ayat 58?",
                                options: ["Bertambah makmur", "Dibinasakan dan tidak didiami lagi", "Dijadikan pusat wisata", "Diberi kekayaan"],
                                correct: 1,
                                explanation: "Dan berapa banyak (penduduk) negeri yang telah Kami binasakan... maka itulah tempat kediaman mereka yang tiada didiami (lagi)."
                            }
                        ]
                    },
                    {
                        id: 23,
                        title: "Al Mubiin, Al Haadiy & Al Raasyid",
                        file: "topic_23.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Memberi Petunjuk (Al Haadiy)</li>
                <li>Tidak Ada yang Bisa Memberi Petunjuk Selain Allah</li>
                <li>Hidayah untuk Orang yang Dikehendaki</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah yang memberi petunjuk (Al Haadiy). Hanya Allah yang mampu memberikan hidayah taufiq (bimbingan hati) kepada hamba-Nya. Jika Allah membiarkan seseorang sesat, tidak ada yang bisa menunjukinya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Barangsiapa Diberi Petunjuk oleh Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Siapa yang diberi petunjuk oleh Allah, maka dialah yang mendapat petunjuk.</p>
                    <span class="source">Surat Al A'raaf Ayat: 178</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tidak Ada Petunjuk Bagi yang Disesatkan Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Siapa yang Allah sesatkan, maka baginya tak ada yang akan memberi petunjuk.</p>
                    <span class="source">Surat Al A'raaf Ayat: 186</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Lapang Dada Menerima Islam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Siapa yang Allah menghendaki akan memberinya petunjuk, niscaya Dia melapangkan dadanya untuk (memeluk agama) Islam.</p>
                    <span class="source">Surat Al An'aam Ayat: 125</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Memberi Petunjuk Kepada yang Dikehendaki</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Allah memberikan petunjuk kepada siapa yang Dia kehendaki.</p>
                    <span class="source">Surat Al Hajj Ayat: 16</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Hidayah adalah milik Allah semata. Bahkan Nabi Muhammad SAW tidak bisa memberi hidayah taufiq kepada orang yang dicintainya (seperti pamannya), hanya Allah yang membolak-balikkan hati.</p>
                        `,
                        quiz: [
                            {
                                question: "Siapakah yang bisa memberi petunjuk jika Allah menyesatkan seseorang (Al A'raaf: 186)?",
                                options: ["Para Nabi", "Malaikat", "Tidak ada seorangpun", "Guru agama"],
                                correct: 2,
                                explanation: "Maka baginya tak ada yang akan memberi petunjuk."
                            },
                            {
                                question: "Apa tanda seseorang dikehendaki mendapat petunjuk menurut Surat Al An'aam ayat 125?",
                                options: ["Dilapangkan dadanya untuk Islam", "Menjadi kaya raya", "Menjadi terkenal", "Badannya sehat"],
                                correct: 0,
                                explanation: "Niscaya Dia melapangkan dadanya untuk (memeluk agama) Islam."
                            },
                            {
                                question: "Sebaliknya, apa tanda orang yang dikehendaki kesesatannya (Al An'aam: 125)?",
                                options: ["Dadanya sempit lagi sesak seolah mendaki langit", "Hidupnya mewah", "Banyak temannya", "Selalu gembira"],
                                correct: 0,
                                explanation: "Niscaya Allah menjadikan dadanya sesak lagi sempit, seolah-olah ia sedang mendaki langit."
                            },
                            {
                                question: "Apakah Nabi bisa memberi petunjuk kepada orang yang dikasihinya (Al Qashash: 56)?",
                                options: ["Bisa, jika mau", "Tidak, sesungguhnya kamu tidak dapat memberi petunjuk kepada orang yang kamu kasihi", "Tentu saja bisa", "Bisa dengan izin malaikat"],
                                correct: 1,
                                explanation: "Sesungguhnya kamu tidak akan dapat memberi petunjuk kepada orang yang kamu kasihi, tetapi Allah memberi petunjuk kepada orang yang dikehendaki-Nya."
                            },
                            {
                                question: "Siapakah yang rugi menurut Surat Al A'raaf ayat 178?",
                                options: ["Orang miskin", "Orang yang disesatkan Allah", "Orang bodoh", "Orang lemah"],
                                correct: 1,
                                explanation: "Dan siapa yang disesatkan Allah, maka merekalah orang-orang yang merugi."
                            }
                        ]
                    },
                    {
                        id: 24,
                        title: "Al Awwal, Al Aakhir, Azh Zhaahir & Al Baathin",
                        file: "topic_24.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Yang Awal (Al Awwal)</li>
                <li>Allah Yang Akhir (Al Aakhir)</li>
                <li>Allah Yang Zhahir (Azh Zhaahir)</li>
                <li>Allah Yang Bathin (Al Baathin)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas empat sifat Allah yang agung dalam Surat Al Hadiid ayat 3. Dialah Yang Awal (tanpa permulaan), Yang Akhir (tanpa kesudahan), Yang Zhahir (nyata bukti kekuasaan-Nya), dan Yang Bathin (tersembunyi zat-Nya dari penglihatan mata).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Empat Sifat Agung dalam Satu Ayat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dialah Yang Awal dan Yang Akhir Yang Zhahir dan Yang Bathin; dan Dia Maha Mengetahui segala sesuatu.</p>
                    <span class="source">Surat Al Hadiid Ayat: 3</span>
                </div>
            </div>

            <div class="note-box">
                <strong>Penjelasan Makna:</strong>
                <ul>
                    <li><b>Al Awwal:</b> Yang telah ada sebelum segala sesuatu ada (Tanpa permulaan).</li>
                    <li><b>Al Aakhir:</b> Yang tetap ada setelah segala sesuatu musnah (Kekal/Tanpa akhir).</li>
                    <li><b>Azh Zhaahir:</b> Yang nyata adanya karena banyak bukti-bukti kekuasaan-Nya (Mahatinggi/Berkuasa).</li>
                    <li><b>Al Baathin:</b> Yang tidak dapat digambarkan hikmat zat-Nya oleh akal atau tersembunyi dari pandangan mata (Mahadekat/Mengetahui yang gaib).</li>
                </ul>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Keempat sifat ini mencakup segala aspek ketuhanan. Allah meliputi segala sesuatu dari segi waktu (Awal dan Akhir) dan dari segi ruang/eksistensi (Zhahir dan Bathin).</p>
                        `,
                        quiz: [
                            {
                                question: "Di surat manakah keempat sifat (Awal, Akhir, Zhahir, Bathin) disebutkan sekaligus?",
                                options: ["Al Ikhlas", "Al Hadiid ayat 3", "Al Baqarah", "Al Mulk"],
                                correct: 1,
                                explanation: "Surat Al Hadiid Ayat 3: Dialah Yang Awal dan Yang Akhir Yang Zhahir dan Yang Bathin."
                            },
                            {
                                question: "Apa arti dari Al Awwal?",
                                options: ["Yang paling muda", "Yang telah ada sebelum segala sesuatu ada (Tanpa permulaan)", "Yang diciptakan pertama", "Yang nomor satu"],
                                correct: 1,
                                explanation: "Al Awwal ialah yang telah ada sebelum segala sesuatu ada."
                            },
                            {
                                question: "Apa arti dari Al Aakhir?",
                                options: ["Yang terakhir datang", "Yang paling belakang", "Yang tetap ada setelah segala sesuatu musnah (Kekal)", "Yang berakhir"],
                                correct: 2,
                                explanation: "Al Aakhir ialah yang tetap ada setelah segala sesuatu musnah."
                            },
                            {
                                question: "Apa arti dari Azh Zhaahir?",
                                options: ["Yang terlihat mata", "Yang nyata adanya karena bukti-bukti kekuasaan-Nya", "Yang pamer", "Yang di luar"],
                                correct: 1,
                                explanation: "Yang Zhahir ialah yang nyata adanya karena banyak bukti-buktinya."
                            },
                            {
                                question: "Apa arti dari Al Baathin?",
                                options: ["Yang ada di perut", "Yang tidak dapat digambarkan zat-Nya / Tersembunyi", "Yang berilmu hitam", "Yang sakit dalam"],
                                correct: 1,
                                explanation: "Yang Bathin ialah yang tak dapat digambarkan hikmat zat-Nya oleh akal."
                            }
                        ]
                    }
                ]

            },
            {
                id: "subject-5",
                title: "Pokok Bahasan 5: Sifat Allah Bagian 5",
                topics: [
                    {
                        id: 25,
                        title: "Al Baqaa (Maha Kekal)",
                        file: "topic_25.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Kekal (Al Baqaa)</li>
                <li>Segala Sesuatu Akan Binasa Kecuali Wajah-Nya</li>
                <li>Apa yang di Sisi Allah Lebih Kekal</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Al Baqaa (Maha Kekal). Dunia dan segala isinya bersifat fana (akan binasa), sedangkan zat Allah kekal abadi selamanya. Amal saleh yang kita lakukan ikhlas karena Allah adalah sesuatu yang kekal ganjarannya di sisi-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Segala Sesuatu Akan Binasa Kecuali Wajah-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Semua yang ada di bumi itu akan binasa. Dan tetap kekal Wajah (Dzat) Tuhanmu yang mempunyai kebesaran dan kemuliaan.</p>
                    <span class="source">Surat Ar Rahmaan Ayat: 26-27</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Apa yang di Sisi Allah Lebih Baik dan Kekal</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan amal-amal saleh yang kekal itu lebih baik pahalanya di sisi Tuhanmu dan lebih baik kesudahannya.</p>
                    <span class="source">Surat Maryam Ayat: 76</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Menyadari sifat Al Baqaa membuat kita tidak tertipu dengan keindahan dunia yang sementara. Kita harus fokus mencari bekal yang kekal (akhirat) dengan beramal saleh.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Baqaa?",
                                options: ["Maha Kuasa", "Maha Kekal", "Maha Mengetahui", "Maha Adil"],
                                correct: 1,
                                explanation: "Al Baqaa artinya Maha Kekal, tidak akan pernah binasa."
                            },
                            {
                                question: "Menurut Surat Ar Rahmaan ayat 26, apa yang terjadi pada semua yang ada di bumi?",
                                options: ["Akan kekal", "Akan bertambah", "Akan binasa (fana)", "Akan pindah"],
                                correct: 2,
                                explanation: "Semua yang ada di bumi itu akan binasa."
                            },
                            {
                                question: "Siapakah yang tetap kekal menurut Surat Ar Rahmaan ayat 27?",
                                options: ["Malaikat", "Langit", "Wajah (Dzat) Tuhanmu", "Gunung"],
                                correct: 2,
                                explanation: "Dan tetap kekal Wajah (Dzat) Tuhanmu yang mempunyai kebesaran dan kemuliaan."
                            },
                            {
                                question: "Apa yang disebut lebih baik dan kekal di sisi Tuhan (Maryam: 76)?",
                                options: ["Harta benda", "Amal-amal saleh", "Jabatan", "Anak keturunan"],
                                correct: 1,
                                explanation: "Dan amal-amal saleh yang kekal itu lebih baik pahalanya di sisi Tuhanmu."
                            },
                            {
                                question: "Sifat Allah ini mengajarkan kita untuk?",
                                options: ["Mencintai dunia berlebihan", "Takut mati", "Mengutamakan akhirat yang kekal", "Menumpuk harta"],
                                correct: 2,
                                explanation: "Sifat Al Baqaa menyadarkan kita bahwa dunia sementara, sehingga kita harus mengutamakan akhirat yang kekal."
                            }
                        ]
                    },
                    {
                        id: 26,
                        title: "Al 'Aliy, Al Muta'aal & Al Raafi'",
                        file: "topic_26.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Tinggi (Al 'Aliy / Al Muta'aal)</li>
                <li>Allah Maha Meninggikan Derajat (Al Raafi')</li>
                <li>Tingginya Allah di atas 'Arsy</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Tinggi (Al 'Aliy / Al Muta'aal). Allah Maha Tinggi zat-Nya di atas 'Arsy dan Maha Tinggi sifat-Nya dari segala kekurangan. Allah juga Al Raafi', yang meninggikan derajat hamba-hambaNya yang beriman dan berilmu.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Tinggi dari Kesyirikan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maha Tinggi Allah daripada apa yang mereka persekutukan.</p>
                    <span class="source">Surat An Nahl Ayat: 3</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Yang Maha Tinggi Derajat-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">(Dialah) Yang Maha Tinggi derajat-Nya, yang mempunyai 'Arsy.</p>
                    <span class="source">Surat Al Mu'min Ayat: 15</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kita harus selalu mengagungkan Allah yang Maha Tinggi. Jangan pernah merasa sombong di hadapan-Nya, dan mintalah agar Allah meninggikan derajat kita dengan ilmu dan iman.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al 'Aliy / Al Muta'aal?",
                                options: ["Maha Dekat", "Maha Tinggi / Luhur", "Maha Lembut", "Maha Keras"],
                                correct: 1,
                                explanation: "Al 'Aliy dan Al Muta'aal artinya Yang Maha Tinggi."
                            },
                            {
                                question: "Dalam Surat An Nahl ayat 3, Allah Maha Tinggi dari apa?",
                                options: ["Dari langit", "Dari apa yang mereka persekutukan", "Dari bumi", "Dari manusia"],
                                correct: 1,
                                explanation: "Maha Tinggi Allah daripada apa yang mereka persekutukan."
                            },
                            {
                                question: "Apa arti dari Al Raafi'?",
                                options: ["Yang Maha Merendahkan", "Yang Maha Meninggikan / Mengangkat", "Yang Maha Memberi Rizki", "Yang Maha Mematikan"],
                                correct: 1,
                                explanation: "Al Raafi' artinya Yang Maha Meninggikan (derajat)."
                            },
                            {
                                question: "Di manakah Allah bersemayam menurut sifat-Nya yang disebut 'Dzu Al 'Arsy'?",
                                options: ["Di bumi", "Di mana-mana", "Di atas 'Arsy (Singgasana)", "Di dalam hati"],
                                correct: 2,
                                explanation: "Yang mempunyai 'Arsy (Singgasana)."
                            },
                            {
                                question: "Apa tujuan Allah mengutus Ruh (Jibril) dengan perintah-Nya (Al Mu'min: 15)?",
                                options: ["Untuk memberi harta", "Untuk memperingatkan tentang hari pertemuan (Kiamat)", "Untuk menghibur", "Untuk bermain"],
                                correct: 1,
                                explanation: "Supaya Dia memperingatkan (manusia) tentang hari pertemuan (hari kiamat)."
                            }
                        ]
                    },
                    {
                        id: 27,
                        title: "Al 'Azhiim, Al Maajid & Al Kariim",
                        file: "topic_27.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Agung (Al 'Azhiim)</li>
                <li>Allah Maha Mulia (Al Maajid / Al Majiid)</li>
                <li>Allah Maha Pemurah (Al Kariim)</li>
                <li>Pemilik Kebesaran dan Kemuliaan (Dzu Al Jalaali wa Al Ikraam)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas keagungan dan kemuliaan Allah. Dia Al 'Azhiim (Maha Agung) yang menguasai langit dan bumi. Dia Al Kariim (Maha Pemurah) yang nikmat-Nya melimpah. Dia Dzu Al Jalaali wa Al Ikraam, pemilik segala kebesaran dan penghormatan.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Tinggi lagi Maha Besar</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah Yang Maha Tinggi lagi Maha Besar (Agung).</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 4</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Pemilik Arsy yang Maha Mulia</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Yang mempunyai 'Arsy, lagi Maha Mulia.</p>
                    <span class="source">Surat Al Buruuj Ayat: 15</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tuhan Yang Maha Pemurah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hai manusia, apakah yang telah memperdayakan kamu (berbuat durhaka) terhadap Tuhanmu Yang Maha Pemurah.</p>
                    <span class="source">Surat Al Infithaar Ayat: 6</span>
                </div>
            </div>

             <div class="content-section">
                <h3>Pemilik Kebesaran dan Karunia</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maha Agung nama Tuhanmu yang mempunyai kebesaran dan karunia.</p>
                    <span class="source">Surat Ar Rahmaan Ayat: 78</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Hanya Allah yang berhak atas segala keagungan (Kibriyaa'). Kita sebagai hamba yang kecil dan hina tidak pantas menyombongkan diri. Kita harus senantiasa memuji Allah dengan asma-Nya yang indah.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al 'Azhiim?",
                                options: ["Maha Kecil", "Maha Besar / Agung", "Maha Mendengar", "Maha Melihat"],
                                correct: 1,
                                explanation: "Al 'Azhiim artinya Yang Maha Agung atau Maha Besar."
                            },
                            {
                                question: "Sifat apa yang disebutkan bersama Al 'Aliy dalam Surat Asy Syuuraa ayat 4?",
                                options: ["Al 'Azhiim", "Al Ghafuur", "Al Rahiim", "Al Qudduus"],
                                correct: 1,
                                explanation: "Dan Dialah Yang Maha Tinggi (Al 'Aliy) lagi Maha Besar (Al 'Azhiim)."
                            },
                            {
                                question: "Dalam Surat Al Infithaar ayat 6, manusia diperingatkan agar tidak durhaka kepada Tuhan yang...?",
                                options: ["Maha Keras", "Maha Pemurah (Al Kariim)", "Maha Menghukum", "Maha Jauh"],
                                correct: 1,
                                explanation: "Terhadap Tuhanmu Yang Maha Pemurah (Al Kariim)."
                            },
                            {
                                question: "Apa arti dari Al Majiid?",
                                options: ["Maha Mulia", "Maha Kaya", "Maha Indah", "Maha Dekat"],
                                correct: 1,
                                explanation: "Al Majiid artinya Yang Maha Mulia."
                            },
                            {
                                question: "Apa arti Dzu Al Jalaali wa Al Ikraam?",
                                options: ["Pemilik langit dan bumi", "Yang mempunyai kebesaran dan karunia/kemuliaan", "Raja manusia", "Pencipta alam"],
                                correct: 1,
                                explanation: "Yang mempunyai kebesaran dan karunia (kemuliaan)."
                            }
                        ]
                    },
                    {
                        id: 28,
                        title: "Al Tawwaab & Al 'Afuww",
                        file: "topic_28.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Penerima Tobat (Al Tawwaab)</li>
                <li>Allah Maha Pemaaf (Al 'Afuww)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Penerima Tobat (Al Tawwaab) dan Maha Pemaaf (Al 'Afuww). Allah senantiasa membuka pintu tobat bagi hamba-Nya yang mau kembali, dan Dia juga memaafkan kesalahan-kesalahan hamba-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Penerima Tobat lagi Maha Penyayang</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tidaklah mereka mengetahui, bahwasanya Allah menerima taubat dari hamba-hamba-Nya... dan bahwasanya Allah Maha Penerima taubat lagi Maha Penyayang?</p>
                    <span class="source">Surat At Taubah Ayat: 104</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Hendak Menerima Tobatmu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Allah hendak menerima taubatmu, sedang orang-orang yang mengikuti hawa nafsunya bermaksud supaya kamu berpaling sejauh-jauhnya.</p>
                    <span class="source">Surat An Nisaa' Ayat: 27</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Memaafkan Kesalahan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah yang menerima taubat dari hamba-hamba-Nya dan memaafkan kesalahan-kesalahan.</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 25</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sifat Al Tawwaab dan Al 'Afuww memberikan harapan besar bagi kita yang sering berbuat dosa. Jangan pernah berputus asa dari rahmat Allah, segeralah bertobat dan memohon maaf kepada-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Tawwaab?",
                                options: ["Maha Pemberi Rezeki", "Maha Penerima Tobat", "Maha Perkasa", "Maha Melihat"],
                                correct: 2,
                                explanation: "Al Tawwaab artinya Yang Maha Penerima Tobat."
                            },
                            {
                                question: "Apa arti dari Al 'Afuww?",
                                options: ["Maha Pemaaf", "Maha Menghukum", "Maha Adil", "Maha Kaya"],
                                correct: 1,
                                explanation: "Al 'Afuww artinya Yang Maha Pemaaf."
                            },
                            {
                                question: "Menurut Surat At Taubah ayat 104, siapakah yang menerima tobat hamba?",
                                options: ["Nabi", "Malaikat", "Allah", "Ulama"],
                                correct: 3,
                                explanation: "Tidaklah mereka mengetahui, bahwasanya Allah menerima taubat dari hamba-hamba-Nya."
                            },
                            {
                                question: "Apa yang dilakukan Allah terhadap kesalahan-kesalahan hamba-Nya (Asy Syuuraa: 25)?",
                                options: ["Mencatatnya saja", "Memaafkannya (jika bertobat)", "Mengumumkannya", "Melupakannya"],
                                correct: 2,
                                explanation: "Dan memaafkan kesalahan-kesalahan."
                            },
                            {
                                question: "Apa tujuan orang yang mengikuti hawa nafsu (An Nisaa': 27)?",
                                options: ["Supaya kamu berpaling sejauh-jauhnya", "Supaya kamu bertobat", "Supaya kamu kaya", "Supaya kamu pintar"],
                                correct: 1,
                                explanation: "Sedang orang-orang yang mengikuti hawa nafsunya bermaksud supaya kamu berpaling sejauh-jauhnya."
                            }
                        ]
                    },
                    {
                        id: 29,
                        title: "Al Ghafuur, Al Ghaffaar & Al Ghaafir",
                        file: "topic_29.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pengampun (Al Ghafuur/Al Ghaffaar/Al Ghaafir)</li>
                <li>Allah Menjanjikan Maghfirah (Ampunan)</li>
                <li>Allah Tidak Mengampuni Dosa Syirik</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat-sifat pengampunan Allah (Al Ghafuur, Al Ghaffaar). Allah menjanjikan ampunan yang luas bagi hamba-Nya yang beriman dan beramal saleh. Namun, ada satu dosa yang tidak akan diampuni jika dibawa mati tanpa tobat, yaitu syirik.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Kabar Gembira dan Peringatan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kabarkanlah kepada hamba-hamba-Ku, bahwa sesungguhnya Aku-lah Yang Maha Pengampun lagi Maha Penyayang, dan bahwa sesungguhnya azab-Ku adalah azab yang sangat pedih.</p>
                    <span class="source">Surat Al Hijr Ayat: 49-50</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Janji Ampunan bagi Orang Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah telah menjanjikan kepada orang-orang yang beriman dan yang beramal saleh, (bahwa) untuk mereka ampunan dan pahala yang besar.</p>
                    <span class="source">Surat Al Maaidah Ayat: 9</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Dosa yang Tidak Diampuni</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah tidak mengampuni syirik (mempersekutukan sesuatu) dengan-Nya, dan Dia mengampuni apa (dosa) yang selain (syirik) bagi siapa yang Dia kehendaki.</p>
                    <span class="source">Surat An Nisaa' Ayat: 48</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Luasnya ampunan Allah seharusnya memotivasi kita untuk terus beristighfar dan beramal saleh. Namun, kita juga harus sangat waspada menjauhi syirik, karena itu adalah penghalang mutlak mendapat ampunan-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Ghafuur?",
                                options: ["Maha Pemberi", "Maha Pengampun", "Maha Bijaksana", "Maha Mengetahui"],
                                correct: 2,
                                explanation: "Al Ghafuur artinya Yang Maha Pengampun."
                            },
                            {
                                question: "Dalam Surat Al Hijr ayat 49, apa yang diperintahkan Allah untuk dikabarkan kepada hamba-Nya?",
                                options: ["Bahwa Allah punya anak", "Bahwa Allah Maha Pengampun lagi Maha Penyayang", "Bahwa Allah tidur", "Bahwa kiamat sudah dekat"],
                                correct: 2,
                                explanation: "Kabarkanlah... bahwa sesungguhnya Aku-lah Yang Maha Pengampun lagi Maha Penyayang."
                            },
                            {
                                question: "Apa janji Allah bagi orang beriman dan beramal saleh (Al Maaidah: 9)?",
                                options: ["Kekayaan dunia", "Umur panjang", "Ampunan dan pahala yang besar", "Kekuasaan"],
                                correct: 3,
                                explanation: "Untuk mereka ampunan dan pahala yang besar."
                            },
                            {
                                question: "Dosa apakah yang tidak akan diampuni Allah menurut Surat An Nisaa' ayat 48?",
                                options: ["Mencuri", "Berbohong", "Syirik (mempersekutukan Allah)", "Durhaka kepada orang tua"],
                                correct: 3,
                                explanation: "Sesungguhnya Allah tidak mengampuni dosa syirik."
                            },
                            {
                                question: "Apa akibat mempersekutukan Allah (An Nisaa': 116)?",
                                options: ["Sesat sejauh-jauhnya", "Mendapat petunjuk", "Bahagia selamanya", "Menjadi kaya"],
                                correct: 1,
                                explanation: "Maka sungguh ia telah sesat sejauh-jauhnya."
                            }
                        ]
                    },
                    {
                        id: 30,
                        title: "Al Qaadir, Al Qadiir & Al Muqtadir",
                        file: "topic_30.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Kuasa (Al Qaadir/Al Qadiir/Al Muqtadir)</li>
                <li>Maha Kuasa Menciptakan & Mengganti Makhluk</li>
                <li>Maha Kuasa Menghidupkan yang Mati</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat kemahakuasaan Allah (Al Qaadir, Al Qadiir, Al Muqtadir). Tidak ada yang melemahkan Allah di langit dan di bumi. Dia berkuasa menciptakan manusia dari air, mengganti suatu kaum dengan kaum lain, menurunkan azab, hingga membangkitkan manusia kembali dari kematian.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Maha Kuasa Atas Segala Sesuatu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan kepunyaan Allah kerajaan langit dan bumi, dan Allah Maha Perkasa (Kuasa) atas segala sesuatu.</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 189</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Menciptakan Manusia dari Air</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dia (pula) yang menciptakan manusia dari air... dan adalah Tuhanmu Maha Kuasa.</p>
                    <span class="source">Surat Al Furqaan Ayat: 54</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kuasa Mengganti dengan Kaum yang Lebih Baik</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami benar-benar Maha Kuasa. Untuk mengganti (mereka) dengan kaum yang lebih baik dari mereka, dan Kami sekali-kali tidak dapat dikalahkan.</p>
                    <span class="source">Surat Al Ma'aarij Ayat: 40-41</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kuasa Mengembalikan Hidup Sesudah Mati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah benar-benar Kuasa untuk mengembalikannya (hidup sesudah mati).</p>
                    <span class="source">Surat Ath Thaariq Ayat: 8</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Meyakini sifat Al Qadiir membuat kita sadar akan kelemahan diri dan kehebatan Allah. Kita tidak boleh sombong, karena Allah berkuasa membinasakan kita dan mengganti dengan makhluk lain kapan saja Dia kehendaki.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Qadiir?",
                                options: ["Maha Mengetahui", "Maha Kuasa/Perkasa", "Maha Mendengar", "Maha Melihat"],
                                correct: 2,
                                explanation: "Al Qadiir artinya Yang Maha Kuasa atau Maha Perkasa atas segala sesuatu."
                            },
                            {
                                question: "Dari apakah Allah menciptakan manusia menurut Surat Al Furqaan ayat 54?",
                                options: ["Dari api", "Dari cahaya", "Dari air", "Dari udara"],
                                correct: 3,
                                explanation: "Dan Dia (pula) yang menciptakan manusia dari air."
                            },
                            {
                                question: "Apa bukti kekuasaan Allah dalam Surat Al Ma'aarij ayat 40-41?",
                                options: ["Menciptakan langit", "Mengganti dengan kaum yang lebih baik", "Menurunkan hujan", "Menerbitkan matahari"],
                                correct: 2,
                                explanation: "Untuk mengganti (mereka) dengan kaum yang lebih baik dari mereka."
                            },
                            {
                                question: "Menurut Surat Ath Thaariq ayat 8, Allah berkuasa untuk apa?",
                                options: ["Mengembalikan hidup sesudah mati", "Memutar waktu", "Menghancurkan gunung", "Mengeringkan laut"],
                                correct: 1,
                                explanation: "Sesungguhnya Allah benar-benar Kuasa untuk mengembalikannya (hidup sesudah mati)."
                            },
                            {
                                question: "Siapakah pemilik kerajaan langit dan bumi (Ali 'Imraan: 189)?",
                                options: ["Manusia", "Raja-raja", "Allah", "Malaikat"],
                                correct: 3,
                                explanation: "Dan kepunyaan Allah kerajaan langit dan bumi."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-6",
                title: "Pokok Bahasan 6: Sifat Allah Bagian 6",
                topics: [
                    {
                        id: 31,
                        title: "Al Qaahir, Al Qahhaar & Al Jabbaar",
                        file: "topic_31.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pemaksa (Al Qahhaar/Al Jabbaar)</li>
                <li>Semua Makhluk Tunduk dan Patuh</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Pemaksa (Al Qaahir, Al Qahhaar, Al Jabbaar). Allah memiliki kekuasaan mutlak di atas hamba-hamba-Nya. Semua makhluk di langit dan di bumi tunduk dan patuh kepada-Nya, baik dengan kemauan sendiri maupun terpaksa.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Pemaksa di Atas Hamba-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah Yang Maha Pemaksa (mempunyai kekuasaan tertinggi) di atas semua hamba-Nya.</p>
                    <span class="source">Surat Al An'aam Ayat: 61</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Azab Tuhan Sangat Keras</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya azab Tuhanmu benar-benar keras.</p>
                    <span class="source">Surat Al Buruuj Ayat: 12</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Semua Sujud dan Patuh Kepada-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hanya kepada Allah-lah sujud (patuh) segala apa yang di langit dan di bumi, baik dengan kemauan sendiri ataupun terpaksa.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 15</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sifat Al Qahhaar dan Al Jabbaar menunjukkan bahwa tidak ada yang bisa lari dari kekuasaan Allah. Kita harus tunduk dengan sukarela sebelum dipaksa tunduk pada hari kiamat.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Qahhaar?",
                                options: ["Maha Lembut", "Maha Pemaksa/Perkasa", "Maha Indah", "Maha Dekat"],
                                correct: 2,
                                explanation: "Al Qahhaar artinya Yang Maha Pemaksa atau Perkasa."
                            },
                            {
                                question: "Menurut Surat Al An'aam ayat 61, dimanakah posisi kekuasaan Allah terhadap hamba-Nya?",
                                options: ["Di bawah hamba-Nya", "Sejajar dengan hamba-Nya", "Di atas semua hamba-Nya", "Di samping hamba-Nya"],
                                correct: 3,
                                explanation: "Dan Dialah Yang Maha Pemaksa (mempunyai kekuasaan tertinggi) di atas semua hamba-Nya."
                            },
                            {
                                question: "Siapakah yang diutus Allah ketika kematian datang kepada seseorang (Al An'aam: 61)?",
                                options: ["Setan", "Jin", "Malaikat-malaikat penjaga", "Manusia lain"],
                                correct: 3,
                                explanation: "Dan diutus-Nya kepadamu malaikat-malaikat penjaga."
                            },
                            {
                                question: "Bagaimana cara makhluk di langit dan bumi sujud kepada Allah (Ar Ra'd: 15)?",
                                options: ["Hanya dengan terpaksa", "Hanya dengan kemauan sendiri", "Baik dengan kemauan sendiri ataupun terpaksa", "Tidak sujud"],
                                correct: 3,
                                explanation: "Sujud (patuh)... baik dengan kemauan sendiri ataupun terpaksa."
                            },
                            {
                                question: "Apa bantahan Allah terhadap orang kafir yang mengatakan Allah punya anak (Al Baqarah: 116)?",
                                options: ["Allah punya cucu", "Semua tunduk kepada-Nya", "Mereka benar", "Allah diam saja"],
                                correct: 2,
                                explanation: "Maha Suci Allah... semua tunduk kepada-Nya."
                            }
                        ]
                    },
                    {
                        id: 32,
                        title: "Al Kabiir & Al Mutakabbir",
                        file: "topic_32.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Besar (Al Kabiir)</li>
                <li>Kebesaran di Langit dan Bumi Hanya Milik Allah (Al Mutakabbir)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat kebesaran Allah (Al Kabiir, Al Mutakabbir). Allah Maha Besar zat-Nya dan sifat-Nya. Segala keagungan di langit dan di bumi hanyalah milik-Nya, sehingga makhluk tidak pantas untuk sombong (takabur).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Tinggi lagi Maha Besar</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya Allah Dialah Yang Maha Tinggi lagi Maha Besar.</p>
                    <span class="source">Surat Luqmaan Ayat: 30</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kebesaran Hanyalah Milik-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan bagi-Nyalah keagungan di langit dan bumi, Dialah Yang Maha Perkasa lagi Maha Bijaksana.</p>
                    <span class="source">Surat Al Jaatsiyah Ayat: 37</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Mengimani sifat Al Kabiir dan Al Mutakabbir mengajarkan kita untuk rendah hati (tawadhu'). Hanya Allah yang berhak mengenakan "selendang" kesombongan/kebesaran.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Kabiir?",
                                options: ["Maha Kecil", "Maha Besar", "Maha Lembut", "Maha Halus"],
                                correct: 2,
                                explanation: "Al Kabiir artinya Yang Maha Besar."
                            },
                            {
                                question: "Sifat apakah yang bergandengan dengan Al Kabiir dalam Surat Luqmaan ayat 30?",
                                options: ["Al 'Aliy (Maha Tinggi)", "Al Rahiim (Maha Penyayang)", "Al Ghafuur (Maha Pengampun)", "Al Sami' (Maha Mendengar)"],
                                correct: 1,
                                explanation: "Dan sesungguhnya Allah Dialah Yang Maha Tinggi lagi Maha Besar."
                            },
                            {
                                question: "Menyembah selain Allah disebut sebagai perbuatan yang... (Luqmaan: 30)?",
                                options: ["Benar", "Batil", "Bijaksana", "Baik"],
                                correct: 2,
                                explanation: "Apa yang mereka seru selain dari Allah itulah yang batil."
                            },
                            {
                                question: "Siapakah pemilik 'Kibriyaa' (Keagungan/Kebesaran) di langit dan bumi (Al Jaatsiyah: 37)?",
                                options: ["Para Malaikat", "Para Nabi", "Allah", "Raja-raja dunia"],
                                correct: 3,
                                explanation: "Dan bagi-Nyalah keagungan di langit dan bumi."
                            },
                            {
                                question: "Sikap apa yang harus kita hindari jika mengingat sifat Al Mutakabbir Allah?",
                                options: ["Sombong", "Jujur", "Sabar", "Dermawan"],
                                correct: 1,
                                explanation: "Sifat Al Mutakabbir (Maha Memiliki Kebesaran) mengajarkan kita untuk tidak sombong."
                            }
                        ]
                    },
                    {
                        id: 33,
                        title: "Al 'Aziiz",
                        file: "topic_33.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Perkasa (Al 'Aziiz)</li>
                <li>Seluruh Keperkasaan dan Kemuliaan Hanya Milik Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Perkasa (Al 'Aziiz). Tidak ada yang bisa mengalahkan-Nya. Dia memberikan kemuliaan kepada siapa yang Dia kehendaki dan menghinakan siapa yang Dia kehendaki. Mencari kekuatan selain kepada Allah adalah kesia-siaan.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Perkasa lagi Maha Bijaksana</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah Yang Maha Perkasa lagi Maha Bijaksana.</p>
                    <span class="source">Surat Faathir Ayat: 2</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kekuatan Seluruhnya Milik Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya kekuasaan (kemuliaan/kekuatan) itu seluruhnya milik Allah.</p>
                    <span class="source">Surat Yuunus Ayat: 65</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Jangan Mencari Kekuatan pada Orang Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Apakah mereka mencari kekuatan di sisi orang kafir itu? Maka sesungguhnya semua kekuatan kepunyaan Allah.</p>
                    <span class="source">Surat An Nisaa' Ayat: 139</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Al 'Aziiz mengajarkan kita untuk hanya bergantung dan memohon kekuatan kepada Allah. Bersandar pada makhluk atau orang kafir tidak akan memberikan kemuliaan yang hakiki.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al 'Aziiz?",
                                options: ["Maha Kaya", "Maha Perkasa/Mulia", "Maha Pengasih", "Maha Adil"],
                                correct: 2,
                                explanation: "Al 'Aziiz artinya Yang Maha Perkasa."
                            },
                            {
                                question: "Apa yang terjadi jika Allah menahan rahmat-Nya (Faathir: 2)?",
                                options: ["Ada yang bisa melepaskannya", "Tidak ada seorangpun yang sanggup melepaskannya", "Manusia bisa membukanya", "Malaikat akan menolong"],
                                correct: 2,
                                explanation: "Dan apa saja yang ditahan oleh Allah maka tidak seorangpun yang sanggup melepaskannya."
                            },
                            {
                                question: "Kepada siapakah seluruh kekuatan/kemuliaan itu milik (Yuunus: 65)?",
                                options: ["Para Raja", "Orang kaya", "Allah", "Presiden"],
                                correct: 3,
                                explanation: "Sesungguhnya kekuasaan itu seluruhnya milik Allah."
                            },
                            {
                                question: "Siapakah yang dikecam dalam Surat An Nisaa' ayat 139?",
                                options: ["Orang yang shalat", "Orang yang menjadikan orang kafir sebagai penolong/sumber kekuatan", "Orang yang puasa", "Orang yang bersedekah"],
                                correct: 2,
                                explanation: "Orang-orang yang mengambil orang-orang kafir menjadi teman-teman penolong."
                            },
                            {
                                question: "Sifat Al 'Aziiz sering digandengan dengan sifat apa dalam Al Quran (misal Faathir: 2)?",
                                options: ["Al Hakiim (Maha Bijaksana)", "Al Razzaaq (Maha Pemberi Rezeki)", "Al Khaliq (Maha Pencipta)", "Al Baari' (Maha Mengadakan)"],
                                correct: 1,
                                explanation: "Dan Dialah Yang Maha Perkasa (Al 'Aziiz) lagi Maha Bijaksana (Al Hakiim)."
                            }
                        ]
                    },
                    {
                        id: 34,
                        title: "Al Qawiyy & Al Matiin",
                        file: "topic_34.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Kuat (Al Qawiyy)</li>
                <li>Allah Maha Kokoh (Al Matiin)</li>
                <li>Seluruh Kekuatan Hanya Milik Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas kekuatan dan kekokohan Allah (Al Qawiyy, Al Matiin). Kekuatan Allah tidak tertandingi, dan azab-Nya sangat pedih bagi mereka yang ingkar. Sebaliknya, Allah menyelamatkan orang-orang beriman dengan rahmat-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Kuat lagi Maha Perkasa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Tuhanmu Dia-lah Yang Maha Kuat lagi Maha Perkasa.</p>
                    <span class="source">Surat Huud Ayat: 66</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kekuatan Itu Kepunyaan Allah Semuanya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Bahwa kekuatan itu kepunyaan Allah semuanya, dan bahwa Allah amat berat siksaan-Nya.</p>
                    <span class="source">Surat Al Baqarah Ayat: 165</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Kuat lagi Maha Perkasa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah benar-benar Maha Kuat lagi Maha Perkasa.</p>
                    <span class="source">Surat Al Hajj Ayat: 74</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Mengetahui sifat Al Qawiyy dan Al Matiin membuat kita sadar bahwa kekuatan manusia itu lemah dan terbatas. Kita hanya bisa berlindung kepada Allah Yang Maha Kuat.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Qawiyy?",
                                options: ["Maha Lembut", "Maha Kuat", "Maha Indah", "Maha Melihat"],
                                correct: 2,
                                explanation: "Al Qawiyy artinya Yang Maha Kuat."
                            },
                            {
                                question: "Sifat apakah yang sering digandengkan dengan Al Qawiyy (misal Huud: 66)?",
                                options: ["Al 'Aziiz (Maha Perkasa)", "Al Rahiim (Maha Penyayang)", "Al Kariim (Maha Pemurah)", "Al Haliim (Maha Penyantun)"],
                                correct: 1,
                                explanation: "Sesungguhnya Tuhanmu Dia-lah Yang Maha Kuat (Al Qawiyy) lagi Maha Perkasa (Al 'Aziiz)."
                            },
                            {
                                question: "Apa persaksian Allah tentang kekuatan dalam Surat Al Baqarah ayat 165?",
                                options: ["Kekuatan dibagi-bagi", "Kekuatan milik raja", "Kekuatan itu kepunyaan Allah semuanya", "Kekuatan milik tentara"],
                                correct: 3,
                                explanation: "Bahwa kekuatan itu kepunyaan Allah semuanya."
                            },
                            {
                                question: "Bagaimanakah sifat azab Allah menurut Al Baqarah ayat 165?",
                                options: ["Amat ringan", "Amat berat/pedih", "biasa saja", "Tidak ada azab"],
                                correct: 2,
                                explanation: "Dan bahwa Allah amat berat siksaan-Nya."
                            },
                            {
                                question: "Apa ketetapan Allah dalam Surat Al Mujaadilah ayat 21?",
                                options: ["Aku dan rasul-rasul-Ku pasti menang", "Manusia pasti menang", "Jin pasti menang", "Tidak ada yang menang"],
                                correct: 1,
                                explanation: "Allah telah menetapkan: 'Aku dan rasul-rasul-Ku pasti menang'."
                            }
                        ]
                    },
                    {
                        id: 35,
                        title: "Al Raqiib, Al Muhaimin & Al Haafizh",
                        file: "topic_35.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Mengawasi (Al Raqiib/Al Muhaimin)</li>
                <li>Allah Maha Menjaga (Al Haafizh)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah yang senantiasa mengawasi dan menjaga hamba-Nya. Tidak ada satu pun yang luput dari pengawasan Allah (Al Raqiib, Al Muhaimin). Dia juga sebaik-baik penjaga (Al Haafizh) yang memelihara segala sesuatu.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Mengawasi Hamba-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah selalu menjaga dan mengawasi kamu.</p>
                    <span class="source">Surat An Nisaa' Ayat: 1</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Mengawasi Segala Sesuatu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan adalah Allah Maha Mengawasi segala sesuatu.</p>
                    <span class="source">Surat Al Ahzaab Ayat: 52</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Menjaga (Al Haafizh)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka Allah adalah sebaik-baik Penjaga dan Dia adalah Maha Penyayang diantara para penyayang.</p>
                    <span class="source">Surat Yuusuf Ayat: 64</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Merasa diawasi oleh Allah (Muraqabah) akan membuat kita takut berbuat dosa di saat sendiri maupun ramai. Kita juga harus yakin bahwa penjagaan Allah adalah yang paling sempurna.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Raqiib?",
                                options: ["Maha Memberi", "Maha Mengawasi", "Maha Mencipta", "Maha Mematikan"],
                                correct: 2,
                                explanation: "Al Raqiib artinya Yang Maha Mengawasi."
                            },
                            {
                                question: "Dalam Surat Al Maaidah ayat 117, apa yang dikatakan Nabi Isa tentang pengawasan Allah?",
                                options: ["Engkau-lah yang mengawasi mereka", "Aku mengawasi mereka selamanya", "Malaikat tidak tahu", "Mereka bebas"],
                                correct: 1,
                                explanation: "Maka setelah Engkau wafatkan aku, Engkau-lah yang mengawasi mereka."
                            },
                            {
                                question: "Surat Ar Rahmaan ayat 33 menantang jin dan manusia untuk...?",
                                options: ["Terbang ke bulan", "Menembus penjuru langit dan bumi", "Menghitung bintang", "Menciptakan lalat"],
                                correct: 2,
                                explanation: "Jika kamu sanggup menembus (melintasi) penjuru langit dan bumi, maka tembuslah."
                            },
                            {
                                question: "Siapakah sebaik-baik penjaga menurut Surat Yuusuf ayat 64?",
                                options: ["Polisi", "Orang tua", "Allah", "Teman"],
                                correct: 3,
                                explanation: "Maka Allah adalah sebaik-baik Penjaga."
                            },
                            {
                                question: "Apa maksud Allah Maha Muhaimin?",
                                options: ["Maha Memelihara/Mengawasi", "Maha Kaya", "Maha Dekat", "Maha Melihat"],
                                correct: 1,
                                explanation: "Al Muhaimin artinya Yang Maha Memelihara atau Mengawasi."
                            }
                        ]
                    },
                    {
                        id: 36,
                        title: "Al Syaahid & Al Syahiid",
                        file: "topic_36.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Menyaksikan (Al Syaahid/Al Syahiid)</li>
                <li>Cukuplah Allah Sebagai Saksi</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Menyaksikan (Al Syaahid, Al Syahiid). Allah menyaksikan segala sesuatu, tidak ada yang tersembunyi bagi-Nya. Allah cukup menjadi saksi atas kebenaran Rasul-Nya dan amal perbuatan hamba-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Menjadi Saksi atas Segala Sesuatu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tidakkah cukup bahwa sesungguhnya Tuhanmu menjadi saksi atas segala sesuatu?</p>
                    <span class="source">Surat Fushshilat Ayat: 53</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Saksi Antara Hamba-Nya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: Cukuplah Allah menjadi saksi antaraku dan antaramu.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 43</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Mengetahui dan Menyaksikan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah Maha Menyaksikan segala sesuatu.</p>
                    <span class="source">Surat An Nisaa' Ayat: 33</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sifat Al Syahiid mengingatkan kita bahwa setiap perbuatan, baik tersembunyi maupun terang-terangan, disaksikan oleh Allah. Kelak di hari kiamat, Allah akan menjadi saksi atas semua amal kita.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Syahiid?",
                                options: ["Maha Melihat", "Maha Menyaksikan", "Maha Mendengar", "Maha Mengetahui"],
                                correct: 2,
                                explanation: "Al Syahiid artinya Yang Maha Menyaksikan."
                            },
                            {
                                question: "Dalam Surat Fushshilat ayat 53, Allah menjadi saksi atas...?",
                                options: ["Sebagian sesuatu", "Segala sesuatu", "Langit saja", "Bumi saja"],
                                correct: 2,
                                explanation: "Tidakkah cukup bahwa sesungguhnya Tuhanmu menjadi saksi atas segala sesuatu?"
                            },
                            {
                                question: "Siapakah yang memberi keputusan di antara golongan-golongan (Yahudi, Nasrani, dll) pada hari kiamat (Al Hajj: 17)?",
                                options: ["Nabi", "Malaikat", "Allah", "Manusia sendiri"],
                                correct: 3,
                                explanation: "Allah akan memberi keputusan di antara mereka pada hari kiamat."
                            },
                            {
                                question: "Apa bunyi persaksian dalam Surat Ar Ra'd ayat 43?",
                                options: ["Cukuplah Allah menjadi saksi antaraku dan antaramu", "Aku tidak bersaksi", "Saksikanlah sendiri", "Malaikat menjadi saksi"],
                                correct: 1,
                                explanation: "Katakanlah: Cukuplah Allah menjadi saksi antaraku dan antaramu."
                            },
                            {
                                question: "Apa yang ditekankan dalam sifat Al Syaahid?",
                                options: ["Allah tidak melihat", "Allah hadir dan menyaksikan segala hal", "Allah jauh", "Allah tidak peduli"],
                                correct: 2,
                                explanation: "Sifat Al Syaahid menekankan bahwa Allah hadir dan menyaksikan segala sesuatu."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-7",
                title: "Pokok Bahasan 7: Sifat Allah Bagian 7",
                topics: [
                    {
                        id: 37,
                        title: "Al Samii', Al Bashiir, Al 'Aliim & 'Allaam al Ghuyuub",
                        file: "topic_37.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Mendengar dan Maha Melihat (Al Samii', Al Bashiir)</li>
                <li>Allah Maha Mengetahui (Al 'Aliim)</li>
                <li>Allah Maha Mengetahui Segala yang Ghaib ('Allaam al Ghuyuub)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas kemahatahuan Allah yang meliputi pendengaran, penglihatan, dan ilmu-Nya yang tak terbatas. Allah mendengar segala suara, melihat segala gerak-gerik, dan mengetahui segala sesuatu yang nyata maupun yang ghaib, termasuk isi hati manusia.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Mendengar lagi Maha Mengetahui</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan bertawakkallah kepada Yang Maha Perkasa lagi Maha Penyayang... Sesungguhnya Dialah Yang Maha Mendengar lagi Maha Mengetahui.</p>
                    <span class="source">Surat Asy Syu’araa’ Ayat: 217-220</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Mengetahui yang Ghaib dan yang Nyata</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Yang mengetahui semua yang ghaib dan yang nyata; Yang Maha Besar lagi Maha Tinggi.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 9</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Mengetahui Segala Isi Hati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Allah Maha Mengetahui segala isi hati.</p>
                    <span class="source">Surat Luqmaan Ayat: 23</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Meyakini sifat-sifat ini (Al Samii', Al Bashiir, Al 'Aliim) akan melahirkan sikap waspada (muraqabah) dan kejujuran. Kita tidak akan berani berbuat dosa, karena Allah selalu mendengar, melihat, dan mengetahui apa pun yang kita lakukan atau sembunyikan.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Samii' dan Al Bashiir?",
                                options: ["Maha Kaya dan Maha Kuat", "Maha Mendengar dan Maha Melihat", "Maha Mengetahui dan Maha Bijaksana", "Maha Pengasih dan Maha Penyayang"],
                                correct: 2,
                                explanation: "Al Samii' artinya Maha Mendengar, Al Bashiir artinya Maha Melihat."
                            },
                            {
                                question: "Menurut Surat Asy Syu’araa’ ayat 218-219, Allah melihat kita ketika...?",
                                options: ["Tidur saja", "Makan saja", "Berdiri (shalat) dan perubahan gerak badan", "Bermain saja"],
                                correct: 3,
                                explanation: "Yang melihat kamu ketika kamu berdiri (untuk shalat), Dan (melihat pula) perubahan gerak badanmu."
                            },
                            {
                                question: "Apa arti 'Allaam al Ghuyuub?",
                                options: ["Maha Mengetahui yang Nyata", "Maha Mengetahui segala yang Ghaib", "Maha Perkasa", "Maha Adil"],
                                correct: 2,
                                explanation: "'Allaam al Ghuyuub artinya Maha Mengetahui segala yang ghaib."
                            },
                            {
                                question: "Apakah ada sesuatu yang tersembunyi bagi Allah di langit dan bumi (Ali 'Imraan: 5)?",
                                options: ["Ada sedikit", "Tidak ada sesuatupun", "Hanya yang di laut", "Hanya yang di goa"],
                                correct: 2,
                                explanation: "Sesungguhnya bagi Allah tidak ada sesuatupun yang tersembunyi di bumi dan tidak (pula) di langit."
                            },
                            {
                                question: "Menurut Surat Al Mulk ayat 13, Allah mengetahui...",
                                options: ["Segala isi hati", "Hanya ucapan keras", "Hanya perbuatan siang", "Mimpi saja"],
                                correct: 1,
                                explanation: "Sesungguhnya Dia Maha Mengetahui segala isi hati."
                            }
                        ]
                    },
                    {
                        id: 38,
                        title: "Al Khabiir",
                        file: "topic_38.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Mengenal/Waspada (Al Khabiir)</li>
                <li>Allah Maha Mengetahui Dosa Hamba-Nya</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Mengetahui perkara yang tersembunyi (Al Khabiir). Pengetahuan Allah sangat detail dan mendalam, meliputi segala rahasia yang paling halus sekalipun. Tidak ada dosa atau amal yang luput dari pengetahuan-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Halus lagi Maha Mengetahui</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Apakah (Allah) yang menciptakan itu tidak tahu (yang kamu lahirkan dan rahasiakan); dan Dia Maha Halus lagi Maha Mengetahui?</p>
                    <span class="source">Surat Al Mulk Ayat: 14</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Cukuplah Tuhanmu Maha Mengetahui Dosa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan cukuplah Tuhanmu Maha Mengetahui lagi Maha Melihat dosa hamba-hamba-Nya.</p>
                    <span class="source">Surat Al Israa' Ayat: 17</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Al Khabiir mengajarkan kita bahwa Allah mengetahui sedetail-detailnya urusan kita. Tidak ada gunanya menyembunyikan kejahatan, karena Allah Maha Waspada terhadap segala gerak-gerik hamba-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Khabiir?",
                                options: ["Maha Besar", "Maha Mengenal/Waspada (Mengetahui yang tersembunyi)", "Maha Pencipta", "Maha Pemberi"],
                                correct: 2,
                                explanation: "Al Khabiir artinya Yang Maha Mengenal atau Waspada (Mengetahui perkara yang tersembunyi/halus)."
                            },
                            {
                                question: "Dalam Surat Al Mulk ayat 14, sifat Al Khabiir digandengkan dengan sifat...?",
                                options: ["Al Lathiif (Maha Halus)", "Al Kariim (Maha Mulia)", "Al Aziiz (Maha Perkasa)", "Al Ghaffaar (Maha Pengampun)"],
                                correct: 1,
                                explanation: "Dan Dia Maha Halus (Al Lathiif) lagi Maha Mengetahui (Al Khabiir)."
                            },
                            {
                                question: "Apa yang diketahui Allah tentang dosa hamba-Nya dalam Surat Al Israa' ayat 17?",
                                options: ["Allah tidak peduli", "Allah lupa", "Allah Maha Mengetahui lagi Maha Melihat", "Malaikat yang catat saja"],
                                correct: 3,
                                explanation: "Dan cukuplah Tuhanmu Maha Mengetahui lagi Maha Melihat dosa hamba-hamba-Nya."
                            },
                            {
                                question: "Apakah pencipta (Allah) mengetahui ciptaan-Nya (Al Mulk: 14)?",
                                options: ["Tidak tahu", "Ragu-ragu", "Tentu tahu", "Mungkin tahu"],
                                correct: 3,
                                explanation: "Apakah (Allah) yang menciptakan itu tidak tahu...?"
                            },
                            {
                                question: "Sifat Al Khabiir menekankan pada pengetahuan Allah yang bersifat...?",
                                options: ["Umum saja", "Detail dan mendalam (rahasia)", "Hanya lahiriah", "Masa lalu saja"],
                                correct: 2,
                                explanation: "Al Khabiir menekankan pengetahuan yang detail, mendalam, dan meliputi hal-hal yang tersembunyi."
                            }
                        ]
                    },
                    {
                        id: 39,
                        title: "Al Muhiith",
                        file: "topic_39.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Meliputi (Al Muhiith)</li>
                <li>Ilmu Allah Meliputi Segala Sesuatu</li>
                <li>Allah Mengepung Orang Kafir</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Meliputi (Al Muhiith). Kekuasaan dan ilmu Allah mengepung segala sesuatu. Tidak ada jalan keluar bagi orang kafir untuk lari dari azab Allah, karena Dia meliputi mereka dari segala penjuru.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Maha Meliputi Segala Sesuatu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Ingatlah bahwasanya Dia Maha Meliputi segala sesuatu.</p>
                    <span class="source">Surat Fushshilat Ayat: 54</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Mengepung Orang Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Padahal Allah mengepung mereka dari belakang mereka.</p>
                    <span class="source">Surat Al Buruuj Ayat: 20</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sifat Al Muhiith menyadarkan kita bahwa kita benar-benar dalam genggaman kekuasaan Allah. Tidak ada tempat lari dari-Nya kecuali kembali kepada-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Muhiith?",
                                options: ["Maha Kecil", "Maha Meliputi/Mengepung", "Maha Jauh", "Maha Lemah"],
                                correct: 2,
                                explanation: "Al Muhiith artinya Yang Maha Meliputi atau Mengepung."
                            },
                            {
                                question: "Apa peringatan Allah dalam Surat Fushshilat ayat 54?",
                                options: ["Allah tidur", "Allah Maha Meliputi segala sesuatu", "Allah tidak melihat", "Manusia bebas"],
                                correct: 2,
                                explanation: "Ingatlah bahwasanya Dia Maha Meliputi segala sesuatu."
                            },
                            {
                                question: "Bagaimana posisi Allah terhadap orang-orang kafir yang mendustakan (Al Buruuj: 20)?",
                                options: ["Mengepung mereka dari belakang", "Membiarkan mereka lari", "Takut kepada mereka", "Mengabaikan mereka"],
                                correct: 1,
                                explanation: "Padahal Allah mengepung mereka dari belakang mereka."
                            },
                            {
                                question: "Berita tentang kaum apa yang disebut penentang dalam Surat Al Buruuj?",
                                options: ["'Aad dan Tsamud", "Fir'aun dan Tsamud", "Nuh dan Lut", "Ibrahim dan Ismail"],
                                correct: 2,
                                explanation: "(Yaitu kaum) Fir'aun dan (kaum) Tsamud."
                            },
                            {
                                question: "Apa implikasi dari sifat Al Muhiith bagi manusia?",
                                options: ["Bisa sembunyi dari Allah", "Bisa lari dari Allah", "Tidak ada tempat lari dari kekuasaan Allah", "Allah tidak tahu keberadaan kita"],
                                correct: 3,
                                explanation: "Maksudnya: mereka tidak dapat lolos dari kekuasaan Allah (karena Dia meliputi segala sesuatu)."
                            }
                        ]
                    },
                    {
                        id: 40,
                        title: "Al Hakam, Al Fattaah & Al Hakiim",
                        file: "topic_40.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pemberi Keputusan (Al Hakam/Al Fattaah)</li>
                <li>Hukum Hanya Milik Allah</li>
                <li>Allah Maha Bijaksana (Al Hakiim)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah sebagai Pemutus Perkara (Al Hakam, Al Fattaah) dan Maha Bijaksana (Al Hakiim). Segala hukum dan keputusan mutlak milik Allah. Dia memberi keputusan dengan adil dan bijaksana, serta membuka pintu rahmat bagi hamba-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Sebaik-baik Pemberi Keputusan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Menetapkan hukum itu hanyalah hak Allah. Dia menerangkan yang sebenarnya dan Dia sebaik-baik pemberi keputusan.</p>
                    <span class="source">Surat Al An’aam Ayat: 57</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Pemberi Keputusan (Al Fattaah)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah Maha Pemberi keputusan lagi Maha Mengetahui.</p>
                    <span class="source">Surat Saba' Ayat: 26</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Perkasa lagi Maha Bijaksana</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah Allah Yang Maha Perkasa lagi Maha Bijaksana.</p>
                    <span class="source">Surat Saba' Ayat: 27</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kita harus menerima segala keputusan dan hukum Allah dengan lapang dada. Sifat Al Hakiim mengajarkan kita bahwa di balik setiap takdir dan syariat-Nya, pasti ada hikmah yang besar.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Hakam?",
                                options: ["Maha Bijaksana", "Maha Pemberi Keputusan/Hakim", "Maha Perkasa", "Maha Kaya"],
                                correct: 2,
                                explanation: "Al Hakam artinya Yang Maha Pemberi Keputusan atau Hakim."
                            },
                            {
                                question: "Dalam Surat Al An'aam ayat 57, siapakah yang berhak menetapkan hukum?",
                                options: ["Manusia", "Raja", "Allah", "Malaikat"],
                                correct: 3,
                                explanation: "Menetapkan hukum itu hanyalah hak Allah."
                            },
                            {
                                question: "Apa arti dari Al Fattaah dalam konteks Surat Saba' ayat 26?",
                                options: ["Maha Pembuka/Pemberi Keputusan", "Maha Penutup", "Maha Pencipta", "Maha Pemelihara"],
                                correct: 1,
                                explanation: "Al Fattaah artinya Maha Pemberi Keputusan (juga berarti Maha Pembuka)."
                            },
                            {
                                question: "Apa yang ditekankan dalam Surat Al Baqarah ayat 209 tentang sifat Allah?",
                                options: ["Allah Maha Perkasa lagi Maha Bijaksana", "Allah Maha Pengampun", "Allah Maha Keras Azabnya", "Allah Maha Lembut"],
                                correct: 1,
                                explanation: "Ketahuilah, bahwasanya Allah Maha Perkasa lagi Maha Bijaksana."
                            },
                            {
                                question: "Siapakah yang dianugerahi Al Hikmah menurut Surat Al Baqarah ayat 269?",
                                options: ["Semua orang", "Orang kaya", "Siapa yang dikehendaki-Nya", "Hanya Nabi"],
                                correct: 3,
                                explanation: "Allah menganugerahkan Alhikmah kepada siapa yang dikehendaki-Nya."
                            }
                        ]
                    },
                    {
                        id: 41,
                        title: "Al Muhshiy & Al Hasiib",
                        file: "topic_41.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Menghitung (Al Muhshiy)</li>
                <li>Allah Maha Pembuat Perhitungan (Al Hasiib)</li>
                <li>Allah Maha Cepat Perhitungannya</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah Yang Maha Menghitung dan Membuat Perhitungan (Al Muhshiy, Al Hasiib). Allah menghitung segala amal perbuatan hamba-Nya dengan sangat teliti, tidak ada yang terlewat. Perhitungan-Nya sangat cepat dan adil.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Menghitung dengan Teliti</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sungguh Allah telah menentukan jumlah mereka dan menghitung mereka dengan hitungan yang teliti.</p>
                    <span class="source">Surat Maryam Ayat: 94</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Pembuat Perhitungan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan cukuplah Allah sebagai Pembuat Perhitungan.</p>
                    <span class="source">Surat An Nisaa' Ayat: 6</span>
                </div>
            </div>

             <div class="content-section">
                <h3>Allah Maha Cepat Perhitungannya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Dialah Pembuat perhitungan yang paling cepat.</p>
                    <span class="source">Surat Al An'aam Ayat: 62</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kesadaran akan sifat Al Hasiib membuat kita selalu introspeksi diri (muhasabah). Kita harus mempersiapkan bekal amal baik sebelum datang hari perhitungan (Yaumul Hisab) yang sangat cepat dan teliti.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Muhshiy?",
                                options: ["Maha Menghidupkan", "Maha Menghitung (dengan teliti)", "Maha Mematikan", "Maha Mencipta"],
                                correct: 2,
                                explanation: "Al Muhshiy artinya Yang Maha Menghitung."
                            },
                            {
                                question: "Menurut Surat Maryam ayat 93-94, bagaimana kedatangan makhluk kepada Allah?",
                                options: ["Sebagai raja", "Sebagai teman", "Selaku seorang hamba", "Sebagai musuh"],
                                correct: 3,
                                explanation: "Kecuali akan datang kepada Tuhan Yang Maha Pemurah selaku seorang hamba."
                            },
                            {
                                question: "Apa konsekuensi menyembunyikan atau melahirkan isi hati (Al Baqarah: 284)?",
                                options: ["Allah tidak tahu", "Allah membuat perhitungan denganmu", "Allah membiarkan", "Malaikat lupa"],
                                correct: 2,
                                explanation: "Niscaya Allah membuat perhitungan denganmu tentang perbuatanmu itu."
                            },
                            {
                                question: "Bagaimana sifat hisab Allah terhadap kaum yang mendurhakai (Ath Thalaaq: 8)?",
                                options: ["Hisab yang mudah", "Hisab yang ringan", "Hisab yang keras (syadiid)", "Tidak dihisab"],
                                correct: 3,
                                explanation: "Maka Kami hisab mereka dengan hisab keras."
                            },
                            {
                                question: "Apa arti Sarii' al Hisaab (Al An'aam: 62)?",
                                options: ["Lambat perhitungannya", "Cepat perhitungannya", "Batal perhitungannya", "Salah perhitungannya"],
                                correct: 2,
                                explanation: "Sarii' al Hisaab artinya Pembuat perhitungan yang paling cepat."
                            }
                        ]
                    },
                    {
                        id: 42,
                        title: "Al Muntaqim, Al Baa'its & Al Jaami'",
                        file: "topic_42.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Allah Maha Pemberi Balasan (Al Muntaqim)</li>
                <li>Allah Maha Membangkitkan (Al Baa'its)</li>
                <li>Allah Maha Mengumpulkan (Al Jaami')</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas sifat Allah sebagai Pemberi Balasan (Al Muntaqim) bagi orang yang berdosa. Namun, Allah juga Maha Membangkitkan (Al Baa'its) manusia dari kubur dan Maha Mengumpulkan (Al Jaami') seluruh makhluk di Padang Mahsyar untuk diadili.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Allah Membalas Orang Berdosa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami akan membalas orang-orang yang berdosa.</p>
                    <span class="source">Surat As Sajdah Ayat: 22</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Membangkitkan yang di Dalam Kubur</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan bahwasanya Allah membangkitkan semua orang yang di dalam kubur.</p>
                    <span class="source">Surat Al Hajj Ayat: 7</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Allah Maha Mengumpulkan Manusia</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Ya Tuhan Kami, sesungguhnya Engkau mengumpulkan manusia untuk (menerima balasan pada) hari yang tak ada keraguan padanya.</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 9</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Mengingat sifat Al Baa'its dan Al Jaami' memperkuat iman kita kepada Hari Akhir. Kita sadar bahwa kematian bukanlah akhir, melainkan awal dari kehidupan abadi di mana setiap jiwa akan dikumpulkan dan dibalas sesuai amalnya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa arti dari Al Muntaqim?",
                                options: ["Maha Penyayang", "Maha Pemberi Balasan (Siksaan)", "Maha Pemberi Rezeki", "Maha Pengampun"],
                                correct: 2,
                                explanation: "Al Muntaqim artinya Yang Maha Memberi Balasan (khususnya balasan siksa bagi yang berdosa)."
                            },
                            {
                                question: "Siapakah yang diancam balasan dalam Surat As Sajdah ayat 22?",
                                options: ["Orang beriman", "Orang yang bersedekah", "Orang-orang yang berdosa (Mujrimin)", "Orang yang shalat"],
                                correct: 3,
                                explanation: "Sesungguhnya Kami akan membalas orang-orang yang berdosa."
                            },
                            {
                                question: "Apa arti dari Al Baa'its?",
                                options: ["Maha Mematikan", "Maha Membangkitkan", "Maha Mengumpulkan", "Maha Menjaga"],
                                correct: 2,
                                explanation: "Al Baa'its artinya Yang Maha Membangkitkan (dari kematian/kubur)."
                            },
                            {
                                question: "Apa arti dari Al Jaami'?",
                                options: ["Maha Mengumpulkan", "Maha Memisahkan", "Maha Menghancurkan", "Maha Menciptakan"],
                                correct: 1,
                                explanation: "Al Jaami' artinya Yang Maha Mengumpulkan."
                            },
                            {
                                question: "Di mana Allah akan mengumpulkan manusia (Ali 'Imraan: 9)?",
                                options: ["Di dunia", "Di pasar", "Pada hari yang tak ada keraguan padanya (Kiamat)", "Di laut"],
                                correct: 3,
                                explanation: "Mengumpulkan manusia untuk (menerima balasan pada) hari yang tak ada keraguan padanya."
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        id: "theme-2",
        title: "Tema 2: Golongan Manusia",
        subjects: [
            {
                id: "subject-1",
                title: "Golongan Beriman",
                topics: [
                    {
                        id: 43,
                        title: "Perintah, Pemeliharaan, dan Perumpamaan Iman",
                        file: "topic_43.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Perintah Iman</li>
                <li>Pemeliharaan Iman</li>
                <li>Perumpamaan Iman</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas perintah Allah untuk beriman kepada-Nya, Rasul-Nya, dan Alquran. Juga dibahas bagaimana memelihara iman agar tidak tergerus, serta perumpamaan iman yang kokoh seperti pohon yang baik atau air yang memberi manfaat.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Perintah Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka berimanlah kamu kepada Allah dan Rasul-Nya dan kepada cahaya (Alquran) yang telah Kami turunkan.</p>
                    <span class="source">Surat At Taghaabun Ayat: 8</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tetaplah Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Wahai orang-orang yang beriman, tetaplah beriman kepada Allah dan Rasul-Nya.</p>
                    <span class="source">Surat An Nisaa' Ayat: 136</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Perumpamaan yang Benar dan Bathil</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Demikian Allah membuat perumpamaan yang benar dan yang bathil.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 17</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Iman adalah fondasi kehidupan seorang muslim. Kita diperintahkan untuk terus memperbaharui dan menjaga keimanan kita agar selamat di dunia dan akhirat.</p>
                        `,
                        quiz: [
                            {
                                question: "Kepada siapa kita diperintahkan beriman dalam Surat At Taghaabun ayat 8?",
                                options: ["Kepada Harta", "Kepada Allah, Rasul-Nya, dan Cahaya (Alquran)", "Kepada Raja", "Kepada Nenek Moyang"],
                                correct: 2,
                                explanation: "Maka berimanlah kamu kepada Allah dan Rasul-Nya dan kepada cahaya (Alquran) yang telah Kami turunkan."
                            },
                            {
                                question: "Apa seruan kepada orang yang beriman dalam Surat An Nisaa' ayat 136?",
                                options: ["Tetaplah beriman", "Berhentilah beriman", "Ragu-ragulah", "Kufurlah"],
                                correct: 1,
                                explanation: "Wahai orang-orang yang beriman, tetaplah beriman kepada Allah dan Rasul-Nya."
                            },
                            {
                                question: "Siapa yang sesat sejauh-jauhnya menurut An Nisaa' ayat 136?",
                                options: ["Orang miskin", "Orang bodoh", "Siapa yang kafir kepada Allah, malaikat, kitab, rasul, dan hari akhir", "Orang sakit"],
                                correct: 3,
                                explanation: "Siapa yang kafir kepada Allah... maka sungguh ia telah sesat sejauh-jauhnya."
                            },
                            {
                                question: "Bagaimana reaksi orang beriman ketika diturunkan suatu surat (At Taubah: 124)?",
                                options: ["Bertambah kekafirannya", "Bertambah imannya dan gembira", "Marah", "Sedih"],
                                correct: 2,
                                explanation: "Adapun orang-orang beriman, maka surat ini menambah imannya, dan mereka gembira."
                            },
                            {
                                question: "Apa perumpamaan 'buih' dalam Surat Ar Ra'd ayat 17?",
                                options: ["Sesuatu yang bermanfaat", "Sesuatu yang abadi", "Sesuatu yang akan hilang dan tak berharga", "Sesuatu yang kuat"],
                                correct: 3,
                                explanation: "Adapun buih itu, akan hilang sebagai sesuatu yang tak ada harganya."
                            }
                        ]
                    },
                    {
                        id: 44,
                        title: "Sifat & Keutamaan Orang Mukmin",
                        file: "topic_44.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Sifat Orang Mukmin</li>
                <li>Keutamaan Orang Mukmin</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan sifat-sifat mulia orang mukmin seperti khusyu' dalam shalat, menjauhi hal yang tidak berguna, menunaikan zakat, dan menjaga kehormatan. Juga dibahas keutamaan dan derajat tinggi yang Allah janjikan bagi mereka.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Keberuntungan Orang Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya beruntunglah orang-orang yang beriman.</p>
                    <span class="source">Surat Al Mu’minuun Ayat: 1</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Ciri Hati Orang Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya orang-orang yang beriman ialah mereka yang bila disebut nama Allah gemetarlah hati mereka.</p>
                    <span class="source">Surat Al Anfaal Ayat: 2</span>
                </div>
            </div>

             <div class="content-section">
                <h3>Kedudukan di Sisi Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">(Kedudukan) mereka itu bertingkat-tingkat di sisi Allah.</p>
                    <span class="source">Surat Ali 'Imran Ayat: 163</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Menjadi mukmin sejati memerlukan perjuangan untuk menghiasi diri dengan akhlak dan sifat terpuji. Janji Allah berupa surga Firdaus adalah motivasi terbesar bagi orang beriman.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa sifat pertama orang mukmin yang disebut dalam Al Mu'minuun ayat 2?",
                                options: ["Menunaikan zakat", "Khusyu' dalam shalatnya", "Menjaga kemaluan", "Berpuasa"],
                                correct: 2,
                                explanation: "(Yaitu) orang-orang yang khusyu' dalam shalatnya."
                            },
                            {
                                question: "Apa yang dilakukan orang mukmin terhadap hal yang tiada berguna (Al Mu'minuun: 3)?",
                                options: ["Mengerjakannya", "Menyukainya", "Menjauhkan diri darinya", "Mempromosikannya"],
                                correct: 3,
                                explanation: "Dan orang-orang yang menjauhkan diri dari yang tiada berguna."
                            },
                            {
                                question: "Surga apa yang akan diwarisi oleh orang mukmin (Al Mu'minuun: 11)?",
                                options: ["Surga 'Adn", "Surga Firdaus", "Surga Na'im", "Surga Ma'wa"],
                                correct: 2,
                                explanation: "(Yakni) yang mewarisi surga Firdaus."
                            },
                            {
                                question: "Bagaimana hati orang beriman bila disebut nama Allah (Al Anfaal: 2)?",
                                options: ["Biasa saja", "Gemetarlah hati mereka", "Keras membatu", "Ragu-ragu"],
                                correct: 2,
                                explanation: "Sesungguhnya orang-orang yang beriman ialah mereka yang bila disebut nama Allah gemetarlah hati mereka."
                            },
                            {
                                question: "Apa balasan bagi orang yang menuruti keridhaan Allah (Ali 'Imran: 162-163)?",
                                options: ["Sama dengan orang yang dimurkai", "Mendapat kedudukan bertingkat-tingkat di sisi Allah", "Masuk neraka", "Tidak mendapat apa-apa"],
                                correct: 2,
                                explanation: "(Kedudukan) mereka itu bertingkat-tingkat di sisi Allah."
                            }
                        ]
                    },
                    {
                        id: 45,
                        title: "Balasan Bagi Orang Beriman & Beramal Soleh",
                        file: "topic_45.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Mendapat Perlindungan & Pertolongan</li>
                <li>Mendapat Kesentosaan di Dunia & Akhirat</li>
                <li>Dihapuskan Dosa-dosanya</li>
                <li>Disempurnakan Pahalanya</li>
                <li>Mendapat Surga & Kenikmatannya</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini merangkum berbagai balasan indah yang Allah janjikan bagi orang beriman dan beramal saleh. Mulai dari kehidupan yang baik di dunia (hayatan thayyibah), pengampunan dosa, hingga puncak kenikmatan abadi di surga.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Kehidupan yang Baik</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka sungguh akan Kami berikan padanya kehidupan yang baik.</p>
                    <span class="source">Surat An Nahl Ayat: 97</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Penghapusan Dosa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sungguh akan Kami hapuskan dari mereka dosa-dosa mereka.</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 7</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Balasan Surga</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka itulah para penghuni surga; mereka kekal di dalamnya.</p>
                    <span class="source">Surat Al A'raaf Ayat: 42</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Allah tidak akan menyia-nyiakan iman dan amal hamba-Nya. Balasan yang disiapkan jauh lebih baik dari apa yang bisa dibayangkan manusia. Semoga kita termasuk penduduk surga-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa janji Allah bagi orang beriman & beramal saleh di dunia (An Nahl: 97)?",
                                options: ["Kekayaan melimpah", "Kehidupan yang baik (hayatan thayyibah)", "Kekuasaan mutlak", "Umur panjang tanpa sakit"],
                                correct: 2,
                                explanation: "Maka sungguh akan Kami berikan padanya kehidupan yang baik."
                            },
                            {
                                question: "Apa yang Allah janjikan terkait dosa-dosa orang beriman (Al 'Ankabuut: 7)?",
                                options: ["Dibiarkan saja", "Akan Kami hapuskan dosa-dosanya", "Akan ditambah dosanya", "Akan diingat selamanya"],
                                correct: 2,
                                explanation: "Sungguh akan Kami hapuskan dari mereka dosa-dosa mereka."
                            },
                            {
                                question: "Apa balasan di akhirat bagi orang beriman (Al A'raaf: 42)?",
                                options: ["Menjadi debu", "Masuk neraka sementara", "Penghuni surga dan kekal di dalamnya", "Reinkarnasi"],
                                correct: 3,
                                explanation: "Mereka itulah para penghuni surga; mereka kekal di dalamnya."
                            },
                            {
                                question: "Di mana orang beriman dan beramal saleh akan ditempatkan (Saba': 37)?",
                                options: ["Di tempat yang rendah", "Di tempat-tempat yang tinggi (dalam surga)", "Di luar angkasa", "Di bawah bumi"],
                                correct: 2,
                                explanation: "Dan mereka aman sentosa di tempat-tempat yang tinggi (dalam surga)."
                            },
                            {
                                question: "Apa sebutan bagi golongan Allah (Al Mujaadilah: 22)?",
                                options: ["Golongan yang merugi", "Golongan yang beruntung", "Golongan yang kalah", "Golongan yang lemah"],
                                correct: 2,
                                explanation: "Ketahuilah, bahwa sesungguhnya golongan Allah adalah golongan yang beruntung."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-2",
                title: "Golongan Kafir",
                topics: [
                    {
                        id: 46,
                        title: "Hakikat, Sifat, & Perumpamaan Kufur",
                        file: "topic_46.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Hakikat & Sifat Orang Kafir</li>
                <li>Hati yang Terkunci Mati</li>
                <li>Perumpamaan Orang Kafir vs Mukmin</li>
                <li>Perumpamaan Amal Orang Kafir</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini mengupas hakikat kekafiran, di mana hati orang kafir telah dikunci mati oleh Allah sehingga tidak bisa menerima petunjuk. Dijelaskan pula sifat-sifat mereka, serta perumpamaan keadaan mereka yang seperti orang buta berjalan dalam kegelapan, dan amal mereka yang sia-sia seperti fatamorgana.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Hati yang Terkunci</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah telah mengunci hati dan pendengaran mereka, dan penglihatan mereka ditutup.</p>
                    <span class="source">Surat Al Baqarah Ayat: 7</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Perumpamaan Orang Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apakah orang yang sudah mati lalu ia Kami hidupkan... serupa dengan orang yang keadaannya berada dalam gelap gulita yang sekali-kali tidak dapat keluar daripadanya?</p>
                    <span class="source">Surat Al An'am Ayat: 122</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Amal yang Sia-sia</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Amal-amal mereka seperti fatamorgana di tanah yang datar.</p>
                    <span class="source">Surat An Nuur Ayat: 39</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kekafiran bukan sekadar status, tapi kondisi hati yang tertutup dari kebenaran. Semoga kita terhindar dari sifat-sifat ini dan selalu mendapat hidayah-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa yang dilakukan Allah terhadap hati orang kafir menurut Al Baqarah ayat 7?",
                                options: ["Membersihkannya", "Mengunci matinya", "Meneranginya", "Membukanya lebar-lebar"],
                                correct: 2,
                                explanation: "Allah telah mengunci hati dan pendengaran mereka."
                            },
                            {
                                question: "Bagaimana perumpamaan amal orang kafir dalam Surat An Nuur ayat 39?",
                                options: ["Seperti emas murni", "Seperti pohon yang rindang", "Seperti fatamorgana di tanah datar", "Seperti air yang mengalir"],
                                correct: 3,
                                explanation: "Amal-amal mereka seperti fatamorgana di tanah yang datar, yang disangka air oleh orang-orang yang dahaga."
                            },
                            {
                                question: "Siapa yang tidak akan senang kepada Nabi Muhammad SAW menurut Al Baqarah ayat 120?",
                                options: ["Orang-orang miskin", "Orang-orang musafir", "Orang-orang Yahudi dan Nasrani", "Orang-orang Arab"],
                                correct: 3,
                                explanation: "Orang-orang Yahudi dan Nasrani tidak akan senang kepadamu hingga kamu mengikuti agama mereka."
                            },
                            {
                                question: "Apa perumpamaan orang yang sudah mati lalu dihidupkan (diberi hidayah) vs orang kafir dalam Al An'am 122?",
                                options: ["Orang kaya vs Orang miskin", "Orang berjalan di cahaya vs Orang dalam gelap gulita", "Raja vs Hamba sahaya", "Singa vs Domba"],
                                correct: 2,
                                explanation: "Dan apakah orang... Kami berikan kepadanya cahaya... serupa dengan orang yang keadaannya berada dalam gelap gulita."
                            },
                            {
                                question: "Amal orang kafir dalam Ibrahim 18 diumpamakan seperti apa?",
                                options: ["Debu yang bermanfaat", "Abu yang ditiup angin dengan keras", "Batu yang keras", "Tanah yang subur"],
                                correct: 2,
                                explanation: "Amal-amal mereka adalah seperti abu yang ditiup angin dengan keras pada suatu hari yang berangin kencang."
                            }
                        ]
                    },
                    {
                        id: 47,
                        title: "Balasan Bagi Orang Kafir",
                        file: "topic_47.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Azab Kebinasaan di Dunia</li>
                <li>Amal yang Sia-sia</li>
                <li>Celaka pada Hari Kiamat</li>
                <li>Laknat yang Kekal</li>
                <li>Menjadi Bahan Bakar Neraka</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan berbagai balasan mengerikan bagi orang kafir, baik di dunia maupun akhirat. Di dunia mereka dibinasakan seperti kaum terdahulu, dan di akhirat mereka mendapat laknat abadi, siksa pedih, dan menjadi bahan bakar neraka.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Kehinaan di Dunia & Akhirat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Bagi mereka di dunia kehinaan dan bagi mereka di akhirat siksa yang berat.</p>
                    <span class="source">Surat Al Baqarah Ayat: 114</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Bahan Bakar Neraka</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka itu adalah bahan bakar api neraka.</p>
                    <span class="source">Surat Ali 'Imran Ayat: 10</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Laknat Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka itulah yang mendapat laknat Allah, para malaikat dan manusia seluruhnya.</p>
                    <span class="source">Surat Al Baqarah Ayat: 161</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Peringatan tentang azab ini bukan untuk menakut-nakuti tanpa alasan, melainkan agar manusia sadar dan kembali ke jalan yang benar sebelum terlambat.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa balasan bagi orang yang menghalangi menyebut nama Allah di masjid (Al Baqarah 114)?",
                                options: ["Diberi harta berlimpah", "Kehinaan di dunia dan siksa berat di akhirat", "Menjadi penguasa dunia", "Dipuji manusia"],
                                correct: 2,
                                explanation: "Bagi mereka di dunia kehinaan dan bagi mereka di akhirat siksa yang berat."
                            },
                            {
                                question: "Siapakah yang disebut sebagai 'bahan bakar api neraka' dalam Ali 'Imran ayat 10?",
                                options: ["Batu-batuan", "Kayu bakar", "Orang-orang kafir", "Setan saja"],
                                correct: 3,
                                explanation: "Sesungguhnya orang-orang yang kafir... Dan mereka itu adalah bahan bakar api neraka."
                            },
                            {
                                question: "Apa yang terjadi pada amal-amal orang kafir (Muhammad: 32)?",
                                options: ["Akan dilipatgandakan", "Akan diampuni", "Allah akan menghapuskan (pahala) amalnya", "Akan disimpan"],
                                correct: 3,
                                explanation: "Dan Allah akan menghapuskan (pahala) amal-amal mereka."
                            },
                            {
                                question: "Siapa yang melaknat orang yang mati dalam kekafiran (Al Baqarah 161)?",
                                options: ["Hanya Allah", "Hanya Malaikat", "Hanya Manusia", "Allah, para malaikat, dan manusia seluruhnya"],
                                correct: 4,
                                explanation: "Mereka itulah yang mendapat laknat Allah, para malaikat dan manusia seluruhnya."
                            },
                            {
                                question: "Di mana tempat kembali orang yang fasik/kafir menurut As Sajdah ayat 20?",
                                options: ["Surga Firdaus", "Neraka Jahanam", "Padang Mahsyar", "Antara surga dan neraka"],
                                correct: 2,
                                explanation: "Dan adapun orang-orang yang fasik (kafir), maka tempat mereka adalah Jahanam."
                            }
                        ]
                    },
                    {
                        id: 48,
                        title: "Cara Menghadapi Orang Kafir",
                        file: "topic_48.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Larangan Mengikuti Orang Kafir</li>
                <li>Larangan Menjadikan Pemimpin</li>
                <li>Cara Bergaul & Batasannya</li>
                <li>Menghadapi di Medan Perang</li>
                <li>Perintah Menjaga Persatuan</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini memberikan panduan Syariat dalam berinteraksi dengan orang kafir. Ada batasan tegas dalam hal akidah dan kepemimpinan (wala' wal bara'), namun tetap diperintahkan berbuat adil dan baik dalam urusan duniawi selama mereka tidak memerangi.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Larangan Mengikuti Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hai Nabi, bertakwalah kepada Allah dan janganlah kamu menuruti orang-orang kafir dan orang-orang munafik.</p>
                    <span class="source">Surat Al Ahzab Ayat: 1</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Larangan Memilih Pemimpin Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hai orang-orang yang beriman, janganlah kamu mengambil orang-orang Yahudi dan Nasrani menjadi pemimpin-pemimpin.</p>
                    <span class="source">Surat Al Maaidah Ayat: 51</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Berbuat Baik dan Adil</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah tidak melarang kamu untuk berbuat baik dan berlaku adil terhadap orang-orang yang tiada memerangimu...</p>
                    <span class="source">Surat Al Mumtahanah Ayat: 8</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Islam mengajarkan prinsip yang seimbang: tegas dalam prinsip keimanan dan loyalitas, namun tetap santun dan adil dalam muamalah kemanusiaan.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa akibat jika orang mukmin mentaati orang kafir menurut Ali 'Imran 149?",
                                options: ["Akan menjadi kaya", "Akan menjadi modern", "Dikembalikan ke kekafiran dan merugi", "Akan mendapat jabatan"],
                                correct: 3,
                                explanation: "Niscaya mereka mengembalikan kamu ke belakang (kepada kekafiran), lalu jadilah kamu orang-orang yang rugi."
                            },
                            {
                                question: "Siapakah yang dilarang dijadikan pemimpin dalam Al Maaidah ayat 51?",
                                options: ["Orang-orang muslemen", "Orang-orang Yahudi dan Nasrani", "Orang-orang yang sholeh", "Orang-orang yang berilmu"],
                                correct: 2,
                                explanation: "Janganlah kamu mengambil orang-orang Yahudi dan Nasrani menjadi pemimpin-pemimpin."
                            },
                            {
                                question: "Bolehkah berbuat baik kepada orang kafir yang tidak memerangi umat Islam (Al Mumtahanah: 8)?",
                                options: ["Dilarang keras", "Makruh", "Allah tidak melarang (boleh berbuat baik dan adil)", "Haram"],
                                correct: 3,
                                explanation: "Allah tidak melarang kamu untuk berbuat baik dan berlaku adil terhadap orang-orang yang tiada memerangimu."
                            },
                            {
                                question: "Apa yang dilarang dilakukan terhadap sembahan orang kafir (Al An'am: 108)?",
                                options: ["Memakinya", "Mengingkarinya", "Menjauhinya", "Mempelajarinya"],
                                correct: 1,
                                explanation: "Dan janganlah kamu memaki sembahan-sembahan yang mereka seru selain Allah."
                            },
                            {
                                question: "Apa perintah Allah kepada orang beriman dalam Ali Imran 103 agar tidak seperti orang kafir?",
                                options: ["Bercerai-berai", "Berpegang teguh pada tali agama Allah dan jangan bercerai-berai", "Saling bermusuhan", "Berbangga-bangga"],
                                correct: 2,
                                explanation: "Dan berpeganglah kamu semuanya kepada tali (agama) Allah, dan janganlah kamu bercerai-berai."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-3",
                title: "Golongan Munafik",
                topics: [
                    {
                        id: 49,
                        title: "Hakikat & Perumpamaan Nifaq",
                        file: "topic_49.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Hakikat Nifaq</li>
                <li>Menipu Diri Sendiri</li>
                <li>Perumpamaan Api</li>
                <li>Perumpamaan Hujan Lebat</li>
                <li>Penampilan Fisik vs Hati</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan hakikat kemunafikan, yaitu menampakkan keimanan di lisan namun menyembunyikan kekafiran di hati. Allah membuat perumpamaan bagi mereka seperti orang yang menyalakan api lalu padam, atau seperti orang yang ditimpa hujan lebat dalam kegelapan.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Hakikat Munafik</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka hendak menipu Allah dan orang-orang yang beriman, padahal mereka hanya menipu dirinya sendiri sedang mereka tidak sadar.</p>
                    <span class="source">Surat Al Baqarah Ayat: 9</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Perumpamaan Api</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Perumpamaan mereka adalah seperti orang yang menyalakan api, maka setelah api itu menerangi sekelilingnya Allah hilangkan cahaya (yang menyinari) mereka, dan membiarkan mereka dalam kegelapan.</p>
                    <span class="source">Surat Al Baqarah Ayat: 17</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Penampilan vs Hati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apabila kamu melihat mereka, tubuh-tubuh mereka membuatmu kagum... Mereka adalah seakan-akan kayu yang tersandar.</p>
                    <span class="source">Surat Al Munafiqun Ayat: 4</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kemunafikan adalah penyakit hati yang berbahaya. Penampilan fisik yang menarik dan kata-kata manis bisa menipu manusia, namun tidak bisa menipu Allah.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa yang dilakukan orang munafik menurut Al Baqarah ayat 9?",
                                options: ["Memerangi orang kafir", "Menipu Allah dan orang beriman", "Bersedekah secara sembunyi", "Berpuasa terus menerus"],
                                correct: 2,
                                explanation: "Mereka hendak menipu Allah dan orang-orang yang beriman, padahal mereka hanya menipu dirinya sendiri."
                            },
                            {
                                question: "Dalam Al Baqarah 17, apa yang terjadi setelah api menerangi sekeliling orang munafik?",
                                options: ["Api semakin besar", "Allah hilangkan cahayanya dan biarkan dalam kegelapan", "Mereka merasa hangat", "Hujan turun memadamkan"],
                                correct: 2,
                                explanation: "Allah hilangkan cahaya (yang menyinari) mereka, dan membiarkan mereka dalam kegelapan."
                            },
                            {
                                question: "Bagaimana perumpamaan fisik orang munafik dalam Al Munafiqun ayat 4?",
                                options: ["Seperti singa yang gagah", "Seperti pohon yang rindang", "Seakan-akan kayu yang tersandar", "Seperti gunung yang kokoh"],
                                correct: 3,
                                explanation: "Mereka adalah seakan-akan kayu yang tersandar."
                            },
                            {
                                question: "Apa sumpah palsu orang munafik dalam Al Munafiqun ayat 1?",
                                options: ["Kami akan berperang", "Kami bersedekah", "Kami mengakui engkau benar-benar Rasul Allah", "Kami tidak akan berkhianat"],
                                correct: 3,
                                explanation: "Mereka berkata: 'Kami mengakui, bahwa sesungguhnya kamu benar-benar Rasul Allah'."
                            },
                            {
                                question: "Apa penyakit yang ada dalam hati orang munafik menurut Al Baqarah ayat 10?",
                                options: ["Keraguan/Kekafiran", "Jantung koroner", "Sesak nafas", "Tidak ada penyakit"],
                                correct: 1,
                                explanation: "Dalam hati mereka ada penyakit, lalu ditambah Allah penyakitnya."
                            }
                        ]
                    },
                    {
                        id: 50,
                        title: "Sifat-Sifat Orang Munafiq",
                        file: "topic_50.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Berbuat Kerusakan</li>
                <li>Sombong & Menolak Kebenaran</li>
                <li>Bermuka Dua (Oportunis)</li>
                <li>Malas Beribadah (Riya')</li>
                <li>Menghalangi Manusia dari Jalan Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini merinci sifat-sifat buruk orang munafik. Mereka mengaku memperbaiki bumi padahal merusaknya, sombong saat diingatkan takwa, bermuka dua di hadapan mukmin dan kafir, serta malas dan riya' dalam shalat.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Membuat Kerusakan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan bila dikatakan kepada mereka: 'Janganlah kamu membuat kerusakan di muka bumi'. Mereka menjawab: 'Sesungguhnya kami orang-orang yang mengadakan perbaikan.'</p>
                    <span class="source">Surat Al Baqarah Ayat: 11</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Malas Shalat & Riya'</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apabila mereka berdiri untuk shalat mereka berdiri dengan malas. Mereka bermaksud riya (dengan shalat) di hadapan manusia.</p>
                    <span class="source">Surat An Nisa Ayat: 142</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Bermuka Dua</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan bila mereka berjumpa dengan orang-orang yang beriman, mereka mengatakan: 'Kami telah beriman'. Dan bila mereka kembali kepada setan-setan mereka, mereka mengatakan: 'Sesungguhnya kami sependirian dengan kamu'.</p>
                    <span class="source">Surat Al Baqarah Ayat: 14</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sifat-sifat ini harus kita waspadai agar tidak menjangkiti hati kita. Orang munafik selalu mencari keuntungan duniawi dengan menggadaikan agama.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa jawaban orang munafik saat dilarang membuat kerusakan (Al Baqarah 11)?",
                                options: ["Kami tidak sengaja", "Kami orang-orang yang mengadakan perbaikan", "Kami hanya mengikuti perintah", "Kami tidak peduli"],
                                correct: 2,
                                explanation: "Mereka menjawab: 'Sesungguhnya kami orang-orang yang mengadakan perbaikan'."
                            },
                            {
                                question: "Bagaimana cara orang munafik mendirikan shalat (An Nisa 142)?",
                                options: ["Khusyuk dan lama", "Tepat waktu", "Dengan malas dan riya'", "Berjamaah di masjid"],
                                correct: 3,
                                explanation: "Dan apabila mereka berdiri untuk shalat mereka berdiri dengan malas. Mereka bermaksud riya."
                            },
                            {
                                question: "Apa yang dikatakan orang munafik saat kembali kepada golongan/setan mereka (Al Baqarah 14)?",
                                options: ["Kami telah bertaubat", "Kami sependirian dengan kamu, kami hanya berolok-olok", "Kami takut kepada Islam", "Kami ingin masuk Islam"],
                                correct: 2,
                                explanation: "Mereka mengatakan: 'Sesungguhnya kami sependirian dengan kamu, kami hanyalah berolok-olok'."
                            },
                            {
                                question: "Sifat apa yang muncul pada orang munafik saat dikatakan 'Bertakwalah kepada Allah' (Al Baqarah 206)?",
                                options: ["Kesombongan (Izzah) yang menyebabkannya berbuat dosa", "Ketakutan yang amat sangat", "Kesadaran untuk bertaubat", "Menangis tersedu-sedu"],
                                correct: 1,
                                explanation: "Bangkitlah kesombongannya yang menyebabkannya berbuat dosa."
                            },
                            {
                                question: "Apa yang mereka lakukan terhadap sedekah orang mukmin (At Taubah 79)?",
                                options: ["Memujinya", "Mencela dan mengolok-olok", "Menambahinya", "Mencatatnya"],
                                correct: 2,
                                explanation: "(Orang munafik) mencela orang-orang mukmin yang memberi sedekah dengan sukarela."
                            }
                        ]
                    },
                    {
                        id: 51,
                        title: "Balasan Bagi Orang Munafik",
                        file: "topic_51.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Azab Dunia & Akhirat</li>
                <li>Tingkatan Paling Bawah di Neraka</li>
                <li>Tidak Ada Penolong</li>
                <li>Kekafiran setelah Keislaman</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan hukuman berat bagi orang munafik. Karena pengkhianatan mereka lebih berbahaya dari kekafiran yang terang-terangan, mereka ditempatkan di kerak neraka yang paling bawah.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Kerak Neraka</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya orang-orang munafik itu (ditempatkan) pada tingkatan yang paling bawah dari neraka.</p>
                    <span class="source">Surat An Nisa Ayat: 145</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Azab Dunia & Akhirat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka jika mereka bertobat, hal itu lebih baik bagi mereka, dan jika mereka berpaling, niscaya Allah mengazab mereka dengan azab yang pedih di dunia dan akhirat.</p>
                    <span class="source">Surat At Taubah Ayat: 74</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Tidak ada penolong bagi orang munafik di akhirat, kecuali mereka bertaubat tulus sebelum ajal menjemput.</p>
                        `,
                        quiz: [
                            {
                                question: "Di tingkatan mana orang munafik ditempatkan dalam neraka (An Nisa 145)?",
                                options: ["Tingkatan paling atas", "Tingkatan tengah", "Tingkatan yang paling bawah (kerak neraka)", "Di pintu gerbang"],
                                correct: 3,
                                explanation: "Sesungguhnya orang-orang munafik itu (ditempatkan) pada tingkatan yang paling bawah dari neraka."
                            },
                            {
                                question: "Apa tujuan Allah memberikan harta dan anak kepada orang munafik menurut At Taubah 55?",
                                options: ["Sebagai berkah", "Untuk menyiksa mereka di dunia dengan hal itu", "Sebagai ujian kesabaran", "Tanda kasih sayang"],
                                correct: 2,
                                explanation: "Sesungguhnya Allah menghendaki dengan (memberi) harta dan anak-anak itu untuk menyiksa mereka dalam kehidupan dunia."
                            },
                            {
                                question: "Apa yang dilakukan orang munafik menurut At Taubah 74?",
                                options: ["Mengucapkan perkataan kekafiran setelah Islam", "Membangun masjid", "Pergi berjihad", "Membayar zakat"],
                                correct: 1,
                                explanation: "Dan sungguh mereka telah mengucapkan perkataan kekafiran, dan telah menjadi kafir sesudah Islam."
                            },
                            {
                                question: "Adakah penolong bagi orang munafik di api neraka (An Nisa 145)?",
                                options: ["Ada, malaikat", "Ada, setan", "Kamu sekali-kali tidak akan mendapat seorang penolongpun bagi mereka", "Ada, sesama munafik"],
                                correct: 3,
                                explanation: "Dan kamu sekali-kali tidak akan mendapat seorang penolongpun bagi mereka."
                            },
                            {
                                question: "Siapakah yang dikecualikan dari ancaman neraka bagi munafik (An Nisa 146)?",
                                options: ["Orang yang kaya raya", "Orang yang bertaubat dan memperbaiki diri", "Orang yang punya jabatan", "Orang yang pandai bicara"],
                                correct: 2,
                                explanation: "Kecuali orang-orang yang tobat dan mengadakan perbaikan dan berpegang teguh pada agama Allah."
                            }
                        ]
                    },
                    {
                        id: 52,
                        title: "Cara Menghadapi Orang Munafik",
                        file: "topic_52.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Larangan Menjadi Penolong Mereka</li>
                <li>Larangan Menyolatkan Jenazah Mereka</li>
                <li>Sikap Waspada</li>
                <li>Perintah Berpaling dari Mereka</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan panduan Syariat dalam berinteraksi dengan orang munafik. Umat Islam dilarang mendoakan jenazah mereka, dilarang menjadikan mereka teman setia/pelindung, dan diperintahkan untuk bersikap tegas namun tetap waspada terhadap tipu daya mereka.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Larangan Menyolatkan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan janganlah kamu sekali-kali menyolatkan (jenazah) seorang yang mati di antara mereka, dan janganlah kamu berdiri (mendoakan) di kuburnya.</p>
                    <span class="source">Surat At Taubah Ayat: 84</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Larangan Mengambil Walj</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka janganlah kamu jadikan di antara mereka sebagai penolong-penolong, hingga mereka berhijrah pada jalan Allah.</p>
                    <span class="source">Surat An Nisa Ayat: 89</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sikap tegas diperlukan untuk menjaga kemurnian barisan umat Islam dari pengkhianatan orang-orang munafik.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa larangan Allah terhadap jenazah orang munafik (At Taubah 84)?",
                                options: ["Dilarang menguburkannya", "Dilarang memandikannya", "Dilarang menyolatkan dan mendoakan di kuburnya", "Dilarang melayat"],
                                correct: 3,
                                explanation: "Dan janganlah kamu sekali-kali menyolatkan (jenazah) seorang yang mati di antara mereka, dan janganlah kamu berdiri (mendoakan) di kuburnya."
                            },
                            {
                                question: "Mengapa dilarang menyolatkan mereka (At Taubah 84)?",
                                options: ["Karena mereka miskin", "Karena mereka mati dalam keadaan fasik/kafir", "Karena jenazahnya kotor", "Karena tidak ada perintah"],
                                correct: 2,
                                explanation: "Sesungguhnya mereka telah kafir kepada Allah dan Rasul-Nya dan mereka mati dalam keadaan fasik."
                            },
                            {
                                question: "Kapan boleh menjadikan mereka teman/penolong (An Nisa 89)?",
                                options: ["Jika mereka kaya", "Jika mereka berhijrah di jalan Allah", "Jika mereka memberi hadiah", "Kapan saja boleh"],
                                correct: 2,
                                explanation: "Maka janganlah kamu jadikan di antara mereka sebagai penolong-penolong, hingga mereka berhijrah pada jalan Allah."
                            },
                            {
                                question: "Bagaimana sikap terhadap orang munafik yang menyebarkan kabar bohong di Madinah (Al Ahzab 60-61)?",
                                options: ["Dibiarkan saja", "Diberi hadiah", "Dilaknat, ditangkap dan dibunuh (jika terus menerus mengganggu)", "Diangkat jadi pemimpin"],
                                correct: 3,
                                explanation: "Dalam keadaan terlaknat. Di mana saja mereka dijumpai, mereka ditangkap dan dibunuh dengan sehebat-hebatnya."
                            },
                            {
                                question: "Apa alasan mereka ingin kamu menjadi kafir (An Nisa 89)?",
                                options: ["Agar kamu masuk surga", "Agar kamu menjadi sama dengan mereka", "Agar kamu kaya", "Agar kamu pintar"],
                                correct: 2,
                                explanation: "Mereka ingin supaya kamu menjadi kafir sebagaimana mereka telah kafir, lalu kamu menjadi sama (dengan mereka)."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-4",
                title: "Golongan Murtad",
                topics: [
                    {
                        id: 53,
                        title: "Definisi & Hukum Riddah",
                        file: "topic_53.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Definisi Murtad</li>
                <li>Pengecualian bagi yang Dipaksa</li>
                <li>Penyebab Murtad</li>
                <li>Hati yang Terkunci</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas tentang Riddah (Murtad), yaitu kembali menjadi kafir setelah beriman. Allah memperingatkan kemurkaan besar bagi pelakunya, kecuali bagi mereka yang dipaksa mengucapkan kekafiran sementara hatinya tetap tenang dalam keimanan.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Kafir Setelah Iman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Barangsiapa yang kafir kepada Allah sesudah ia beriman (dia mendapat kemurkaan Allah), kecuali orang yang dipaksa kafir padahal hatinya tetap tenang dalam beriman (dia tidak berdosa)...</p>
                    <span class="source">Surat An Nahl Ayat: 106</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Penyebab & Akibat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hal itu karena mereka mencintai kehidupan dunia lebih dari akhirat... Itulah orang-orang yang hati, pendengaran, dan penglihatan mereka telah dikunci mati oleh Allah.</p>
                    <span class="source">Surat An Nahl Ayat: 107-108</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Murtad adalah kerugian yang nyata di dunia dan akhirat. Penyebab utamanya seringkali adalah kecintaan yang berlebihan terhadap dunia yang fana.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa definisi orang yang mendapat kemurkaan Allah dalam An Nahl 106?",
                                options: ["Orang yang tidak shalat", "Siapa yang kafir kepada Allah sesudah ia beriman", "Orang yang berdusta", "Orang yang mencuri"],
                                correct: 2,
                                explanation: "Barangsiapa yang kafir kepada Allah sesudah ia beriman (dia mendapat kemurkaan Allah)."
                            },
                            {
                                question: "Siapakah yang dikecualikan dari dosa kekafiran dalam An Nahl 106?",
                                options: ["Orang yang dipaksa kafir padahal hatinya tenang beriman", "Orang yang berpura-pura", "Orang yang bercanda", "Orang yang lupa"],
                                correct: 1,
                                explanation: "Kecuali orang yang dipaksa kafir padahal hatinya tetap tenang dalam beriman."
                            },
                            {
                                question: "Apa penyebab utama seseorang menjadi murtad menurut An Nahl 107?",
                                options: ["Kurang ilmu", "Miskin", "Mencintai kehidupan dunia lebih dari akhirat", "Diganggu setan"],
                                correct: 3,
                                explanation: "Hal itu karena bahwa mereka mencintai kehidupan dunia lebih dari akhirat."
                            },
                            {
                                question: "Apa yang dilakukan Allah terhadap hati orang-orang murtad tersebut (An Nahl 108)?",
                                options: ["Dibuka lebar-lebar", "Disucikan", "Dikunci mati", "Dibiarkan ragu"],
                                correct: 3,
                                explanation: "Itulah orang-orang yang hati, pendengaran, dan penglihatan mereka telah dikunci mati oleh Allah."
                            },
                            {
                                question: "Bagaimana nasib mereka di akhirat (An Nahl 109)?",
                                options: ["Masuk surga", "Mendapat syafaat", "Pasti merugi", "Diampuni"],
                                correct: 3,
                                explanation: "Pastilah bahwa mereka di akhirat adalah orang-orang yang rugi."
                            }
                        ]
                    },
                    {
                        id: 54,
                        title: "Balasan Bagi Orang Murtad",
                        file: "topic_54.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Laknat Allah & Malaikat</li>
                <li>Tobat yang Tidak Diterima</li>
                <li>Diganti Kaum yang Lebih Baik</li>
                <li>Rugi Dunia Akhirat</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan hukuman berat bagi orang murtad. Mereka dilaknat oleh seluruh makhluk, tobat mereka tertolak jika mempermainkan agama, dan Allah akan menggantikan mereka dengan kaum yang mencintai Allah dan dicintai-Nya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Laknat Bagi Mereka</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Itulah, balasan mereka ialah: bahwa laknat Allah ditimpakan kepada mereka, (demikian pula) para malaikat dan manusia seluruhnya.</p>
                    <span class="source">Surat Ali Imran Ayat: 87</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tidak Diterima Tobatnya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya orang-orang kafir sesudah beriman, kemudian bertambah kekafirannya, sekali-kali tidak akan diterima tobatnya.</p>
                    <span class="source">Surat Ali Imran Ayat: 90</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Pengganti Kaum Murtad</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hai orang-orang yang beriman, siapa di antara kamu yang murtad dari agamanya, maka kelak Allah akan mendatangkan suatu kaum yang Allah mencintai mereka dan merekapun mencintai-Nya.</p>
                    <span class="source">Surat Al Maaidah Ayat: 54</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Janganlah kita menjadi orang yang 'beribadah di tepi jurang' (Al Hajj: 11), jika untung tenang, jika rugi murtad. Jadilah mukmin yang istiqomah.</p>
                        `,
                        quiz: [
                            {
                                question: "Siapakah yang melaknat orang murtad menurut Ali Imran 87?",
                                options: ["Hanya Allah", "Hanya Malaikat", "Allah, Malaikat, dan manusia seluruhnya", "Tidak ada yang melaknat"],
                                correct: 3,
                                explanation: "Bahwa laknat Allah ditimpakan kepada mereka, (demikian pula) para malaikat dan manusia seluruhnya."
                            },
                            {
                                question: "Bagaimana hukum tobat bagi orang yang kafir sesudah iman lalu bertambah kekafirannya (Ali Imran 90)?",
                                options: ["Diterima jika membayar denda", "Sekali-kali tidak akan diterima tobatnya", "Diterima kapan saja", "Ditangguhkan"],
                                correct: 2,
                                explanation: "Sesungguhnya orang-orang kafir sesudah beriman, kemudian bertambah kekafirannya, sekali-kali tidak akan diterima tobatnya."
                            },
                            {
                                question: "Apakah tebusan emas sepenuh bumi bisa menyelamatkan orang kafir di akhirat (Ali Imran 91)?",
                                options: ["Bisa", "Bisa jika ditambah perak", "Tidaklah akan diterima dari seseorang di antara mereka", "Tergantung amal lainnya"],
                                correct: 3,
                                explanation: "Maka tidaklah akan diterima dari seseorang di antara mereka emas sepenuh bumi."
                            },
                            {
                                question: "Apa ancaman Allah dalam Al Maaidah 54 jika umat Islam murtad?",
                                options: ["Langit akan runtuh", "Bumi akan gempa", "Allah akan mendatangkan kaum lain yang dicintai-Nya dan mereka mencintai-Nya", "Akan terjadi kiamat"],
                                correct: 3,
                                explanation: "Maka kelak Allah akan mendatangkan suatu kaum yang Allah mencintai mereka dan merekapun mencintai-Nya."
                            },
                            {
                                question: "Bagaimana gambaran orang yang 'menyembah Allah di tepi' (Al Hajj 11)?",
                                options: ["Selalu khusyuk", "Jika untung tenang, jika rugi murtad", "Selalu ragu-ragu", "Beribadah di pinggir sungai"],
                                correct: 2,
                                explanation: "Jika ia memperoleh kebajikan, tetaplah ia dalam keadaan itu, dan jika ia ditimpa oleh suatu bencana, berbaliklah ia ke belakang (murtad)."
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        id: "theme-3",
        title: "Tema 3: Malaikat, Kitab, dan Rasul",
        subjects: [
            {
                id: "subject-1",
                title: "Beriman Kepada Malaikat",
                topics: [
                    {
                        id: 55,
                        title: "Keutamaan Malaikat",
                        file: "topic_55.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Malaikat Utusan Allah</li>
                <li>Sayap Malaikat</li>
                <li>Kecepatan Luar Biasa</li>
                <li>Memusuhi Malaikat = Musuh Allah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas kemuliaan malaikat sebagai utusan Allah yang memiliki sayap dan kecepatan luar biasa. Mereka adalah makhluk yang taat, dan memusuhi mereka (seperti Jibril dan Mikail) berarti menyatakan permusuhan kepada Allah.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Malaikat sebagai Utusan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah memilih utusan-utusan-(Nya) dari malaikat dan dari manusia.</p>
                    <span class="source">Surat Al Hajj Ayat: 75</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Sayap Malaikat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Yang menjadikan malaikat sebagai utusan-utusan (untuk mengurus berbagai urusan) yang mempunyai sayap, masing-masing (ada yang) dua, tiga, dan empat.</p>
                    <span class="source">Surat Faathir Ayat: 1</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kecepatan Malaikat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Malaikat-malaikat dan Jibril naik (menghadap) kepada Tuhan dalam sehari yang kadarnya lima puluh ribu tahun.</p>
                    <span class="source">Surat Al Ma’aarij Ayat: 4</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Malaikat adalah tentara dan utusan Allah yang mulia. Wajib bagi kita untuk mencintai dan mempercayai keberadaan serta tugas-tugas mereka sebagai bagian dari rukun iman.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa peran malaikat menurut Al Hajj ayat 75?",
                                options: ["Sebagai Tuhan", "Sebagai anak Allah", "Sebagai utusan Allah (Rusul)", "Sebagai manusia biasa"],
                                correct: 3,
                                explanation: "Allah memilih utusan-utusan-(Nya) dari malaikat dan dari manusia."
                            },
                            {
                                question: "Berapa jumlah sayap malaikat yang disebutkan dalam Surat Faathir ayat 1?",
                                options: ["Satu saja", "Dua, tiga, dan empat", "Tidak bersayap", "Tak terhingga"],
                                correct: 2,
                                explanation: "Yang mempunyai sayap, masing-masing (ada yang) dua, tiga, dan empat."
                            },
                            {
                                question: "Berapa lama waktu yang ditempuh malaikat menghadap Tuhan dibandingkan perhitungan manusia (Al Ma'aarij: 4)?",
                                options: ["1000 tahun", "50.000 tahun", "1 tahun", "100 tahun"],
                                correct: 2,
                                explanation: "Dalam sehari yang kadarnya lima puluh ribu tahun."
                            },
                            {
                                question: "Siapakah yang disebut sebagai musuh Allah dalam Al Baqarah 98?",
                                options: ["Orang yang memusuhi Jibril dan Mikail", "Orang miskin", "Orang bodoh", "Orang yang sakit"],
                                correct: 1,
                                explanation: "Barang siapa yang menjadi musuh Allah, malaikat-malaikat-Nya, rasul-rasul-Nya, Jibril, dan Mikail, maka sesungguhnya Allah adalah musuh orang-orang kafir."
                            },
                            {
                                question: "Selain malaikat, dari golongan mana lagi Allah memilih utusan (Al Hajj 75)?",
                                options: ["Jin", "Manusia", "Hewan", "Tumbuhan"],
                                correct: 2,
                                explanation: "Allah memilih utusan-utusan-(Nya) dari malaikat dan dari manusia."
                            }
                        ]
                    },
                    {
                        id: 56,
                        title: "Keutamaan Jibril",
                        file: "topic_56.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Jibril yang Mulia dan Kuat</li>
                <li>Ruh Al Qudus (Roh Suci)</li>
                <li>Pembawa Wahyu (Alquran)</li>
                <li>Kepercayan di Langit</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Jibril adalah penghulu para malaikat yang bertugas membawa wahyu. Ia memiliki kekuatan yang dahsyat, kedudukan tinggi di sisi Allah, ditaati oleh malaikat lain, dan sangat dipercaya (Al Amin).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Sifat-sifat Jibril</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Alquran itu benar-benar firman (Allah yang dibawa oleh) utusan yang mulia (Jibril), yang mempunyai kekuatan, yang mempunyai kedudukan tinggi di sisi Allah yang mempunyai 'Arsy, yang ditaati di sana lagi dipercaya.</p>
                    <span class="source">Surat At Takwiir Ayat: 19-21</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Jibril Menemui Maryam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Lalu Kami mengutus roh Kami (Jibril) kepadanya, maka ia menjelma di hadapannya (dalam bentuk) manusia yang sempurna.</p>
                    <span class="source">Surat Maryam Ayat: 17</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Menurunkan Alquran Ke Hati Nabi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Siapa yang menjadi musuh Jibril, maka Jibril itu telah menurunkannya (Alquran) ke dalam hatimu dengan izin Allah.</p>
                    <span class="source">Surat Al Baqarah Ayat: 97</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Jibril ('Alaihis Salam) adalah perantara wahyu antara Allah dan para Rasul-Nya. Membenci Jibril sama dengan membenci Allah yang mengutusnya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa sifat Jibril yang disebutkan dalam At Takwiir 21?",
                                options: ["Pemarah", "Ditaati (di alam malaikat) lagi dipercaya", "Suka tidur", "Lemah"],
                                correct: 2,
                                explanation: "Yang ditaati di sana (di alam malaikat) lagi dipercaya."
                            },
                            {
                                question: "Dalam bentuk apakah Jibril menemui Maryam (Maryam 17)?",
                                options: ["Cahaya menyilaukan", "Burung besar", "Manusia yang sempurna", "Api"],
                                correct: 3,
                                explanation: "Maka ia menjelma di hadapannya (dalam bentuk) manusia yang sempurna."
                            },
                            {
                                question: "Apa tugas utama Jibril terhadap Alquran (Al Baqarah 97)?",
                                options: ["Mengarangnya", "Menurunkannya ke dalam hati Nabi dengan izin Allah", "Menyimpannya di gua", "Membacakannya kepada manusia saja"],
                                correct: 2,
                                explanation: "Maka Jibril itu telah menurunkannya (Alquran) ke dalam hatimu dengan izin Allah."
                            },
                            {
                                question: "Apa sebutan Jibril dalam Surat Maryam ayat 17?",
                                options: ["Ruh Kami (Ruhuna)", "Ruh Jahat", "Malaikat Maut", "Pemimpin Perang"],
                                correct: 1,
                                explanation: "Lalu Kami mengutus roh Kami (Jibril) kepadanya."
                            },
                            {
                                question: "Siapakah yang memberikan kepada Maryam anak laki-laki yang suci (Maryam 19)?",
                                options: ["Nabi Zakaria", "Utusan Tuhan (Jibril)", "Raja Herodes", "Penduduk desa"],
                                correct: 2,
                                explanation: "Sesungguhnya aku ini hanyalah seorang utusan Tuhanmu, untuk memberimu seorang anak laki-laki yang suci."
                            }
                        ]
                    },
                    {
                        id: 57,
                        title: "Sifat-Sifat Malaikat",
                        file: "topic_57.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Selalu Taat & Takut pada Allah</li>
                <li>Tidak Angkuh & Tidak Letih</li>
                <li>Senantiasa Bertasbih</li>
                <li>Memiliki Kedudukan Tertentu</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Malaikat adalah hamba-hamba Allah yang dimuliakan. Mereka tidak pernah maksiat, tidak angkuh, dan tidak pernah lelah menyembah Allah. Setiap malaikat memiliki tugas dan kedudukan (maqam) yang sudah ditentukan.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Tidak Angkuh dan Tidak Letih</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan malaikat-malaikat yang di sisi-Nya, mereka tiada mempunyai rasa angkuh untuk menyembah-Nya dan tiada (pula) merasa letih.</p>
                    <span class="source">Surat Al Anbiyaa’ Ayat: 19</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Selalu Bertasbih</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka selalu bertasbih malam dan siang tiada henti-hentinya.</p>
                    <span class="source">Surat Al Anbiyaa’ Ayat: 20</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kedudukan dan Shaf</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tiada seorangpun di antara kami (malaikat) melainkan mempunyai kedudukan yang tertentu, Dan sesungguhnya kami benar-benar bershaf-shaf.</p>
                    <span class="source">Surat Ash Shaaffaat Ayat: 164-165</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Ketaatan malaikat adalah teladan bagi manusia. Meski mereka makhluk suci tanpa nafsu, mereka tetap takut dan tunduk patuh sepenuhnya kepada Allah SWT.</p>
                        `,
                        quiz: [
                            {
                                question: "Apakah malaikat pernah merasa berat atau enggan menyembah Allah (Al A'raaf 206)?",
                                options: ["Ya, kadang-kadang", "Sering", "Tidaklah merasa enggan menyembah Allah", "Hanya saat sibuk"],
                                correct: 3,
                                explanation: "Sesungguhnya malaikat-malaikat yang ada di sisi Tuhanmu tidaklah merasa enggan menyembah Allah."
                            },
                            {
                                question: "Kapan malaikat bertasbih kepada Allah (Al Anbiyaa 20)?",
                                options: ["Hanya siang hari", "Hanya malam hari", "Malam dan siang tiada henti-hentinya", "Saat diperintah saja"],
                                correct: 3,
                                explanation: "Mereka selalu bertasbih malam dan siang tiada henti-hentinya."
                            },
                            {
                                question: "Apa yang dikatakan malaikat tentang kedudukan mereka dalam Ash Shaaffaat 164?",
                                options: ["Kami bebas melakukan apa saja", "Kami mempunyai kedudukan yang tertentu", "Kami tidak punya tempat", "Kami bersembunyi"],
                                correct: 2,
                                explanation: "Tiada seorangpun di antara kami (malaikat) melainkan mempunyai kedudukan yang tertentu."
                            },
                            {
                                question: "Apakah malaikat di sisi Tuhan merasa letih (Al Anbiyaa 19)?",
                                options: ["Sangat letih", "Sedikit letih", "Tiada (pula) merasa letih", "Butuh istirahat"],
                                correct: 3,
                                explanation: "Mereka tiada mempunyai rasa angkuh untuk menyembah-Nya dan tiada (pula) merasa letih."
                            },
                            {
                                question: "Apa bantahan Allah terhadap tuduhan musyrikin bahwa malaikat adalah anak Allah (Al Anbiyaa 26)?",
                                options: ["Malaikat itu hantu", "Sebenarnya malaikat itu adalah hamba-hamba yang dimuliakan", "Malaikat itu dewa", "Malaikat itu jin"],
                                correct: 2,
                                explanation: "Maha Suci Allah. Sebenarnya (malaikat-malaikat itu), adalah hamba-hamba yang dimuliakan."
                            }
                        ]
                    },
                    {
                        id: 58,
                        title: "Tugas-Tugas Malaikat",
                        file: "topic_58.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Pembawa Kabar Gembira & Azab</li>
                <li>Pencatat Amal & Saksi</li>
                <li>Pencabut Nyawa (Maut)</li>
                <li>Penjaga Surga & Neraka</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini merinci berbagai tugas spesifik malaikat. Mulai dari membawa kabar gembira kepada para Nabi, mencatat setiap ucapan manusia (Raqib & Atid), mencabut nyawa orang kafir dengan keras dan orang mukmin dengan lembut, hingga menjaga pintu surga dan neraka.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Pencatat Amal (Raqib Atid)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tiada suatu ucapanpun yang diucapkannya melainkan ada di dekatnya malaikat pengawas yang selalu hadir.</p>
                    <span class="source">Surat Qaaf Ayat: 18</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Pencabut Nyawa (Malaikat Maut)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Malaikat maut yang diserahi untuk (mencabut nyawa)-mu akan mematikanmu...</p>
                    <span class="source">Surat As Sajdah Ayat: 11</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Penjaga Neraka (19 Malaikat)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan di atasnya ada sembilan belas (malaikat penjaga). Dan tidak Kami jadikan penjaga neraka itu melainkan dari malaikat.</p>
                    <span class="source">Surat Al Muddatstsir Ayat: 30-31</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Setiap detik kita diawasi dan dicatat amalnya. Mengimani tugas malaikat membuat kita lebih waspada dalam berbuat dan sadar akan adanya balasan di akhirat kelak.</p>
                        `,
                        quiz: [
                            {
                                question: "Siapa yang mencatat setiap ucapan manusia (Qaaf 18)?",
                                options: ["Malaikat Ridwan", "Malaikat Malik", "Malaikat pengawas yang selalu hadir (Raqib & Atid)", "Malaikat Jibril"],
                                correct: 3,
                                explanation: "Tiada suatu ucapanpun yang diucapkannya melainkan ada di dekatnya malaikat pengawas yang selalu hadir."
                            },
                            {
                                question: "Apa yang dilakukan malaikat saat mencabut nyawa orang kafir (Al Anfaal 50)?",
                                options: ["Memberi salam", "Memukul muka dan belakang mereka", "Memberi minum", "Tersenyum"],
                                correct: 2,
                                explanation: "Malaikat mencabut jiwa orang-orang yang kafir seraya memukul muka dan belakang mereka."
                            },
                            {
                                question: "Apa ucapan malaikat penjaga surga kepada orang saleh (Ar Ra'd 24)?",
                                options: ["Dilarang masuk", "Bayar dulu", "Salamun 'alaikum bi Maa Shabartum (Selamat atas kesabaranmu)", "Tunggu antrian"],
                                correct: 3,
                                explanation: "(Sambil mengucapkan): 'Salamun 'alaikum bi Maa Shabartum' (Selamat sejahtera atasmu berkat kesabaranmu)."
                            },
                            {
                                question: "Berapa jumlah malaikat penjaga neraka saqar yang disebut dalam Al Muddatstsir 30?",
                                options: ["Seribu", "Tujuh", "Sembilan belas", "Satu"],
                                correct: 3,
                                explanation: "Dan di atasnya ada sembilan belas (malaikat penjaga)."
                            },
                            {
                                question: "Apa fungsi jumlah 19 malaikat penjaga neraka itu bagi orang kafir (Al Muddatstsir 31)?",
                                options: ["Sebagai pasukan", "Sebagai cobaan (fitnah)", "Sebagai teman", "Sebagai hiburan"],
                                correct: 2,
                                explanation: "Dan tidak Kami jadikan bilangan mereka itu melainkan sebagai cobaan bagi orang-orang kafir."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-2",
                title: "Beriman Kepada Kitab",
                topics: [
                    {
                        id: 59,
                        title: "Kewajiban Beriman Kepada Kitab Allah",
                        file: "topic_59.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Perintah Beriman kepada Kitab</li>
                <li>Keutamaan Beriman</li>
                <li>Ancaman Bagi Pendusta Kitab</li>
                <li>Ancaman Bagi Penyembunyi Ayat</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Beriman kepada kitab-kitab Allah adalah rukun iman ketiga. Kita wajib mengimani bahwa Allah telah menurunkan kitab-kitab kepada para Rasul-Nya sebagai petunjuk. Mengingkari, mendustakan, atau menyembunyikan isi kitab Allah diancam dengan azab yang pedih.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Perintah Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah (hai orang-orang mukmin): 'Kami beriman kepada Allah dan apa yang diturunkan kepada kami...'</p>
                    <span class="source">Surat Al Baqarah Ayat: 136</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Ancaman Mendustakan Ayat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Adapun orang-orang yang kafir dan mendustakan ayat-ayat Kami, mereka itu penghuni neraka; mereka kekal di dalamnya.</p>
                    <span class="source">Surat Al Baqarah Ayat: 39</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Ancaman Menyembunyikan Ayat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya orang-orang yang menyembunyikan apa yang telah Kami turunkan berupa keterangan-keterangan dan petunjuk... mereka itu dilaknat Allah.</p>
                    <span class="source">Surat Al Baqarah Ayat: 159</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Iman kepada kitab haruslah utuh, tidak boleh memilah-milah. Kita harus meyakini semua kitab samawi namun hukum syariat yang berlaku bagi umat Nabi Muhammad SAW adalah Alquran.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa yang harus dikatakan kepada Ahli Kitab saat berdebat (Al 'Ankabuut 46)?",
                                options: ["Kami lebih benar", "Kami telah beriman kepada (kitab-kitab) yang diturunkan kepada kami dan yang diturunkan kepadamu", "Kalian salah semua", "Agama kami berbeda total"],
                                correct: 2,
                                explanation: "Katakanlah: 'Kami telah beriman kepada (kitab-kitab) yang diturunkan kepada kami dan yang diturunkan kepadamu'."
                            },
                            {
                                question: "Apa balasan bagi orang yang mendustakan ayat-ayat Allah (Al Baqarah 39)?",
                                options: ["Dimarahi malaikat", "Mereka itu penghuni neraka; mereka kekal di dalamnya", "Masuk surga sementara", "Reinkarnasi"],
                                correct: 2,
                                explanation: "Mereka itu penghuni neraka; mereka kekal di dalamnya."
                            },
                            {
                                question: "Apa akibat bagi orang yang menyembunyikan keterangan yang diturunkan Allah (Al Baqarah 159)?",
                                options: ["Mendapat harta", "Dilaknat Allah dan dilaknat oleh semua yang dapat melaknat", "Dipuji manusia", "Menjadi pemimpin"],
                                correct: 2,
                                explanation: "Mereka itu dilaknat Allah dan dilaknat oleh semua yang dapat melaknat."
                            },
                            {
                                question: "Apa yang dimakan oleh orang yang menyembunyikan ayat Allah demi harga murah (Al Baqarah 174)?",
                                options: ["Emas", "Api (ke dalam perutnya)", "Roti", "Daging"],
                                correct: 2,
                                explanation: "Mereka itu sebenarnya tidak memakan (menelan) ke dalam perutnya melainkan api."
                            },
                            {
                                question: "Apakah Allah akan berbicara dengan kasih sayang kepada penyembunyi ayat di hari kiamat (Al Baqarah 174)?",
                                options: ["Ya, Allah Maha Penyayang", "Allah tidak akan berbicara kepada mereka", "Allah akan memuji mereka", "Allah akan memberi hadiah"],
                                correct: 2,
                                explanation: "Dan Allah tidak akan berbicara kepada mereka pada hari kiamat."
                            }
                        ]
                    },
                    {
                        id: 60,
                        title: "Kedudukan Kitab Allah",
                        file: "topic_60.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Bukti Risalah Para Nabi</li>
                <li>Petunjuk bagi Manusia</li>
                <li>Peringatan bagi Manusia</li>
                <li>Kemuliaan Kitab-Kitab</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Kitab-kitab Allah diturunkan sebagai bukti kebenaran risalah para Nabi, sebagai petunjuk (Hudan) ke jalan yang lurus, dan sebagai peringatan (Dzikra) agar manusia tidak tersesat. Kitab-kitab ini sangat dimuliakan di sisi Allah.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Sebaik-baik Petunjuk</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dia menurunkan Alkitab (Alquran) kepadamu dengan sebenarnya; membenarkan kitab yang diturunkan sebelumnya.</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 3</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Peringatan yang Dimuliakan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Di dalam kitab-kitab yang dimuliakan, yang ditinggikan lagi disucikan.</p>
                    <span class="source">Surat 'Abasa Ayat: 13-14</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Alquran sebagai penyempurna kitab-kitab terdahulu berfungsi sebagai Furqan (pembeda) antara yang hak dan yang batil.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa fungsi Alquran yang disebutkan dalam Ali 'Imran ayat 4?",
                                options: ["Sebagai hiasan", "Menjadi petunjuk bagi manusia dan Al Furqaan", "Sebagai jimat", "Sebagai sejarah"],
                                correct: 2,
                                explanation: "Sebelum (Alquran), menjadi petunjuk bagi manusia, dan Dia menurunkan Alfurqaan."
                            },
                            {
                                question: "Bagaimana sifat kitab-kitab yang disebutkan dalam 'Abasa ayat 13-14?",
                                options: ["Kotor dan rendah", "Biasa saja", "Dimuliakan, ditinggikan lagi disucikan", "Kuno dan usang"],
                                correct: 3,
                                explanation: "Di dalam kitab-kitab yang dimuliakan, yang ditinggikan lagi disucikan."
                            },
                            {
                                question: "Di tangan siapakah kitab-kitab itu berada ('Abasa 15-16)?",
                                options: ["Di tangan manusia biasa", "Di tangan para penulis (malaikat) yang mulia lagi berbakti", "Di tangan jin", "Di tangan raja"],
                                correct: 2,
                                explanation: "Di tangan para penulis (malaikat), Yang mulia lagi berbakti."
                            },
                            {
                                question: "Apa yang Allah berikan kepada Nabi seperti Musa, Isa, dan Muhammad sebagai bukti (Al An'aam 89)?",
                                options: ["Harta karun", "Istana", "Kitab, hikmah, dan kenabian", "Tentara"],
                                correct: 3,
                                explanation: "Itulah orang-orang yang telah Kami berikan kitab, hikmah, dan kenabian."
                            },
                            {
                                question: "Apa ancaman bagi yang kafir terhadap ayat-ayat Allah dalam Ali Imran 4?",
                                options: ["Akan miskin", "Memperoleh siksa yang berat", "Akan sakit", "Akan gila"],
                                correct: 2,
                                explanation: "Sesungguhnya orang-orang yang kafir terhadap ayat-ayat Allah akan memperoleh siksa yang berat."
                            }
                        ]
                    },
                    {
                        id: 61,
                        title: "Taurat, Zabur, Injil, dan Alquran",
                        file: "topic_61.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Taurat (Musa AS)</li>
                <li>Zabur (Daud AS)</li>
                <li>Injil (Isa AS)</li>
                <li>Alquran (Muhammad SAW)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Allah menurunkan 4 kitab utama: Taurat kepada Nabi Musa AS, Zabur kepada Nabi Daud AS, Injil kepada Nabi Isa AS, dan Alquran kepada Nabi Muhammad SAW. Alquran hadir sebagai penyempurna dan penutup kitab-kitab sebelumnya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Taurat (Musa)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sungguh telah Kami berikan Alkitab (Taurat) kepada Musa, agar mereka (Bani Israil) mendapat petunjuk.</p>
                    <span class="source">Surat Al Mu'minuun Ayat: 49</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Zabur (Daud)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Kami berikan Zabur kepada Daud.</p>
                    <span class="source">Surat Al Israa' Ayat: 55</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Injil (Isa)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Kami telah memberikan kepadanya (Isa) kitab Injil sedang di dalamnya (ada) petunjuk dan cahaya.</p>
                    <span class="source">Surat Al Maaidah Ayat: 46</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Alquran (Muhammad)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Alquran ini tidak lain hanyalah peringatan bagi semesta alam.</p>
                    <span class="source">Surat Shaad Ayat: 87</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Umat Islam wajib mengimani turunnya kitab-kitab terdahulu, namun dalam pengamalan, hanya Alquran yang menjadi pedoman hidup terakhir yang dijaga kemurniannya oleh Allah SWT.</p>
                        `,
                        quiz: [
                            {
                                question: "Kitab apa yang diturunkan kepada Nabi Daud AS (Al Israa' 55)?",
                                options: ["Taurat", "Injil", "Zabur", "Suhuf"],
                                correct: 3,
                                explanation: "Dan Kami berikan Zabur kepada Daud."
                            },
                            {
                                question: "Apa isi kitab Injil menurut Al Maaidah 46?",
                                options: ["Dongeng", "Petunjuk dan cahaya", "Syair lagu", "Sejarah perang"],
                                correct: 2,
                                explanation: "Sedang di dalamnya (ada) petunjuk dan dan cahaya (yang menerangi)."
                            },
                            {
                                question: "Apa fungsi Taurat bagi Bani Israil (Al Israa' 2)?",
                                options: ["Agar mereka menjadi raja", "Agar mereka mengambil penolong selain Allah", "Agar jangan mengambil penolong selain Aku (Allah)", "Agar mereka kaya"],
                                correct: 3,
                                explanation: "Menjadikannya petunjuk bagi Bani Israil (agar): 'Janganlah kamu mengambil penolong selain Aku'."
                            },
                            {
                                question: "Bagi siapakah Alquran menjadi peringatan (Shaad 87)?",
                                options: ["Hanya orang Arab", "Hanya orang dewasa", "Bagi semesta alam ('Alamin)", "Bagi jin saja"],
                                correct: 3,
                                explanation: "Alquran ini tidak lain hanyalah peringatan bagi semesta alam."
                            },
                            {
                                question: "Mengapa orang kafir menuduh Nabi gila saat mendengar Alquran (Al Qalam 51)?",
                                options: ["Karena Nabi berteriak", "Karena dengki dengan pandangan mereka", "Karena Nabi sakit", "Karena Nabi diam"],
                                correct: 2,
                                explanation: "Dan sungguh orang-orang kafir benar-benar hampir menggelincirkan kamu dengan pandangan mereka... dan mereka berkata: 'Sesungguhnya ia benar-benar orang gila'."
                            }
                        ]
                    },
                    {
                        id: 62,
                        title: "Sikap Ahli Kitab Terhadap Kitabnya",
                        file: "topic_62.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Memperselisihkan Isi Kitab</li>
                <li>Mendustakan Kebenaran</li>
                <li>Menyembunyikan Ayat</li>
                <li>Mengubah Isi Kitab (Tahrif)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Ahli Kitab (Yahudi dan Nasrani) memiliki berbagai sikap negatif terhadap kitab suci mereka sendiri. Mulai dari memperselisihkan isinya, mendustakan ayat-ayat yang tidak sesuai keinginan hawa nafsu, hingga mengubah (Tahrif) dan menyembunyikan kebenaran tentang Nabi Muhammad SAW.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Memperselisihkan Kebenaran</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan orang-orang Yahudi berkata: "Orang-orang Nasrani itu tidak mempunyai suatu pegangan", dan orang-orang Nasrani berkata: "Orang-orang Yahudi tidak mempunyai suatu pegangan," padahal mereka (sama-sama) membaca Alkitab.</p>
                    <span class="source">Surat Al Baqarah Ayat: 113</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Mengubah Isi Kitab (Tahrif)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka suka mengubah perkataan (Allah) dari tempat-tempatnya, dan mereka (sengaja) melupakan sebagian dari apa yang mereka telah diperingatkan dengannya.</p>
                    <span class="source">Surat Al Maaidah Ayat: 13</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Menyembunyikan Kebenaran</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Orang-orang (Yahudi dan Nasrani) yang telah Kami beri Alkitab (Taurat dan Injil) mengenal Muhammad seperti mereka mengenal anak-anaknya sendiri. Dan sesungguhnya sebagian di antara mereka menyembunyikan kebenaran, padahal mereka mengetahui.</p>
                    <span class="source">Surat Al Baqarah Ayat: 146</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sikap-sikap ini menjadi peringatan bagi umat Islam agar tidak meniru perilaku Ahli Kitab yang mempermainkan agama dan kitab suci mereka demi kepentingan duniawi.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa tuduhan Yahudi terhadap Nasrani dan sebaliknya menurut Al Baqarah 113?",
                                options: ["Mereka bersaudara", "Tidak mempunyai suatu pegangan (kebenaran)", "Mereka sama-sama benar", "Mereka saling melengkapi"],
                                correct: 2,
                                explanation: "Dan orang-orang Yahudi berkata: 'Orang-orang Nasrani itu tidak mempunyai suatu pegangan', dan orang-orang Nasrani berkata: 'Orang-orang Yahudi tidak mempunyai suatu pegangan'."
                            },
                            {
                                question: "Apa ancaman bagi orang yang menulis Alkitab dengan tangan sendiri lalu berkata 'Ini dari Allah' (Al Baqarah 79)?",
                                options: ["Akan menjadi kaya", "Kecelakaan besarlah bagi mereka", "Mendapat pahala", "Diampuni dosanya"],
                                correct: 2,
                                explanation: "Maka kecelakaan besarlah bagi orang-orang yang menulis Alkitab dengan tangan mereka sendiri... Maka kecelakaan besarlah bagi mereka, akibat apa yang ditulis oleh tangan mereka sendiri."
                            },
                            {
                                question: "Bagaimana pengetahuan Ahli Kitab tentang Nabi Muhammad SAW (Al Baqarah 146)?",
                                options: ["Tidak kenal sama sekali", "Hanya tahu nama", "Mengenal seperti mengenal anak-anaknya sendiri", "Ragu-ragu"],
                                correct: 3,
                                explanation: "Orang-orang (Yahudi dan Nasrani) yang telah Kami beri Alkitab (Taurat dan Injil) mengenal Muhammad seperti mereka mengenal anak-anaknya sendiri."
                            },
                            {
                                question: "Apa yang dilakukan Ahli Kitab terhadap ayat-ayat Allah menurut Al Maaidah 13?",
                                options: ["Menghafalnya", "Mengamalkannya", "Mengubah perkataan (Allah) dari tempat-tempatnya", "Menyebarkannya"],
                                correct: 3,
                                explanation: "Mereka suka mengubah perkataan (Allah) dari tempat-tempatnya."
                            },
                            {
                                question: "Apa perumpamaan orang yang dipikul Taurat tapi tidak mengamalkannya (Al Jumu'ah 5)?",
                                options: ["Seperti singa", "Seperti keledai yang membawa kitab-kitab yang tebal", "Seperti burung", "Seperti unta"],
                                correct: 2,
                                explanation: "Perumpamaan orang-orang yang dipikulkan kepadanya Taurat, kemudian mereka tiada memikulnya adalah seperti keledai yang membawa kitab-kitab yang tebal."
                            }
                        ]
                    },
                    {
                        id: 63,
                        title: "Sikap Ahli Kitab Terhadap Alquran",
                        file: "topic_63.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Perintah Beriman pada Alquran</li>
                <li>Mengingkari Kebenaran</li>
                <li>Dengki dan Ingin Menyesatkan</li>
                <li>Sebagian yang Beriman</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Meskipun Alquran membenarkan kitab-kitab sebelumnya, sebagian besar Ahli Kitab mengingkarinya karena dengki bahwa nabi terakhir bukan dari golongan mereka. Mereka bahkan berusaha menyesatkan orang-orang beriman. Namun, ada sebagian kecil dari mereka yang jujur dan menerima kebenaran Islam.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Perintah Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan berimanlah kamu kepada apa yang telah Aku turunkan (Alquran) yang membenarkan apa yang ada padamu (Taurat), dan janganlah kamu menjadi orang yang pertama kafir kepadanya.</p>
                    <span class="source">Surat Al Baqarah Ayat: 41</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Ingin Menyesatkan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Segolongan dari ahli kitab ingin menyesatkan kamu, padahal mereka (sebenarnya) tidak menyesatkan melainkan dirinya sendiri, dan mereka tidak menyadarinya.</p>
                    <span class="source">Surat Ali 'Imran Ayat: 69</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Sebagian yang Beriman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya di antara ahli kitab ada yang beriman kepada Allah dan kepada apa yang diturunkan kepadamu...</p>
                    <span class="source">Surat Ali 'Imran Ayat: 199</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sikap dengki menghalangi hidayah, sedangkan hati yang bersih akan mudah menerima kebenaran. Kita diperintahkan untuk waspada terhadap tipu daya mereka yang ingin memalingkan kita dari Islam.</p>
                        `,
                        quiz: [
                            {
                                question: "Mengapa Ahli Kitab mengingkari Alquran padahal mereka mengetahuinya (Al Baqarah 109)?",
                                options: ["Karena bodoh", "Karena dengki (hasad) dalam diri mereka", "Karena lupa", "Karena sibuk"],
                                correct: 2,
                                explanation: "Karena dengki yang (timbul) dari diri mereka, setelah nyata bagi mereka kebenaran."
                            },
                            {
                                question: "Apa keinginan sebagian Ahli Kitab terhadap orang beriman (Ali Imran 69)?",
                                options: ["Ingin memberi harta", "Ingin menyesatkan kamu", "Ingin belajar bersama", "Ingin berdamai"],
                                correct: 2,
                                explanation: "Segolongan dari ahli kitab ingin menyesatkan kamu."
                            },
                            {
                                question: "Apa balasan bagi Ahli Kitab yang beriman kepada Allah dan Alquran (Al Qashash 54)?",
                                options: ["Diberi pahala satu kali", "Diberi pahala dua kali", "Tidak dapat apa-apa", "Hanya selamat di dunia"],
                                correct: 2,
                                explanation: "Mereka itu diberi pahala dua kali disebabkan kesabaran mereka."
                            },
                            {
                                question: "Bagaimana sikap orang yang diberi ilmu ketika Alquran dibacakan (Al Israa 107)?",
                                options: ["Tertawa", "Menyungkur atas muka mereka sambil bersujud", "Berlari", "Tidur"],
                                correct: 2,
                                explanation: "Sesungguhnya orang-orang yang diberi pengetahuan sebelumnya apabila Alquran dibacakan... mereka menyungkur atas muka mereka sambil bersujud."
                            },
                            {
                                question: "Apa yang dikatakan Ahli Kitab yang beriman saat mendengar Alquran (Al Qashash 53)?",
                                options: ["Ini sihir", "Kami beriman kepadanya, sesungguhnya ia adalah kebenaran", "Ini dongeng", "Kami tidak percaya"],
                                correct: 2,
                                explanation: "Mereka berkata: 'Kami beriman kepadanya; sesungguhnya Alquran adalah kebenaran dari Tuhan kami'."
                            }
                        ]
                    },
                    {
                        id: 64,
                        title: "Sikap Kafir Quraisy Terhadap Alquran",
                        file: "topic_64.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Menuduh Alquran sebagai Sihir</li>
                <li>Menuduh sebagai Dongeng (Asatir Awwalin)</li>
                <li>Menuduh Buatan Manusia</li>
                <li>Menganggap Aneh/Ajaib</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Orang-orang kafir Quraisy menolak kebenaran Alquran dengan berbagai tuduhan palsu. Mereka menyebutnya sihir, dongeng masa lalu, mimpi yang kalut, atau buatan Muhammad SAW. Padahal, jauh di lubuk hati, mereka mengakui keindahan dan keajaiban bahasa Alquran yang tidak mungkin dibuat manusia.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Tuduhan Sihir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apabila dibacakan kepada mereka ayat-ayat Kami yang menjelaskan, berkatalah orang-orang yang mengingkari kebenaran... "Ini adalah sihir yang nyata".</p>
                    <span class="source">Surat Al Ahqaaf Ayat: 7</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tuduhan Dongeng (Asatirul Awwalin)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan jika dibacakan kepada mereka ayat-ayat Kami, mereka berkata... "(Alquran) ini tidak lain hanyalah dongengan orang-orang dahulu".</p>
                    <span class="source">Surat Al Anfaal Ayat: 31</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tuduhan Dusta</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan orang-orang kafir berkata: "Alquran ini tidak lain hanyalah kebohongan yang diada-adakan oleh Muhammad dan ia dibantu oleh kaum yang lain".</p>
                    <span class="source">Surat Al Furqaan Ayat: 4</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Segala tuduhan mereka hanyalah bentuk penolakan terhadap kebenaran yang nyata. Allah sendiri yang menjamin kemurnian Alquran dan membantah segala tuduhan keji mereka.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa tuduhan orang kafir terhadap Alquran dalam Al Anfaal 31?",
                                options: ["Syair indah", "Dongengan orang-orang dahulu (Asatirul Awwalin)", "Hukum yang adil", "Sejarah bangsa"],
                                correct: 2,
                                explanation: "(Alquran) ini tidak lain hanyalah dongengan orang-orang dahulu."
                            },
                            {
                                question: "Apa yang dikatakan orang kafir ketika kebenaran datang (Al Ahqaaf 7)?",
                                options: ["Ini adalah sihir yang nyata", "Ini adalah cahaya", "Ini adalah petunjuk", "Ini adalah keadilan"],
                                correct: 1,
                                explanation: "Berkatalah orang-orang yang mengingkari kebenaran ketika kebenaran itu datang kepada mereka: 'Ini adalah sihir yang nyata'."
                            },
                            {
                                question: "Apa reaksi orang kafir mendengar Alquran menurut Qaaf ayat 2?",
                                options: ["Mereka beriman", "Mereka menangis", "Mereka tercengang/heran", "Mereka tidur"],
                                correct: 3,
                                explanation: "(Mereka tidak menerimanya) bahkan mereka tercengang karena telah datang kepada mereka seorang pemberi peringatan."
                            },
                            {
                                question: "Apa tantangan Allah kepada mereka yang ragu (Al Baqarah 23)?",
                                options: ["Buatlah satu surat (saja) yang semisal Alquran", "Buatlah patung", "Kumpulkan harta", "Pergi ke langit"],
                                correct: 1,
                                explanation: "Dan jika kamu (tetap) dalam keraguan... buatlah satu surat (saja) yang semisal Alquran."
                            },
                            {
                                question: "Siapakah yang sebenarnya membuat kebohongan menurut An Nahl 105?",
                                options: ["Orang beriman", "Orang-orang yang tidak beriman kepada ayat-ayat Allah", "Para malaikat", "Para nabi"],
                                correct: 2,
                                explanation: "Sesungguhnya yang mengada-adakan kebohongan, hanyalah orang-orang yang tidak beriman kepada ayat-ayat Allah."
                            }
                        ]
                    },
                    {
                        id: 65,
                        title: "Sikap Orang Mukmin Terhadap Alquran",
                        file: "topic_65.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Percaya Sepenuhnya</li>
                <li>Muhkamat dan Mutasyabihat</li>
                <li>3 Golongan Pewaris Alquran</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Orang mukmin wajib meyakini kebenaran Alquran sepenuhnya, baik ayat-ayat yang muhkamaat (jelas) maupun mutasyaabihaat (samar/butuh takwil). Alquran diwariskan kepada umat Nabi Muhammad SAW yang terbagi menjadi tiga golongan dalam mengamalkannya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Muhkamat & Mutasyabihat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dialah yang menurunkan Alkitab (Alquran) kepada kamu. Di antara (isi)nya ada ayat-ayat yang muhkamaat, itulah pokok-pokok isi Alquran dan yang lain (ayat-ayat) mutasyaabihaat.</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 7</span>
                </div>
                <p>Orang yang beriman berkata: "Kami beriman kepada ayat-ayat yang mutasyaabihaat, semuanya itu dari sisi Tuhan kami."</p>
            </div>

            <div class="content-section">
                <h3>3 Golongan Pewaris Kitab</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Lalu di antara mereka ada yang menganiaya diri mereka sendiri (Dhalimun li nafsih), dan di antara mereka ada yang pertengahan (Muqtashid), dan di antara mereka ada (pula) yang lebih dahulu berbuat kebaikan (Sabiqun bil khairat).</p>
                    <span class="source">Surat Faathir Ayat: 32</span>
                </div>
                <ul>
                    <li><strong>Dhalimun li nafsih</strong>: Lebih banyak salahnya daripada baiknya.</li>
                    <li><strong>Muqtashid</strong>: Kebaikan dan kesalahannya sebanding.</li>
                    <li><strong>Sabiqun bil khairat</strong>: Kebaikannya amat banyak dan jarang berbuat salah.</li>
                </ul>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Semoga kita termasuk golongan Sabiqun bil khairat yang berlomba-lomba dalam kebaikan dan selalu berpegang teguh pada Alquran.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa yang dimaksud dengan ayat Muhkamaat (Ali Imran 7)?",
                                options: ["Ayat yang samar artinya", "Ayat yang pokok/tegas maksudnya", "Ayat yang dihapus", "Ayat tentang sejarah"],
                                correct: 1,
                                explanation: "Ayat-ayat yang muhkamaat, itulah pokok-pokok isi Alquran (yang terang dan tegas maksudnya)."
                            },
                            {
                                question: "Siapakah golongan 'Dhalimun li nafsih' dalam Surat Faathir 32?",
                                options: ["Orang yang lebih banyak kebaikannya", "Orang yang pertengahan", "Orang yang menganiaya diri sendiri (lebih banyak dosanya)", "Orang yang tidak beriman"],
                                correct: 2,
                                explanation: "Lalu di antara mereka ada yang menganiaya diri mereka sendiri (lebih banyak kesalahannya daripada kebaikannya)."
                            },
                            {
                                question: "Bagaimana sikap orang yang mendalam ilmunya terhadap ayat mutasyabihat?",
                                options: ["Menolaknya", "Ragu-ragu", "Kami beriman kepadanya, semuanya dari sisi Tuhan kami", "Mencari ta'wil sesuka hati"],
                                correct: 2,
                                explanation: "Dan orang-orang yang mendalam ilmunya berkata: 'Kami beriman kepada ayat-ayat yang mutasyaabihaat, semuanya itu dari sisi Tuhan kami'."
                            },
                            {
                                question: "Apa balasan bagi 'Sabiqun bil khairat' di ayat selanjutnya (Faathir 33)?",
                                options: ["Surga 'Adn", "Kekayaan dunia", "Umur panjang", "Kesehatan"],
                                correct: 0,
                                explanation: "(Bagi mereka) surga 'Adn mereka masuk ke dalamnya."
                            },
                            {
                                question: "Apa tujuan orang yang hatinya condong pada kesesatan mencari ta'wil ayat mutasyabihat?",
                                options: ["Untuk belajar", "Untuk menimbulkan fitnah", "Untuk berdakwah", "Untuk mencari kebenaran"],
                                correct: 1,
                                explanation: "Maka mereka mengikuti sebagian ayat-ayat yang mutasyaabihaat daripadanya untuk menimbulkan fitnah."
                            }
                        ]
                    },
                    {
                        id: 66,
                        title: "Keistimewaan Kandungan Alquran",
                        file: "topic_66.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Wahyu dari Allah</li>
                <li>Terpelihara Keotentikannya</li>
                <li>Tidak Dapat Ditiru (Mukjizat)</li>
                <li>Mudah Dipelajari</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Alquran memiliki keistimewaan yang tidak dimiliki kitab lain. Ia adalah murni wahyu Allah, bukan karangan manusia atau sihir. Allah menjamin kemurniannya hingga hari kiamat, dan menantang siapa saja yang meragukannya untuk membuat yang serupa, namun tidak akan ada yang mampu.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Terpelihara Keasliannnya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami-lah yang menurunkan Adz Dzikra (Alquran), dan sesungguhnya Kami benar-benar memeliharanya.</p>
                    <span class="source">Surat Al Hijr Ayat: 9</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Tantangan Membuat Semisal Alquran</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan jika kamu (tetap) dalam keraguan tentang Alquran yang Kami wahyukan kepada hamba Kami (Muhammad), buatlah satu surat (saja) yang semisal Alquran itu.</p>
                    <span class="source">Surat Al Baqarah Ayat: 23</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Mudah Dipelajari</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya telah Kami mudahkan Alquran untuk pelajaran, maka adakah orang yang mengambil pelajaran?</p>
                    <span class="source">Surat Al Qamar Ayat: 17</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Keagungan Alquran terbukti sepanjang masa. Mari kita manfaatkan kemudahan yang Allah berikan untuk mempelajari dan mengamalkannya.</p>
                        `,
                        quiz: [
                            {
                                question: "Siapakah yang menjamin pemeliharaan Alquran (Al Hijr 9)?",
                                options: ["Para Malaikat", "Allah SWT", "Nabi Muhammad", "Para Sahabat"],
                                correct: 1,
                                explanation: "Sesungguhnya Kami-lah yang menurunkan Adz Dzikra (Alquran), dan sesungguhnya Kami benar-benar memeliharanya."
                            },
                            {
                                question: "Apa tantangan Allah bagi yang meragukan Alquran dalam Al Baqarah 23?",
                                options: ["Membuat satu ayat", "Membuat satu surat yang semisal", "Terbang ke langit", "Membelah lautan"],
                                correct: 1,
                                explanation: "Buatlah satu surat (saja) yang semisal Alquran itu."
                            },
                            {
                                question: "Jika manusia dan jin berkumpul untuk membuat semisal Alquran, apakah mereka mampu (Al Israa 88)?",
                                options: ["Mampu", "Niscaya mereka tidak akan dapat membuat yang serupa", "Mungkin bisa", "Hanya sebagian"],
                                correct: 1,
                                explanation: "Niscaya mereka tidak akan dapat membuat yang serupa dengan Dia, sekalipun sebagian mereka menjadi pembantu bagi sebagian yang lain."
                            },
                            {
                                question: "Apa sifat Alquran yang disebutkan dalam Al Qamar 17?",
                                options: ["Sulit dipahami", "Telah dimudahkan untuk pelajaran", "Hanya untuk orang Arab", "Sangat berat"],
                                correct: 1,
                                explanation: "Dan sesungguhnya telah Kami mudahkan Alquran untuk pelajaran."
                            },
                            {
                                question: "Apakah Alquran perkataan penyair atau tukang tenung (Al Haaqqah 41-42)?",
                                options: ["Ya, benar", "Sebagian iya", "Bukan perkataan penyair dan bukan tukang tenung", "Hasil renungan"],
                                correct: 2,
                                explanation: "Dan Alquran itu bukanlah perkataan seorang penyair... Dan bukan perkataan tukang tenung."
                            }
                        ]
                    },
                    {
                        id: 67,
                        title: "Keistimewaan Turunnya Alquran",
                        file: "topic_67.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Turun di Bulan Ramadhan</li>
                <li>Lailatul Qadar (Malam Kemuliaan)</li>
                <li>Diturunkan Berangsur-angsur</li>
                <li>Bahasa Arab yang Jelas</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Proses turunnya Alquran memiliki keistimewaan tersendiri. Ia diturunkan pada bulan mulia (Ramadhan), di malam yang lebih baik dari seribu bulan (Lailatul Qadar). Diturunkan secara berangsur-angsur untuk meneguhkan hati Nabi dan umatnya, serta menggunakan bahasa Arab yang jelas dan kaya makna.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Bulan Ramadhan & Lailatul Qadar</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Bulan Ramadhan, bulan yang di dalamnya diturunkan (permulaan) Alquran.</p>
                    <span class="source">Surat Al Baqarah Ayat: 185</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami telah menurunkannya (Alquran) pada malam kemuliaan.</p>
                    <span class="source">Surat Al Qadr Ayat: 1</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Berangsur-angsur (Tanjim)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Alquran itu telah Kami turunkan dengan berangsur-angsur agar kamu membacakannya perlahan-lahan kepada manusia.</p>
                    <span class="source">Surat Al Israa' Ayat: 106</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Bahasa Arab</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami menurunkannya berupa Alquran dengan bahasa Arab, agar kamu memahaminya.</p>
                    <span class="source">Surat Yuusuf Ayat: 2</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Turunnya Alquran adalah rahmat terbesar bagi semesta alam. Setiap aspek penurunannya mengandung hikmah ilahi yang mendalam.</p>
                        `,
                        quiz: [
                            {
                                question: "Pada bulan apa Alquran diturunkan (Al Baqarah 185)?",
                                options: ["Rajab", "Sya'ban", "Ramadhan", "Muharram"],
                                correct: 2,
                                explanation: "Bulan Ramadhan, bulan yang di dalamnya diturunkan (permulaan) Alquran."
                            },
                            {
                                question: "Malam apa yang lebih baik dari seribu bulan (Al Qadr 3)?",
                                options: ["Malam Jumat", "Malam Lailatul Qadar", "Malam Nisfu Sya'ban", "Malam Idul Fitri"],
                                correct: 1,
                                explanation: "Malam kemuliaan (Lailatul Qadar) itu lebih baik dari seribu bulan."
                            },
                            {
                                question: "Mengapa Alquran diturunkan berangsur-angsur (Al Furqaan 32)?",
                                options: ["Agar Kami perkuat hatimu (Nabi) dengannya", "Karena malaikat lelah", "Agar manusia bingung", "Tidak ada alasan"],
                                correct: 0,
                                explanation: "Demikianlah agar Kami perkuat hatimu dengannya dan Kami membacanya secara tartil."
                            },
                            {
                                question: "Mengapa Alquran diturunkan dalam bahasa Arab (Yuusuf 2)?",
                                options: ["Agar kamu membanggakannya", "Agar kamu memahaminya (menggunakan akal)", "Agar sulit dipelajari", "Hanya kebetulan"],
                                correct: 1,
                                explanation: "Sesungguhnya Kami menurunkannya berupa Alquran dengan bahasa Arab, agar kamu memahaminya."
                            },
                            {
                                question: "Apa yang dilarang saat Alquran sedang dibacakan Jibril kepada Nabi (Al Qiyaamah 16)?",
                                options: ["Menangis", "Menggerakkan lidah (tergesa-gesa)", "Diam mendengarkan", "Mencatat"],
                                correct: 1,
                                explanation: "Janganlah kamu gerakkan lidahmu untuk (membaca) Alquran karena hendak cepat-cepat (menguasai)-nya."
                            }
                        ]
                    },
                    {
                        id: 68,
                        title: "Kedudukan Al-Quran",
                        file: "topic_68.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Al-Quran: Batu Uji, Petunjuk, dan Obat</h3>
                                <p>Al-Quran memiliki kedudukan yang sangat tinggi dan fungsi yang beragam bagi kehidupan manusia. Beberapa fungsi utamanya antara lain:</p>
                                
                                <h4>1. Batu Uji (Al-Muhaimin)</h4>
                                <p>Al-Quran membenarkan kitab-kitab sebelumnya (Taurat, Injil, Zabur) dan menjadi batu uji terhadap kebenaran isi kitab-kitab tersebut yang masih ada saat ini. (QS. Al-Maidah: 48).</p>
                                
                                <h4>2. Pemisah (Al-Furqan)</h4>
                                <p>Al-Quran adalah pemisah antara yang hak (benar) dan yang bathil (salah). (QS. Ath-Thaariq: 13-14).</p>
                                
                                <h4>3. Petunjuk (Al-Huda)</h4>
                                <p>Al-Quran adalah petunjuk bagi orang-orang yang bertakwa, orang-orang beriman, dan seluruh manusia ke jalan yang lurus. (QS. Al-Baqarah: 2).</p>
                                
                                <h4>4. Penjelas (Al-Bayan)</h4>
                                <p>Al-Quran menjelaskan segala sesuatu (Tibyanan likulli syai'), termasuk hukum-hukum, kisah-kisah terdahulu, dan perkara yang diperselisihkan. (QS. An-Nahl: 89).</p>
                                
                                <h4>5. Obat (Asy-Syifa) dan Rahmat</h4>
                                <p>Al-Quran adalah penyembuh bagi penyakit hati (keraguan, kemunafikan) dan fisik, serta menjadi rahmat bagi orang-orang yang beriman. (QS. Al-Isra': 82).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Sesungguhnya Al Quran ini memberikan petunjuk kepada (jalan) yang lebih lurus..." (QS. Al-Isra': 9)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa fungsi Al-Quran terhadap kitab-kitab sebelumnya menurut QS. Al-Maidah ayat 48?",
                                options: [
                                    "Menghapus seluruh isinya",
                                    "Membenarkan dan menjadi batu uji (muhaimin)",
                                    "Hanya sebagai pelengkap",
                                    "Tidak ada hubungannya"
                                ],
                                correct: 1,
                                explanation: "Al-Quran berfungsi sebagai membenarkan kitab-kitab sebelumnya dan menjadi batu uji (muhaimin) terhadapnya."
                            },
                            {
                                question: "Apa arti 'Al-Furqan' sebagai salah satu nama/fungsi Al-Quran?",
                                options: [
                                    "Penyembuh",
                                    "Peringatan",
                                    "Pemisah antara hak dan bathil",
                                    "Kabar gembira"
                                ],
                                correct: 2,
                                explanation: "Al-Furqan berarti pemisah, yaitu memisahkan antara yang hak (benar) dan yang bathil (salah)."
                            },
                            {
                                question: "Bagi siapakah Al-Quran menjadi petunjuk (Hudan) menurut QS. Al-Baqarah ayat 2?",
                                options: [
                                    "Orang-orang musyrik",
                                    "Hanya untuk para Nabi",
                                    "Orang-orang yang bertakwa",
                                    "Orang-orang yang ragu"
                                ],
                                correct: 2,
                                explanation: "Al-Quran adalah petunjuk (hudan) bagi orang-orang yang bertakwa (hude lil muttaqiin)."
                            },
                            {
                                question: "Ayat mana yang menegaskan bahwa Al-Quran adalah obat (Syifa) dan Rahmat?",
                                options: [
                                    "QS. Al-Ikhlas: 1",
                                    "QS. Al-Isra': 82",
                                    "QS. An-Naba': 1",
                                    "QS. Yasin: 1"
                                ],
                                correct: 1,
                                explanation: "QS. Al-Isra' ayat 82: 'Dan Kami turunkan dari Alquran suatu yang menjadi penawar dan rahmat bagi orang-orang yang beriman'."
                            },
                            {
                                question: "Al-Quran disebut sebagai 'Tibyanan likulli syai'', artinya...",
                                options: [
                                    "Penjelas segala sesuatu",
                                    "Cerita masa lalu",
                                    "Syair yang indah",
                                    "Harta karun"
                                ],
                                correct: 0,
                                explanation: "Tibyanan likulli syai' berarti penjelas bagi segala sesuatu (QS. An-Nahl: 89)."
                            }
                        ]
                    },
                    {
                        id: 69,
                        title: "Perintah Dan Etika Membaca Al-Quran",
                        file: "topic_69.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Adab dan Perintah Membaca Al-Quran</h3>
                                <p>Membaca Al-Quran adalah ibadah yang mulia, namun harus disertai dengan etika (adab) agar mendapatkan kesempurnaan pahala dan berkah.</p>
                                
                                <h4>1. Perintah Membaca</h4>
                                <p>Allah memerintahkan untuk membaca apa yang mudah dari Al-Quran dan membacanya dengan tartil (perlahan dan jelas). (QS. Al-Muzzammil: 4).</p>
                                
                                <h4>2. Membaca Ta'awwudz</h4>
                                <p>Disunnahkan membaca Ta'awwudz <i>(A'udzu billahi minasy syaithanir rajim)</i> sebelum memulai membaca Al-Quran untuk berlindung dari godaan setan. (QS. An-Nahl: 98).</p>
                                
                                <h4>3. Diam dan Menyimak</h4>
                                <p>Apabila Al-Quran dibacakan, maka dengarkanlah baik-baik dan perhatikanlah dengan tenang agar mendapat rahmat. (QS. Al-A'raaf: 204).</p>
                                
                                <h4>4. Khusyuk dan Menangis</h4>
                                <p>Dianjurkan untuk khusyuk, merenungi makna ayat, dan menangis (atau berusaha menangis) saat membaca atau mendengar ayat-ayat Allah. (QS. Al-Isra': 109).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Apabila kamu membaca Al Quran hendaklah kamu meminta perlindungan kepada Allah dari syaitan yang terkutuk." (QS. An-Nahl: 98)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa yang harus dilakukan sebelum memulai membaca Al-Quran menurut QS. An-Nahl ayat 98?",
                                options: [
                                    "Berwudhu saja",
                                    "Membaca Ta'awwudz (Istigadzah)",
                                    "Membaca doa makan",
                                    "Langsung membaca surat"
                                ],
                                correct: 1,
                                explanation: "Perintah untuk meminta perlindungan kepada Allah (membaca Ta'awwudz) dari setan yang terkutuk saat hendak membaca Al-Quran."
                            },
                            {
                                question: "Sikap apa yang diperintahkan saat Al-Quran dibacakan menurut QS. Al-A'raaf ayat 204?",
                                options: [
                                    "Berbicara sendiri",
                                    "Mendengarkan dan diam",
                                    "Tidur",
                                    "Meninggalkan tempat"
                                ],
                                correct: 1,
                                explanation: "Apabila dibacakan Alquran, maka dengarkanlah baik-baik, dan perhatikanlah dengan tenang (diam) agar kamu mendapat rahmat."
                            },
                            {
                                question: "Membaca Al-Quran dengan pelan, jelas, dan sesuai tajwid disebut...",
                                options: [
                                    "Tergesa-gesa",
                                    "Tartil",
                                    "Senandung",
                                    "Cepat"
                                ],
                                correct: 1,
                                explanation: "Membaca dengan tartil artinya membaca dengan perlahan-lahan, jelas makhraj dan tajwidnya."
                            },
                            {
                                question: "Apa ciri orang yang diberi ilmu saat mendengar Al-Quran menurut QS. Al-Isra' ayat 107-109?",
                                options: [
                                    "Tertawa terbahak-bahak",
                                    "Marah-marah",
                                    "Menyungkur sujud dan menangis",
                                    "Biasa saja"
                                ],
                                correct: 2,
                                explanation: "Mereka menyungkur atas muka mereka sambil bersujud dan menangis, dan mereka bertambah khusyu'."
                            },
                            {
                                question: "Mengapa kita diperintahkan diam saat Al-Quran dibacakan?",
                                options: [
                                    "Agar penyanyi bisa konsentrasi",
                                    "Agar mendapat rahmat Allah",
                                    "Agar suasana sepi",
                                    "Karena aturan panitia"
                                ],
                                correct: 1,
                                explanation: "...dengarkanlah baik-baik, dan perhatikanlah dengan tenang agar kamu mendapat rahmat. (QS. Al-A'raaf: 204)."
                            }
                        ]
                    },
                    {
                        id: 70,
                        title: "Perintah Memahami Dan Mengamalkan Al-Quran",
                        file: "topic_70.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Kewajiban Tadabbur dan Mengamalkan</h3>
                                <p>Tidak cukup hanya membaca, seorang muslim wajib berusaha memahami (tadabbur) dan mengamalkan isi Al-Quran dalam kehidupan sehari-hari.</p>
                                
                                <h4>1. Perintah Tadabbur</h4>
                                <p>Allah mencela orang yang tidak mentadabburi Al-Quran. "Maka tidakkah mereka memperhatikan (mentadabburi) Al-Quran?..." (QS. An-Nisaa: 82).</p>
                                
                                <h4>2. Perintah Mengikuti dan Mengamalkan</h4>
                                <p>Al-Quran adalah kitab yang diberkati, maka ikutilah ia dan bertakwalah agar diberi rahmat. (QS. Al-An'aam: 155).</p>
                                
                                <h4>3. Ancaman Berpaling</h4>
                                <p>Barangsiapa berpaling dari Al-Quran dan peringatan Allah, ia akan memikul beban dosa yang besar di hari kiamat dan kehidupannya akan sempit. (QS. Thaahaa: 100).</p>
                                
                                <h4>4. Larangan Mempermainkan Ayat</h4>
                                <p>Dilarang keras menjadikan ayat-ayat Allah sebagai bahan olok-olokan atau senda gurau. Hal ini bisa membatalkan keimanan (kekafiran setelah iman). (QS. At-Taubah: 65-66).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Maka tidakkah mereka menghayati (mendalami/mentadabburi) Al Quran?..." (QS. An-Nisaa: 82)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa maksud perintah 'Tadabbur' Al-Quran?",
                                options: [
                                    "Menghafal cepat",
                                    "Memajang di lemari",
                                    "Memperhatikan, menghayati, dan memikirkan maknanya",
                                    "Mencari kesalahan"
                                ],
                                correct: 2,
                                explanation: "Tadabbur artinya memikirkan, merenungkan, dan menghayati makna ayat-ayat Al-Quran untuk diamalkan."
                            },
                            {
                                question: "Apa konsekuensi bagi orang yang berpaling dari Al-Quran di hari kiamat (QS. Thaahaa: 100)?",
                                options: [
                                    "Akan memikul dosa yang besar",
                                    "Akan menjadi kaya",
                                    "Tidak ada konsekuensi",
                                    "Akan mendapat syafaat"
                                ],
                                correct: 0,
                                explanation: "Barangsiapa berpaling dari Alquran, maka sesungguhnya ia akan memikul dosa yang besar di hari kiamat."
                            },
                            {
                                question: "Bagaimana hukum mengolok-olok atau mempermainkan ayat Allah (QS. At-Taubah: 65-66)?",
                                options: [
                                    "Boleh sebagai hiburan",
                                    "Makruh",
                                    "Dosa sangat besar, bahkan bisa kafir",
                                    "Sunnah"
                                ],
                                correct: 2,
                                explanation: "Mengolok-olok Allah, Rasul-Nya, dan ayat-ayat-Nya adalah kekafiran yang nyata setelah beriman."
                            },
                            {
                                question: "Siapakah sasaran ayat 'Maka tidakkah mereka memperhatikan Al-Quran?' (QS. An-Nisaa: 82)?",
                                options: [
                                    "Hanya orang Arab",
                                    "Seluruh manusia (termasuk orang munafik/kafir)",
                                    "Malaikat",
                                    "Jin saja"
                                ],
                                correct: 1,
                                explanation: "Ayat ini pertanyaan retoris (istifham inkari) kepada mereka yang tidak mau merenungkan kebenaran Al-Quran."
                            },
                            {
                                question: "QS. Al-An'aam: 155 memerintahkan kita untuk mengikuti Al-Quran agar...",
                                options: [
                                    "Cepat kaya",
                                    "Terkenal",
                                    "Diberi rahmat",
                                    "Ditakuti orang"
                                ],
                                correct: 2,
                                explanation: "...maka ikutilah ia dan bertakwalah agar kamu diberi rahmat."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject3",
                title: "Beriman Kepada Rasul",
                topics: [
                    {
                        id: 71,
                        title: "Kewajiban Beriman Kepada Para Rasul",
                        file: "topic_71.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Perintah dan Kewajiban Beriman</h3>
                                <p>Beriman kepada para Rasul adalah rukun iman keempat yang wajib diyakini oleh setiap muslim. Mengingkari salah satu rasul sama dengan mengingkari seluruhnya.</p>
                                
                                <h4>1. Perintah Beriman</h4>
                                <p>Allah memerintahkan manusia untuk beriman kepada Rasul (Muhammad) yang membawa kebenaran. "Wahai manusia, sesungguhnya telah datang Rasul (Muhammad) itu kepadamu dengan (membawa) kebenaran dari Tuhanmu, maka berimanlah kamu..." (QS. An-Nisaa': 170).</p>
                                
                                <h4>2. Keutamaan Beriman</h4>
                                <p>Orang yang beriman kepada Allah dan Rasul-Nya disebut sebagai <i>Shiddiqien</i> (orang-orang yang amat teguh kepercayaannya) dan akan mendapatkan pahala serta cahaya di sisi Tuhan mereka. (QS. Al-Hadiid: 19).</p>
                                
                                <h4>3. Tidak Membeda-bedakan Rasul</h4>
                                <p>Seorang mukmin wajib mengimani seluruh nabi dan rasul yang diutus Allah tanpa membeda-bedakan antara satu dengan yang lain. (QS. Al-Baqarah: 136).</p>
                                
                                <h4>4. Ancaman Bagi yang Mendustakan</h4>
                                <p>Mendustakan rasul adalah kekafiran yang nyata. Umat-umat terdahulu seperti kaum Nuh, 'Aad, Tsamud, dan Fir'aun dibinasakan karena mendustakan rasul mereka. (QS. An-Nisaa: 41-42, Al-Ankabut: 18).</p>
                                
                                <h4>5. Kewajiban Taat</h4>
                                <p>Ketaatan kepada Rasul adalah mutlak karena barangsiapa menaati Rasul, sesungguhnya ia telah menaati Allah. (QS. An-Nisaa: 80).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Barangsiapa yang mentaati Rasul itu, sesungguhnya ia telah mentaati Allah..." (QS. An-Nisaa: 80)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa sebutan bagi orang yang beriman kepada Allah dan Rasul-Nya menurut QS. Al-Hadiid: 19?",
                                options: [
                                    "Muslimin",
                                    "Shiddiqien (Orang-orang yang benar/jujur)",
                                    "Muhsinin",
                                    "Muttaqin"
                                ],
                                correct: 1,
                                explanation: "Orang-orang yang beriman kepada Allah dan Rasul-Nya, mereka itulah orang-orang Shiddiqien."
                            },
                            {
                                question: "Bagaimana sikap seorang mukmin terhadap seluruh rasul Allah (QS. Al-Baqarah: 136)?",
                                options: [
                                    "Hanya mengimani Nabi Muhammad saja",
                                    "Membeda-bedakan satu dengan yang lain",
                                    "Tidak membeda-bedakan seorangpun di antara mereka",
                                    "Hanya mengimani Nabi Musa dan Isa"
                                ],
                                correct: 2,
                                explanation: "Kami tidak membeda-bedakan seorangpun di antara mereka dan kami hanya tunduk patuh kepada-Nya."
                            },
                            {
                                question: "Barangsiapa menaati Rasul, maka sesungguhnya ia telah menaati... (QS. An-Nisaa: 80)",
                                options: [
                                    "Malaikat",
                                    "Pemimpin",
                                    "Allah",
                                    "Orang tua"
                                ],
                                correct: 2,
                                explanation: "Siapa yang menaati Rasul itu, sesungguhnya ia telah menaati Allah."
                            },
                            {
                                question: "Apa hukuman bagi umat terdahulu (Nuh, 'Aad, Tsamud) yang mendustakan rasul?",
                                options: [
                                    "Diberi harta melimpah",
                                    "Dibiarkan saja",
                                    "Dibinasakan/Diazab",
                                    "Diberi umur panjang"
                                ],
                                correct: 2,
                                explanation: "Mereka dibinasakan dengan berbagai azab (seperti angin, petir, banjir) karena mendustakan rasul-rasul."
                            },
                            {
                                question: "QS. An-Nisaa ayat 150-151 menyebutkan bahwa orang yang membedakan antara Allah dan Rasul-Nya adalah...",
                                options: [
                                    "Orang beriman",
                                    "Orang kafir dengan sebenar-benarnya",
                                    "Orang munafik",
                                    "Orang fasik"
                                ],
                                correct: 1,
                                explanation: "Merekalah orang-orang yang kafir dengan sebenar-benarnya (Haqqan)."
                            }
                        ]
                    },
                    {
                        id: 72,
                        title: "Hikmah Diturunkannya Para Rasul",
                        file: "topic_72.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Tujuan dan Hikmah Pengutusan Rasul</h3>
                                <p>Allah mengutus para rasul dengan membawa misi dan tujuan mulia bagi umat manusia.</p>
                                
                                <h4>1. Pembawa Kabar Gembira dan Peringatan</h4>
                                <p>Para rasul diutus sebagai <i>Mubasysyirin</i> (pemberi kabar gembira) bagi yang taat dan <i>Mundzirin</i> (pemberi peringatan) bagi yang ingkar, agar tidak ada alasan bagi manusia untuk membantah Allah di hari kiamat. (QS. An-Nisaa': 165).</p>
                                
                                <h4>2. Memberi Keputusan dan Petunjuk</h4>
                                <p>Rasul membawa kitab yang benar untuk memberi keputusan di antara manusia tentang perkara yang mereka perselisihkan. (QS. Al-Baqarah: 213).</p>
                                
                                <h4>3. Membacakan Ayat dan Menyucikan Jiwa</h4>
                                <p>Tugas rasul adalah membacakan ayat-ayat Allah, menyucikan jiwa manusia dari syirik dan penyakit hati, serta mengajarkan Al-Kitab dan Al-Hikmah. (QS. Ali 'Imraan: 164).</p>
                                
                                <h4>4. Menegakkan Tauhid</h4>
                                <p>Inti dakwah seluruh rasul adalah menyeru manusia untuk menyembah Allah semata (Tauhid) dan menjauhi Thaghut (sesembahan selain Allah). (QS. An-Nahl: 36).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Dan sungguhnya Kami telah mengutus rasul pada tiap-tiap umat (untuk menyerukan): 'Sembahlah Allah (saja), dan jauhilah Thaghut itu'..." (QS. An-Nahl: 36)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa tujuan utama diutusnya rasul menurut QS. An-Nisaa' ayat 165?",
                                options: [
                                    "Untuk menjadi raja dunia",
                                    "Agar manusia tidak punya alasan (hujjah) membantah Allah",
                                    "Mengumpulkan harta",
                                    "Membuat kerusakan"
                                ],
                                correct: 1,
                                explanation: "...agar supaya tidak ada alasan bagi manusia membantah Allah sesudah diutusnya rasul-rasul itu."
                            },
                            {
                                question: "Inti dakwah setiap rasul pada setiap umat adalah (QS. An-Nahl: 36)...",
                                options: [
                                    "Sembahlah Allah dan jauhilah Thaghut",
                                    "Perbaiki ekonomi",
                                    "Kuasai teknologi",
                                    "Perluas wilayah"
                                ],
                                correct: 0,
                                explanation: "Dan sungguhnya Kami telah mengutus rasul pada tiap-tiap umat (untuk menyerukan): 'Sembahlah Allah (saja), dan jauhilah Thaghut itu'."
                            },
                            {
                                question: "Apa arti <i>Mubasysyirin</i> dan <i>Mundzirin</i>?",
                                options: [
                                    "Pembawa untung dan rugi",
                                    "Pembawa kabar gembira dan pemberi peringatan",
                                    "Penguasa dan rakyat",
                                    "Guru dan murid"
                                ],
                                correct: 1,
                                explanation: "Mubasysyirin (pembawa kabar gembira) dan Mundzirin (pemberi peringatan)."
                            },
                            {
                                question: "Menurut QS. Ali 'Imraan: 164, apa saja tugas Rasul?",
                                options: [
                                    "Membacakan ayat, menyucikan jiwa, mengajarkan kitab & hikmah",
                                    "Meminta upah, mencari kekayaan, membangun istana",
                                    "Berperang saja",
                                    "Berdebat saja"
                                ],
                                correct: 0,
                                explanation: "Tugas rasul: membacakan ayat-ayat Allah, membersihkan (jiwa) mereka, dan mengajarkan kepada mereka Alkitab dan hikmah."
                            },
                            {
                                question: "Jika tidak ada rasul, manusia seringkali...",
                                options: [
                                    "Rukun dan damai",
                                    "Berselisih tentang kebenaran",
                                    "Langsung masuk surga",
                                    "Tidak butuh makan"
                                ],
                                correct: 1,
                                explanation: "Manusia adalah umat yang satu. (Setelah timbul perselisihan), maka Allah mengutus para nabi... untuk memberi keputusan... tentang perkara yang mereka perselisihkan. (QS. Al-Baqarah: 213)."
                            }
                        ]
                    },
                    {
                        id: 73,
                        title: "Allah Mengambil Janji Para Rasul",
                        file: "topic_73.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Perjanjian Agung Para Nabi</h3>
                                <p>Allah SWT telah mengambil perjanjian yang teguh (Mitsaqan Ghalizha) dari para Nabi dan Rasul.</p>
                                
                                <h4>1. Janji Saling Membenarkan</h4>
                                <p>Allah mengambil perjanjian dari para nabi bahwa jika datang rasul setelah mereka yang membenarkan apa yang ada pada mereka (yaitu Nabi Muhammad SAW), mereka wajib beriman dan menolongnya. Perjanjian ini juga mengikat umat mereka. (QS. Ali 'Imraan: 81).</p>
                                
                                <h4>2. Janji Menyampaikan Risalah</h4>
                                <p>Allah mengambil perjanjian yang teguh dari Nuh, Ibrahim, Musa, dan Isa binti Maryam untuk menyampaikan agama kepada umat masing-masing. (QS. Al-Ahzaab: 7).</p>
                                
                                <h4>3. Tanggung Jawab di Akhirat</h4>
                                <p>Kelak di hari kiamat, Allah akan menanyakan kepada para rasul tentang kebenaran penyampaian mereka dan bagaimana sambutan umat mereka. (QS. Al-Ahzaab: 8).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Dan (ingatlah) ketika Kami mengambil perjanjian dari nabi-nabi dan dari kamu (sendiri) dari Nuh, Ibrahim, Musa dan Isa putra Maryam, dan Kami telah mengambil dari mereka perjanjian yang teguh." (QS. Al-Ahzaab: 7)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Kepada siapakah Allah mengambil 'Janji yang Teguh' (Mitsaqan Ghalizha) menurut QS. Al-Ahzaab: 7?",
                                options: [
                                    "Orang-orang Munafik",
                                    "Para Nabi (termasuk Nuh, Ibrahim, Musa, Isa)",
                                    "Para Malaikat",
                                    "Jin dan Manusia"
                                ],
                                correct: 1,
                                explanation: "Allah mengambil perjanjian dari nabi-nabi dan dari kamu (Muhammad), dari Nuh, Ibrahim, Musa, dan Isa putra Maryam."
                            },
                            {
                                question: "Apa isi perjanjian para nabi dalam QS. Ali 'Imraan: 81 terkait Rasul yang datang belakangan (Nabi Muhammad)?",
                                options: [
                                    "Untuk memeranginya",
                                    "Untuk mengabaikannya",
                                    "Wajib beriman kepadanya dan menolongnya",
                                    "Tidak perlu peduli"
                                ],
                                correct: 2,
                                explanation: "...niscaya kamu akan sungguh-sungguh beriman kepadanya dan menolongnya."
                            },
                            {
                                question: "Apa tujuan Allah mengambil perjanjian dari para nabi menurut QS. Al-Ahzaab: 8?",
                                options: [
                                    "Agar Dia menanyakan orang-orang benar tentang kebenaran mereka",
                                    "Agar mereka menjadi kaya",
                                    "Agar mereka menjadi malaikat",
                                    "Hanya formalitas"
                                ],
                                correct: 0,
                                explanation: "Agar Dia menanyakan kepada orang-orang yang benar tentang kebenaran mereka."
                            },
                            {
                                question: "Siapa saja rasul 'Ulul Azmi' yang disebut namanya secara khusus dalam ayat perjanjian (QS. Al-Ahzaab: 7)?",
                                options: [
                                    "Adam, Idris, Nuh, Hud",
                                    "Muhammad, Nuh, Ibrahim, Musa, Isa",
                                    "Yusuf, Yunus, Yahya, Ya'qub",
                                    "Daud, Sulaiman, Ilyas, Ilyasa"
                                ],
                                correct: 1,
                                explanation: "Ayat tersebut menyebutkan: Kamu (Muhammad), Nuh, Ibrahim, Musa, dan Isa putra Maryam."
                            },
                            {
                                question: "Apa istilah 'Mitsaqan Ghalizha' artinya?",
                                options: [
                                    "Janji yang ringan",
                                    "Perjanjian yang teguh/berat",
                                    "Sumpah palsu",
                                    "Kontrak kerja"
                                ],
                                correct: 1,
                                explanation: "Mitsaqan Ghalizha artinya perjanjian yang teguh atau perjanjian yang berat."
                            }
                        ]
                    },
                    {
                        id: 74,
                        title: "Keistimewaan Para Rasul",
                        file: "topic_74.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Anugerah dan Keistimewaan Rasul</h3>
                                <p>Allah memberikan berbagai keistimewaan kepada para rasul sebagai bukti kebenaran risalah mereka.</p>
                                
                                <h4>1. Menerima Wahyu</h4>
                                <p>Allah menurunkan wahyu kepada para rasul melalui perantaraan malaikat (Jibril), di belakang tabir, atau melalui utusan. (QS. Asy-Syuuraa: 51).</p>
                                
                                <h4>2. Diperkuat dengan Mukjizat</h4>
                                <p>Setiap rasul diperkuat dengan mukjizat yang sesuai dengan zamannya sebagai bukti kebenaran di hadapan kaumnya. Namun, mukjizat hanya terjadi dengan izin Allah. (QS. Al-Mu'min: 78).</p>
                                
                                <h4>3. Allah Menjadi Saksi</h4>
                                <p>Cukuplah Allah menjadi saksi atas kebenaran para rasul-Nya. (QS. Al-Israa': 96).</p>
                                
                                <h4>4. Dilindungi Allah</h4>
                                <p>Allah senantiasa melindungi para rasul-Nya dan memasukkan mereka ke dalam rahmat-Nya, sebagaimana kisah Ismail, Idris, dan Dzulkifli yang sabar. (QS. Al-Anbiyaa: 85-86).</p>
                                
                                <h4>5. Ulul 'Azmi</h4>
                                <p>Di antara para rasul, terdapat <i>Ulul 'Azmi</i>, yaitu rasul-rasul yang memiliki keteguhan hati dan kesabaran yang luar biasa dalam berdakwah. Mereka adalah Nuh, Ibrahim, Musa, Isa, dan Muhammad SAW. (QS. Al-Ahqaaf: 35).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Dan sesungguhnya telah Kami utus beberapa orang rasul sebelum kamu, di antara mereka ada yang Kami ceritakan kepadamu dan di antara mereka ada (pula) yang tidak Kami ceritakan kepadamu..." (QS. Al-Mu'min: 78)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Siapa sajakah 5 Rasul yang bergelar 'Ulul Azmi'?",
                                options: [
                                    "Adam, Idris, Nuh, Hud, Shaleh",
                                    "Nuh, Ibrahim, Musa, Isa, Muhammad",
                                    "Yusuf, Yunus, Yahya, Zakaria, Isa",
                                    "Daud, Sulaiman, Ilyas, Ilyasa, Ayyub"
                                ],
                                correct: 1,
                                explanation: "Ulul Azmi adalah Nuh, Ibrahim, Musa, Isa, dan Muhammad SAW."
                            },
                            {
                                question: "Apakah semua kisah rasul diceritakan dalam Al-Quran (QS. Al-Mu'min: 78)?",
                                options: [
                                    "Ya, semua diceritakan",
                                    "Tidak ada yang diceritakan",
                                    "Ada yang diceritakan dan ada yang tidak",
                                    "Hanya kisah Nabi Musa yang diceritakan"
                                ],
                                correct: 2,
                                explanation: "...di antara mereka ada yang Kami ceritakan kepadamu dan di antara mereka ada (pula) yang tidak Kami ceritakan kepadamu."
                            },
                            {
                                question: "Bagaimana cara Allah menurunkan wahyu menurut QS. Asy-Syuuraa: 51?",
                                options: [
                                    "Bertemu langsung seperti manusia",
                                    "Melalui wahyu, di belakang tabir, atau mengutus utusan (malaikat)",
                                    "Melalui mimpi saja",
                                    "Melalui surat"
                                ],
                                correct: 1,
                                explanation: "Wahyu turun melalui perantaraan wahyu (ilham), atau di belakang tabir, atau dengan mengutus seorang utusan (malaikat)."
                            },
                            {
                                question: "Apa fungsi mukjizat bagi para rasul?",
                                options: [
                                    "Untuk pamer kekuatan",
                                    "Untuk menakuti manusia",
                                    "Sebagai bukti kebenaran risalah atas izin Allah",
                                    "Untuk mencari uang"
                                ],
                                correct: 2,
                                explanation: "Mukjizat diberikan sebagai bukti kebenaran dan keterangan yang nyata (bayyinat) atas izin Allah."
                            },
                            {
                                question: "Apa arti <i>Ulul 'Azmi</i>?",
                                options: [
                                    "Orang yang memiliki harta banyak",
                                    "Orang yang memiliki keteguhan hati dan kesabaran luar biasa",
                                    "Orang yang paling tua",
                                    "Orang yang paling kuat fisiknya"
                                ],
                                correct: 1,
                                explanation: "Ulul 'Azmi artinya orang-orang yang memiliki keteguhan hati yang kuat (Al-Ahqaaf: 35)."
                            }
                        ]
                    },
                    {
                        id: 75,
                        title: "Para Rasul Sebagai Manusia",
                        file: "topic_75.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Sifat Kemanusiaan Para Rasul</h3>
                                <p>Meskipun memiliki keistimewaan, para rasul tetaplah manusia biasa yang memiliki sifat-sifat kemanusiaan (Basyariyah).</p>
                                
                                <h4>1. Memakan Makanan dan Berjalan di Pasar</h4>
                                <p>Para rasul juga memakan makanan dan berjalan-jalan di pasar seperti manusia lainnya. Mereka bukan malaikat. (QS. Al-Furqan: 20).</p>
                                
                                <h4>2. Laki-laki Pilihan</h4>
                                <p>Rasul yang diutus Allah semuanya adalah laki-laki (Rijal) yang diberi wahyu, bukan wanita dan bukan malaikat. (QS. Al-Anbiyaa': 7).</p>
                                
                                <h4>3. Memiliki Keluarga dan Keturunan</h4>
                                <p>Sebagian besar rasul memiliki istri dan keturunan. Allah memuliakan keluarga Imran, keluarga Ibrahim, dan keturunan Nuh. (QS. Ali 'Imraan: 33-34, Al-Hadiid: 26).</p>
                                
                                <h4>4. Tingkat Keutamaan</h4>
                                <p>Allah melebihkan sebagian rasul atas sebagian yang lain dalam hal derajat dan keistimewaan (seperti Musa yang diajak bicara langsung, Isa dengan Ruhul Qudus). (QS. Al-Baqarah: 253).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Dan Kami tidak mengutus rasul-rasul sebelummu, melainkan mereka sungguh memakan makanan dan berjalan di pasar-pasar..." (QS. Al-Furqan: 20)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Apakah para rasul itu malaikat?",
                                options: [
                                    "Ya, mereka malaikat",
                                    "Sebagian malaikat sebagian manusia",
                                    "Tidak, mereka adalah manusia laki-laki yang diberi wahyu",
                                    "Mereka adalah jin"
                                ],
                                correct: 2,
                                explanation: "Kami tidak mengutus rasul sebelummu, kecuali beberapa laki-laki yang Kami beri wahyu kepada mereka (QS. Al-Anbiyaa': 7)."
                            },
                            {
                                question: "Apa sifat kemanusiaan rasul yang disebutkan dalam QS. Al-Furqan: 20?",
                                options: [
                                    "Tidak pernah tidur",
                                    "Memakan makanan dan berjalan di pasar",
                                    "Bisa terbang",
                                    "Hidup abadi"
                                ],
                                correct: 1,
                                explanation: "...melainkan mereka sungguh memakan makanan dan berjalan di pasar-pasar."
                            },
                            {
                                question: "Siapakah keluarga yang disebutkan telah dipilih Allah melebihi segala umat dalam QS. Ali 'Imraan: 33?",
                                options: [
                                    "Keluarga Fir'aun",
                                    "Keluarga Adam, Nuh, Ibrahim, dan Imran",
                                    "Keluarga Qarun",
                                    "Keluarga Abu Lahab"
                                ],
                                correct: 1,
                                explanation: "Sesungguhnya Allah telah memilih Adam, Nuh, keluarga Ibrahim, dan keluarga Imran melebihi segala umat."
                            },
                            {
                                question: "Apa keistimewaan Nabi Musa AS yang disebut dalam QS. Al-Baqarah: 253?",
                                options: [
                                    "Bisa menghidupkan orang mati",
                                    "Allah berbicara langsung dengannya (Kalimullah)",
                                    "Memiliki kerajaan besar",
                                    "Sangat kaya raya"
                                ],
                                correct: 1,
                                explanation: "Di antara mereka ada yang Allah berkata-kata (langsung dengan dia)... (merujuk pada Nabi Musa)."
                            },
                            {
                                question: "Apa maksudnya para rasul itu 'tidak kekal' (QS. Al-Anbiyaa': 8)?",
                                options: [
                                    "Mereka akan hidup selamanya di dunia",
                                    "Mereka juga akan wafat seperti manusia biasa",
                                    "Mereka bisa hidup kembali",
                                    "Mereka tidak punya tubuh"
                                ],
                                correct: 1,
                                explanation: "...dan tidak (pula) mereka itu orang-orang yang kekal (hidup selamanya di dunia)."
                            }
                        ]
                    },
                    {
                        id: 76,
                        title: "Sikap Manusia Terhadap Para Rasul",
                        file: "topic_76.pdf",
                        content: `
                            <div class="topic-content">
                                <h3>Respon Umat Terhadap Dakwah Rasul</h3>
                                <p>Sejarah mencatat berbagai sikap manusia terhadap para rasul yang diutus kepada mereka, yang seringkali penuh dengan penolakan.</p>
                                
                                <h4>1. Ejekan dan Tuduhan</h4>
                                <p>Hampir setiap rasul dituduh sebagai tukang sihir atau orang gila oleh kaumnya yang ingkar. (QS. Adz-Dzaariyaat: 52).</p>
                                
                                <h4>2. Kesombongan Kaum Mewah</h4>
                                <p>Kaum yang hidup mewah (Mutrafin) biasanya menjadi penentang utama para rasul karena merasa harta dan anak-anak mereka lebih banyak. (QS. Saba': 34-35).</p>
                                
                                <h4>3. Membunuh Para Nabi</h4>
                                <p>Bani Israil dikenal sering mendustakan bahkan membunuh para nabi yang tidak sesuai dengan hawa nafsu mereka. (QS. Al-Maidah: 70).</p>
                                
                                <h4>4. Permusuhan dari Syaitan</h4>
                                <p>Allah menjadikan musuh bagi setiap nabi, yaitu syaitan dari jenis manusia dan jin yang saling membisikkan perkataan indah untuk menipu. (QS. Al-An'aam: 112).</p>
                                
                                <h4>5. Bahasa Kaumnya</h4>
                                <p>Setiap rasul diutus dengan bahasa kaumnya agar dapat memberi penjelasan dengan terang. (QS. Ibraahiim: 4).</p>
                                
                                <div class="verse-box">
                                    
                                    <p class="translation">"Kami tidak mengutus seorang rasulpun, melainkan dengan bahasa kaumnya, supaya ia dapat memberi penjelasan dengan terang kepada mereka..." (QS. Ibraahiim: 4)</p>
                                </div>
                            </div>
                        `,
                        quiz: [
                            {
                                question: "Mengapa Allah mengutus rasul dengan bahasa kaumnya (QS. Ibraahiim: 4)?",
                                options: [
                                    "Agar terlihat keren",
                                    "Supaya dapat memberi penjelasan dengan terang/jelas",
                                    "Karena rasul tidak bisa bahasa lain",
                                    "Agar kaumnya bingung"
                                ],
                                correct: 1,
                                explanation: "...supaya ia dapat memberi penjelasan dengan terang kepada mereka."
                            },
                            {
                                question: "Tuduhan apa yang paling sering dilontarkan kaum terdahulu kepada rasul mereka (QS. Adz-Dzaariyaat: 52)?",
                                options: [
                                    "Orang kaya dan dermawan",
                                    "Raja yang adil",
                                    "Tukang sihir atau orang gila",
                                    "Pedagang yang jujur"
                                ],
                                correct: 2,
                                explanation: "...melainkan mereka mengatakan: 'Dia adalah seorang tukang sihir atau seorang gila'."
                            },
                            {
                                question: "Siapakah 'mutrafin' yang sering menentang dakwah rasul (QS. Saba': 34)?",
                                options: [
                                    "Orang-orang miskin",
                                    "Orang-orang yang hidup mewah",
                                    "Para budak",
                                    "Anak-anak yatim"
                                ],
                                correct: 1,
                                explanation: "...melainkan orang-orang yang hidup mewah di negeri itu berkata: 'Sesungguhnya Kami mengingkari...'."
                            },
                            {
                                question: "Apa kejahatan besar yang dilakukan Bani Israil terhadap para nabi (QS. Al-Maidah: 70)?",
                                options: [
                                    "Selalu menaati mereka",
                                    "Mendustakan dan membunuh nabi",
                                    "Memberi hadiah",
                                    "Membangunkan rumah"
                                ],
                                correct: 1,
                                explanation: "...sebagian dari rasul-rasul itu mereka dustakan dan sebagian yang lain mereka bunuh."
                            },
                            {
                                question: "Siapakah musuh para nabi yang disebutkan dalam QS. Al-An'aam: 112?",
                                options: [
                                    "Binatang buas",
                                    "Setan-setan dari jenis manusia dan jin",
                                    "Orang asing",
                                    "Tetangga sendiri"
                                ],
                                correct: 1,
                                explanation: "Dan demikianlah Kami jadikan bagi tiap-tiap nabi itu musuh, yaitu setan-setan (dari jenis) manusia dan (dan jenis) jin..."
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        id: "theme-4",
        title: "Tema 4: Taqdir dan Hari Akhir",
        description: "Pembahasan tentang beriman kepada Qadha dan Qadar serta Hari Kiamat",
        subjects: [
            {
                id: "subject-1",
                title: "Pokok Bahasan 1: Taqdir",
                topics: [
                    {
                        id: 77,
                        title: "Lauh Al Mahfuzh",
                        file: "topic_77.pdf",
                        content: `
            <h2>Lauh Al Mahfuzh</h2>
            <div class="content-section">
                <p>Materi ini membahas tentang Lauh Al Mahfuzh, tempat dimana segala takdir dan ketentuan Allah tercatat. Segala sesuatu yang terjadi di alam semesta ini, baik yang kecil maupun besar, telah tertulis di dalamnya sebelum kejadiannya.</p>
                <hr class="divider">
                
            <h3>1.1.1 Segala Sesuatu Telah Tercatat di Lauh Al Mahfuzh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Apakah kamu tidak mengetahui bahwa sesungguhnya Allah mengetahui apa saja yang ada di langit dan di bumi? Bahwasanya yang demikian itu terdapat dalam sebuah kitab (Lauh Mahfuzh). Sesungguhnya yang demikian itu amat mudah bagi Allah.</p>
                    <span class="source">Surat Al Hajj Ayat: 70</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Tiada sesuatupun yang ghaib di langit dan bumi, melainkan (terdapat) dalam kitab yang nyata (Lauhul Mahfuzh).</p>
                    <span class="source">Surat An Naml Ayat: 75</span>
                </div>

                <h3>1.1.2 Yang Ada di Langit dan Bumi Tercatat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tidaklah binatang-binatang yang ada di bumi... melainkan umat (juga) seperti kamu. Tidaklah Kami alpakan sesuatupun dalam Alkitab (Lauh Mahfuzh).</p>
                    <span class="source">Surat Al An'aam Ayat: 38</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami menghidupkan orang-orang mati dan Kami menuliskan apa yang telah mereka kerjakan dan bekas-bekas yang mereka tinggalkan. Dan segala sesuatu Kami kumpulkan dalam Kitab Induk yang nyata (Lauh Mahfuzh).</p>
                    <span class="source">Surat Yaasiin Ayat: 12</span>
                </div>

                <h3>1.1.3 Seluruh Keadaan Makhluk Tercatat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kamu tidak berada dalam suatu keadaan... melainkan Kami menjadi saksi atasmu... Tidak luput dari pengetahuan Tuhanmu biarpun sebesar zarrah... melainkan (semua tercatat) dalam kitab yang nyata.</p>
                    <span class="source">Surat Yunus Ayat: 61</span>
                </div>

                <h3>1.1.4 Allah Telah Menetapkan atas Diri-Nya Kasih Sayang</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tuhanmu telah menetapkan atas Diri-Nya kasih sayang. (Yaitu) bahwasanya siapa yang berbuat kejahatan di antara kamu lantaran kejahilan, lalu ia bertobat... maka sesungguhnya Allah Maha Pengampun lagi Maha Penyayang.</p>
                    <span class="source">Surat Al An'aam Ayat: 54</span>
                </div>

                <h3>1.1.5 Alquran Terjaga di Lauh Al Mahfuzh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Haa Miim. Demi Kitab (Alquran) yang menerangkan. Sesungguhnya Kami menjadikan Alquran dalam bahasa Arab supaya kamu memahami(nya). Dan sesungguhnya Alquran itu dalam Induk Alkitab (Lauh Mahfuzh) di sisi Kami, adalah benar-benar tinggi (nilainya) dan sangat banyak mengandung hikmah.</p>
                    <span class="source">Surat Az Zukhruf Ayat: 1-4</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apakah yang dimaksud dengan Lauh Mahfuzh?",
                                options: ["Kitab catatan amal manusia", "Kitab tempat segala takdir tercatat", "Kitab Taurat", "Kitab Injil"],
                                correct: 1,
                                explanation: "Lauh Mahfuzh adalah kitab induk tempat segala ketentuan takdir Allah tercatat sebelum kejadiannya."
                            },
                            {
                                question: "Apakah ada sesuatu yang luput dari catatan Allah (Yunus 61)?",
                                options: ["Ada yang kecil", "Hanya yang besar", "Tidak ada, bahkan sebesar dzarrah pun tercatat", "Hanya masa lalu"],
                                correct: 2,
                                explanation: "Tidak luput dari pengetahuan Tuhanmu biarpun sebesar zarrah (atom)... melainkan (semua tercatat) dalam kitab yang nyata."
                            },
                            {
                                question: "Apa yang telah ditetapkan Allah atas Diri-Nya (Al An'aam 54)?",
                                options: ["Murka", "Kasih Sayang (Rahmat)", "Keadilan", "Pembalasan"],
                                correct: 1,
                                explanation: "Tuhanmu telah menetapkan atas Diri-Nya kasih sayang."
                            },
                            {
                                question: "Bagaimana kedudukan Alquran di sisi Allah (Az Zukhruf 4)?",
                                options: ["Biasa saja", "Rendah", "Benar-benar tinggi (nilainya) dan penuh hikmah", "Terlupakan"],
                                correct: 2,
                                explanation: "Dan sesungguhnya Alquran itu dalam Induk Alkitab (Lauh Mahfuzh) di sisi Kami, adalah benar-benar tinggi (nilainya)."
                            },
                            {
                                question: "Apakah binatang-binatang juga disebut umat seperti manusia (Al An'aam 38)?",
                                options: ["Tidak", "Ya, melainkan umat (juga) seperti kamu", "Hanya sebagian", "Tidak disebutkan"],
                                correct: 1,
                                explanation: "...melainkan umat (juga) seperti kamu."
                            }
                        ]
                    },
                    {
                        id: 78,
                        title: "Hakikat Takdir",
                        file: "topic_78.pdf",
                        content: `
            <h2>Hakikat Takdir</h2>
            <div class="content-section">
                <p>Takdir adalah ketentuan Allah yang pasti berlaku bagi setiap makhluk-Nya. Manusia wajib beriman kepada Qadha dan Qadar, menerima segala ketetapan-Nya baik yang menyenangkan maupun yang menyedihkan.</p>
                <hr class="divider">
                
            <h3>1.2.1 Hakikat Kebenaran Takdir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya Kami menciptakan segala sesuatu dengan ukuran.</p>
                    <span class="source">Surat Al Qamar Ayat: 49</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Demi matahari dan cahayanya... Maka Allah mengilhamkan kepada jiwa itu (jalan) kefasikan dan ketakwaannya.</p>
                    <span class="source">Surat Asy Syams Ayat: 1-10</span>
                </div>

                <h3>1.2.2 Takdir Sebelum Penciptaan (Tercatat)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tidak ada suatu negeripun... melainkan Kami membinasakannya sebelum hari kiamat... Yang demikian itu telah tertulis di dalam kitab (Lauh Mahfuzh).</p>
                    <span class="source">Surat Al Israa' Ayat: 58</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Tiada suatu bencanapun... melainkan telah tertulis dalam kitab (Lauhul Mahfuzh) sebelum Kami menciptakannya.</p>
                    <span class="source">Surat Al Hadid Ayat: 22</span>
                </div>

                <h3>1.2.3 Segala Sesuatu Diciptakan dengan Sistem (Kadar)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Dan segala sesuatu pada sisi-Nya ada ukurannya.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 8</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tidak ada sesuatupun melainkan pada sisi Kami khazanahnya; dan Kami tidak menurunkannya melainkan dengan ukuran tertentu.</p>
                    <span class="source">Surat Al Hijr Ayat: 21</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan yang menentukan kadar (masing-masing) dan memberi petunjuk.</p>
                    <span class="source">Surat Al A'laa Ayat: 3</span>
                </div>

                <h3>1.2.4 Segala Sesuatu Berjalan Sesuai Ketetapan Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dia menyingsingkan pagi dan menjadikan malam untuk beristirahat, dan (menjadikan) matahari dan bulan untuk perhitungan. Itulah ketentuan Allah Yang Maha Perkasa.</p>
                    <span class="source">Surat Al An'aam Ayat: 96</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Sekali-kali tidak akan menimpa kami melainkan apa yang telah ditetapkan Allah untuk kami..."</p>
                    <span class="source">Surat At Taubah Ayat: 51</span>
                </div>

                <h3>1.2.5 Alam Semesta Berjalan Sesuai Takdir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan kamu tidak mampu (menempuhnya), kecuali bila Allah kehendaki. Sesungguhnya Allah Maha Mengetahui lagi Maha Bijaksana.</p>
                    <span class="source">Surat Al Insaan Ayat: 30</span>
                </div>

                <h3>1.2.6 Ketentuan (Takdir) Baik dan Buruk Telah Ditentukan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apabila Allah menghendaki keburukan terhadap sesuatu kaum, maka tidak ada yang dapat menolaknya.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 11</span>
                </div>

                <h3>1.2.7 Ketentuan (Takdir) Allah Tidak Dapat Dihindari</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan demikianlah telah pasti ketetapan azab Tuhanmu terhadap orang-orang kafir, karena sesungguhnya mereka penghuni neraka.</p>
                    <span class="source">Surat Al Mu'min Ayat: 6</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">...dan tetaplah atas mereka keputusan azab pada umat-umat yang terdahulu sebelum mereka...</p>
                    <span class="source">Surat Fushshilat Ayat: 25</span>
                </div>

                <h3>1.2.8 Segala Ketentuan Pasti Berlaku</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Di mana saja kamu berada, kematian akan mendapatimu...</p>
                    <span class="source">Surat An Nisaa' Ayat: 78</span>
                </div>

                <h3>1.2.9 Cara Menyikapi Takdir</h3>
                <p>Orang beriman harus menerima takdir dengan sabar (saat musibah) dan syukur (saat nikmat), serta tidak sombong atau putus asa. (QS Al Hadid 23). Apa saja nikmat yang kamu peroleh adalah dari Allah, dan apa saja bencana yang menimpamu, maka dari (kesalahan) dirimu sendiri. (QS An Nisaa 79).</p>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Bagaimanakah Allah menciptakan segala sesuatu (Al Qamar 49)?",
                                options: ["Secara acak", "Dengan ukuran (qadar)", "Tanpa rencana", "Dengan bantuan alam"],
                                correct: 1,
                                explanation: "Sesungguhnya Kami menciptakan segala sesuatu dengan ukuran."
                            },
                            {
                                question: "Apa yang harus dikatakan orang beriman tentang musibah (At Taubah 51)?",
                                options: ["Ini salah nasib", "Sekali-kali tidak akan menimpa kami melainkan ketetapan Allah", "Ini kejam", "Saya tidak terima"],
                                correct: 1,
                                explanation: "Katakanlah: 'Sekali-kali tidak akan menimpa kami melainkan apa yang telah ditetapkan Allah untuk kami'."
                            },
                            {
                                question: "Apakah musibah sudah tertulis sebelum kejadiannya (Al Hadid 22)?",
                                options: ["Ya, di Lauh Mahfuzh", "Tidak, Allah menulis saat kejadian", "Hanya musibah besar", "Tidak ada yang tahu"],
                                correct: 0,
                                explanation: "...melainkan telah tertulis dalam kitab (Lauhul Mahfuzh) sebelum Kami menciptakannya."
                            },
                            {
                                question: "Apa tujuan Allah memberitahu tentang takdir dalam Al Hadid 23?",
                                options: ["Agar sombong", "Supaya kamu jangan berduka cita terhadap apa yang luput dari kamu", "Agar malas", "Agar takut"],
                                correct: 1,
                                explanation: "Supaya kamu jangan berduka cita terhadap apa yang luput dari kamu."
                            },
                            {
                                question: "Dapatkah manusia menolak keburukan yang dikehendaki Allah (Ar Ra'd 11)?",
                                options: ["Bisa dengan teknologi", "Bisa dengan harta", "Tidak ada yang dapat menolaknya", "Bisa dengan lari"],
                                correct: 2,
                                explanation: "Dan apabila Allah menghendaki keburukan terhadap sesuatu kaum, maka tidak ada yang dapat menolaknya."
                            }
                        ]
                    },
                    {
                        id: 79,
                        title: "Ajal",
                        file: "topic_79.pdf",
                        content: `
            <h2>Ajal</h2>
            <div class="content-section">
                <p>Ajal adalah batas waktu kehidupan yang telah ditetapkan Allah bagi setiap makhluk. Materi ini membahas berbagai aspek tentang ajal, bahwa setiap umat dan individu memiliki batas waktu yang tidak dapat ditawar.</p>
                <hr class="divider">
                
            <h3>1.3.1 Segala Sesuatu Memiliki Ajal yang Ditentukan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesuatu yang bernyawa tidak akan mati melainkan dengan izin Allah, sebagai ketetapan yang telah ditentukan waktunya.</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 145</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Kami tiada membinasakan suatu negeripun, melainkan ada baginya ketentuan masa yang telah ditetapkan.</p>
                    <span class="source">Surat Al Hijr Ayat: 4</span>
                </div>

                <h3>1.3.2 Setiap Umat Memiliki Ajal</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tiap-tiap umat mempunyai batas waktu; maka apabila telah datang waktunya mereka tidak dapat mengundurkannya barang sesaatpun dan tidak dapat (pula) memajukannya.</p>
                    <span class="source">Surat Al A'raaf Ayat: 34</span>
                </div>

                <h3>1.3.3 Ajal Umat Tidak Dapat Dimajukan/Dimundurkan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Aku tidak berkuasa mendatangkan mudharat dan tidak (pula) manfaat kepada diriku... Tiap umat mempunyai ajal..."</p>
                    <span class="source">Surat Yunus Ayat: 49</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Tidaklah (dapat) suatu umatpun mendahului ajalnya, dan tidak (dapat pula) mereka terlambat (dari ajalnya itu).</p>
                    <span class="source">Surat Al Mu'minuun Ayat: 43</span>
                </div>

                <h3>1.3.4 Ajal Manusia Telah Ditentukan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Kemudian Dia membangkitkan (membangunkan) kamu pada siang hari untuk disempurnakan umur(mu) yang telah ditentukan...</p>
                    <span class="source">Surat Al An'aam Ayat: 60</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">...kemudian dilahirkannya kamu sebagai seorang anak... supaya kamu sampai kepada ajal yang ditentukan...</p>
                    <span class="source">Surat Al Mu'min Ayat: 67</span>
                </div>

                <h3>1.3.5 Ajal Manusia Tidak Dapat Dimajukan/Dimundurkan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Allah sekali-kali tidak akan menangguhkan (kematian) seseorang apabila telah datang ajalnya.</p>
                    <span class="source">Surat Al Munaafiquun Ayat: 11</span>
                </div>

                <h3>1.3.6 Ajal Dunia Tidak Dapat Dimajukan/Dimundurkan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Kami tidaklah mengundurkannya (hari Kiamat), melainkan sampai waktu yang tertentu.</p>
                    <span class="source">Surat Huud Ayat: 104</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Bagaimanakah ketentuan ajal bagi setiap umat?",
                                options: ["Dapat dimajukan dengan doa", "Dapat dimundurkan dengan sedekah", "Tidak dapat dimajukan atau dimundurkan sesaatpun", "Tergantung amal perbuatan"],
                                correct: 2,
                                explanation: "Apabila telah datang ajalnya, mereka tidak dapat mengundurkannya barang sesaatpun dan tidak dapat (pula) memajukannya."
                            },
                            {
                                question: "Apakah bisa seseorang mati tanpa izin Allah (Ali Imran 145)?",
                                options: ["Bisa karena kecelakaan", "Bisa karena sakit", "Tidak akan mati melainkan dengan izin Allah", "Bisa karena dibunuh"],
                                correct: 2,
                                explanation: "Sesuatu yang bernyawa tidak akan mati melainkan dengan izin Allah."
                            },
                            {
                                question: "Apakah Allah akan menangguhkan kematian seseorang jika ajalnya tiba (Al Munafiqun 11)?",
                                options: ["Ya, jika dia minta ampun", "Ya, jika dia bersedekah", "Allah sekali-kali tidak akan menangguhkan", "Tergantung kondisi"],
                                correct: 2,
                                explanation: "Dan Allah sekali-kali tidak akan menangguhkan (kematian) seseorang apabila telah datang ajalnya."
                            },
                            {
                                question: "Kapan ajal dunia (kiamat) akan terjadi (Huud 104)?",
                                options: ["Bisa dimundurkan", "Sampai waktu yang tertentu (Ma'dud)", "Tidak akan terjadi", "Tergantung manusia"],
                                correct: 1,
                                explanation: "Dan Kami tidaklah mengundurkannya, melainkan sampai waktu yang tertentu."
                            },
                            {
                                question: "Apa yang terjadi di siang hari menurut Al An'aam 60?",
                                options: ["Kita tidur", "Kita bekerja", "Disempurnakan umur yang telah ditentukan", "Kita bermain"],
                                correct: 2,
                                explanation: "...kemudian Dia membangunkan kamu pada siang hari untuk disempurnakan umur(mu) yang telah ditentukan."
                            }
                        ]
                    },
                    {
                        id: 80,
                        title: "Ruh dan Kematian",
                        file: "topic_80.pdf",
                        content: `
            <h2>Ruh dan Kematian</h2>
            <div class="content-section">
                <p>Materi ini membahas tentang hakikat ruh dan kematian sebagai ketetapan Allah yang pasti bagi setiap makhluk yang bernyawa.</p>
                <hr class="divider">
                
                <h3>1.4.1 Hakikat Ruh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka bertanya kepadamu tentang roh. Katakanlah: "Roh itu termasuk urusan Tuhanku, dan tidaklah kamu diberi pengetahuan melainkan sedikit".</p>
                    <span class="source">Surat Al Israa' Ayat: 85</span>
                </div>

                <h3>1.4.2 Ruh dalam Genggaman Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah memegang jiwa (orang) ketika matinya dan (memegang) jiwa (orang) yang belum mati di waktu tidurnya...</p>
                    <span class="source">Surat Az Zumar Ayat: 42</span>
                </div>

                <h3>1.4.3 Kematian Hanya dengan Izin Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesuatu yang bernyawa tidak akan mati melainkan dengan izin Allah, sebagai ketetapan yang telah ditentukan waktunya.</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 145</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Yang menjadikan mati dan hidup, supaya Dia menguji kamu, siapa di antara kamu yang lebih baik amalnya.</p>
                    <span class="source">Surat Al Mulk Ayat: 2</span>
                </div>

                <h3>1.4.4 Kematian sebagai Ujian dan Ancaman</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Sesungguhnya kematian yang kamu lari darinya, maka sesungguhnya kematian itu akan menemuimu..."</p>
                    <span class="source">Surat Al Jumu’ah Ayat: 8</span>
                </div>

                <h3>1.4.5 Setiap Makhluk Pasti Mati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Tiap yang berjiwa akan merasakan mati.</p>
                    <span class="source">Surat Al Anbiyaa Ayat: 35</span>
                </div>

                <h3>1.4.6 Sakaratul Maut</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan datanglah sakaratul maut dengan sebenar-benarnya. Itulah yang kamu selalu lari darinya.</p>
                    <span class="source">Surat Qaaf Ayat: 19</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Sekali-kali jangan. Apabila nafas (seseorang) telah (mendesak) sampai ke kerongkongan.</p>
                    <span class="source">Surat Al Qiyaamah Ayat: 26</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa hakikat ruh menurut QS Al Israa 85?",
                                options: ["Dapat dipelajari penuh oleh manusia", "Urusan Tuhanku, manusia diberi pengetahuan sedikit", "Merupakan energi listrik", "Berasal dari udara"],
                                correct: 1,
                                explanation: "Katakanlah: 'Roh itu termasuk urusan Tuhanku, dan tidaklah kamu diberi pengetahuan melainkan sedikit'."
                            },
                            {
                                question: "Kapan Allah memegang jiwa orang yang belum mati (Az Zumar 42)?",
                                options: ["Saat bekerja", "Saat makan", "Di waktu tidurnya", "Saat berjalan"],
                                correct: 2,
                                explanation: "Allah memegang jiwa... (orang) yang belum mati di waktu tidurnya."
                            },
                            {
                                question: "Apa tujuan Allah menjadikan mati dan hidup (Al Mulk 2)?",
                                options: ["Supaya Dia menguji kamu, siapa yang lebih baik amalnya", "Supaya manusia takut", "Supaya bumi tidak penuh", "Untuk kesimbangan alam"],
                                correct: 0,
                                explanation: "Yang menjadikan mati dan hidup, supaya Dia menguji kamu, siapa di antara kamu yang lebih baik amalnya."
                            },
                            {
                                question: "Apakah kematian bisa dihindari dengan lari darinya (Al Jumu'ah 8)?",
                                options: ["Bisa", "Tidak, kematian itu akan menemuimu", "Bisa jika bersembunyi di benteng", "Hanya orang kaya yang bisa"],
                                correct: 1,
                                explanation: "Sesungguhnya kematian yang kamu lari darinya, maka sesungguhnya kematian itu akan menemuimu."
                            },
                            {
                                question: "Apa yang terjadi saat sakaratul maut (Qaaf 19)?",
                                options: ["Datang dengan sebenar-benarnya", "Terasa nikmat", "Hanya mimpi", "Bisa ditunda"],
                                correct: 0,
                                explanation: "Dan datanglah sakaratul maut dengan sebenar-benarnya."
                            }
                        ]
                    },
                    {
                        id: 81,
                        title: "Kubur (Barzakh)",
                        file: "topic_81.pdf",
                        content: `
            <h2>Kubur (Barzakh)</h2>
            <div class="content-section">
                <p>Alam Barzakh atau alam kubur adalah alam pembatas antara dunia dan akhirat, tempat manusia menanti hari kebangkitan.</p>
                <hr class="divider">
                
                <h3>1.5.1 Kebenaran Adanya Alam Kubur</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan bahwasa Allah membangkitkan yang di dalam kubur.</p>
                    <span class="source">Surat Al Hajj Ayat: 7</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">...Dan di belakang mereka ada dinding (barzakh) sampai hari mereka dibangkitkan.</p>
                    <span class="source">Surat Al Mu'minuun Ayat: 99-100</span>
                </div>

                <h3>1.5.2 Putus Asa Orang Kafir di Kubur</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya mereka telah putus asa terhadap negeri akhirat sebagaimana orang-orang kafir yang telah berada dalam kubur berputus asa.</p>
                    <span class="source">Surat Al Mumtahanah Ayat: 13</span>
                </div>

                <h3>1.5.3 Siksa dan Nikmat Kubur</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kepada mereka dinampakkan neraka pada pagi dan petang...</p>
                    <span class="source">Surat Al Mu'min Ayat: 46</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">...(Malaikat berkata): "Salaamun 'alaikum (Salam sejahtera bagimu), masuklah kamu ke dalam surga..."</p>
                    <span class="source">Surat An Nahl Ayat: 32</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa yang dimaksud dengan Barzakh (Al Mu'minuun 100)?",
                                options: ["Dinding pembatas antara dunia dan akhirat", "Tempat rekreasi", "Lubang neraka saja", "Taman surga saja"],
                                correct: 0,
                                explanation: "Dan di belakang mereka ada dinding (barzakh) sampai hari mereka dibangkitkan."
                            },
                            {
                                question: "Apakah Allah akan membangkitkan orang yang di dalam kubur (Al Hajj 7)?",
                                options: ["Tidak", "Ya, pasti", "Hanya sebagian", "Ragu-ragu"],
                                correct: 1,
                                explanation: "Dan bahwasa Allah membangkitkan yang di dalam kubur."
                            },
                            {
                                question: "Bagaimana keadaan orang kafir di dalam kubur (Al Mumtahanah 13)?",
                                options: ["Berharap kembali", "Berputus asa", "Bahagia", "Tenang"],
                                correct: 1,
                                explanation: "...sebagaimana orang-orang kafir yang telah berada dalam kubur berputus asa."
                            },
                            {
                                question: "Apa yang ditampakkan kepada Firaun dan kaumnya pagi dan petang (Al Mu'min 46)?",
                                options: ["Surga", "Makanan lezat", "Neraka", "Kekayaan dunia"],
                                correct: 2,
                                explanation: "Kepada mereka dinampakkan neraka pada pagi dan petang."
                            },
                            {
                                question: "Siapakah yang menyambut orang beriman dengan 'Salaamun 'alaikum' saat wafat?",
                                options: ["Manusia", "Jin", "Para Malaikat", "Setan"],
                                correct: 2,
                                explanation: "Orang-orang yang diwafatkan dalam keadaan baik oleh para malaikat dengan berkata... Salaamun 'alaikum."
                            }
                        ]
                    }
                ]
            }
            ,
            {
                id: "subject-2",
                title: "Pokok Bahasan 2: Hari Kiamat",
                topics: [
                    {
                        id: 82,
                        title: "Kerendahan Dunia dan Keutamaan Akhirat",
                        file: "topic_82.pdf",
                        content: `
            <h2>Kerendahan Dunia dan Keutamaan Akhirat</h2>
            <div class="content-section">
                <p>Materi ini membahas perbandingan antara kehidupan dunia yang sementara dan kehidupan akhirat yang kekal. Dunia hanyalah tempat ujian dan permainan, sedangkan akhirat adalah tujuan akhir yang hakiki.</p>
                <hr class="divider">
                
                <h3>2.1.1 Akhirat Adalah Kehidupan Hakiki</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tidaklah kehidupan dunia ini melainkan senda gurau dan main-main. Dan sesungguhnya akhirat itulah yang sebenarnya kehidupan, kalau mereka mengetahui.</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 64</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dijadikan indah pada (pandangan) manusia kecintaan kepada apa yang diingini... Itulah kesenangan hidup di dunia, dan di sisi Allahlah tempat kembali yang baik (surga).</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 14</span>
                </div>

                <h3>2.1.2 Akhirat Adalah Kekal</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apa saja yang diberikan kepadamu, maka itulah kenikmatan hidup dunia... sedang apa yang di sisi Allah lebih baik dan lebih kekal.</p>
                    <span class="source">Surat Al Qashash Ayat: 60</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Sedang kehidupan akhirat adalah lebih baik dan lebih kekal.</p>
                    <span class="source">Surat Al A'laa Ayat: 17</span>
                </div>

                <h3>2.1.3 Kehidupan Dunia Kesenangan yang Memperdaya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Tidaklah kehidupan dunia kecuali kesenangan yang menipu.</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 185</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">...Sesungguhnya kehidupan dunia ini hanyalah permainan dan sesuatu yang melalaikan...</p>
                    <span class="source">Surat Al Hadiid Ayat: 20</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa hakekat kehidupan dunia menurut QS Al 'Ankabuut 64?",
                                options: ["Kehidupan yang abadi", "Tempat bersenang-senang selamanya", "Senda gurau dan main-main", "Tempat istirahat"],
                                correct: 2,
                                explanation: "Dan tidaklah kehidupan dunia ini melainkan senda gurau dan main-main."
                            },
                            {
                                question: "Manakah yang lebih baik dan kekal (Al A'laa 17)?",
                                options: ["Kehidupan dunia", "Harta yang banyak", "Kehidupan akhirat", "Jabatan tinggi"],
                                correct: 2,
                                explanation: "Sedang kehidupan akhirat adalah lebih baik dan lebih kekal."
                            },
                            {
                                question: "Disebut apakah kesenangan dunia dalam QS Ali 'Imraan 185?",
                                options: ["Kesenangan yang hakiki", "Kesenangan yang menipu (memperdaya)", "Kesenangan yang abadi", "Rezeki yang berkah"],
                                correct: 1,
                                explanation: "Tidaklah kehidupan dunia kecuali kesenangan yang menipu."
                            },
                            {
                                question: "Apa yang dijadikan indah pada pandangan manusia (Ali 'Imraan 14)?",
                                options: ["Iman dan takwa", "Kecintaan kepada syahwat (wanita, anak, harta)", "Amal saleh", "Ilmu pengetahuan"],
                                correct: 1,
                                explanation: "Dijadikan indah pada (pandangan) manusia kecintaan kepada apa yang diingini..."
                            },
                            {
                                question: "Bagaimana perumpamaan kehidupan dunia dalam Al Hadiid 20?",
                                options: ["Seperti hujan yang tanamannya mengagumkan lalu kering", "Seperti air yang mengalir terus", "Seperti gunung yang kokoh", "Seperti bintang yang bersinar"],
                                correct: 0,
                                explanation: "...seperti hujan yang tanam-tanamannya mengagumkan para petani; kemudian tanaman itu menjadi kering..."
                            }
                        ]
                    },
                    {
                        id: 83,
                        title: "Balasan Bagi Yang Beriman Kepada Hari Akhir",
                        file: "topic_83.pdf",
                        content: `
            <h2>Balasan Bagi Yang Beriman Kepada Hari Akhir</h2>
            <div class="content-section">
                <p>Materi ini menjelaskan janji Allah bagi mereka yang beriman kepada Allah dan Hari Akhir. Balasan berupa pahala yang besar, ketenangan hati, dan keberuntungan menanti mereka.</p>
                <hr class="divider">
                
                <h3>2.2.1 Tiada Rasa Khawatir dan Sedih Hati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Siapa di antara mereka yang benar-benar beriman kepada Allah, hari Akhir, dan beramal saleh, maka bagi mereka pahala dari Tuhan mereka, tidak ada kekhawatiran atas mereka, dan tidak (pula) mereka bersedih hati.</p>
                    <span class="source">Surat Al Baqarah Ayat: 62</span>
                </div>

                <h3>2.2.2 Mendapat Pahala dan Keberuntungan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan yang beriman kepada Allah dan hari Akhir. Orang-orang itulah yang akan Kami berikan kepada mereka pahala yang besar.</p>
                    <span class="source">Surat An Nisaa' Ayat: 162</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">...dan jika ada kebaikan sebesar zarrah, niscaya Allah akan melipatgandakannya dan memberikan dari sisi-Nya pahala yang besar.</p>
                    <span class="source">Surat An Nisaa' Ayat: 40</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa balasan bagi orang yang beriman kepada Allah dan Hari Akhir serta beramal saleh (Al Baqarah 62)?",
                                options: ["Kaya raya di dunia", "Tidak ada kekhawatiran dan tidak bersedih hati", "Menjadi pemimpin dunia", "Umur panjang"],
                                correct: 1,
                                explanation: "...maka bagi mereka pahala dari Tuhan mereka, tidak ada kekhawatiran atas mereka, dan tidak (pula) mereka bersedih hati."
                            },
                            {
                                question: "Siapa yang akan diberikan pahala yang besar menurut An Nisaa 162?",
                                options: ["Orang yang mendirikan shalat, menunaikan zakat, beriman kepada Allah dan Hari Akhir", "Orang yang hanya kaya", "Orang yang pandai bicara", "Orang yang mempunyai jabatan"],
                                correct: 0,
                                explanation: "...Orang-orang itulah yang akan Kami berikan kepada mereka pahala yang besar."
                            },
                            {
                                question: "Apakah Allah akan menyia-nyiakan amal kebaikan sekecil apapun (An Nisaa 40)?",
                                options: ["Ya, jika sedikit", "Tidak, Allah akan melipatgandakannya", "Mungkin", "Hanya amal besar yang dihitung"],
                                correct: 1,
                                explanation: "...dan jika ada kebaikan sebesar zarrah, niscaya Allah akan melipatgandakannya."
                            },
                            {
                                question: "Termasuk golongan manakah orang Yahudi dan Nasrani yang mendapat pahala di sisi-Nya (Al Baqarah 62)?",
                                options: ["Yang memusuhi Islam", "Yang benar-benar beriman kepada Allah, Hari Akhir dan beramal saleh", "Yang mengubah kitab suci", "Semua golongan"],
                                correct: 1,
                                explanation: "...siapa di antara mereka yang benar-benar beriman kepada Allah, hari Akhir, dan beramal saleh..."
                            },
                            {
                                question: "Apa arti 'Ajran 'Azhiima'?",
                                options: ["Siksa yang pedih", "Pahala yang besar", "Ampunan", "Rezeki yang sedikit"],
                                correct: 1,
                                explanation: "Ajran 'Azhiima artinya Pahala yang besar."
                            }
                        ]
                    },
                    {
                        id: 84,
                        title: "Ancaman Bagi Yang Kufur Terhadap Hari Akhir",
                        file: "topic_84.pdf",
                        content: `
            <h2>Ancaman Bagi Yang Kufur Terhadap Hari Akhir</h2>
            <div class="content-section">
                <p>Mereka yang mengingkari adanya Hari Akhir akan menghadapi azab yang pedih, penyesalan yang terlambat, dan kerugian yang nyata di akhirat kelak.</p>
                <hr class="divider">
                
                <h3>2.3.1 Mendapat Adzab di Dunia dan Kerugian di Akhirat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya orang-orang yang tidak beriman kepada negeri akhirat, Kami jadikan mereka memandang indah perbuatan-perbuatan mereka, maka mereka bergelimang (dalam kesesatan).</p>
                    <span class="source">Surat An Naml Ayat: 4</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">...Dan Kami sediakan neraka yang menyala-nyala bagi siapa yang mendustakan hari kiamat.</p>
                    <span class="source">Surat Al Furqaan Ayat: 11</span>
                </div>

                <h3>2.3.2 Akan Dibelenggu Lehernya dan Kekal dalam Neraka</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan orang-orang itulah (yang dilekatkan) belenggu di lehernya; mereka itulah penghuni neraka, mereka kekal di dalamnya.</p>
                    <span class="source">Surat Ar Ra'd Ayat: 5</span>
                </div>

                <h3>2.3.3 Kehancuran Umat Terdahulu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kaum Tsamud dan 'Aad telah mendustakan hari kiamat (Al Qaari'ah).</p>
                    <span class="source">Surat Al Haaqqah Ayat: 4</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">Adapun kaum Tsamud, maka mereka telah dibinasakan dengan kejadian yang luar biasa.</p>
                    <span class="source">Surat Al Haaqqah Ayat: 5</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa akibat bagi orang yang tidak beriman kepada akhirat (An Naml 4)?",
                                options: ["Hidup tenang", "Pandangan mereka dijadikan indah terhadap perbuatan buruknya (tersesat)", "Mendapat petunjuk", "Sukses dunia akhirat"],
                                correct: 1,
                                explanation: "...Kami jadikan mereka memandang indah perbuatan-perbuatan mereka, maka mereka bergelimang (dalam kesesatan)."
                            },
                            {
                                question: "Apa yang disediakan Allah bagi pendusta hari kiamat (Al Furqaan 11)?",
                                options: ["Surga Firdaus", "Neraka yang menyala-nyala (Sa'ir)", "Pengampunan", "Istana"],
                                correct: 1,
                                explanation: "Dan Kami sediakan neraka yang menyala-nyala bagi siapa yang mendustakan hari kiamat."
                            },
                            {
                                question: "Bagaimana nasib kaum 'Aad dan Tsamud (Al Haaqqah)?",
                                options: ["Selamat sentosa", "Dibinasakan karena mendustakan kiamat", "Diangkat derajatnya", "Diberi kekayaan"],
                                correct: 1,
                                explanation: "Kaum Tsamud dan 'Aad telah mendustakan hari kiamat... maka mereka telah dibinasakan."
                            },
                            {
                                question: "Apa yang akan dilekatkan di leher orang kafir (Ar Ra'd 5)?",
                                options: ["Kalung emas", "Belenggu (Aghlal)", "Bunga", "Sorban"],
                                correct: 1,
                                explanation: "...dan orang-orang itulah (yang dilekatkan) belenggu di lehernya."
                            },
                            {
                                question: "Apakah orang kafir kekal di neraka (Ar Ra'd 5)?",
                                options: ["Kekal di dalamnya", "Sebentar saja", "Akan keluar setelah dibersihkan", "Tidak masuk neraka"],
                                correct: 0,
                                explanation: "...mereka itulah penghuni neraka, mereka kekal di dalamnya."
                            }
                        ]
                    },
                    {
                        id: 85,
                        title: "Kebenaran Hari Akhir",
                        file: "topic_85.pdf",
                        content: `
            <h2>Kebenaran Hari Akhir</h2>
            <div class="content-section">
                <p>Hari Akhir adalah janji Allah yang pasti terjadi. Tidak ada yang mengetahui kapan terjadinya kecuali Allah, namun kedatangannya sangat dekat dan tiba-tiba.</p>
                <hr class="divider">
                
                <h3>2.4.1 Hari Akhir Pasti Terjadi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya apa yang dijanjikan kepadamu pasti datang, dan kamu sekali-kali tidak sanggup menolaknya.</p>
                    <span class="source">Surat Al An'aam Ayat: 134</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya azab Tuhanmu pasti terjadi.</p>
                    <span class="source">Surat Ath Thuur Ayat: 7</span>
                </div>

                <h3>2.4.2 Hanya Allah yang Mengetahui Waktunya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Katakanlah: "Sesungguhnya pengetahuan tentang kiamat itu adalah pada sisi Tuhanku; tidak seorangpun yang dapat menjelaskan waktu kedatangannya selain Dia...</p>
                    <span class="source">Surat Al A'raaf Ayat: 187</span>
                </div>

                <h3>2.4.3 Waktu Hari Akhir Telah Dekat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Tidaklah kejadian kiamat itu melainkan seperti sekejap mata atau lebih cepat (lagi)...</p>
                    <span class="source">Surat An Nahl Ayat: 77</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Telah dekat terjadinya hari kiamat.</p>
                    <span class="source">Surat An Najm Ayat: 57</span>
                </div>

                <h3>2.4.4 Datang dengan Tiba-tiba</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sebenarnya (azab) itu akan mendatangi mereka dengan sekonyong-konyong lalu membuat mereka menjadi panik, maka mereka tidak sanggup menolaknya...</p>
                    <span class="source">Surat Al Anbiyaa Ayat: 40</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Siapakah yang mengetahui waktu terjadinya kiamat (Al A'raaf 187)?",
                                options: ["Nabi Muhammad SAW", "Malaikat Jibril", "Hanya Allah SWT", "Para Ulama"],
                                correct: 2,
                                explanation: "...Sesungguhnya pengetahuan tentang kiamat itu adalah pada sisi Tuhanku..."
                            },
                            {
                                question: "Bagaimana kecepatan datangnya kiamat digambarkan dalam An Nahl 77?",
                                options: ["Seperti sekejap mata atau lebih cepat", "Seperti angin sepoi-sepoi", "Sangat lambat", "Bertahap selama 1000 tahun"],
                                correct: 0,
                                explanation: "...Tidaklah kejadian kiamat itu melainkan seperti sekejap mata atau lebih cepat (lagi)."
                            },
                            {
                                question: "Apakah manusia sanggup menolak kedatangan hari akhir (Al An'aam 134)?",
                                options: ["Sanggup dengan teknologi", "Sanggup dengan kekayaan", "Tidak sanggup menolaknya", "Bisa ditunda"],
                                correct: 2,
                                explanation: "...dan kamu sekali-kali tidak sanggup menolaknya."
                            },
                            {
                                question: "Bagaimana kedatangan azab kiamat menurut Al Anbiyaa 40?",
                                options: ["Dengan pemberitahuan dahulu", "Sekonyong-konyong (tiba-tiba) dan membuat panik", "Pelan-pelan", "Saat semua orang tidur"],
                                correct: 1,
                                explanation: "Sebenarnya (azab) itu akan mendatangi mereka dengan sekonyong-konyong lalu membuat mereka menjadi panik."
                            },
                            {
                                question: "Apa arti 'Azifatil aazifah' (An Najm 57)?",
                                options: ["Telah dekat terjadinya hari kiamat", "Telah jauh perjalanannya", "Telah datang pertolongan", "Telah selesai urusan"],
                                correct: 0,
                                explanation: "Telah dekat terjadinya hari kiamat."
                            }
                        ]
                    },
                    {
                        id: 86,
                        title: "Tanda-Tanda Datangnya Hari Akhir",
                        file: "topic_86.pdf",
                        content: `
            <h2>Tanda-Tanda Datangnya Hari Akhir</h2>
            <div class="content-section">
                <p>Sebelum Hari Kiamat tiba, akan muncul tanda-tanda besar sebagai peringatan bagi manusia, di antaranya munculnya Ya'juj dan Ma'juj serta binatang melata dari bumi.</p>
                <hr class="divider">
                
                <h3>2.5.1 Munculnya Ya'juj dan Ma'juj</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hingga apabila dibukakan (tembok) Ya'juj dan Ma'juj, dan mereka turun dengan cepat dari seluruh tempat yang tinggi.</p>
                    <span class="source">Surat Al Anbiyaa Ayat: 96</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan telah dekat kedatangan janji yang benar (hari berbangkit)...</p>
                    <span class="source">Surat Al Anbiyaa Ayat: 97</span>
                </div>

                <h3>2.5.2 Munculnya Binatang Melata (Daabbah)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Kami keluarkan sejenis binatang melata dari bumi yang akan mengatakan kepada mereka, bahwasanya manusia dahulu tidak yakin kepada ayat-ayat Kami.</p>
                    <span class="source">Surat An Naml Ayat: 82</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa yang dilakukan Ya'juj dan Ma'juj saat temboknya dibuka (Al Anbiyaa 96)?",
                                options: ["Diam saja", "Turun dengan cepat dari seluruh tempat yang tinggi", "Tidur kembali", "Membangun rumah"],
                                correct: 1,
                                explanation: "...dan mereka turun dengan cepat dari seluruh tempat yang tinggi."
                            },
                            {
                                question: "Apa yang dikatakan orang kafir saat janji yang benar (kiamat) datang (Al Anbiyaa 97)?",
                                options: ["Hore kiamat datang", "Aduhai celakalah kami, kami dalam kelalaian", "Mari kita berpesta", "Kami siap menghadapinya"],
                                correct: 1,
                                explanation: "...Aduhai, celakalah kami, sesungguhnya kami dalam kelalaian tentang ini..."
                            },
                            {
                                question: "Apa itu 'Daabbah' yang disebut dalam QS An Naml 82?",
                                options: ["Malaikat penjaga", "Sejenis binatang melata dari bumi", "Burung Ababil", "Angin kencang"],
                                correct: 1,
                                explanation: "...Kami keluarkan sejenis binatang melata dari bumi..."
                            },
                            {
                                question: "Apa yang dikatakan Daabbah kepada manusia?",
                                options: ["Manusia dahulu tidak yakin kepada ayat-ayat Kami", "Selamat datang di hari kiamat", "Semua dosa diampuni", "Silakan masuk surga"],
                                correct: 0,
                                explanation: "...binatang melata... yang akan mengatakan kepada mereka, bahwasanya manusia dahulu tidak yakin kepada ayat-ayat Kami."
                            }
                        ]
                    },
                    {
                        id: 87,
                        title: "Kedahsyatan Hari Akhir",
                        file: "topic_87.pdf",
                        content: `
            <h2>Kedahsyatan Hari Akhir</h2>
            <div class="content-section">
                <p>Hari Kiamat adalah peristiwa yang sangat dahsyat. Alam semesta akan hancur lebur, langit terbelah, gunung-gunung dihancurkan, dan bumi diguncangkan.</p>
                <hr class="divider">
                
                <h3>2.6.1 Langit Terbelah dan Hancur</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan (ingatlah) hari (ketika) langit pecah-belah mengeluarkan kabut putih...</p>
                    <span class="source">Surat Al Furqaan Ayat: 25</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Pada hari ketika langit menjadi seperti luluhan perak.</p>
                    <span class="source">Surat Al Ma'aarij Ayat: 8</span>
                </div>

                <h3>2.6.2 Matahari Digulung dan Bintang Berjatuhan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Apabila matahari digulung. Dan apabila bintang-bintang berjatuhan.</p>
                    <span class="source">Surat At Takwiir Ayat: 1-2</span>
                </div>

                <h3>2.6.3 Bumi Diguncangkan dengan Dahsyat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Apabila bumi digoncangkan dengan goncangan (yang dahsyat).</p>
                    <span class="source">Surat Al Zalzalah Ayat: 1</span>
                </div>

                <h3>2.6.4 Gunung-gunung Dihancurkan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan diangkatlah bumi dan gunung-gunung, lalu dibenturkan keduanya sekali bentur.</p>
                    <span class="source">Surat Al Haaqqah Ayat: 14</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">Dan gunung-gunung menjadi seperti bulu (yang berterbangan).</p>
                    <span class="source">Surat Al Ma'aarij Ayat: 9</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa yang terjadi pada matahari saat kiamat (At Takwiir 1)?",
                                options: ["Bersinar terang", "Digulung (kuwwirat)", "Menjadi dingin", "Menjadi dua"],
                                correct: 1,
                                explanation: "Apabila matahari digulung."
                            },
                            {
                                question: "Seperti apa kondisi langit menurut Al Ma'aarij 8?",
                                options: ["Seperti asap hitam", "Seperti luluhan perak (Al Muhl)", "Seperti kaca pecah", "Seperti air jernih"],
                                correct: 1,
                                explanation: "Pada hari ketika langit menjadi seperti luluhan perak."
                            },
                            {
                                question: "Apa yang terjadi pada bumi dan gunung menurut Al Haaqqah 14?",
                                options: ["Tetap kokoh", "Diangkat dan dibenturkan keduanya sekali bentur", "Tenggelam ke laut", "Melayang-layang"],
                                correct: 1,
                                explanation: "Dan diangkatlah bumi dan gunung-gunung, lalu dibenturkan keduanya sekali bentur."
                            },
                            {
                                question: "Bagaimana keadaan gunung-gunung menurut Al Ma'aarij 9?",
                                options: ["Seperti paku bumi", "Seperti bulu yang berterbangan", "Seperti batu karang", "Seperti debu"],
                                correct: 1,
                                explanation: "Dan gunung-gunung menjadi seperti bulu (yang berterbangan)."
                            },
                            {
                                question: "Apa yang dikeluarkan bumi saat diguncangkan (Al Zalzalah 2)?",
                                options: ["Air mancur", "Beban berat yang dikandungnya (mayat, harta)", "Minyak bumi", "Api abadi"],
                                correct: 1,
                                explanation: "Dan bumi telah mengeluarkan beban berat (yang dikandung)-nya."
                            }
                        ]
                    }
                    ,
                    {
                        id: 88,
                        title: "Keadaan Manusia Pada Hari Kiamat",
                        file: "topic_88.pdf",
                        content: `
            <h2>Keadaan Manusia Pada Hari Kiamat</h2>
            <div class="content-section">
                <p>Pada Hari Kiamat, manusia akan mengalami kepanikan yang luar biasa. Hubungan persaudaraan terputus, dan setiap orang hanya memikirkan keselamatan dirinya sendiri.</p>
                <hr class="divider">
                
                <h3>2.7.1 Goncangan yang Dahsyat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hai manusia, bertakwalah kepada Tuhanmu; sesungguhnya goncangan hari kiamat ialah sesuatu yang sangat besar (dahsyat).</p>
                    <span class="source">Surat Al Hajj Ayat: 1</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">...lalailah semua wanita yang menyusui anaknya dari anak yang disusuinya...</p>
                    <span class="source">Surat Al Hajj Ayat: 2</span>
                </div>

                <h3>2.7.2 Lari dari Saudara dan Keluarga</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Pada hari ketika manusia lari dari saudaranya, dari ibu dan bapaknya, dari istri dan anak-anaknya.</p>
                    <span class="source">Surat 'Abasa Ayat: 34-36</span>
                </div>

                <h3>2.7.3 Datang Sendiri-sendiri</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tiap-tiap mereka akan datang kepada Allah pada hari kiamat dengan sendiri-sendiri.</p>
                    <span class="source">Surat Maryam Ayat: 95</span>
                </div>

                <h3>2.7.4 Anak-anak Menjadi Beruban</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...hari yang menjadikan anak-anak beruban.</p>
                    <span class="source">Surat Al Muzzammil Ayat: 17</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa yang terjadi pada ibu menyusui saat kiamat (Al Hajj 2)?",
                                options: ["Melindungi anaknya", "Melalaikan/lupa pada anaknya", "Mencari anaknya", "Menangis"],
                                correct: 1,
                                explanation: "...lalailah semua wanita yang menyusui anaknya dari anak yang disusuinya..."
                            },
                            {
                                question: "Mengapa manusia lari dari keluarganya saat kiamat ('Abasa 34-37)?",
                                options: ["Karena benci", "Karena setiap orang punya urusan yang menyibukkan dirinya sendiri", "Karena tidak kenal", "Karena malu"],
                                correct: 1,
                                explanation: "Setiap orang dari mereka pada hari itu mempunyai urusan yang cukup menyibukkannya."
                            },
                            {
                                question: "Bagaimana kedatangan manusia menghadap Allah (Maryam 95)?",
                                options: ["Berkelompok", "Membawa harta", "Sendiri-sendiri (fardan)", "Bersama pemimpin"],
                                correct: 2,
                                explanation: "Dan tiap-tiap mereka akan datang kepada Allah pada hari kiamat dengan sendiri-sendiri."
                            },
                            {
                                question: "Apa efek dahsyatnya hari kiamat terhadap anak-anak (Al Muzzammil 17)?",
                                options: ["Menjadi dewasa instan", "Menjadi beruban (sangat tua/takut)", "Menjadi bayi kembali", "Bermain-main"],
                                correct: 1,
                                explanation: "...hari yang menjadikan anak-anak beruban."
                            },
                            {
                                question: "Siapa yang lari dari saudaranya, ibu, bapak, istri, dan anak ('Abasa)?",
                                options: ["Manusia (Al Mar'u)", "Malaikat", "Jin", "Hewan"],
                                correct: 0,
                                explanation: "Pada hari ketika manusia lari dari saudaranya..."
                            }
                        ]
                    },
                    {
                        id: 89,
                        title: "Hari Kebangkitan (Yaum Al Ba'ats)",
                        file: "topic_89.pdf",
                        content: `
            <h2>Hari Kebangkitan (Yaum Al Ba'ats)</h2>
            <div class="content-section">
                <p>Setelah alam semesta hancur dan semua makhluk mati, Allah akan membangkitkan kembali manusia dari kuburnya untuk mempertanggungjawabkan perbuatannya.</p>
                <hr class="divider">
                
                <h3>2.8.1 Tiupan Sangkakala Kedua</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Kemudian ditiup sangkakala sekali lagi maka tiba-tiba mereka berdiri menunggu (putusan masing-masing).</p>
                    <span class="source">Surat Az Zumar Ayat: 68</span>
                </div>

                <h3>2.8.2 Keluar dari Kubur</h3>
                <div class="quran-quote">
                    
                    <p class="translation">(Yaitu) pada hari mereka keluar dari kubur dengan cepat...</p>
                    <span class="source">Surat Al Ma'aarij Ayat: 43</span>
                </div>

                <h3>2.8.3 Penyesalan Orang Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka berkata: "Aduhai celakalah kami! siapa yang membangkitkan kami dari tempat tidur kami (kubur)?".</p>
                    <span class="source">Surat Yaasiin Ayat: 52</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">...Inilah yang dijanjikan (Tuhan) Yang Maha Pemurah dan benarlah rasul-rasul-(Nya).</p>
                    <span class="source">Surat Yaasiin Ayat: 52</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa yang terjadi setelah tiupan sangkakala kedua (Az Zumar 68)?",
                                options: ["Semua mati", "Semua hancur", "Manusia bangkit berdiri menunggu", "Langit terbelah"],
                                correct: 2,
                                explanation: "...maka tiba-tiba mereka berdiri menunggu (putusan masing-masing)."
                            },
                            {
                                question: "Apa yang dikatakan orang kafir saat dibangkitkan (Yaasiin 52)?",
                                options: ["Alhamdulillah", "Siapa yang membangkitkan kami dari tempat tidur kami?", "Kami siap masuk surga", "Di mana harta kami?"],
                                correct: 1,
                                explanation: "Mereka berkata: \"Aduhai celakalah kami! siapa yang membangkitkan kami dari tempat tidur kami (kubur)?\"."
                            },
                            {
                                question: "Bagaimana cara manusia keluar dari kubur (Al Ma'aarij 43)?",
                                options: ["Pelan-pelan", "Dengan cepat (siraa'an)", "Sambil tidur", "Digotong malaikat"],
                                correct: 1,
                                explanation: "(Yaitu) pada hari mereka keluar dari kubur dengan cepat..."
                            },
                            {
                                question: "Apa sebutan untuk hari dibangkitkannya manusia?",
                                options: ["Yaumul Ba'ats", "Yaumul Ied", "Yaumul Jumuah", "Yaumul Arafah"],
                                correct: 0,
                                explanation: "Hari Kebangkitan disebut Yaum Al Ba'ats."
                            },
                            {
                                question: "Siapa yang membenarkan janji Allah saat kebangkitan (Yaasiin 52)?",
                                options: ["Orang kafir", "Rasul-rasul (Al Mursalun)", "Jin", "Setan"],
                                correct: 1,
                                explanation: "...Inilah yang dijanjikan (Tuhan) Yang Maha Pemurah dan benarlah rasul-rasul-(Nya)."
                            }
                        ]
                    },
                    {
                        id: 90,
                        title: "Hari Penghimpunan (Mahsyar)",
                        file: "topic_90.pdf",
                        content: `
            <h2>Hari Penghimpunan (Mahsyar)</h2>
            <div class="content-section">
                <p>Setelah dibangkitkan, seluruh manusia dari zaman Nabi Adam hingga manusia terakhir akan dikumpulkan di Padang Mahsyar untuk menunggu pengadilan Allah.</p>
                <hr class="divider">
                
                <h3>2.9.1 Dikumpulkan Tanpa Terkecuali</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan Kami kumpulkan seluruh manusia, dan tidak Kami tinggalkan seorangpun dari mereka.</p>
                    <span class="source">Surat Al Kahf Ayat: 47</span>
                </div>

                <h3>2.9.2 Keadaan Wajah Manusia</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Banyak muka pada hari itu berseri-seri.</p>
                    <span class="source">Surat 'Abasa Ayat: 38</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">Dan banyak (pula) muka pada hari itu tertutup debu.</p>
                    <span class="source">Surat 'Abasa Ayat: 40</span>
                </div>

                <h3>2.9.3 Tidak Berguna Syafaat Kecuali Izin Allah</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Pada hari itu tidak berguna syafa'at, kecuali (syafa'at) orang yang Allah Maha Pemurah telah memberi izin kepadanya...</p>
                    <span class="source">Surat Thaahaa Ayat: 109</span>
                </div>

                <h3>2.9.4 Orang Buta di Mahsyar</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan Kami akan menghimpunkannya pada hari kiamat dalam keadaan buta.</p>
                    <span class="source">Surat Thaahaa Ayat: 124</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Siapa yang dikumpulkan Allah di Mahsyar (Al Kahf 47)?",
                                options: ["Orang beriman saja", "Orang kafir saja", "Seluruh manusia tanpa terkecuali", "Hanya para Nabi"],
                                correct: 2,
                                explanation: "...dan Kami kumpulkan seluruh manusia, dan tidak Kami tinggalkan seorangpun dari mereka."
                            },
                            {
                                question: "Bagaimana wajah orang beriman di Mahsyar ('Abasa 38-39)?",
                                options: ["Tertutup debu", "Hitam legam", "Berseri-seri, tertawa dan gembira", "Menangis"],
                                correct: 2,
                                explanation: "Banyak muka pada hari itu berseri-seri. Tertawa dan bergembira ria."
                            },
                            {
                                question: "Kenapa ada orang yang dibangkitkan dalam keadaan buta (Thaahaa 124)?",
                                options: ["Karena sakit mata", "Karena berpaling dari peringatan Allah (Al Quran)", "Karena terkena debu", "Karena tidur terus"],
                                correct: 1,
                                explanation: "Dan siapa berpaling dari peringatan-Ku, maka sesungguhnya baginya penghidupan yang sempit, dan Kami akan menghimpunkannya pada hari kiamat dalam keadaan buta."
                            },
                            {
                                question: "Apakah syafaat berguna di hari itu (Thaahaa 109)?",
                                options: ["Berguna bagi semua orang", "Tidak berguna sama sekali", "Tidak berguna kecuali siapa yang diizinkan Allah", "Bisa dibeli"],
                                correct: 2,
                                explanation: "Pada hari itu tidak berguna syafa'at, kecuali (syafa'at) orang yang Allah Maha Pemurah telah memberi izin kepadanya."
                            },
                            {
                                question: "Apa arti 'Mahsyar'?",
                                options: ["Tempat tidur", "Tempat berkumpul/penghimpunan", "Tempat makan", "Tempat bermain"],
                                correct: 1,
                                explanation: "Mahsyar atau Yaum Al Jam'i adalah Hari Penghimpunan."
                            }
                        ]
                    },
                    {
                        id: 91,
                        title: "Hari Penghitungan (Yaum Al Hisaab)",
                        file: "topic_91.pdf",
                        content: `
            <h2>Hari Penghitungan (Yaum Al Hisaab)</h2>
            <div class="content-section">
                <p>Pada hari ini, setiap manusia akan dimintai pertanggungjawaban atas segala perbuatannya di dunia, sekecil apapun itu. Tidak ada yang luput dari perhitungan Allah.</p>
                <hr class="divider">
                
                <h3>2.10.1 Seluruh Makhluk akan Ditanya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Dan sungguh kamu akan ditanya tentang apa yang telah kamu kerjakan.</p>
                    <span class="source">Surat An Nahl Ayat: 93</span>
                </div>

                <h3>2.10.2 Orang Musyrik dan Sesembahannya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan dikatakan kepada mereka: "Di manakah berhala-berhala yang dahulu kamu selalu sembah? Selain dari Allah?, dapatkah mereka menolong kamu atau menolong diri mereka sendiri?"</p>
                    <span class="source">Surat Asy Syu’araa’ Ayat: 92-93</span>
                </div>
                 <p>Pada hari itu hubungan terputus, dan berhala-berhala itu tidak dapat memberikan pertolongan.</p>

                <h3>2.10.3 Para Rasul pun Ditanya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka sesungguhnya Kami akan menanyai umat-umat yang telah diutus rasul-rasul kepada mereka dan sesungguhnya Kami akan menanyai (pula) rasul-rasul (Kami).</p>
                    <span class="source">Surat Al A'raaf Ayat: 6</span>
                </div>

                <h3>2.10.4 Pendengaran, Penglihatan, dan Hati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Sesungguhnya pendengaran, penglihatan dan hati, semuanya itu akan
diminta pertanggungjawabannya.</p>
                    <span class="source">Surat Al Israa’ Ayat: 36</span>
                </div>

                <h3>2.10.5 Anggota Tubuh Menjadi Saksi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Pada hari ini Kami tutup mulut mereka; dan berkatalah kepada Kami tangan mereka dan memberi kesaksianlah kaki mereka terhadap apa yang dahulu mereka usahakan.</p>
                    <span class="source">Surat Yaasiin Ayat: 65</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa yang akan terjadi pada pendengaran, penglihatan, dan hati (Al Israa 36)?",
                                options: ["Akan hilang", "Akan bertambah tajam", "Akan diminta pertanggungjawaban", "Akan menjadi saksi bisu"],
                                correct: 2,
                                explanation: "Sesungguhnya pendengaran, penglihatan dan hati, semuanya itu akan diminta pertanggungjawabannya."
                            },
                            {
                                question: "Siapa yang akan ditanya selain umat manusia (Al A'raaf 6)?",
                                options: ["Hanya Iblis", "Para Rasul (Al Mursalin)", "Hewan", "Tumbuhan"],
                                correct: 1,
                                explanation: "...dan sesungguhnya Kami akan menanyai (pula) rasul-rasul (Kami)."
                            },
                            {
                                question: "Bagaimana cara anggota tubuh bersaksi (Yaasiin 65)?",
                                options: ["Mulut berbicara", "Mulut dikunci, tangan berbicara, kaki bersaksi", "Semua anggota tubuh diam", "Hanya hati yang bicara"],
                                correct: 1,
                                explanation: "Pada hari ini Kami tutup mulut mereka; dan berkatalah kepada Kami tangan mereka dan memberi kesaksianlah kaki mereka..."
                            },
                            {
                                question: "Apa yang ditanyakan kepada bayi perempuan yang dikubur hidup-hidup (At Takwiir 8-9)?",
                                options: ["Siapa ibunya?", "Kenapa dia menangis?", "Karena dosa apakah ia dibunuh?", "Di mana mainannya?"],
                                correct: 2,
                                explanation: "Dan apabila bayi-bayi perempuan yang dikubur hidup-hidup ditanya, Karena dosa apakah ia dibunuh."
                            },
                            {
                                question: "Apakah berhala dapat menolong penyembahnya saat hisab?",
                                options: ["Ya, pasti", "Mungkin", "Tidak dapat menolong kamu atau diri mereka sendiri", "Bisa jika dibayar"],
                                correct: 2,
                                explanation: "...dapatkah mereka menolong kamu atau menolong diri mereka sendiri?"
                            }
                        ]
                    },
                    {
                        id: 92,
                        title: "Buku Catatan Amal",
                        file: "topic_92.pdf",
                        content: `
            <h2>Buku Catatan Amal</h2>
            <div class="content-section">
                <p>Setiap manusia akan menerima buku catatan amalnya sendiri yang mencatat segala perbuatan besar maupun kecil tanpa terlewat sedikitpun.</p>
                <hr class="divider">
                
                <h3>2.11.1 Catatan yang Detail</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...kitab apakah ini yang tidak meninggalkan yang kecil dan tidak (pula) yang besar, melainkan ia mencatat semuanya...</p>
                    <span class="source">Surat Al Kahf Ayat: 49</span>
                </div>

                <h3>2.11.2 Orang yang Menerima dari Kanan (Ashabul Yamin)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Adapun orang-orang yang diberikan kitabnya dari sebelah kanannya, maka ia berkata: "Ambillah, bacalah kitabku (ini)".</p>
                    <span class="source">Surat Al Haaqqah Ayat: 19</span>
                </div>
                <p>Mereka akan diperiksa dengan hisab yang mudah dan kembali ke kaumnya dengan gembira.</p>

                <h3>2.11.3 Orang yang Menerima dari Kiri/Belakang (Ashabul Syimal)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Adapun orang-orang yang diberikan kitabnya dari belakang, maka ia akan berteriak: "Celakalah aku".</p>
                    <span class="source">Surat Al Insyiqaaq Ayat: 10-11</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">Adapun orang yang diberikan kepadanya kitabnya dari sebelah kirinya...</p>
                    <span class="source">Surat Al Haaqqah Ayat: 25</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa reaksi orang yang menerima kitab dari kanan (Al Haaqqah 19)?",
                                options: ["Menyembunyikannya", "Menangis", "Bangga dan berkata 'Bacalah kitabku ini'", "Membuangnya"],
                                correct: 2,
                                explanation: "Maka ia berkata: \"Ambillah, bacalah kitabku (ini)\"."
                            },
                            {
                                question: "Apa isi buku catatan amal menurut Al Kahf 49?",
                                options: ["Hanya amal besar", "Hanya amal kecil", "Mencatat semuanya tanpa lewat yang kecil maupun besar", "Kosong"],
                                correct: 2,
                                explanation: "...kitab apakah ini yang tidak meninggalkan yang kecil dan tidak (pula) yang besar, melainkan ia mencatat semuanya..."
                            },
                            {
                                question: "Bagaimana cara orang celaka menerima kitabnya (Al Insyiqaaq 10)?",
                                options: ["Dari depan", "Dari atas", "Dari belakang punggungnya", "Dari langit"],
                                correct: 2,
                                explanation: "Adapun orang-orang yang diberikan kitabnya dari belakang..."
                            },
                            {
                                question: "Apa nama kitab catatan orang berbakti (Al Muthaffifiin 18)?",
                                options: ["Sijjin", "Illiyyin", "Lauhul Mahfudz", "Suhuf"],
                                correct: 1,
                                explanation: "Sesungguhnya kitab orang-orang yang berbakti itu (tersimpan) dalam 'Illiyyin."
                            },
                            {
                                question: "Apa nama kitab catatan orang durhaka (Al Muthaffifiin 7)?",
                                options: ["Sijjin", "Illiyyin", "Zabur", "Injil"],
                                correct: 0,
                                explanation: "Sekali-kali jangan curang, karena sesungguhnya kitab orang yang durhaka tersimpan dalam Sijjin."
                            }
                        ]
                    },
                    {
                        id: 93,
                        title: "Penimbangan Amal (Mizan)",
                        file: "topic_93.pdf",
                        content: `
            <h2>Penimbangan Amal (Mizan)</h2>
            <div class="content-section">
                <p>Setelah hisab, amal manusia akan ditimbang dengan Mizan (timbangan) yang sangat adil. Berat ringannya timbangan kebaikan akan menentukan nasib manusia.</p>
                <hr class="divider">
                
                <h3>2.12.1 Keadilan Timbangan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kami akan memasang timbangan yang tepat pada hari kiamat, maka tidaklah dirugikan seseorang sedikitpun...</p>
                    <span class="source">Surat Al Anbiyaa’ Ayat: 47</span>
                </div>

                <h3>2.12.2 Timbangan yang Berat (Muflihun)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Barangsiapa yang berat timbangan (kebaikan)nya, maka mereka itulah orang-orang yang dapat keberuntungan.</p>
                    <span class="source">Surat Al Mu’minuun Ayat: 102</span>
                </div>

                <h3>2.12.3 Timbangan yang Ringan (Khasirun)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan barangsiapa yang ringan timbangannya, maka mereka itulah orang-orang yang merugikan dirinya sendiri...</p>
                    <span class="source">Surat Al Mu’minuun Ayat: 103</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa tujuan adanya timbangan (Mizan) di hari kiamat?",
                                options: ["Untuk menghitung narta", "Untuk mengetahui berat badan", "Untuk menimbang amal dengan adil", "Untuk hiasan"],
                                correct: 2,
                                explanation: "Kami akan memasang timbangan yang tepat pada hari kiamat..."
                            },
                            {
                                question: "Siapakah orang yang beruntung (Al Muflihun) itu (Al A'raaf 8)?",
                                options: ["Yang banyak hartanya", "Yang berat timbangan kebaikannya", "Yang ringan timbangannya", "Yang punya jabatan"],
                                correct: 1,
                                explanation: "...maka siapa berat timbangan kebaikannya, maka mereka itulah orang-orang yang beruntung."
                            },
                            {
                                question: "Apa nasib orang yang ringan timbangan kebaikannya (Al Mu'minuun 103)?",
                                options: ["Masuk surga", "Merugikan dirinya sendiri / kekal di neraka", "Diberi kesempatan kedua", "Tidur nyenyak"],
                                correct: 1,
                                explanation: "Dan barangsiapa yang ringan timbangannya, maka mereka itulah orang-orang yang merugikan dirinya sendiri..."
                            },
                            {
                                question: "Apakah amal seberat biji sawi akan ditimbang (Al Anbiyaa 47)?",
                                options: ["Tidak, terlalu kecil", "Ya, pasti didatangkan (dibalas)", "Hanya yang besar saja", "Tergantung mood malaikat"],
                                correct: 1,
                                explanation: "Dan jika (amalan itu) hanya seberat biji sawipun pasti Kami mendatangkan (pahala)-nya."
                            },
                            {
                                question: "Apa arti 'Mizan'?",
                                options: ["Jembatan", "Timbangan", "Pintu", "Sungai"],
                                correct: 1,
                                explanation: "Mizan adalah Timbangan Amal."
                            }
                        ]
                    },
                    {
                        id: 94,
                        title: "2.13 Syafaat (Pertolongan)",
                        file: "topic_94.pdf",
                        content: `
            <h2>Syafaat (Pertolongan)</h2>
            <div class="content-section">
                <p><strong>Syafaat</strong> diperuntukkan bagi hamba Allah yang diridhai-Nya. Syafaat adalah pertolongan pada hari kiamat yang hanya milik Allah semata. Syafaat yang tidak diterima di sisi Allah adalah syafaat bagi orang-orang kafir.</p>
                <hr class="divider">
                
                <h3>2.13.1 Syafaat Hanya Milik Allah Semata</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Hanya milik Allah syafaat itu semuanya. Milik-Nya kerajaan langit dan bumi..."</p>
                    <span class="source">Surat Az Zumar Ayat: 44</span>
                </div>
                <p>Nabi Muhammad Saw. dan nabi-nabi yang lain dapat memberi syafaat sesudah diberi izin oleh Allah Swt.</p>

                <h3>2.13.2 Kepada Siapa Syafaat Diberikan?</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan mereka tiada memberi syafaat melainkan kepada orang yang diridhai Allah...</p>
                    <span class="source">Surat Al Anbiyaa’ Ayat: 28</span>
                </div>

                <h3>2.13.3 Penyesalan Orang Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...maka adakah bagi kami pemberi syafaat yang akan memberi syafaat bagi kami...</p>
                    <span class="source">Surat Al A'raaf Ayat: 53</span>
                </div>
                <p>Orang kafir menyesal karena berhala mereka tidak dapat menolong. Mereka berharap dikembalikan ke dunia untuk beramal saleh (Al A'raaf: 53).</p>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Syafaat hanya milik siapa (Az Zumar 44)?",
                                options: ["Para Malaikat", "Hanya milik Allah", "Para Nabi", "Raja-raja dunia"],
                                correct: 1,
                                explanation: "Katakanlah: 'Hanya milik Allah syafaat itu semuanya'."
                            },
                            {
                                question: "Siapakah yang bisa memberikan syafaat?",
                                options: ["Siapapun yang mau", "Orang yang diizinkan Allah", "Orang kaya", "Berhala"],
                                correct: 1,
                                explanation: "Dan tiadalah berguna syafaat di sisi Allah melainkan bagi orang yang telah diizinkan-Nya."
                            },
                            {
                                question: "Apakah orang kafir mendapatkan syafaat?",
                                options: ["Ya, dari berhala mereka", "Tidak sama sekali", "Sedikit", "Bisa beli syafaat"],
                                correct: 1,
                                explanation: "Syafaat yang tidak diterima di sisi Allah adalah syafaat bagi orang-orang kafir."
                            },
                            {
                                question: "Apa penyesalan orang kafir di hari kiamat?",
                                options: ["Kurang kaya", "Kurang terkenal", "Tidak beramal saleh dan menyembah selain Allah", "Kurang tidur"],
                                correct: 2,
                                explanation: "Mereka berkata: '...dapatkah kami dikembalikan (ke dunia) sehingga kami dapat beramal yang lain dari yang pernah kami amalkan?'"
                            },
                            {
                                question: "Apa syarat utama mendapat syafaat?",
                                options: ["Diridhai Allah (Iman/Tauhid)", "Punya banyak uang", "Keturunan bangsawan", "Terkenal"],
                                correct: 0,
                                explanation: "...melainkan kepada orang yang diridhai Allah."
                            }
                        ]
                    },
                    {
                        id: 95,
                        title: "2.14 Hari Keputusan (Yaum Al Fashl)",
                        file: "topic_95.pdf",
                        content: `
            <h2>Hari Keputusan (Yaum Al Fashl)</h2>
            <div class="content-section">
                <p><strong>Yaum Al Fashl</strong> adalah hari keputusan yang adil. Allah memberikan balasan tanpa menganiaya sedikitpun.</p>
                <hr class="divider">
                
                <h3>2.14.1 Keputusan yang Adil</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan diberi keputusan di antara mereka dengan adil, sedang mereka tidak dirugikan.</p>
                    <span class="source">Surat Az Zumar Ayat: 69</span>
                </div>

                <h3>2.14.2 Tanggung Jawab Pribadi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan orang yang berdosa tidak akan memikul dosa orang lain...</p>
                    <span class="source">Surat Faathir Ayat: 18</span>
                </div>

                <h3>2.14.3 Keadaan Orang Kafir</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka apabila bintang-bintang telah dihapuskan, Dan apabila langit telah dibelah...</p>
                    <span class="source">Surat Al Mursalaat Ayat: 8-9</span>
                </div>
                <p>Kecelakaan besar pada hari itu bagi para pendusta (Al Mursalaat: 15).</p>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa arti Yaum Al Fashl?",
                                options: ["Hari Kemenangan", "Hari Keputusan", "Hari Raya", "Hari Libur"],
                                correct: 1,
                                explanation: "Yaum Al Fashl artinya Hari Keputusan."
                            },
                            {
                                question: "Apakah Allah menganiaya hamba-Nya?",
                                options: ["Ya", "Tidak sedikitpun", "Kadang-kadang", "Hanya orang kafir"],
                                correct: 1,
                                explanation: "Sesungguhnya Allah tidak berbuat zalim kepada manusia sedikitpun."
                            },
                            {
                                question: "Siapakah yang menanggung dosa orang lain?",
                                options: ["Tidak ada", "Orang tua", "Teman", "Pemimpin"],
                                correct: 0,
                                explanation: "Dan orang yang berdosa tidak akan memikul dosa orang lain."
                            },
                            {
                                question: "Apa yang terjadi pada bintang-bintang saat Hari Keputusan (Al Mursalaat 8)?",
                                options: ["Bersinar terang", "Jatuh ke laut", "Dihapuskan/Redup", "Bertambah banyak"],
                                correct: 2,
                                explanation: "Maka apabila bintang-bintang telah dihapuskan."
                            },
                            {
                                question: "Balasan amal baik dilipatgandakan berapa kali (Al An'aam 160)?",
                                options: ["2 kali", "10 kali", "100 kali", "Tidak dilipatgandakan"],
                                correct: 1,
                                explanation: "pahala sepuluh kali lipat amalnya."
                            }
                        ]
                    },
                    {
                        id: 96,
                        title: "2.15 Hari Pembalasan (Yaum Al Diin)",
                        file: "topic_96.pdf",
                        content: `
            <h2>Hari Pembalasan (Yaum Al Diin)</h2>
            <div class="content-section">
                <p>Hari Pembalasan adalah hari penerimaan buku catatan amal dan penentuan tempat kembali: Surga atau Neraka.</p>
                <hr class="divider">
                
                <h3>2.15.1 Tiga Golongan Manusia (Al Waaqi'ah)</h3>
                <ul>
                    <li><strong>Golongan Kanan (Ashabul Yamin):</strong> Orang beriman, berada di antara pohon bidara dan air yang tercurah. Bahagia.</li>
                    <li><strong>Golongan Kiri (Ashabul Syimal):</strong> Orang kafir, berada dalam siksaan angin samum dan air panas. Sengsara.</li>
                    <li><strong>Al Saabiquun (Al Muqarrabuun):</strong> Orang-orang terdahulu yang didekatkan kepada Allah. Berada di surga kenikmatan.</li>
                </ul>

                <h3>2.15.2 Siksaan yang Pedih</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...bagi mereka azab dari jenis siksaan yang sangat pedih.</p>
                    <span class="source">Surat Saba' Ayat: 5</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Siapa itu Ashabul Yamin?",
                                options: ["Golongan Kiri", "Golongan Kanan (Ahli Surga)", "Golongan Tengah", "Golongan Munafik"],
                                correct: 1,
                                explanation: "Ashabul Yamin adalah Golongan Kanan."
                            },
                            {
                                question: "Apa siksaan Golongan Kiri (Al Waaqi'ah)?",
                                options: ["Angin Samum dan Air Hamim", "Hujan es", "Angin sepoi-sepoi", "Kelaparan"],
                                correct: 0,
                                explanation: "Dalam (siksaan) angin yang amat panas, dan air panas yang mendidih."
                            },
                            {
                                question: "Siapakah Al Saabiquun?",
                                options: ["Orang yang datang terlambat", "Orang yang paling dahulu beriman/didekatkan kepada Allah", "Orang yang lari", "Orang musyrik"],
                                correct: 1,
                                explanation: "Dan orang-orang yang beriman paling dahulu. Mereka itulah yang didekatkan kepada Allah."
                            },
                            {
                                question: "Apa arti Yaum Al Diin?",
                                options: ["Hari Agama", "Hari Pembalasan", "Hari Kiamat", "Hari Perhitungan"],
                                correct: 1,
                                explanation: "Yaum Al Diin atau Hari Pembalasan."
                            },
                            {
                                question: "Dimana tempat Ashabul Yamin?",
                                options: ["Neraka Jahim", "Surga (di antara pohon bidara)", "Padang Mahsyar", "Jembatan"],
                                correct: 1,
                                explanation: "Berada di antara pohon bidara yang tak berduri."
                            }
                        ]
                    },
                    {
                        id: 97,
                        title: "2.16 Surga (Jannah)",
                        file: "topic_97.pdf",
                        content: `
            <h2>Surga (Jannah)</h2>
            <div class="content-section">
                <p><strong>Surga</strong> adalah tempat kebahagiaan abadi bagi orang bertakwa. Penuh dengan kenikmatan yang belum pernah dilihat mata, didengar telinga, atau terlintas di hati.</p>
                <hr class="divider">
                
                <h3>2.16.1 Nama-Nama Surga</h3>
                <ul>
                    <li><strong>Jannat 'Adn:</strong> Surga tempat menetap yang kekal (Maryam 61).</li>
                    <li><strong>Darussalam:</strong> Negeri keselamatan/kedamaian (Al An'aam 127).</li>
                    <li><strong>Jannat Firdaus:</strong> Surga tertinggi (Al Kahf 107).</li>
                    <li><strong>Jannat Na'iim:</strong> Surga yang penuh nikmat (Luqmaan 8).</li>
                    <li><strong>Jannat Al Khuldi:</strong> Surga yang kekal (Al Furqaan 15).</li>
                </ul>

                <h3>2.16.2 Kenikmatan Surga</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...mengalir sungai-sungai di dalamnya; buahnya tak henti-henti sedang naungannya (demikian pula)...</p>
                    <span class="source">Surat Ar Ra'd Ayat: 35</span>
                </div>
                <p>Penghuni surga tidak merasa lelah, tidak mendengar perkataan sia-sia, dan kekal di dalamnya.</p>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa nama surga yang disebutkan sebagai tempat kedamaian/keselamatan?",
                                options: ["Darul Bawar", "Darussalam", "Darul Harb", "Darul Fana"],
                                correct: 1,
                                explanation: "Bagi mereka (disediakan) Darussalam (surga) pada sisi Tuhannya."
                            },
                            {
                                question: "Apa nama surga tertinggi (Al Kahf 107)?",
                                options: ["Adn", "Na'iim", "Firdaus", "Ma'wa"],
                                correct: 2,
                                explanation: "...bagi mereka adalah surga Firdaus menjadi tempat tinggal."
                            },
                            {
                                question: "Bagaimana buah-buahan di surga (Ar Ra'd 35)?",
                                options: ["Habis jika dimakan", "Tak henti-henti (Daim)", "Hanya ada di musim panas", "Pahit"],
                                correct: 1,
                                explanation: "...buahnya tak henti-henti..."
                            },
                            {
                                question: "Apakah ada kelelahan di surga?",
                                options: ["Sangat lelah", "Tidak ada rasa lelah dan lesu", "Sedikit capek", "Harus tidur siang"],
                                correct: 1,
                                explanation: "...di dalamnya kami tiada merasa lelah..."
                            },
                            {
                                question: "Jannat 'Adn artinya?",
                                options: ["Taman Sementara", "Taman Eden / Tempat Menetap", "Taman Bunga", "Taman Air"],
                                correct: 1,
                                explanation: "Yaitu surga 'Adn yang telah dijanjikan..."
                            }
                        ]
                    },
                    {
                        id: 98,
                        title: "2.17 Neraka",
                        file: "topic_98.pdf",
                        content: `
            <h2>Neraka</h2>
            <div class="content-section">
                <p><strong>Neraka</strong> adalah tempat kembali yang paling buruk bagi orang-orang kafir dan pendosa. Di dalamnya terdapat berbagai macam siksaan yang pedih dan menghinakan.</p>
                <hr class="divider">
                
                <h3>2.17.1 Keadaan dan Nama-Nama Neraka</h3>
                <p>Allah menyebutkan berbagai nama neraka yang menggambarkan sifat siksaannya:</p>
                <ul>
                    <li><strong>Jahanam:</strong> Tempat yang memiliki 7 pintu, tempat kembali orang sesat (Al Hijr 43-44).</li>
                    <li><strong>Jahim:</strong> Api yang menyala-nyala, tempat bagi pendusta (Al Waaqi'ah 94).</li>
                    <li><strong>Sa'ir:</strong> Api yang gejolaknya sangat dahsyat (Al Mulk 5).</li>
                    <li><strong>Saqar:</strong> Pembakar kulit manusia yang tidak meninggalkan sisa (Al Muddatstsir 26-29).</li>
                    <li><strong>Hawiyah:</strong> Api yang sangat panas (menganga) (Al Qaari'ah 9-11).</li>
                    <li><strong>Huthamah:</strong> Api yang membakar sampai ke hati (Al Humazah 4-7).</li>
                </ul>

                <h3>2.17.2 Makanan dan Minuman Penghuni Neraka</h3>
                <ul>
                    <li><strong>Pohon Zaqqum:</strong> Pohon yang keluar dari dasar neraka, mayangnya seperti kepala setan. Buahnya mendidih dalam perut seperti luluh lantak (Ash Shaaffaat 62-66).</li>
                    <li><strong>Air Hamim:</strong> Air yang sangat panas yang memotong-motong usus.</li>
                    <li><strong>Ghassaq:</strong> Nanah dan darah yang mengalir dari kulit penghuni neraka.</li>
                </ul>

                <h3>2.17.3 Penyesalan dan Pertengkaran</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dia mengatakan: "Alangkah baiknya kiranya aku dahulu mengerjakan (amal saleh) untuk hidupku ini".</p>
                    <span class="source">Surat Al Fajr Ayat: 24</span>
                </div>
                <p>Penghuni neraka akan saling menyalahkan antara pengikut dan pemimpin, dan memohon untuk dikembalikan ke dunia, namun permintaan mereka ditolak dan mereka kekal di dalamnya.</p>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Neraka apakah yang disebut sebagai 'pembakar kulit manusia'?",
                                options: ["Jahanam", "Hawiyah", "Saqar", "Huthamah"],
                                correct: 2,
                                explanation: "Saqar itu... adalah pembakar kulit manusia (Al Muddatstsir 29)."
                            },
                            {
                                question: "Apa makanan penghuni neraka yang disebutkan dalam Ash Shaaffaat 62?",
                                options: ["Buah Tin", "Pohon Zaqqum", "Kurma", "Anggur"],
                                correct: 1,
                                explanation: "(Makanan surga) itukah hidangan yang lebih baik ataukah pohon zaqqum."
                            },
                            {
                                question: "Neraka yang apinya membakar sampai ke hati disebut...",
                                options: ["Huthamah", "Jahim", "Sa'ir", "Hawiyah"],
                                correct: 0,
                                explanation: "Huthamah... (Yaitu) api... yang (membakar) sampai ke hati."
                            },
                            {
                                question: "Apa yang dikatakan penghuni neraka saat melihat azab (Al Fajr 24)?",
                                options: ["Kami senang", "Alangkah baiknya kiranya aku dahulu mengerjakan (amal saleh)", "Kami ingin tidur", "Ini tidak adil"],
                                correct: 1,
                                explanation: "Alangkah baiknya kiranya aku dahulu mengerjakan (amal saleh) untuk hidupku ini."
                            },
                            {
                                question: "Siapakah penjaga neraka yang dipanggil penghuni neraka (Az Zukhruf 77)?",
                                options: ["Jibril", "Mikail", "Malik", "Ridwan"],
                                correct: 2,
                                explanation: "Mereka berseru: 'Hai Malik, biarlah Tuhanmu membunuh kami saja'."
                            }
                        ]
                    },
                    {
                        id: 99,
                        title: "2.18 Ashab Al A'raf",
                        file: "topic_99.pdf",
                        content: `
            <h2>Ashab Al A'raf</h2>
            <div class="content-section">
                <p><strong>Al A'raf</strong> adalah tempat tertinggi (tembok pemisah) antara surga dan neraka. Penghuninya adalah orang-orang yang timbangan amal baik dan buruknya seimbang.</p>
                <hr class="divider">
                
                <h3>2.18.1 Siapakah Ashab Al A'raf?</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan di antara keduanya (penghuni surga dan neraka) ada batas; dan di atas Al A'raf ada orang-orang yang mengenal masing-masing... dengan tanda-tanda mereka.</p>
                    <span class="source">Surat Al A'raaf Ayat: 46</span>
                </div>
                <p>Mereka belum masuk surga namun mereka sangat ingin memasukinya. Mereka mengenal penghuni surga dan neraka dari tanda-tanda di wajah mereka.</p>

                <h3>2.18.2 Dialog Ashab Al A'raf</h3>
                <p><strong>Kepada Penghuni Surga:</strong> Mereka menyeru dan mengucapkan "Salamun 'alaikum" (Kesejahteraan atasmu).</p>
                <p><strong>Kepada Penghuni Neraka:</strong> Ketika pandangan mereka dialihkan ke penghuni neraka, mereka berdoa:</p>
                <div class="quran-quote">
                    
                    <p class="translation">"Ya Tuhan kami, janganlah Engkau tempatkan kami bersama-sama orang-orang yang zalim itu."</p>
                    <span class="source">Surat Al A'raaf Ayat: 47</span>
                </div>
            </div>
                        `,
                        quiz: [
                            {
                                question: "Apa arti Al A'raf?",
                                options: ["Tempat terendah", "Tempat tertinggi/tembok pemisah", "Sungai", "Jembatan"],
                                correct: 1,
                                explanation: "Al A'raaf artinya tempat yang tertinggi di antara surga dan neraka."
                            },
                            {
                                question: "Siapakah penghuni Al A'raf menurut tafsir umum?",
                                options: ["Orang kafir", "Para Nabi", "Orang yang timbangan amal baik dan buruknya seimbang", "Malaikat"],
                                correct: 2,
                                explanation: "Penghuninya adalah orang-orang yang timbangan amal baik dan buruknya seimbang."
                            },
                            {
                                question: "Apa doa Ashab Al A'raf saat melihat penghuni neraka (Al A'raaf 47)?",
                                options: ["Ya Tuhan kami, menangkanlah kami", "Ya Tuhan kami, janganlah Engkau tempatkan kami bersama orang-orang zalim", "Biarkan kami masuk neraka", "Hancurkan mereka"],
                                correct: 1,
                                explanation: "Ya Tuhan kami, janganlah Engkau tempatkan kami bersama-sama orang-orang yang zalim itu."
                            },
                            {
                                question: "Bagaimana sapaan mereka kepada penghuni surga?",
                                options: ["Salamun 'alaikum (Salam sejahtera atasmu)", "Kalian beruntung", "Tunggu kami", "Hai orang kaya"],
                                correct: 0,
                                explanation: "Mereka menyeru penduduk surga: 'Mudah-mudahan kesejahteraan atasmu' (Salamun 'alaikum)."
                            },
                            {
                                question: "Apakah mereka (Ashab Al A'raf) akan masuk surga pada akhirnya?",
                                options: ["Tidak akan pernah", "Ya, dengan rahmat Allah", "Mereka langsung ke neraka", "Mereka jadi malaikat"],
                                correct: 1,
                                explanation: "Mereka belum memasukinya, sedang mereka ingin segera (memasukinya) dan Allah akan memasukkan mereka dengan rahmat-Nya."
                            }
                        ]
                    }
                ]
            }
        ]
    }
    , {
        id: "theme-5",
        title: "Tema 5: Nabi Muhammad SAW",
        description: "Sejarah Perjalanan Hidup Nabi Muhammad SAW",
        subjects: [
            {
                id: "subject-5-1",
                title: "Pokok Bahasan 1: Zaman Jahiliyah",
                topics: [
                    {
                        id: 100,
                        title: "Kepercayaan Masyarakat Mekah",
                        file: "topic_100.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Kepercayaan tentang Bahirah, Saibah, Washilah, dan Ham</li>
                <li>Kepercayaan tentang Sesajian</li>
                <li>Kepercayaan tentang Mengorbankan Anak Laki-laki</li>
                <li>Kepercayaan tentang Anak Perempuan</li>
                <li>Kepercayaan tentang Ibadah di Baitullah</li>
                <li>Kepercayaan tentang Penyembahan Berhala</li>
                <li>Kepercayaan tentang Malaikat sebagai Perempuan</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas kondisi kepercayaan masyarakat Arab pada masa Jahiliyah sebelum kedatangan Islam. Mereka memiliki berbagai tradisi dan kepercayaan yang menyimpang, seperti mengharamkan binatang tertentu (Bahirah, Saibah), mempersembahkan sesajian untuk berhala, membunuh anak karena takut miskin atau malu, serta menyembah berhala seperti Lata, Uzza, dan Manah yang mereka anggap sebagai perantara kepada Allah.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Kepercayaan tentang Binatang Ternak (Bahirah, Saibah, dll)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Allah sekali-kali tidak pernah mensyari'atkan adanya bahiirah, saaibah, washiilah dan haam. Akan tetapi orang-orang kafir membuat-buat kedustaan terhadap Allah, dan kebanyakan mereka tidak mengerti.</p>
                    <span class="source">Surat Al Maaidah Ayat: 103</span>
                </div>
                <div class="note-box">
                    <strong>Istilah-istilah:</strong>
                    <ul>
                        <li><strong>Bahiirah:</strong> Unta betina yang telah beranak 5 kali (terakhir jantan), dibelah telinganya dan dilepaskan untuk berhala.</li>
                        <li><strong>Saaibah:</strong> Unta betina yang dibiarkan pergi karena nazar.</li>
                        <li><strong>Washiilah:</strong> Domba yang melahirkan anak kembar jantan-betina (jantan untuk berhala).</li>
                        <li><strong>Haam:</strong> Unta jantan yang sudah membuntingkan betina 10 kali, tidak boleh diganggu.</li>
                    </ul>
                </div>
            </div>

            <div class="content-section">
                <h3>Kepercayaan tentang Sesajian</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka memperuntukkan bagi Allah satu bagian dari tanaman dan ternak yang telah diciptakan Allah, lalu mereka berkata sesuai dengan persangkaan mereka: "Ini untuk Allah dan ini untuk berhala-berhala kami".</p>
                    <span class="source">Surat Al An'aam Ayat: 136</span>
                </div>
                <p>Mereka membagi hasil bumi untuk Allah dan berhala. Namun, bagian untuk berhala dijaga ketat, sedangkan bagian untuk Allah (fakir miskin) seringkali dialihkan untuk berhala jika kurang.</p>
            </div>

            <div class="content-section">
                <h3>Kepercayaan tentang Mengorbankan Anak</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan begitulah para pemimpin mereka telah menjadikan kebanyakan dari orang-orang musyrik itu memandang baik membunuh anak-anak mereka untuk membinasakan mereka.</p>
                    <span class="source">Surat Al An'aam Ayat: 137</span>
                </div>
                <p>Mereka membunuh anak laki-laki karena takut miskin (kurang makan) dan kurban untuk berhala.</p>
            </div>

            <div class="content-section">
                <h3>Kepercayaan tentang Anak Perempuan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan apabila seseorang dari mereka diberi kabar dengan (kelahiran) anak perempuan, hitamlah (merah padamlah) mukanya, dan dia sangat marah.</p>
                    <span class="source">Surat An Nahl Ayat: 58</span>
                </div>
                <p>Mereka merasa malu memiliki anak perempuan dan seringkali menguburnya hidup-hidup. Anehnya, mereka malah menganggap malaikat sebagai anak-anak perempuan Allah.</p>
            </div>

            <div class="content-section">
                <h3>Ibadah di Baitullah yang Menyimpang</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan shalat mereka di sekitar Baitullah itu, lain tidak hanyalah siulan dan tepukan tangan.</p>
                    <span class="source">Surat Al Anfaal Ayat: 35</span>
                </div>
                <p>Mereka juga melakukan thawaf mengelilingi Ka'bah dalam keadaan telanjang, menganggap pakaian mereka kotor oleh dosa.</p>
            </div>

            <div class="content-section">
                <h3>Penyembahan Berhala (Lata, Uzza, Manah)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka patutkah kamu (hai orang-orang musyrik) menganggap Al Lata dan Al Uzza, dan Manah yang ketiga, yang paling terkemudian (sebagai anak perempuan Allah)?</p>
                    <span class="source">Surat An Najm Ayat: 19-20</span>
                </div>
                <p>Mereka menyembah berhala-berhala ini bukan karena meyakini berhala itu menciptakan alam, tetapi sebagai perantara (syafaat) untuk mendekatkan diri kepada Allah (menurut sangkaan mereka).</p>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Zaman Jahiliyah adalah masa kegelapan dimana manusia tersesat jauh dari ajaran tauhid. Mereka membuat hukum sendiri, menghalalkan yang haram, dan mengharamkan yang halal, serta menyekutukan Allah dengan makhluk-Nya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa yang dimaksud dengan 'Bahiirah' dalam kepercayaan Jahiliyah?",
                                options: ["Unta jantan yang dilepas", "Unta betina yang dibelah telinganya", "Domba kembar", "Sapi perah"],
                                correct: 1,
                                explanation: "Bahiirah adalah unta betina yang telah beranak 5 kali (terakhir jantan), lalu telinganya dibelah dan dilepaskan untuk berhala."
                            },
                            {
                                question: "Bagaimana sikap orang Jahiliyah jika mendengar kelahiran anak perempuan (Surat An Nahl: 58)?",
                                options: ["Sangat gembira", "Bersyukur", "Marah dan mukanya merah padam", "Biasa saja"],
                                correct: 2,
                                explanation: "Apabila mereka diberi kabar kelahiran anak perempuan, muka mereka menjadi hitam (merah padam) karena marah dan malu."
                            },
                            {
                                question: "Siapakah nama berhala yang disebut dalam Surat An Najm ayat 19-20?",
                                options: ["Hubal, Latta, Uzza", "Latta, Uzza, Manah", "Yaguts, Ya'uq, Nasr", "Wadd, Suwa, Latta"],
                                correct: 1,
                                explanation: "Ayat tersebut menyebutkan: Al Lata, Al Uzza, dan Manah."
                            },
                            {
                                question: "Apa bentuk ibadah mereka di sekitar Baitullah (Surat Al Anfaal: 35)?",
                                options: ["Shalat berjamaah", "Dzikir dan doa", "Siulan dan tepukan tangan", "Membaca syair"],
                                correct: 2,
                                explanation: "Shalat mereka di sekitar Baitullah hanyalah siulan dan tepukan tangan."
                            },
                            {
                                question: "Mengapa mereka membunuh anak-anak mereka menurut Surat Al An'aam ayat 137?",
                                options: ["Karena perintah Raja", "Karena takut miskin dan bujukan setan", "Karena wabah penyakit", "Karena anak itu cacat"],
                                correct: 1,
                                explanation: "Mereka memandang baik membunuh anak-anak mereka (karena hasutan pemimpin/setan) dan karena takut kemiskinan."
                            }
                        ]
                    },
                    {
                        id: 101,
                        title: "Peristiwa Penyerangan Ka'bah",
                        file: "topic_101.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Kebiasaan Masyarakat Quraisy dalam Perniagaan</li>
                <li>Peristiwa Penyerangan Ka'bah (Tentara Gajah)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas dua peristiwa penting yang terekam dalam Al-Qur'an terkait masyarakat Mekah menjelang kenabian. Pertama, kebiasaan dagang suku Quraisy yang menjamin kemakmuran mereka (Surat Quraisy). Kedua, peristiwa penyerangan Ka'bah oleh tentara bergajah pimpinan Abrahah yang dihancurkan oleh Allah (Surat Al Fiil).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Kebiasaan Masyarakat Quraisy (Surat Quraisy)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Karena kebiasaan orang-orang Quraisy, (yaitu) kebiasaan mereka bepergian pada musim dingin dan musim panas.</p>
                    <span class="source">Surat Quraisy Ayat: 1-2</span>
                </div>
                <div class="note-box">
                    <strong>Jalur Perdagangan:</strong>
                    <p>Mereka bepergian ke Yaman pada <strong>musim dingin</strong> (karena Yaman hangat) dan ke Syam pada <strong>musim panas</strong> (karena Syam sejuk). Allah memerintahkan mereka untuk mensyukuri nikmat keamanan dan kemakmuran ini dengan menyembah Tuhan Pemilik Ka'bah.</p>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Maka hendaklah mereka menyembah Tuhan Pemilik rumah ini (Ka'bah). Yang telah memberi makanan kepada mereka untuk menghilangkan lapar dan mengamankan mereka dari ketakutan.</p>
                    <span class="source">Surat Quraisy Ayat: 3-4</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Peristiwa Tentara Gajah (Surat Al Fiil)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Apakah kamu tidak memperhatikan bagaimana Tuhanmu telah bertindak terhadap tentara bergajah?</p>
                    <span class="source">Surat Al Fiil Ayat: 1</span>
                </div>
                <p>Abrahah, Gubernur Yaman, membawa pasukan besar dengan gajah untuk menghancurkan Ka'bah agar orang-orang beralih haji ke gereja yang dibangunnya di Yaman. Namun, Allah melindungi Rumah-Nya.</p>

                <div class="quran-quote">
                    
                    <p class="translation">Dan Dia mengirimkan kepada mereka burung yang berbondong-bondong. Yang melempari mereka dengan batu (berasal) dari tanah yang terbakar.</p>
                    <span class="source">Surat Al Fiil Ayat: 3-4</span>
                </div>
                <p>Pasukan tersebut hancur lebur seperti "daun yang dimakan ulat" (Ka'ashfin ma'kuul). Peristiwa ini terjadi pada tahun kelahiran Nabi Muhammad SAW, yang kemudian dikenal sebagai Tahun Gajah.</p>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kedua surat ini menunjukkan nikmat Allah kepada penduduk Mekah: nikmat rezeki (perdagangan) dan nikmat keamanan (perlindungan dari serangan Abrahah). Seharusnya, hal ini membuat mereka semakin taat mengabdi kepada Allah, Tuhan Pemilik Ka'bah.</p>
                        `,
                        quiz: [
                            {
                                question: "Kapan orang Quraisy biasa bepergian ke Syam?",
                                options: ["Musim Dingin", "Musim Panas", "Musim Hujan", "Musim Gugur"],
                                correct: 1,
                                explanation: "Mereka bepergian pada musim dingin (ke Yaman) dan musim panas (ke Syam)."
                            },
                            {
                                question: "Apa tujuan utama Abrahah datang ke Mekah dengan pasukan gajah?",
                                options: ["Untuk berdagang", "Untuk menghancurkan Ka'bah", "Untuk berhaji", "Untuk membantu penduduk Mekah"],
                                correct: 1,
                                explanation: "Tujuan mereka adalah menghancurkan Ka'bah agar orang-orang berpaling ke tempat ibadah buatan Abrahah."
                            },
                            {
                                question: "Dengan apa Allah menghancurkan pasukan gajah?",
                                options: ["Banjir besar", "Gempa bumi", "Burung Ababil yang melempar batu panas", "Pasukan Quraisy"],
                                correct: 2,
                                explanation: "Allah mengirimkan burung Ababil yang melempari mereka dengan batu dari tanah yang terbakar (sijjin)."
                            },
                            {
                                question: "Apa perintah Allah kepada orang Quraisy dalam Surat Quraisy ayat 3?",
                                options: ["Pergi berperang", "Membangun benteng", "Menyembah Tuhan Pemilik Ka'bah", "Membayar pajak"],
                                correct: 2,
                                explanation: "Maka hendaklah mereka menyembah Tuhan Pemilik rumah ini (Ka'bah)."
                            },
                            {
                                question: "Bagaimana keadaan pasukan gajah setelah diazab Allah (Surat Al Fiil: 5)?",
                                options: ["Seperti debu yang beterbangan", "Seperti daun yang dimakan ulat", "Seperti kayu bakar", "Seperti air yang menguap"],
                                correct: 1,
                                explanation: "Dia menjadikan mereka seperti daun-daun yang dimakan (ulat) - 'Ka'ashfin ma'kuul'."
                            }
                        ]
                    }
                ]
            }
            , {
                id: "subject-5-2",
                title: "Pokok Bahasan 2: Kenabian dan Kerasulan Muhammad SAW",
                topics: [
                    {
                        id: 102,
                        title: "Muhammad SAW Diangkat Menjadi Rasul",
                        file: "topic_102.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Muhammad Saw. Diutus sebagai Penyampai Risalah</li>
                <li>Muhammad Saw. Diutus sebagai Pembawa Kabar Gembira (Basyir)</li>
                <li>Muhammad Saw. Diutus sebagai Pemberi Peringatan (Nadzir)</li>
                <li>Muhammad Saw. Diutus sebagai Rahmat bagi Semesta Alam</li>
                <li>Muhammad Saw. Diutus sebagai Saksi (di Akhirat)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan peran dan tugas utama Nabi Muhammad SAW sebagai utusan Allah. Beliau bukan sekadar manusia biasa, tetapi seorang Rasul yang memikul tanggung jawab besar untuk menyampaikan risalah, membawa kabar gembira bagi orang beriman, memberi peringatan bagi yang ingkar, serta menjadi rahmat bagi seluruh alam semesta.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>1. Sebagai Penyampai Risalah (Al-Muballigh)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Hai Rasul, sampaikanlah apa yang diturunkan kepadamu dari Tuhanmu. Dan jika tidak kamu kerjakan (apa yang diperintahkan itu, berarti) kamu tidak menyampaikan risalah-Nya.</p>
                    <span class="source">Surat Al Maaidah Ayat: 67</span>
                </div>
                <p>Tugas Nabi hanyalah menyampaikan (Tabligh). Hidayah (petunjuk) untuk beriman sepenuhnya ada di tangan Allah. Nabi tidak bisa memaksakan keimanan kepada orang lain, bahkan kepada orang yang dicintainya sekalipun.</p>
            </div>

            <div class="content-section">
                <h3>2. Sebagai Pembawa Kabar Gembira (Basyir)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sampaikanlah berita gembira kepada orang-orang mukmin bahwa sesungguhnya bagi mereka karunia yang besar dari Allah.</p>
                    <span class="source">Surat Al Ahzaab Ayat: 47</span>
                </div>
                <p>Nabi diutus untuk memberikan kabar gembira (kemenangan, surga, dan keridhaan Allah) bagi mereka yang taat dan beriman.</p>
            </div>

            <div class="content-section">
                <h3>3. Sebagai Pemberi Peringatan (Nadzir)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Aku tidak lain hanyalah seorang pemberi peringatan yang nyata.</p>
                    <span class="source">Surat Asy Syuuraa Ayat: 115 </span>
                </div>
                <p>Beliau memberikan peringatan keras akan azab neraka bagi orang-orang yang ingkar dan mendustakan ayat-ayat Allah.</p>
            </div>

            <div class="content-section">
                <h3>4. Sebagai Rahmat bagi Semesta Alam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tiadalah Kami mengutusmu, melainkan untuk (menjadi) rahmat bagi semesta alam.</p>
                    <span class="source">Surat Al Anbiyaa' Ayat: 107</span>
                </div>
                <p>Kedatangan Nabi Muhammad adalah wujud kasih sayang Allah. Dengan syariat yang dibawanya, manusia dituntun dari kegelapan menuju cahaya, dan azab yang menyeluruh (seperti umat terdahulu) ditangguhkan.</p>
            </div>

            <div class="content-section">
                <h3>5. Sebagai Saksi di Akhirat (Syahid)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan (ingatlah) akan hari (ketika) Kami bangkitkan pada tiap-tiap umat seorang saksi atas mereka dari mereka sendiri dan Kami datangkan kamu (Muhammad) menjadi saksi atas seluruh umat manusia.</p>
                    <span class="source">Surat An Nahl Ayat: 89</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Nabi Muhammad SAW adalah penutup para Nabi yang membawa syariat sempurna. Beliau bukanlah malaikat, dan tidak mengetahui hal ghaib kecuali yang diberitahukan Allah. Ketaatan kepada beliau adalah cerminan ketaatan kepada Allah.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa tugas utama Rasul menurut Surat Al Maaidah ayat 99?",
                                options: ["Memaksa orang masuk Islam", "Menghukum orang kafir", "Hanyalah menyampaikan (risalah)", "Menjadi raja"],
                                correct: 2,
                                explanation: "Kewajiban Rasul tidak lain hanya menyampaikan, dan Allah tahu apa yang kamu lahirkan dan apa yang kamu sembunyikan."
                            },
                            {
                                question: "Apa yang dimaksud dengan 'Rahmatan lil 'Alamin' (Surat Al Anbiyaa' 107)?",
                                options: ["Pembawa rezeki", "Rahmat bagi semesta alam", "Pemimpin dunia", "Penyembuh penyakit"],
                                correct: 1,
                                explanation: "Dan tiadalah Kami mengutusmu, melainkan untuk (menjadi) rahmat bagi semesta alam."
                            },
                            {
                                question: "Apakah Nabi Muhammad mengetahui perkara ghaib (Surat Al An'aam 50)?",
                                options: ["Ya, semuanya", "Tidak, kecuali yang diwahyukan Allah", "Ya, karena beliau malaikat", "Tahu sedikit-sedikit"],
                                correct: 1,
                                explanation: "Katakanlah: 'Aku tidak mengatakan kepadamu, bahwa padaku ada perbendaharaan Allah, dan tidak (pula) aku mengetahui yang ghaib'."
                            },
                            {
                                question: "Apa arti dari peran Nabi sebagai 'Nadzir'?",
                                options: ["Pemberi kabar gembira", "Pemberi peringatan", "Penyampai wahyu", "Saksi"],
                                correct: 1,
                                explanation: "Nadzir artinya pemberi peringatan, sedangkan Basyir artinya pemberi kabar gembira."
                            },
                            {
                                question: "Apa konsekuensi jika Nabi tidak menyampaikan wahyu (Surat Al Maaidah 67)?",
                                options: ["Akan dimarahi malaikat", "Berarti tidak menyampaikan risalah-Nya (gagal tugas)", "Akan dikurangi umurnya", "Akan jatuh miskin"],
                                correct: 1,
                                explanation: "Dan jika tidak kamu kerjakan (apa yang diperintahkan itu), berarti kamu tidak menyampaikan risalah-Nya."
                            }
                        ]
                    },
                    {
                        id: 103,
                        title: "Agama Muhammad SAW",
                        file: "topic_103.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Larangan Mencari Agama Selain Agama Allah</li>
                <li>Agama yang Diridhai di sisi Allah Hanya Islam</li>
                <li>Ancaman bagi Orang yang Mencari Agama Selain Islam</li>
                <li>Muhammad Diutus Membawa Agama yang Benar</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menegaskan bahwa Islam adalah satu-satunya agama yang diridhai Allah dan dibawa oleh seluruh Nabi, mulai dari Ibrahim a.s. hingga Muhammad SAW. Mencari jalan keselamatan di luar Islam adalah kesia-siaan yang akan membawa kerugian di akhirat.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Islam: Agama Seluruh Nabi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka apakah mereka mencari agama yang lain dari agama Allah, padahal kepada-Nya menyerahkan diri segala apa yang di langit dan di bumi, baik dengan suka maupun terpaksa.</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 83</span>
                </div>
                <p>Para Nabi terdahulu (Ibrahim, Ismail, Musa, Isa) pada hakikatnya mengajarkan ketundukan (Islam) kepada Allah Yang Esa.</p>
            </div>

            <div class="content-section">
                <h3>Agama yang Diridhai Hanyalah Islam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Sesungguhnya agama (yang diridhai) di sisi Allah hanyalah Islam.</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 19</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Pada hari ini telah Kusempurnakan untukmu agamamu, dan telah Kucukupkan padamu nikmat-Ku, dan telah Kuridhai Islam sebagai agama bagimu.</p>
                    <span class="source">Surat Al Maaidah Ayat: 3</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Ancaman Mencari Agama Selain Islam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Barangsiapa mencari agama selain agama Islam, maka sekali-kali tidaklah akan diterima (agama itu) daripadanya, dan dia di akhirat termasuk orang-orang yang rugi.</p>
                    <span class="source">Surat Ali ‘Imraan Ayat: 85</span>
                </div>
            </div>

            <div class="content-section">
                <h3>Kemenangan Agama Islam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dialah yang mengutus Rasul-Nya dengan membawa petunjuk dan agama yang benar agar Dia memenangkannya di atas segala agama meskipun orang-orang musyrik membenci.</p>
                    <span class="source">Surat Ash Shaff Ayat: 9</span>
                </div>
                <p>Kebenaran pasti akan menang dan kebatilan pasti akan lenyap (Al Israa' : 81).</p>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Islam bukan sekadar label, melainkan sikap penyerahan diri secara total kepada kehendak Allah. Dengan disempurnakannya agama ini pada Haji Wada', maka tidak ada lagi alasan bagi manusia untuk mencari pedoman hidup selain Al-Qur'an dan Sunnah.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa satu-satunya agama yang diridhai di sisi Allah (Ali 'Imraan 19)?",
                                options: ["Nasrani", "Yahudi", "Islam", "Majusi"],
                                correct: 2,
                                explanation: "Sesungguhnya agama (yang diridhai) di sisi Allah hanyalah Islam."
                            },
                            {
                                question: "Apa ancaman bagi orang yang mencari agama selain Islam (Ali 'Imraan 85)?",
                                options: ["Tidak akan diterima dan merugi di akhirat", "Akan menjadi kaya di dunia", "Hanya dosanya diampuni", "Tetap masuk surga"],
                                correct: 0,
                                explanation: "Maka sekali-kali tidaklah akan diterima (agama itu) daripadanya, dan dia di akhirat termasuk orang-orang yang rugi."
                            },
                            {
                                question: "Kapan Allah menyatakan telah menyempurnakan agama Islam (Al Maaidah 3)?",
                                options: ["Saat Nabi lahir", "Saat wahyu pertama turun", "Saat Haji Wada' (Hari ini)", "Saat Nabi wafat"],
                                correct: 2,
                                explanation: "Ayat ini ('Pada hari ini telah Kusempurnakan...') turun saat Haji Wada'."
                            },
                            {
                                question: "Siapakah yang mengklaim 'Tidak masuk surga kecuali Yahudi atau Nasrani' (Al Baqarah 111)?",
                                options: ["Orang Muslim", "Orang Musyrik", "Ahli Kitab (Yahudi & Nasrani)", "Orang Munafik"],
                                correct: 2,
                                explanation: "Mereka (Yahudi dan Nasrani) berkata: 'Sekali-kali tidak akan masuk surga kecuali orang-orang (yang beragama) Yahudi atau Nasrani'."
                            },
                            {
                                question: "Apa tujuan Allah mengutus Rasul dengan agama yang benar (Ash Shaff 9)?",
                                options: ["Agar manusia berperang", "Agar Dia memenangkannya di atas segala agama", "Agar menjadi kaya", "Agar menguasai tanah Arab saja"],
                                correct: 1,
                                explanation: "Agar Dia memenangkannya di atas segala agama meskipun orang-orang musyrik membenci."
                            }
                        ]
                    }
                    , {
                        id: 104,
                        title: "Keistimewaan Risalah Muhammad SAW",
                        file: "topic_104.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Termaktub di Dalam Kitab Samawi Sebelumnya</li>
                <li>Dibenarkan oleh Seluruh Para Nabi/Rasul Sebelumnya</li>
                <li>Sebagai Risalah Terakhir</li>
                <li>Diutus untuk Seluruh Umat Manusia</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini menjelaskan keistimewaan risalah Nabi Muhammad SAW. Kedatangan beliau telah diberitakan oleh kitab-kitab sebelumnya (Taurat dan Injil) serta dinubuatkan oleh Nabi Isa a.s. Risalah beliau bersifat universal untuk seluruh umat manusia dan menjadi penutup risalah para nabi sebelumnya.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>1. Termaktub di Kitab-Kitab Sebelumnya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">(Yaitu) orang-orang yang mengikuti Rasul, Nabi yang ummi yang (namanya) mereka dapati tertulis di dalam Taurat dan Injil yang ada di sisi mereka.</p>
                    <span class="source">Surat Al A'raaf Ayat: 157</span>
                </div>
                <div class="note-box">
                    <strong>Nabi yang Ummi:</strong>
                    <p>Meskipun tidak bisa membaca dan menulis (Ummi), beliau membawa ajaran yang membenarkan kebenaran, menghalalkan yang baik, dan mengharamkan yang buruk, serta membebaskan manusia dari belenggu kesesatan.</p>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan (Isa berkata): ...memberi khabar gembira dengan (datangnya) seorang Rasul yang akan datang sesudahku, yang namanya Ahmad (Muhammad).</p>
                    <span class="source">Surat Ash Shaff Ayat: 6</span>
                </div>
            </div>

            <div class="content-section">
                <h3>2. Perjanjian Para Nabi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan (ingatlah), ketika Allah mengambil perjanjian dari para nabi: "...niscaya kamu akan sungguh-sungguh beriman kepadanya (Muhammad) dan menolongnya."</p>
                    <span class="source">Surat Ali 'Imraan Ayat: 81</span>
                </div>
                <p>Seluruh Nabi telah diambil janjinya oleh Allah untuk mengimani dan mendukung kenabian Muhammad SAW jika mereka bertemu dengannya.</p>
            </div>

            <div class="content-section">
                <h3>3. Penutup Para Nabi (Khatamun Nabiyyin)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Muhammad itu sekali-kali bukanlah bapak dari seorang laki-laki di antara kamu, tetapi dia adalah Rasulullah dan penutup nabi-nabi.</p>
                    <span class="source">Surat Al Ahzaab Ayat: 40</span>
                </div>
                <p>Tidak ada nabi baru setelah beliau. Syariatnya menyempurnakan syariat sebelumnya.</p>
            </div>

            <div class="content-section">
                <h3>4. Untuk Seluruh Umat Manusia</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Kami tidak mengutus kamu, melainkan kepada umat manusia seluruhnya sebagai pembawa berita gembira dan sebagai pemberi peringatan.</p>
                    <span class="source">Surat Saba' Ayat: 28</span>
                </div>
                <p>Berbeda dengan nabi terdahulu yang diutus khusus untuk kaumnya, Nabi Muhammad SAW diutus untuk seluruh ras dan bangsa (Rahmatan lil 'Alamin).</p>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Keistimewaan ini menunjukkan posisi sentral Nabi Muhammad SAW dalam skenario penyelamatan manusia oleh Allah SWT. Beliau adalah puncak dari mata rantai kenabian.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa sebutan Nabi Muhammad yang tertulis dalam Taurat dan Injil (Al A'raaf 157)?",
                                options: ["Nabi yang kaya", "Nabi yang Ummi", "Raja diraja", "Malaikat"],
                                correct: 1,
                                explanation: "(Yaitu) orang-orang yang mengikuti Rasul, Nabi yang ummi yang (namanya) mereka dapati tertulis di dalam Taurat dan Injil."
                            },
                            {
                                question: "Siapakah Nabi yang menubuatkan kedatangan Rasul bernama Ahmad (Ash Shaff 6)?",
                                options: ["Nabi Musa a.s.", "Nabi Ibrahim a.s.", "Nabi Isa a.s.", "Nabi Daud a.s."],
                                correct: 2,
                                explanation: "Dan (ingatlah) ketika Isa Ibnu Maryam berkata: ...memberi khabar gembira dengan (datangnya) seorang Rasul... yang namanya Ahmad."
                            },
                            {
                                question: "Apa arti 'Khatamun Nabiyyin' dalam Surat Al Ahzaab ayat 40?",
                                options: ["Pembuka para nabi", "Penutup nabi-nabi", "Pemimpin nabi-nabi", "Guru para nabi"],
                                correct: 1,
                                explanation: "Muhammad itu... adalah Rasulullah dan penutup nabi-nabi (Khatamun Nabiyyin)."
                            },
                            {
                                question: "Apakah wilayah dakwah Nabi Muhammad SAW menurut Surat Saba' 28?",
                                options: ["Hanya untuk bangsa Arab", "Hanya untuk kaum Quraisy", "Kepada umat manusia seluruhnya", "Hanya untuk penduduk Mekah"],
                                correct: 2,
                                explanation: "Dan Kami tidak mengutus kamu, melainkan kepada umat manusia seluruhnya."
                            },
                            {
                                question: "Apa isi perjanjian Allah dengan para Nabi terdahulu (Ali 'Imraan 81)?",
                                options: ["Untuk saling berperang", "Untuk beriman dan menolong Muhammad SAW", "Untuk membuat kitab sendiri", "Untuk menjadi malaikat"],
                                correct: 1,
                                explanation: "Niscaya kamu akan sungguh-sungguh beriman kepadanya (Muhammad) dan menolongnya."
                            }
                        ]
                    },
                    {
                        id: 105,
                        title: "Bukti Risalah Muhammad SAW",
                        file: "topic_105.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Alquran sebagai Bukti Risalah Muhammad</li>
                <li>Berita Ghaib sebagai Bukti Kenabian</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas bukti-bukti kebenaran risalah Nabi Muhammad SAW. Bukti terbesarnya adalah Al-Qur'an, sebuah mukjizat abadi yang berisi petunjuk, rahmat, dan kisah-kisah ghaib masa lalu (seperti kisah Musa) yang tidak mungkin diketahui Nabi yang Ummi kecuali melalui wahyu.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>Al-Qur'an: Mukjizat Terbesar</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka berkata: "Mengapa tidak diturunkan padanya mukjizat-mukjizat dari Tuhannya?" Katakan: "Sesungguhnya mukjizat-mukjizat itu terserah kepada Allah. Dan sesungguhnya aku hanya seorang pemberi peringatan yang nyata".</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 50</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tidak cukupkah bagi mereka bahwasanya Kami telah menurunkan kepadamu Alkitab (Alquran) sedang ia dibacakan kepada mereka?</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 51</span>
                </div>
                <p>Orang musyrik meminta mukjizat fisik (seperti tongkat Musa atau unta Saleh), namun Allah menegaskan bahwa Al-Qur'an yang dibacakan kepada mereka sudah lebih dari cukup sebagai bukti kemukjizatan (intelektual & spiritual).</p>
            </div>

            <div class="content-section">
                <h3>Berita Ghaib Masa Lalu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tidaklah kamu (Muhammad) berada di sisi yang sebelah barat ketika Kami menyampaikan perintah kepada Musa...</p>
                    <span class="source">Surat Al Qashash Ayat: 44</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan tiadalah kamu berada di dekat gunung Thur ketika Kami menyeru (Musa)...</p>
                    <span class="source">Surat Al Qashash Ayat: 46</span>
                </div>
                <p>Nabi Muhammad SAW tidak hadir saat peristiwa Musa menerima wahyu di Bukit Tursina (ribuan tahun sebelumnya). Namun, beliau bisa menceritakannya dengan detail dalam Al-Qur'an. Ini adalah bukti bahwa informasi tersebut bersumber dari Wahyu Allah, bukan karangan beliau.</p>
            </div>

            <div class="content-section">
                <h3>Tantangan bagi yang Ragu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Datangkanlah olehmu sebuah kitab dari sisi Allah yang kitab itu lebih (dapat) memberi petunjuk daripada keduanya (Taurat dan Alquran) niscaya aku mengikutinya, jika kamu sungguh orang-orang yang benar".</p>
                    <span class="source">Surat Al Qashash Ayat: 49</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Bukti kenabian Nabi Muhammad SAW sangat jelas bagi mereka yang menggunakan akal sehat. Al-Qur'an adalah bukti hidup yang terus bisa disaksikan hingga hari ini, berbeda dengan mukjizat fisik nabi-nabi terdahulu yang hanya bisa disaksikan oleh umat zamannya.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa jawaban Allah ketika orang kafir meminta mukjizat fisik (Al 'Ankabuut 51)?",
                                options: ["Diberikan unta ajaib", "Diberikan tongkat sakti", "Tidak cukupkah Al-Qur'an diturunkan kepada mereka?", "Mereka diazab langsung"],
                                correct: 2,
                                explanation: "Dan tidak cukupkah bagi mereka bahwasanya Kami telah menurunkan kepadamu Alkitab (Alquran) sedang ia dibacakan kepada mereka?"
                            },
                            {
                                question: "Dari mana Nabi Muhammad mengetahui kisah Musa di Bukit Thur padahal beliau tidak ada di sana (Al Qashash 46)?",
                                options: ["Membaca buku sejarah", "Bertanya kepada pendeta", "Sebagai rahmat dari Tuhanmu (Wahyu)", "Mimpi"],
                                correct: 2,
                                explanation: "Tetapi (kami beritahukan itu kepadamu) sebagai rahmat dari Tuhanmu."
                            },
                            {
                                question: "Di mana posisi Musa menerima perintah menurut Al Qashash ayat 44?",
                                options: ["Sisi sebelah Timur", "Sisi sebelah Barat (Lembah Suci Thuwa)", "Di tengah gurun", "Di atas awan"],
                                correct: 1,
                                explanation: "Dan tidaklah kamu (Muhammad) berada di sisi yang sebelah barat ketika Kami menyampaikan perintah kepada Musa."
                            },
                            {
                                question: "Apa tantangan Allah kepada mereka yang menolak Al-Qur'an (Al Qashash 49)?",
                                options: ["Membuat patung emas", "Mendatangkan kitab yang lebih memberi petunjuk", "Terbang ke langit", "Menghidupkan orang mati"],
                                correct: 1,
                                explanation: "Datangkanlah olehmu sebuah kitab dari sisi Allah yang kitab itu lebih (dapat) memberi petunjuk daripada keduanya."
                            },
                            {
                                question: "Apa sifat bukti (bayyinah) yang dibacakan oleh Rasulullah (Al Bayyinah 2)?",
                                options: ["Lembaran-lembaran yang disucikan", "Batu bertulis", "Daun lontar", "Kulit binatang"],
                                correct: 0,
                                explanation: "(Yaitu) seorang rasul dari Allah (Muhammad) yang membacakan lembaran-lembaran yang disucikan (Alquran)."
                            }
                        ]
                    }
                ]
            }
            , {
                id: "subject-5-3",
                title: "Pokok Bahasan 3: Periode Makkah",
                topics: [
                    {
                        id: 106,
                        title: "Dakwah Rasulullah SAW (Periode Mekah)",
                        file: "topic_106.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Perintah Dakwah kepada Keluarga dan Kerabat</li>
                <li>Dakwah Secara Terang-terangan</li>
                <li>Dakwah kepada Penduduk Mekah dan Sekitarnya</li>
                <li>Dakwah kepada Tauhidullah</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas tahapan dakwah Nabi Muhammad SAW di Mekah. Dimulai dari dakwah kepada keluarga terdekat (Bani Hasyim), kemudian perintah untuk berdakwah secara terang-terangan kepada penduduk Mekah (Ummul Qura) dan sekitarnya, dengan materi inti yaitu mengajak kepada Tauhid (mengesakan Allah).</p>
            <hr class="divider">

            <div class="content-section">
                <h3>1. Dakwah kepada Kerabat Terdekat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan berilah peringatan kepada kerabat-kerabatmu yang terdekat.</p>
                    <span class="source">Surat Asy Syu'araa' Ayat: 214</span>
                </div>
                <p>Rasulullah diperintahkan untuk memulai dakwah dari lingkungan terdekatnya. Namun, beliau diingatkan bahwa beliau tidak bertanggung jawab jika mereka menolak (mendurhakai).</p>
            </div>

            <div class="content-section">
                <h3>2. Dakwah Terang-terangan (Jahar)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka sampaikanlah olehmu secara terang-terangan apa yang diperintahkan (kepadamu) dan berpalinglah dari orang-orang musyrik.</p>
                    <span class="source">Surat Al Hijr Ayat: 94</span>
                </div>
                <p>Setelah tiga tahun dakwah sembunyi-sembunyi, turunlah perintah ini. Nabi menaiki Bukit Shafa dan menyeru kaum Quraisy secara terbuka.</p>
            </div>

            <div class="content-section">
                <h3>3. Tantangan dan Hiburan bagi Nabi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Kami sungguh mengetahui, bahwa dadamu menjadi sempit disebabkan apa yang mereka ucapkan. Maka bertasbihlah dengan memuji Tuhanmu dan jadilah kamu di antara orang-orang yang bersujud (shalat).</p>
                    <span class="source">Surat Al Hijr Ayat: 97-98</span>
                </div>
                <p>Allah menghibur Nabi yang sedih karena penolakan kaumnya dengan perintah shalat dan tasbih.</p>
            </div>

            <div class="content-section">
                <h3>4. Dakwah Tauhid</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Katakanlah: "Inilah jalanku, aku dan orang-orang yang mengikutiku mengajak (kamu) kepada Allah dengan hujjah yang nyata..."</p>
                    <span class="source">Surat Yuusuf Ayat: 108</span>
                </div>
                <p>Inti dakwah adalah mengajak manusia hanya menyembah Allah dan meninggalkan berhala (Tauhidullah).</p>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Dakwah di Mekah penuh tantangan, namun Nabi tetap teguh menyampaikan risalah Tauhid sesuai perintah Allah, baik kepada kerabat maupun masyarakat umum.</p>
                        `,
                        quiz: [
                            {
                                question: "Kepada siapakah perintah dakwah pertama kali ditujukan dalam Surat Asy Syu'araa ayat 214?",
                                options: ["Seluruh manusia", "Penduduk Madinah", "Kerabat-kerabat terdekat", "Raja-raja dunia"],
                                correct: 2,
                                explanation: "Dan berilah peringatan kepada kerabat-kerabatmu yang terdekat (wa andzir 'asyiratakal aqrabin)."
                            },
                            {
                                question: "Apa perintah Allah ketika dada Nabi terasa sempit karena ucapan kaum musyrikin (Al Hijr 98)?",
                                options: ["Membalas makian mereka", "Bertasbih dan bersujud (shalat)", "Berhenti berdakwah", "Pindah ke Thaif"],
                                correct: 1,
                                explanation: "Maka bertasbihlah dengan memuji Tuhanmu dan jadilah kamu di antara orang-orang yang bersujud."
                            },
                            {
                                question: "Ayat manakah yang memerintahkan dakwah secara terang-terangan?",
                                options: ["Al Hijr ayat 94", "Al Muddatsir ayat 1", "Al Alaq ayat 1", "Al Fatihah ayat 1"],
                                correct: 0,
                                explanation: "Fashda' bima tu'mar (Maka sampaikanlah olehmu secara terang-terangan apa yang diperintahkan)."
                            },
                            {
                                question: "Apa inti ajakan Nabi dan pengikutnya menurut Surat Yuusuf ayat 108?",
                                options: ["Mengajak kepada harta", "Mengajak kepada kekuasaan", "Mengajak kepada Allah (Tauhid)", "Mengajak perang"],
                                correct: 2,
                                explanation: "Aku dan orang-orang yang mengikutiku mengajak (kamu) kepada Allah dengan hujjah yang nyata."
                            },
                            {
                                question: "Apakah Nabi bertanggung jawab jika kerabatnya menolak dakwah (Asy Syu'araa 216)?",
                                options: ["Ya, beliau menanggung dosa mereka", "Tidak, beliau berlepas diri dari apa yang mereka kerjakan", "Beliau harus memaksa mereka", "Beliau gagal menjadi Nabi"],
                                correct: 1,
                                explanation: "Jika mereka mendurhakaimu maka katakanlah: 'Sesungguhnya aku tidak bertanggung jawab terhadap apa yang kamu kerjakan'."
                            }
                        ]
                    },
                    {
                        id: 107,
                        title: "Permusuhan Abu Jahal dan Abu Lahab",
                        file: "topic_107.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Permusuhan Abu Jahal (Surat Al 'Alaq)</li>
                <li>Permusuhan Abu Lahab (Surat Al Lahab)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini membahas dua tokoh utama penentang dakwah Nabi di Mekah: Abu Jahal dan Abu Lahab. Abu Jahal berusaha melarang Nabi shalat di Ka'bah, sementara Abu Lahab dan istrinya secara aktif menyakiti dan memfitnah Nabi.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>1. Abu Jahal: Melarang Shalat</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Bagaimana pendapatmu tentang orang yang melarang, seorang hamba ketika mengerjakan shalat.</p>
                    <span class="source">Surat Al 'Alaq Ayat: 9-10</span>
                </div>
                <p>Abu Jahal mengancam akan menginjak leher Nabi jika melihat beliau shalat. Namun, Allah mengancam balik akan menarik ubun-ubunnya (ke neraka) dan memanggil malaikat Zabaniyah (penyiksa).</p>
                <div class="quran-quote">
                    
                    <p class="translation">Ketahuilah, sungguh jika dia tidak berhenti (berbuat demikian) niscaya Kami tarik ubun-ubunnya.</p>
                    <span class="source">Surat Al 'Alaq Ayat: 15</span>
                </div>
            </div>

            <div class="content-section">
                <h3>2. Abu Lahab: Celaka dan Binasa</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Binasalah kedua tangan Abu Lahab dan sungguh dia akan binasa.</p>
                    <span class="source">Surat Al Lahab Ayat: 1</span>
                </div>
                <p>Abu Lahab adalah paman Nabi yang paling keras menentang. Istrinya (Ummu Jamil) disebut sebagai "pembawa kayu bakar" (penyebar fitnah). Keduanya diancam dengan api neraka yang bergejolak.</p>
                <div class="quran-quote">
                    
                    <p class="translation">Kelak ia akan masuk ke dalam api yang bergejolak.</p>
                    <span class="source">Surat Al Lahab Ayat: 3</span>
                </div>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Kisah kedua tokoh ini menjadi pelajaran bahwa hubungan kekerabatan (seperti Abu Lahab) atau kedudukan tinggi (seperti Abu Jahal) tidak akan menyelamatkan seseorang dari azab Allah jika mereka memusuhi kebenaran.</p>
                        `,
                        quiz: [
                            {
                                question: "Siapakah yang dimaksud dengan 'orang yang melarang seorang hamba ketika shalat' dalam Surat Al 'Alaq?",
                                options: ["Abu Lahab", "Abu Jahal", "Abu Sufyan", "Walid bin Mughirah"],
                                correct: 1,
                                explanation: "Yang dimaksud adalah Abu Jahal yang melarang Rasulullah shalat."
                            },
                            {
                                question: "Apa ancaman Allah bagi orang yang melarang shalat tersebut (Al 'Alaq 15)?",
                                options: ["Diberi harta banyak", "Ditarik ubun-ubunnya (ke neraka)", "Dijadikan raja", "Dimaafkan"],
                                correct: 1,
                                explanation: "Niscaya Kami tarik ubun-ubunnya (La nasfa'an bin naashiyah)."
                            },
                            {
                                question: "Siapakah istri Abu Lahab yang disebut 'pembawa kayu bakar'?",
                                options: ["Hindun", "Arwa (Ummu Jamil)", "Khadijah", "Aisyah"],
                                correct: 1,
                                explanation: "Istri Abu Lahab adalah Ummu Jamil yang suka menyebar fitnah (kayu bakar)."
                            },
                            {
                                question: "Apa arti 'Zabaniyah' dalam surat Al 'Alaq ayat 18?",
                                options: ["Malaikat penjaga surga", "Malaikat penyiksa di neraka", "Malaikat pembawa wahyu", "Pasukan kuda"],
                                correct: 1,
                                explanation: "Zabaniyah ialah malaikat yang menyiksa orang yang berdosa di neraka."
                            },
                            {
                                question: "Mengapa harta Abu Lahab tidak berguna baginya (Al Lahab 2)?",
                                options: ["Karena hartanya sedikit", "Karena dicuri orang", "Tidak dapat menolak azab Allah", "Karena sudah disedekahkan"],
                                correct: 2,
                                explanation: "Tidaklah berfaedah baginya hartanya dan apa yang ia usahakan (untuk menolak azab)."
                            }
                        ]
                    },
                    {
                        id: 108,
                        title: "Sikap Musyrikin Mekah terhadap Dakwah",
                        file: "topic_108.pdf",
                        content: `
            <h2>Daftar Isi</h2>
            <ul class="toc-list">
                <li>Mengingkari Dakwah</li>
                <li>Menuduh Rasulullah Gila dan Penyihir</li>
                <li>Mengejek dan Meminta Disegerakan Azab</li>
                <li>Meminta Mukjizat Fisik (Mata Air, Kebun, Malaikat)</li>
                <li>Berpaling dari Mukjizat (Terbelahnya Bulan)</li>
            </ul>
            <hr class="divider">
            <h2>Isi Materi</h2>
            <p>Materi ini merangkum berbagai reaksi dan penolakan kaum Musyrikin Mekah terhadap dakwah Nabi. Mulai dari tuduhan gila, tukang sihir, hingga tuntutan yang tidak masuk akal seperti meminta malaikat turun atau meminta azab disegerakan.</p>
            <hr class="divider">

            <div class="content-section">
                <h3>1. Tuduhan Keji (Gila dan Sihir)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka berkata: "Hai orang yang diturunkan Alquran kepadanya, sesungguhnya kamu benar-benar orang gila".</p>
                    <span class="source">Surat Al Hijr Ayat: 6</span>
                </div>
                <p>Mereka juga menuduh Al-Qur'an sebagai dongengan orang dahulu dan Nabi sebagai penyair atau tukang tenung, padahal mereka tahu Nabi adalah orang yang jujur (Al Amin).</p>
            </div>

            <div class="content-section">
                <h3>2. Meminta Mukjizat yang Aneh-Aneh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka berkata: "Kami sekali-kali tidak percaya kepadamu hingga kamu memancarkan mata air dari bumi untuk kami..."</p>
                    <span class="source">Surat Al Israa' Ayat: 90</span>
                </div>
                <p>Mereka meminta sungai, kebun, rumah emas, atau naik ke langit. Allah menjawab bahwa Nabi hanyalah seorang manusia yang menjadi Rasul, bukan Tuhan yang bisa mengabulkan permintaan itu sesuka hati.</p>
            </div>

            <div class="content-section">
                <h3>3. Mukjizat Terbelahnya Bulan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Telah dekat datangnya saat itu dan telah terbelah bulan. Dan jika mereka melihat suatu tanda (mukjizat), mereka berpaling dan berkata: "(Ini adalah) sihir yang terus menerus".</p>
                    <span class="source">Surat Al Qamar Ayat: 1-2</span>
                </div>
                <p>Bahkan ketika ditunjukkan mukjizat fisik seperti bulan terbelah, mereka tetap ingkar dan menyebutnya sihir.</p>
            </div>

            <div class="content-section">
                <h3>4. Meminta Azab Disegerakan</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka meminta kepadamu supaya segera diturunkan azab.</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 53</span>
                </div>
                <p>Saking sombongnya, mereka menantang agar azab segera turun jika memang Nabi benar.</p>
            </div>

            <hr class="divider">
            <h2>Penutup</h2>
            <p>Sikap keras kepala kaum Musyrikin menunjukkan bahwa masalah mereka bukan pada kurangnya bukti, tetapi pada kesombongan dan penolakan hati (tertutupnya hati) untuk menerima kebenaran.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa tuduhan mereka terhadap Nabi dalam Surat Al Hijr ayat 6?",
                                options: ["Orang yang cerdas", "Orang gila (Majnun)", "Raja", "Orang kaya"],
                                correct: 1,
                                explanation: "Sesungguhnya kamu benar-benar orang gila (innaka lamajnun)."
                            },
                            {
                                question: "Bagaimana reaksi mereka saat melihat bulan terbelah (Al Qamar 2)?",
                                options: ["Langsung beriman", "Takjub dan bersujud", "Berpaling dan berkata 'Ini sihir'", "Lari ketakutan"],
                                correct: 2,
                                explanation: "Mereka berpaling dan berkata: '(Ini adalah) sihir yang terus menerus'."
                            },
                            {
                                question: "Apa permintaan mereka dalam Surat Al Israa' 90?",
                                options: ["Meminta uang", "Meminta mata air memancar dari bumi", "Meminta jabatan", "Meminta istri cantik"],
                                correct: 1,
                                explanation: "Hingga kamu memancarkan mata air dari bumi untuk kami."
                            },
                            {
                                question: "Apa jawaban Nabi ketika diminta mukjizat aneh-aneh (Al Israa' 93)?",
                                options: ["Aku akan mengabulkannya", "Tunggu sebentar", "Maha Suci Tuhanku, bukankah aku ini hanya seorang manusia yang menjadi rasul?", "Itu mudah bagi Allah"],
                                correct: 2,
                                explanation: "Katakanlah: 'Maha Suci Tuhanku, bukankah aku ini hanya seorang manusia yang menjadi rasul?'"
                            },
                            {
                                question: "Mengapa Allah tidak menurunkan mukjizat fisik seperti unta Nabi Saleh kepada Quraisy (Al Israa' 59)?",
                                options: ["Karena Allah tidak mampu", "Karena tanda-tanda itu telah didustakan orang dahulu (dan mereka dibinasakan)", "Karena Nabi tidak meminta", "Karena malaikat sibuk"],
                                correct: 1,
                                explanation: "Melainkan karena tanda-tanda itu telah didustakan oleh orang-orang dahulu (dan jika didustakan lagi, mereka akan langsung dibinasakan)."
                            }
                        ]
                    },
                    {
                        id: 109,
                        title: "Kegundahan Rasulullah SAW & Hiburan Allah",
                        file: "topic_109.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Kegundahan Rasulullah SAW Menghadapi Umatnya</li>
    <li>Allah Memantapkan Hati Rasulullah SAW</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini menggambarkan sisi manusiawi Rasulullah SAW yang merasa sedih dan sempit dada ketika kaumnya menolak dakwah dan mengingkari ayat-ayat Allah. Allah SWT kemudian menurunkan berbagai ayaat untuk menghibur, memantapkan hati, dan menjanjikan kemudahan setelah kesulitan bagi kekasih-Nya tersebut.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Kesedihan Nabi atas Kekafiran Umatnya</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya Kami mengetahui bahwasanya apa yang mereka katakan itu menyedihkan hatimu, (janganlah kamu bersedih hati), karena mereka sebenarnya bukan mendustakan kamu, akan tetapi orang-orang yang zalim itu mengingkari ayat-ayat Allah.</p>
        <span class="source">Surat Al An'aam Ayat: 33</span>
    </div>
    <p>Allah menegaskan bahwa penolakan mereka bukan karena pribadi Nabi (mereka tahu Nabi itu jujur/Al Amin), tapi karena keingkaran terhadap hukum Allah.</p>
    <div class="quran-quote">
        
        <p class="translation">Maka (apakah) barangkali kamu akan membunuh dirimu karena bersedih hati setelah mereka berpaling, sekiranya mereka tidak beriman kepada keterangan ini (Alquran).</p>
        <span class="source">Surat Al Kahf Ayat: 6</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Hiburan dan Janji Allah (Adh Dhuhaa & Al Insyiraah)</h3>
    <div class="quran-quote">
        
        <p class="translation">Tuhanmu tiada meninggalkanmu dan tiada benci kepadamu.</p>
        <span class="source">Surat Adh Dhuhaa Ayat: 3</span>
    </div>
    <div class="quran-quote">
        
        <p class="translation">Karena sesungguhnya sesudah kesulitan itu ada kemudahan. Sesungguhnya sesudah kesulitan itu ada kemudahan.</p>
        <span class="source">Surat Al Insyiraah Ayat: 5-6</span>
    </div>
    <p>Allah bersumpah demi waktu Dhuha dan malam bahwa Dia tidak pernah meninggalkan Nabi. Allah juga melapangkan dada Nabi dan menjanjikan kemudahan yang berlipat ganda setelah kesulitan.</p>
</div>

<div class="content-section">
    <h3>3. Kisah Nabi Terdahulu sebagai Penguat Hati</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan semua kisah dari rasul-rasul Kami ceritakan kepadamu, ialah kisah-kisah yang dengannya Kami teguhkan hatimu...</p>
        <span class="source">Surat Huud Ayat: 120</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Seorang pendakwah wajar merasa sedih jika ajakannya ditolak, namun tidak boleh berputus asa. Kunci keteguhan hati adalah meyakini pertolongan Allah, mengingat perjuangan nabi terdahulu, dan meyakini bahwa setelah kesulitan pasti ada kemudahan.</p>
        `,
                        quiz: [
                            {
                                question: "Mengapa Nabi merasa sedih menurut Surat Al An'aam ayat 33?",
                                options: ["Karena kehilangan harta", "Karena ucapan pendustaan kaumnya", "Karena sakit", "Karena ditinggal sahabat"],
                                correct: 1,
                                explanation: "Sesungguhnya Kami mengetahui bahwasanya apa yang mereka katakan itu menyedihkan hatimu."
                            },
                            {
                                question: "Sumpah Allah dalam Surat Adh Dhuhaa ayat 1-2 adalah demi...",
                                options: ["Matahari dan Bulan", "Langit dan Bumi", "Waktu Dhuha dan Malam", "Masa (Ashr)"],
                                correct: 2,
                                explanation: "Demi waktu matahari sepenggalahan naik (Dhuha), dan demi malam apabila telah sunyi."
                            },
                            {
                                question: "Apa janji Allah setelah kesulitan dalam Surat Al Insyiraah?",
                                options: ["Ada kesulitan lagi", "Ada kemudahan", "Ada kekayaan", "Ada kemenangan perang"],
                                correct: 1,
                                explanation: "Karena sesungguhnya sesudah kesulitan itu ada kemudahan (yusra)."
                            },
                            {
                                question: "Apa tujuan Allah menceritakan kisah rasul-rasul terdahulu (Huud 120)?",
                                options: ["Untuk dongeng sebelum tidur", "Untuk meneguhkan hati Nabi", "Untuk menakuti orang kafir", "Untuk sejarah semata"],
                                correct: 1,
                                explanation: "...ialah kisah-kisah yang dengannya Kami teguhkan hatimu (nutebbitu bihi fuadak)."
                            },
                            {
                                question: "Apakah Allah meninggalkan Nabi saat wahyu terhenti (Adh Dhuhaa 3)?",
                                options: ["Ya, karena Nabi salah", "Tuhanmu tiada meninggalkanmu dan tiada benci kepadamu", "Mungkin saja", "Ya, selamanya"],
                                correct: 1,
                                explanation: "Ma wadda'aka rabbuka wa ma qala (Tuhanmu tiada meninggalkanmu dan tiada benci kepadamu)."
                            }
                        ]
                    },
                    {
                        id: 110,
                        title: "Sikap Musyrikin terhadap Umat Islam",
                        file: "topic_110.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Ejekan Kaum Musyrikin kepada Orang Beriman</li>
    <li>Tanggapan Allah terhadap Ejekan Tersebut</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini menjelaskan perilaku buruk kaum Musyrikin Mekah yang suka mengejek, menertawakan, dan merendahkan orang-orang beriman. Mereka merasa diri mereka lebih baik, padahal di sisi Allah merekalah yang sesat dan akan merugi.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Menertawakan dan Mengedipkan Mata</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya orang-orang yang berdosa, adalah mereka yang menertawakan orang-orang yang beriman. Dan apabila orang-orang yang beriman lewat di hadapan mereka, mereka saling mengedip-ngedipkan matanya.</p>
        <span class="source">Surat Al Muthaffifiin Ayat: 29-30</span>
    </div>
    <p>Ini adalah gambaran arogansi orang kafir yang memandang rendah orang mukmin (yang rata-rata miskin dan lemah di Mekah).</p>
</div>

<div class="content-section">
    <h3>2. Tuduhan Sesat</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan apabila mereka melihat orang-orang mukmin, mereka mengatakan: "Sesungguhnya mereka itu benar-benar orang-orang yang sesat".</p>
        <span class="source">Surat Al Muthaffifiin Ayat: 32</span>
    </div>
    <p>Padahal mereka tidak diutus untuk menjaga atau mengurusi orang-orang mukmin.</p>
</div>

<div class="content-section">
    <h3>3. Balasan di Hari Akhir</h3>
    <div class="quran-quote">
        
        <p class="translation">Maka pada hari ini (kiamat), orang-orang yang beriman menertawakan orang-orang kafir.</p>
        <span class="source">Surat Al Muthaffifiin Ayat: 34</span>
    </div>
    <p>Keadaan akan berbalik. Orang beriman akan duduk di atas dipan-dipan (Araik) sambil memandang kenikmatan surga, sementara orang kafir mendapat balasan atas ejekan mereka.</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Sikap sombong dan suka mengejek adalah ciri orang yang 'Mujrim' (berdosa). Orang beriman diajarkan untuk bersabar karena kemenangan akhir ada di tangan mereka.</p>
        `,
                        quiz: [
                            {
                                question: "Apa sikap orang berdosa terhadap orang beriman di dunia (Al Muthaffifiin 29)?",
                                options: ["Menolong mereka", "Menghormati mereka", "Menertawakan mereka", "Memberi uang"],
                                correct: 2,
                                explanation: "Sesungguhnya orang-orang yang berdosa, adalah mereka yang menertawakan orang-orang yang beriman."
                            },
                            {
                                question: "Apa arti 'Yataghamazun' dalam ayat 30?",
                                options: ["Saling memukul", "Saling mengedip-ngedipkan mata (mengejek)", "Saling bersalaman", "Saling berpelukan"],
                                correct: 1,
                                explanation: "Dan apabila orang-orang yang beriman lewat... mereka saling mengedip-ngedipkan matanya."
                            },
                            {
                                question: "Apa tuduhan mereka kepada orang mukmin (Al Muthaffifiin 32)?",
                                options: ["Orang-orang kaya", "Orang-orang gila", "Orang-orang yang sesat", "Orang-orang pintar"],
                                correct: 2,
                                explanation: "Mereka mengatakan: 'Sesungguhnya mereka itu benar-benar orang-orang yang sesat'."
                            },
                            {
                                question: "Siapa yang akan tertawa pada hari kiamat (Al Muthaffifiin 34)?",
                                options: ["Orang kafir", "Orang beriman", "Malaikat Malik", "Tidak ada"],
                                correct: 1,
                                explanation: "Maka pada hari ini (kiamat), orang-orang yang beriman menertawakan orang-orang kafir."
                            },
                            {
                                question: "Apakah orang berdosa diutus untuk menjaga orang mukmin?",
                                options: ["Ya, tentu saja", "Tidak", "Kadang-kadang", "Hanya pemimpin mereka"],
                                correct: 1,
                                explanation: "Padahal orang-orang yang berdosa itu tidak dikirim untuk penjaga bagi orang-orang mukmin."
                            }
                        ]
                    },
                    {
                        id: 111,
                        title: "Peristiwa Isra' Mi'raj",
                        file: "topic_111.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Perjalanan Isra' dari Masjidil Haram ke Masjidil Aqsha</li>
    <li>Mi'raj dan Sidratul Muntaha</li>
    <li>Melihat Tanda-tanda Kebesaran Allah</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas peristiwa luar biasa Isra' dan Mi'raj. Isra' adalah perjalanan malam Nabi dari Mekah ke Palestina (Masjidil Aqsha), sedangkan Mi'raj adalah naiknya beliau ke langit tinggi hingga Sidratul Muntaha untuk menerima perintah shalat dan melihat tanda-tanda kebesaran Allah.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Isra': Perjalanan Malam yang Suci</h3>
    <div class="quran-quote">
        
        <p class="translation">Maha Suci Allah, yang telah memperjalankan hamba-Nya pada suatu malam dari Masjidil Haram ke Masjidil Aqsha...</p>
        <span class="source">Surat Al Israa' Ayat: 1</span>
    </div>
    <div class="note-box">
        <p><strong>Masjidil Aqsha:</strong> Diberkahi sekelilingnya (Palestina) karena banyaknya Nabi yang diutus di sana dan kesuburan tanahnya.</p>
    </div>
</div>

<div class="content-section">
    <h3>2. Mi'raj: Naik ke Langit Tinggi</h3>
    <p>Peristiwa Mi'raj dijelaskan dalam Surat An Najm. Nabi melihat Jibril dalam rupa aslinya dan melihat keajaiban alam malakut.</p>
    <div class="quran-quote">
        
        <p class="translation">Dan sesungguhnya Muhammad telah melihat Jibril itu (dalam rupanya yang asli) pada waktu yang lain. (Yaitu) di Sidratil Muntaha.</p>
        <span class="source">Surat An Najm Ayat: 13-14</span>
    </div>
    <p>Sidratul Muntaha adalah tempat tertinggi yang tak bisa dilewati makhluk lain, di dekatnya ada Surga Ma'wa.</p>
</div>

<div class="content-section">
    <h3>3. Validitas Penglihatan Nabi</h3>
    <div class="quran-quote">
        
        <p class="translation">Penglihatannya (Muhammad) tidak berpaling dari yang dilihatnya itu dan tidak (pula) melampauinya.</p>
        <span class="source">Surat An Najm Ayat: 17</span>
    </div>
    <p>Apa yang Nabi sampaikan bukan khayalan atau dusta. Beliau benar-benar melihat tanda-tanda kekuasaan Tuhan yang paling besar (Ayat 18).</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Isra' Mi'raj adalah mukjizat besar yang menguji keimanan. Bagi Abu Bakar dkk, ini adalah kebenaran mutlak. Bagi kaum musyrikin, ini bahan ejekan. Namun, Allah menegaskan kebenaran peristiwa ini dalam Al-Qur'an.</p>
        `,
                        quiz: [
                            {
                                question: "Dari mana kemana perjalanan Isra' Nabi Muhammad SAW (Al Israa' 1)?",
                                options: ["Mekah ke Madinah", "Masjidil Haram ke Masjidil Aqsha", "Bumi ke Langit", "Masjid Nabawi ke Masjidil Haram"],
                                correct: 1,
                                explanation: "Dari Masjidil Haram (Mekah) ke Masjidil Aqsha (Palestina)."
                            }
                            ,
                            {
                                question: "Apa arti 'Subhana' di awal ayat Isra'?",
                                options: ["Maha Besar", "Maha Suci", "Segala Puji", "Maha Pengasih"],
                                correct: 1,
                                explanation: "Subhana artinya Maha Suci Allah. Biasanya digunakan untuk hal yang menakjubkan."
                            },
                            {
                                question: "Di mana Nabi melihat Jibril dalam rupa aslinya yang kedua kali (An Najm 14)?",
                                options: ["Gua Hira", "Bukit Tursina", "Sidratul Muntaha", "Ka'bah"],
                                correct: 2,
                                explanation: "(Yaitu) di Sidratil Muntaha."
                            },
                            {
                                question: "Apa yang ada di dekat Sidratul Muntaha (An Najm 15)?",
                                options: ["Surga Ma'wa", "Neraka Jahim", "Arsy", "Baitul Makmur"],
                                correct: 0,
                                explanation: "Di dekatnya ada surga tempat tinggal (Jannatul Ma'wa)."
                            },
                            {
                                question: "Apakah penglihatan Nabi saat Mi'raj itu palsu (An Najm 17)?",
                                options: ["Ya, hanya mimpi", "Tidak, penglihatannya tidak berpaling dan tidak melampaui", "Mungkin halusinasi", "Beliau pingsan"],
                                correct: 1,
                                explanation: "Penglihatannya (Muhammad) tidak berpaling dari yang dilihatnya itu dan tidak (pula) melampauinya."
                            }
                        ]
                    }
                ]
            }
            , {
                id: "subject-5-4",
                title: "Pokok Bahasan 4: Hijrah",
                topics: [
                    {
                        id: 112,
                        title: "Peristiwa Menjelang Hijrah",
                        file: "topic_112.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Bai'at Aqabah Kedua</li>
    <li>Rencana Jahat Musyrikin Mekah</li>
    <li>Konspirasi Membunuh Nabi</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas situasi genting menjelang Hijrah Nabi ke Madinah. Dimulai dari Bai'at Aqabah Kedua di mana kaum Anshar berjanji setia melindungi Nabi, hingga respon kaum Musyrikin yang mengadakan pertemuan di Darun Nadwah untuk merencanakan pembunuhan Nabi.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Bai'at Aqabah Kedua</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan ingatlah karunia Allah kepadamu dan perjanjian-Nya yang telah diikat-Nya dengan kamu...</p>
        <span class="source">Surat Al Maaidah Ayat: 7</span>
    </div>
    <p>Ini merujuk pada sumpah setia kaum Muslimin (khususnya Anshar) untuk mendengar dan taat kepada Nabi dalam segala keadaan.</p>
</div>

<div class="content-section">
    <h3>2. Rencana Jahat Kaum Musyrikin</h3>
    <div class="quran-quote">
        
        <p class="translation">Bahkan mereka telah menetapkan satu tipu daya (jahat), maka sesungguhnya Kami menetapkan pula.</p>
        <span class="source">Surat Az Zukhruf Ayat: 79</span>
    </div>
    <p>Mereka berkumpul untuk menyusun strategi menghentikan dakwah Nabi. Namun, Allah memiliki rencana yang lebih kuat.</p>
</div>

<div class="content-section">
    <h3>3. Konspirasi Pembunuhan</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan (ingatlah), ketika orang-orang kafir (Quraisy) memikirkan daya upaya terhadapmu untuk menangkap dan memenjarakanmu atau membunuhmu, atau mengusirmu.</p>
        <span class="source">Surat Al Anfaal Ayat: 30</span>
    </div>
    <p>Tiga opsi mereka: penjara, bunuh, atau usir. Akhirnya mereka memilih opsi membunuh (tiap kabilah mengirim wakil), tapi Allah menggagalkannya dengan memerintahkan Hijrah.</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Momen ini adalah titik balik sejarah Islam. Kesetiaan kaum Anshar dan perlindungan Allah dari makar Quraisy membuka jalan bagi tegaknya Negara Madinah.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa isi perjanjian dalam Bai'at Aqabah menurut Al Maaidah ayat 7?",
                                options: ["Kami dengar dan kami taat", "Kami akan berperang saja", "Kami akan memberi harta", "Kami akan diam"],
                                correct: 0,
                                explanation: "Ketika kamu mengatakan: 'Kami dengar dan kami taat' (Sami'na wa atha'na)."
                            },
                            {
                                question: "Apa tiga rencana jahat Quraisy terhadap Nabi dalam Surat Al Anfaal ayat 30?",
                                options: ["Menangkap, Membunuh, Mengusir", "Menyuap, Mengangkat Raja, Mengusir", "Membunuh, Membakar, Menenggelamkan", "Tidak ada rencana"],
                                correct: 0,
                                explanation: "Untuk menangkap (memenjara), membunuh, atau mengusirmu."
                            },
                            {
                                question: "Siapakah 'sebaik-baik pembalas tipu daya' menurut Al Anfaal ayat 30?",
                                options: ["Rasulullah", "Malaikat", "Allah", "Kaum Anshar"],
                                correct: 2,
                                explanation: "Dan Allah sebaik-baik pembalas tipu daya (Wallaahu khairul maakirin)."
                            },
                            {
                                question: "Apa yang dilakukan malaikat terhadap bisikan jahat mereka (Az Zukhruf 80)?",
                                options: ["Membiarkannya", "Mencatat di sisi mereka", "Melaporkan ke Nabi", "Menghapusnya"],
                                correct: 1,
                                explanation: "Dan utusan-utusan (malaikat) Kami selalu mencatat di sisi mereka."
                            },
                            {
                                question: "Di mana kaum Musyrikin berkumpul untuk merencanakan makar?",
                                options: ["Masjidil Haram", "Darun Nadwah", "Gua Hira", "Rumah Abu Bakar"],
                                correct: 1,
                                explanation: "Mereka berkumpul di Darun Nadwah (tempat pertemuan pembesar Quraisy)."
                            }
                        ]
                    },
                    {
                        id: 113,
                        title: "Perintah, Alasan, dan Hikmah Hijrah",
                        file: "topic_113.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Perintah Hijrah</li>
    <li>Keutamaan Muhajirin dan Anshar</li>
    <li>Peristiwa di Gua Tsur</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini menjelaskan perintah Allah untuk berhijrah bagi mereka yang tertindas, janji Allah bagi orang yang berhijrah, serta kisah detik-detik menegangkan saat Nabi dan Abu Bakar bersembunyi di Gua Tsur dikejar musuh.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Mengapa Harus Hijrah?</h3>
    <div class="quran-quote">
        
        <p class="translation">Bukankah bumi Allah itu luas, sehingga kamu dapat berhijrah di bumi itu?</p>
        <span class="source">Surat An Nisaa' Ayat: 97</span>
    </div>
    <p>Bagi mereka yang menzalimi diri sendiri (tetap tinggal di negeri kafir padahal mampu hijrah), tempat kembalinya adalah neraka.</p>
</div>

<div class="content-section">
    <h3>2. Janji Allah bagi Muhajirin</h3>
    <div class="quran-quote">
        
        <p class="translation">Siapa berhijrah di jalan Allah, niscaya mereka mendapati di muka bumi ini tempat hijrah yang luas dan rezeki yang banyak.</p>
        <span class="source">Surat An Nisaa' Ayat: 100</span>
    </div>
</div>

<div class="content-section">
    <h3>3. Peristiwa di Gua Tsur</h3>
    <div class="quran-quote">
        
        <p class="translation">Di waktu dia berkata kepada temannya: "Janganlah kamu berduka cita, sesungguhnya Allah beserta kita."</p>
        <span class="source">Surat At Taubah Ayat: 40</span>
    </div>
    <p>Allah menolong Nabi saat di Gua Tsur dengan ketenangan (sakinah) dan tentara yang tidak terlihat (malaikat), sehingga musuh gagal menemukannya meski sudah sangat dekat.</p>
</div>

<div class="content-section">
    <h3>4. Pujian untuk Muhajirin dan Anshar</h3>
    <div class="quran-quote">
        
        <p class="translation">Orang-orang yang terdahulu lagi yang pertama-tama (masuk Islam) dari golongan Muhajirin dan Anshar... Allah ridha kepada mereka dan merekapun ridha kepada Allah.</p>
        <span class="source">Surat At Taubah Ayat: 100</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Hijrah bukan sekadar pindah tempat, tapi perjuangan mempertahankan iman. Allah menjanjikan keridhaan dan surga bagi mereka yang berkorban harta dan jiwa untuk Hijrah.</p>
                        `,
                        quiz: [
                            {
                                question: "Apa alasan malaikat mencela orang yang tidak mau hijrah (An Nisaa' 97)?",
                                options: ["Karena bumi Allah sempit", "Karena mereka sakit", "Karena bumi Allah luas (bisa hijrah)", "Karena mereka kaya"],
                                correct: 2,
                                explanation: "Bukankah bumi Allah itu luas, sehingga kamu dapat berhijrah di bumi itu?"
                            }

                            ,
                            {
                                question: "Siapakah 'teman' Nabi yang dimaksud dalam Surat At Taubah ayat 40?",
                                options: ["Umar bin Khattab", "Ali bin Abi Thalib", "Abu Bakar Ash Shiddiq", "Utsman bin Affan"],
                                correct: 2,
                                explanation: "Dia berkata kepada temannya (sahibih), yaitu Abu Bakar saat di Gua Tsur."
                            },
                            {
                                question: "Apa yang Allah turunkan kepada Nabi saat cemas di Gua Tsur?",
                                options: ["Harta karun", "Ketenangan (Sakinah)", "Makanan", "Senjata"],
                                correct: 1,
                                explanation: "Maka Allah menurunkan keterangan-Nya (sakinah) kepada Muhammad."
                            },
                            {
                                question: "Apa janji Allah bagi orang yang berhijrah (An Nisaa' 100)?",
                                options: ["Menjadi raja", "Mendapati tempat luas dan rezeki banyak", "Hidup abadi", "Tidak akan sakit"],
                                correct: 1,
                                explanation: "Niscaya mereka mendapati di muka bumi ini tempat hijrah yang luas dan rezeki yang banyak."
                            },
                            {
                                question: "Siapakah 'Assabiqunal Awwalun' (At Taubah 100)?",
                                options: ["Orang yang terakhir masuk Islam", "Orang yang terdahulu masuk Islam (Muhajirin & Anshar)", "Orang munafik", "Orang kafir"],
                                correct: 1,
                                explanation: "Orang-orang yang terdahulu lagi yang pertama-tama (masuk Islam) dari golongan Muhajirin dan Anshar."
                            }
                        ]
                    }
                ]
            }
            , {
                id: "subject-5-5",
                title: "Pokok Bahasan 5: Periode Madinah",
                topics: [
                    {
                        id: 114,
                        title: "Sikap Ahli Kitab dan Orang Arab Badawi",
                        file: "topic_114.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Dialog dengan Ahli Kitab</li>
    <li>Sikap Ahli Kitab terhadap Rasulullah</li>
    <li>Mubahalah dengan Nasrani Najran</li>
    <li>Sikap Orang Arab Badawi</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas interaksi Nabi Muhammad SAW dengan Ahli Kitab (Yahudi dan Nasrani) serta orang-orang Arab Badawi di Madinah. Terdapat ajakan untuk mencari titik temu (Kalimatun Sawa'), bantahan terhadap klaim mereka, tantangan Mubahalah, dan teguran terhadap klaim iman orang Badawi yang belum meresap ke hati.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Ajakan kepada Kalimatun Sawa'</h3>
    <div class="quran-quote">
        
        <p class="translation">Katakanlah: "Hai Ahli Kitab, marilah (berpegang) kepada suatu kalimat (ketetapan) yang tidak ada perselisihan antara kami dan kamu, bahwa tidak kita sembah kecuali Allah dan tidak kita persekutukan Dia dengan sesuatupun..."</p>
        <span class="source">Surat Ali 'Imraan Ayat: 64</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Bantahan terhadap Klaim Yahudi & Nasrani</h3>
    <div class="quran-quote">
        
        <p class="translation">Hai Ahli Kitab, mengapa kamu bantah-membantah tentang hal Ibrahim, padahal Taurat dan Injil tidak diturunkan melainkan sesudah Ibrahim. Apakah kamu tidak berpikir?</p>
        <span class="source">Surat Ali 'Imraan Ayat: 65</span>
    </div>
    <p>Mereka saling klaim Ibrahim adalah golongan mereka, padahal Ibrahim hidup jauh sebelum Musa (Taurat) dan Isa (Injil).</p>
</div>

<div class="content-section">
    <h3>3. Tantangan Mubahalah</h3>
    <div class="quran-quote">
        
        <p class="translation">Siapa yang membantahmu tentang kisah Isa sesudah datang ilmu (yang meyakinkan kamu), maka katakanlah (kepadanya): "Mari kita memanggil anak-anak kami dan anak-anak kamu... kemudian kita bermubahalah (berdoa bersungguh-sungguh) agar laknat Allah ditimpakan kepada orang-orang yang dusta."</p>
        <span class="source">Surat Ali 'Imraan Ayat: 61</span>
    </div>
    <p>Ayat ini turun terkait utusan Nasrani Najran. Mereka menolak Mubahalah karena takut akan kebenarannya.</p>
</div>

<div class="content-section">
    <h3>4. Iman Orang Arab Badawi</h3>
    <div class="quran-quote">
        
        <p class="translation">Orang-orang Arab Badui itu berkata: "Kami telah beriman". Katakanlah: "Kamu belum beriman, tapi katakanlah 'kami telah tunduk', karena iman itu belum masuk ke dalam hatimu..."</p>
        <span class="source">Surat Al Hujuraat Ayat: 14</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Islam mengajarkan dialog yang adil (Kalimatun Sawa') namun tegas dalam prinsip tauhid. Sikap orang Badawi menunjukkan bahwa Islam bukan sekadar pengakuan lisan, tapi keyakinan yang menghunjam di hati.</p>
        `,
                        quiz: [
                            {
                                question: "Apa inti ajakan 'Kalimatun Sawa' dalam Ali 'Imraan 64?",
                                options: ["Menyatukan semua agama", "Hanya menyembah Allah dan tidak menyekutukan-Nya", "Mengikuti syariat Yahudi", "Membagi wilayah kekuasaan"],
                                correct: 1,
                                explanation: "Bahwa tidak kita sembah kecuali Allah dan tidak kita persekutukan Dia dengan sesuatupun."
                            },
                            {
                                question: "Mengapa klaim Yahudi/Nasrani tentang Ibrahim dibantah (Ali 'Imraan 65)?",
                                options: ["Karena Ibrahim bukan orang Arab", "Karena Taurat dan Injil turun sesudah Ibrahim", "Karena Ibrahim tidak punya kitab", "Karena Ibrahim orang Palestina"],
                                correct: 1,
                                explanation: "Padahal Taurat dan Injil tidak diturunkan melainkan sesudah Ibrahim."
                            },
                            {
                                question: "Apa itu Mubahalah (Ali 'Imraan 61)?",
                                options: ["Perang tanding", "Debat terbuka", "Saling mendoakan laknat bagi yang dusta", "Tukar menukar tawanan"],
                                correct: 2,
                                explanation: "Kemudian kita bermubahalah... agar laknat Allah ditimpakan kepada orang-orang yang dusta."
                            },
                            {
                                question: "Apa respon Nabi terhadap orang Badawi yang mengaku beriman (Al Hujuraat 14)?",
                                options: ["Membenarkan mereka", "Mengatakan 'Kamu belum beriman, tapi katakanlah kami telah tunduk (Islam)'", "Mengusir mereka", "Memberi hadiah"],
                                correct: 1,
                                explanation: "Katakanlah: 'Kamu belum beriman, tapi katakanlah kami telah tunduk', karena iman itu belum masuk ke dalam hatimu."
                            },
                            {
                                question: "Siapakah yang paling dekat persahabatannya dengan orang mukmin (Al Maaidah 82)?",
                                options: ["Orang Yahudi", "Orang Musyrik", "Orang yang berkata 'Kami Nasrani'", "Orang Majusi"],
                                correct: 2,
                                explanation: "Sesungguhnya kamu dapati yang paling dekat persahabatannya... ialah orang-orang yang berkata: 'Sesungguhnya kami ini orang Nasrani'."
                            }
                        ]
                    },
                    {
                        id: 115,
                        title: "Perpindahan Arah Kiblat",
                        file: "topic_115.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Latar Belakang Pemindahan Kiblat</li>
    <li>Reaksi Orang Kurang Akal (Sufaha)</li>
    <li>Kiblat: Ujian Ketaatan</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas peristiwa besar pemindahan arah kiblat dari Baitul Maqdis (Palestina) ke Masjidil Haram (Ka'bah, Mekah). Peristiwa ini menjadi ujian keimanan bagi kaum muslimin dan bahan ejekan bagi kaum Yahudi dan Munafik.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Perintah Memalingkan Wajah ke Masjidil Haram</h3>
    <div class="quran-quote">
        
        <p class="translation">Sungguh Kami (sering) melihat mukamu menengadah ke langit, maka sungguh Kami akan memalingkan kamu ke kiblat yang kamu sukai. Palingkanlah mukamu ke arah Masjidil Haram.</p>
        <span class="source">Surat Al Baqarah Ayat: 144</span>
    </div>
    <p>Rasulullah sangat mendambakan Ka'bah (kiblat Nabi Ibrahim) sebagai kiblat umat Islam.</p>
</div>

<div class="content-section">
    <h3>2. Reaksi Orang-Orang 'Sufaha' (Kurang Akal)</h3>
    <div class="quran-quote">
        
        <p class="translation">Orang-orang yang kurang akalnya di antara manusia akan berkata: "Apakah yang memalingkan mereka (umat Islam) dari kiblatnya (Baitul Maqdis) yang dahulu mereka telah berkiblat kepadanya?" Katakanlah: "Kepunyaan Allah-lah timur dan barat..."</p>
        <span class="source">Surat Al Baqarah Ayat: 142</span>
    </div>
</div>

<div class="content-section">
    <h3>3. Ujian Ketaatan</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan Kami tidak menetapkan kiblat yang menjadi kiblatmu (sekarang) melainkan agar Kami mengetahui (supaya nyata) siapa yang mengikuti Rasul dan siapa yang membelot...</p>
        <span class="source">Surat Al Baqarah Ayat: 143</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Kiblat bukan sekadar arah fisik, tapi simbol ketaatan total kepada perintah Allah. Pemindahan ke Ka'bah juga menegaskan kemandirian umat Islam (Ummatan Wasathan).</p>
        `,
                        quiz: [
                            {
                                question: "Ke mana arah kiblat umat Islam sebelum dipindah ke Ka'bah?",
                                options: ["Masjid Nabawi", "Baitul Maqdis (Palestina)", "Gunung Tursina", "Yaman"],
                                correct: 1,
                                explanation: "Sebelum ke Masjidil Haram, kiblat menghadap ke Baitul Maqdis selama sekitar 16-17 bulan di Madinah."
                            },
                            {
                                question: "Apa sebutan Al-Qur'an bagi orang yang mempertanyakan perpindahan kiblat (Al Baqarah 142)?",
                                options: ["Al-Kafirun (Orang Kafir)", "As-Sufaha (Orang Kurang Akal)", "Al-Munafiqun (Orang Munafik)", "Ad-Dhalun (Orang Sesat)"],
                                correct: 1,
                                explanation: "Orang-orang yang kurang akalnya (As-Sufaha) di antara manusia akan berkata..."
                            },
                            {
                                question: "Apa tujuan ujian perpindahan kiblat menurut Al Baqarah 143?",
                                options: ["Untuk membedakan siapa yang mengikuti Rasul dan siapa yang membelot", "Untuk menyusahkan umat", "Untuk mencari arah mata angin", "Untuk membedakan Arab dan non-Arab"],
                                correct: 0,
                                explanation: "Agar Kami mengetahui (supaya nyata) siapa yang mengikuti Rasul dan siapa yang membelot (berbalik ke belakang)."
                            },
                            {
                                question: "Apa yang dilakukan Rasulullah sebelum turun perintah pindah kiblat (Al Baqarah 144)?",
                                options: ["Menangis", "Sering menengadah ke langit (berdoa)", "Bertanya kepada Yahudi", "Diam saja"],
                                correct: 1,
                                explanation: "Sungguh Kami (sering) melihat mukamu menengadah ke langit."
                            },
                            {
                                question: "Milik siapakah Timur dan Barat itu (Al Baqarah 142)?",
                                options: ["Milik manusia", "Milik Allah", "Milik Malaikat", "Milik Penguasa"],
                                correct: 1,
                                explanation: "Katakanlah: 'Kepunyaan Allah-lah timur dan barat'."
                            }
                        ]
                    },
                    {
                        id: 116,
                        title: "Perang Badar",
                        file: "topic_116.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Latar Belakang & Motivasi</li>
    <li>Pertolongan Allah (Malaikat)</li>
    <li>Kekalahan Musyrikin</li>
    <li>Harta Rampasan (Ghanimah)</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas Perang Badar Kubra, pertempuran besar pertama dalam Islam. Materi mencakup janji Allah atas salah satu dari dua kelompok (kafilah dagang atau pasukan perang), turunnya ribuan malaikat sebagai bala bantuan, dan aturan pembagian harta rampasan perang.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Janji Kemenangan</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan (ingatlah), ketika Allah menjanjikan kepadamu bahwa salah satu dari dua golongan (yang kamu hadapi) adalah untukmu, sedang kamu menginginkan bahwa yang tidak mempunyai kekekuatan senjatalah yang untukmu...</p>
        <span class="source">Surat Al Anfaal Ayat: 7</span>
    </div>
    <p>Umat Islam ingin kafilah dagang (harta), tapi Allah ingin pertempuran (untuk memenangkan kebenaran).</p>
</div>

<div class="content-section">
    <h3>2. Bala Bantuan Malaikat</h3>
    <div class="quran-quote">
        
        <p class="translation">(Ingatlah), ketika kamu memohon pertolongan kepada Tuhanmu, lalu Dia kabulkan bagimu: "Sesungguhnya Aku akan datangkan bantuan kepadamu dengan seribu malaikat yang datang berturut-turut."</p>
        <span class="source">Surat Al Anfaal Ayat: 9</span>
    </div>
    <p>Dalam ayat lain (Ali 'Imraan 124-125), disebutkan jumlahnya mencapai 3000 bahkan 5000 malaikat.</p>
</div>

<div class="content-section">
    <h3>3. Allah yang Melempar</h3>
    <div class="quran-quote">
        
        <p class="translation">Maka (yang sebenarnya) bukan kamu yang membunuh mereka, akan tetapi Allahlah yang membunuh mereka, dan bukan kamu yang melempar ketika kamu melempar, tetapi Allahlah yang melempar.</p>
        <span class="source">Surat Al Anfaal Ayat: 17</span>
    </div>
</div>

<div class="content-section">
    <h3>4. Ketentuan Ghanimah</h3>
    <div class="quran-quote">
        
        <p class="translation">Ketahuilah, sesungguhnya apa yang kamu peroleh sebagai rampasan perang, maka sesungguhnya seperlima untuk Allah, Rasul, kerabat Rasul, anak-anak yatim, orang-orang miskin dan ibnu sabil...</p>
        <span class="source">Surat Al Anfaal Ayat: 41</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Perang Badar adalah 'Yaumul Furqan' (Hari Pembeda). Kemenangan ini bukan karena jumlah pasukan, tapi semata-mata pertolongan Allah bagi mereka yang sabar dan bertakwa.</p>
        `,
                        quiz: [
                            {
                                question: "Berapa jumlah malaikat yang dijanjikan dalam Al Anfaal ayat 9?",
                                options: ["100", "1000", "500", "10.000"],
                                correct: 1,
                                explanation: "Sesungguhnya Aku akan datangkan bantuan kepadamu dengan seribu (alf) malaikat."
                            },
                            {
                                question: "Apa yang diinginkan kaum muslimin menurut Al Anfaal ayat 7?",
                                options: ["Pasukan bersenjata lengkap", "Yang tidak mempunyai kekuatan senjata (kafilah dagang)", "Mati syahid", "Kekuasaan Mekah"],
                                correct: 1,
                                explanation: "Sedang kamu menginginkan bahwa yang tidak mempunyai kekekuatan senjatalah (ghaira dzatisy syaukah) yang untukmu."
                            },
                            {
                                question: "Siapa hakikatnya yang melempar panah/pasir saat perang menurut Al Anfaal 17?",
                                options: ["Nabi Muhammad", "Para Sahabat", "Allah", "Malaikat Jibril"],
                                correct: 2,
                                explanation: "Dan bukan kamu yang melempar ketika kamu melempar, tetapi Allahlah yang melempar."
                            },
                            {
                                question: "Berapa bagian Ghanimah untuk Allah dan Rasul (Al Anfaal 41)?",
                                options: ["Setengah (1/2)", "Seperempat (1/4)", "Seperlima (1/5)", "Seluruhnya"],
                                correct: 2,
                                explanation: "Maka sesungguhnya seperlima (khumus) untuk Allah, Rasul..."
                            },
                            {
                                question: "Disebut apakah hari pertemuan dua pasukan di Badar (Al Anfaal 41)?",
                                options: ["Yaumul Fath", "Yaumul Ba'ts", "Yaumul Furqan", "Yaumul Hisab"],
                                correct: 2,
                                explanation: "Yaitu di hari Furqan (Pembeda), yaitu di hari bertemunya dua pasukan."
                            }
                        ]
                    }
                    ,
                    {
                        id: 117,
                        title: "Perang Melawan Bani Nadhir dan Qainuqa",
                        file: "topic_117.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Pengusiran Bani Nadhir</li>
    <li>Pengusiran Bani Qainuqa</li>
    <li>Harta Rampasan (Fa'i)</li>
    <li>Koalisi Munafik dan Yahudi</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas pengusiran Yahudi Bani Nadhir dan Bani Qainuqa dari Madinah karena pengkhianatan mereka (melanggar Piagam Madinah). Juga dibahas tentang harta Fa'i dan sifat orang munafik yang berjanji palsu kepada Yahudi.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Pengusiran Bani Nadhir</h3>
    <div class="quran-quote">
        
        <p class="translation">Dialah yang mengeluarkan orang-orang kafir di antara ahli kitab dari kampung-kampung mereka pada saat pengusiran yang pertama... Dia lemparkan rasa takut ke dalam hati mereka...</p>
        <span class="source">Surat Al Hasyr Ayat: 2</span>
    </div>
    <p>Mereka diusir karena berencana membunuh Nabi SAW. Mereka menghancurkan rumah mereka sendiri sebelum pergi.</p>
</div>

<div class="content-section">
    <h3>2. Sifat Orang Munafik</h3>
    <div class="quran-quote">
        
        <p class="translation">Apakah kamu tidak memperhatikan orang-orang munafik yang berkata kepada saudara-saudara mereka yang kafir di antara ahli kitab: "Sesungguhnya jika kamu diusir niscaya kamipun akan keluar bersamamu..." Dan Allah menyaksikan bahwa sesungguhnya mereka benar-benar pendusta.</p>
        <span class="source">Surat Al Hasyr Ayat: 11</span>
    </div>
    <p>Abdullah bin Ubay (tokoh munafik) menjanjikan bantuan kepada Bani Nadhir tapi tidak ditepati.</p>
</div>

<div class="content-section">
    <h3>3. Harta Fa'i</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan apa saja harta rampasan (fai-i) yang diberikan Allah kepada Rasul-Nya (dari harta benda) mereka, maka untuk mendapatkannya kamu tidak mengerahkan seekor kudapun dan (tidak pula) seekor unta...</p>
        <span class="source">Surat Al Hasyr Ayat: 6</span>
    </div>
    <p>Fa'i adalah harta yang didapat tanpa pertempuran/kekerasan, beda dengan Ghanimah.</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Kisah ini menunjukkan akibat dari pengkhianatan janji dan rapuhnya koalisi antara orang kafir dan munafik. Allah Maha Kuasa menghukum mereka dari arah yang tidak disangka (rasa takut).</p>
        `,
                        quiz: [
                            {
                                question: "Siapakah Ahli Kitab yang dimaksud dalam Surat Al Hasyr ayat 2?",
                                options: ["Bani Quraizhah", "Bani Nadhir", "Nasrani Najran", "Yahudi Khaibar"],
                                correct: 1,
                                explanation: "Yang dimaksud dengan ahli kitab ialah orang-orang Yahudi Bani Nadhir."
                            },
                            {
                                question: "Apa perbedaan Fa'i dan Ghanimah?",
                                options: ["Fa'i didapat dengan perang, Ghanimah tanpa perang", "Fa'i didapat tanpa perang, Ghanimah dengan perang", "Fa'i haram, Ghanimah halal", "Sama saja"],
                                correct: 1,
                                explanation: "Fa'i: harta rampasan yang diperoleh tanpa terjadi perang. Ghanimah diperoleh setelah terjadi pertempuran."
                            },
                            {
                                question: "Bagaimana sikap orang Munafik terhadap Bani Nadhir (Al Hasyr 11)?",
                                options: ["Membantu sepenuh hati", "Ikut diusir bersama mereka", "Berjanji palsu akan membantu", "Memerangi Bani Nadhir"],
                                correct: 2,
                                explanation: "Dan Allah menyaksikan bahwa sesungguhnya mereka benar-benar pendusta (dalam janji bantuannya)."
                            },
                            {
                                question: "Apa hukuman bagi Bani Nadhir di dunia menurut Al Hasyr ayat 3?",
                                options: ["Dibunuh semua", "Diusir (Jala')", "Dihancurkan rumahnya oleh petir", "Tenggelam"],
                                correct: 1,
                                explanation: "Dan jika tidaklah karena Allah telah menetapkan pengusiran (Al-Jala') terhadap mereka..."
                            },
                            {
                                question: "Siapakah yang melemparkan rasa takut ke hati Bani Nadhir (Al Hasyr 2)?",
                                options: ["Pasukan Muslim", "Malaikat", "Allah", "Setan"],
                                correct: 2,
                                explanation: "Dan Allah melemparkan ketakutan (sehingga menyerah) dalam hati mereka."
                            }
                        ]
                    },
                    {
                        id: 118,
                        title: "Perang Uhud",
                        file: "topic_118.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Keadaan Pasukan & Ujian Kekalahan</li>
    <li>Larangan Bersikap Lemah</li>
    <li>Sebab Kekalahan (Melanggar Perintah Rasul)</li>
    <li>Kabar Bohong Wafatnya Rasulullah</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas Perang Uhud (Tahun 3 H), di mana kaum muslimin mengalami kekalahan sementara akibat ketidaktaatan sebagian pasukan pemanah. Ayat-ayat ini turun untuk menghibur, menegur, dan memberikan pelajaran berharga bagi umat Islam.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Jangan Bersikap Lemah</h3>
    <div class="quran-quote">
        
        <p class="translation">Janganlah kamu bersikap lemah, dan janganlah (pula) kamu bersedih hati, padahal kamulah orang-orang yang paling tinggi (derajatnya), jika kamu orang-orang yang beriman.</p>
        <span class="source">Surat Ali 'Imraan Ayat: 139</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Ujian Syahid dan Pembersih Dosa</h3>
    <div class="quran-quote">
        
        <p class="translation">Jika kamu (pada perang Uhud) mendapat luka, maka sesungguhnya kaum (kafir) itupun (pada perang Badar) mendapat luka yang serupa... agar sebagian kamu dijadikan-Nya (gugur sebagai) syuhada'.</p>
        <span class="source">Surat Ali 'Imraan Ayat: 140</span>
    </div>
</div>

<div class="content-section">
    <h3>3. Sebab Kekalahan: Cinta Dunia</h3>
    <div class="quran-quote">
        
        <p class="translation">...sampai pada saat kamu lemah dan berselisih dalam urusan itu dan mendurhakai perintah (Rasul) sesudah Allah memperlihatkan kepadamu apa yang kamu sukai (harta rampasan). Di antaramu ada orang yang menghendaki dunia...</p>
        <span class="source">Surat Ali 'Imraan Ayat: 152</span>
    </div>
    <p>Ini merujuk pada pasukan pemanah yang turun dari bukit karena tergiur Ghanimah.</p>
</div>

<div class="content-section">
    <h3>4. Isu Wafatnya Rasulullah</h3>
    <div class="quran-quote">
        
        <p class="translation">Muhammad itu tidak lain hanyalah seorang rasul, sungguh telah berlalu sebelumnya beberapa orang rasul. Apakah jika dia wafat atau dibunuh kamu berbalik ke belakang (murtad)?</p>
        <span class="source">Surat Ali 'Imraan Ayat: 144</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Kekalahan Uhud mengajarkan bahwa kemenangan hanya datang dengan ketaatan penuh kepada Rasulullah SAW. Cinta dunia (harta) bisa menjadi penyebab kegagalan perjuangan.</p>
        `,
                        quiz: [
                            {
                                question: "Kapan terjadinya Perang Uhud?",
                                options: ["Tahun 2 H", "Tahun 3 H", "Tahun 5 H", "Tahun 8 H"],
                                correct: 1,
                                explanation: "Peristiwa ini terjadi pada perang Uhud yang terjadi pada tahun ke 3 H."
                            },
                            {
                                question: "Apa penyebab utama kekalahan di Uhud menurut Ali 'Imraan 152?",
                                options: ["Musuh terlalu kuat", "Hujan deras", "Berselisih dan menginginkan dunia (harta ghanimah)", "Rasulullah sakit"],
                                correct: 2,
                                explanation: "Di antaramu ada orang yang menghendaki dunia (sehingga meninggalkan pos pemanah)."
                            },
                            {
                                question: "Apa tujuan Allah mempergilirkan masa menang dan kalah (Ali 'Imraan 140)?",
                                options: ["Agar manusia bingung", "Sebagai permainan", "Agar Allah membedakan orang beriman dan mengambil syuhada", "Karena Allah tidak peduli"],
                                correct: 2,
                                explanation: "...supaya Allah membedakan orang yang beriman (dengan orang kafir) agar sebagian kamu dijadikan-Nya syuhada."
                            },
                            {
                                question: "Apa teguran Allah saat isu Nabi wafat beredar (Ali 'Imraan 144)?",
                                options: ["Apakah jika dia wafat kamu berbalik ke belakang (murtad)?", "Segeralah pulang", "Menyerahlah kepada Quraisy", "Buatlah patung Nabi"],
                                correct: 0,
                                explanation: "Apakah jika dia wafat atau dibunuh kamu berbalik ke belakang (murtad)?"
                            },
                            {
                                question: "Siapa yang dimaksud 'dua golongan yang ingin mundur' di Ali 'Imraan 122?",
                                options: ["Bani Nadhir & Qainuqa", "Bani Salamah & Bani Haritsah", "Muhajirin & Anshar", "Aus & Khazraj"],
                                correct: 1,
                                explanation: "Yakni: Bani Salamah dari suku Khazraj dan Bani Haritsah dari suku Aus."
                            }
                        ]
                    },
                    {
                        id: 119,
                        title: "Perang Hamra Al Asad (Badar Shugra)",
                        file: "topic_119.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Pengejaran Pasca Uhud</li>
    <li>Ancaman Abu Sofyan</li>
    <li>Kekuatan Tawakkal</li>
    <li>Keutamaan Mengikuti Perintah Allah</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas peristiwa setelah Perang Uhud, di mana Rasulullah mengajak pasukan yang terluka untuk mengejar musuh hingga Hamra Al Asad (Badar Shugra). Meski ditakut-takuti, keimanan mereka justru bertambah.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Ketaatan Pasca Luka Uhud</h3>
    <div class="quran-quote">
        
        <p class="translation">(Yaitu) orang-orang yang menaati perintah Allah dan Rasul-Nya sesudah mereka mendapat luka (dalam perang Uhud). Bagi orang-orang yang berbuat baik di antara mereka dan yang bertakwa ada pahala yang besar.</p>
        <span class="source">Surat Ali 'Imraan Ayat: 172</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Hasbunallah Wanikmal Wakil</h3>
    <div class="quran-quote">
        
        <p class="translation">(Yaitu) orang-orang (yang menaati Allah dan Rasul) yang kepada mereka ada orang-orang yang berkata: "Sesungguhnya manusia (musyrikin Quraisy) telah mengumpulkan pasukan untuk menyerang kamu, maka takutlah kepada mereka", maka perkataan itu menambah keimanan mereka dan mereka menjawab: "Cukuplah Allah menjadi Penolong kami dan Allah adalah sebaik-baik Pelindung."</p>
        <span class="source">Surat Ali 'Imraan Ayat: 173</span>
    </div>
    <p>Ayat ini turun saat Nu'aim bin Mas'ud menakut-nakuti kaum muslimin tentang kekuatan Abu Sofyan.</p>
</div>

<div class="content-section">
    <h3>3. Kemenangan Tanpa Perang</h3>
    <div class="quran-quote">
        
        <p class="translation">Maka mereka kembali dengan nikmat dan karunia (yang besar) dari Allah, mereka tidak mendapat bencana apa-apa, mereka mengikuti keridhaan Allah...</p>
        <span class="source">Surat Ali 'Imraan Ayat: 174</span>
    </div>
    <p>Musuh (Abu Sofyan) ketakutan dan tidak jadi menyerang, kaum muslimin justru mendapat keuntungan pasar (dagang) di Badar.</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Kisah ini membuktikan kekuatan mental dan tawakkal. Ancaman musuh bagi orang beriman tidak melemahkan, tapi justru menambah keyakinan (Hasbunallah Wanikmal Wakil).</p>
        `,
                        quiz: [
                            {
                                question: "Perang Hamra Al Asad (Badar Shugra) terjadi setelah perang apa?",
                                options: ["Perang Badar", "Perang Uhud", "Perang Khandaq", "Perang Tabuk"],
                                correct: 1,
                                explanation: "Terjadi sesudah mereka mendapat luka (dalam perang Uhud)."
                            },
                            {
                                question: "Apa ucapan kaum muslimin saat ditakut-takuti oleh musuh (Ali 'Imraan 173)?",
                                options: ["Kami menyerah", "Hasbunallah Wanikmal Wakil", "La Haula Wala Quwwata", "Subhanallah"],
                                correct: 1,
                                explanation: "Mereka menjawab: 'Cukuplah Allah menjadi Penolong kami dan Allah adalah sebaik-baik Pelindung' (Hasbunallah wa ni'mal wakil)."
                            },
                            {
                                question: "Siapa yang menyebarkan kabar bohong untuk menakuti muslimin?",
                                options: ["Abu Jahal", "Nu'aim Ibnu Mas'ud", "Abdullah bin Ubay", "Musailamah"],
                                correct: 1,
                                explanation: "Dia menyuruh Nu'aim Ibnu Mas'ud... pergi ke Madinah untuk menakut-nakuti kaum muslimin."
                            },
                            {
                                question: "Apa dampak ancaman musuh terhadap orang yang beriman (Ali 'Imraan 173)?",
                                options: ["Menambah ketakutan", "Menambah keimanan", "Membuat mereka lari", "Membuat mereka ragu"],
                                correct: 1,
                                explanation: "...maka perkataan itu menambah keimanan mereka."
                            },
                            {
                                question: "Bagaimana akhir dari peristiwa Badar Shugra (Ali 'Imraan 174)?",
                                options: ["Terjadi perang dahsyat", "Muslimin kalah telak", "Tidak terjadi perang, muslimin untung berdagang", "Gencatan senjata"],
                                correct: 2,
                                explanation: "Mereka kembali dengan nikmat... mereka tidak mendapat bencana apa-apa (tidak jadi berperang dan untung berdagang)."
                            }
                        ]
                    },
                    {
                        id: 120,
                        title: "Peristiwa Hadits Ifki",
                        file: "topic_120.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Kronologi Fitnah (Hadits Ifki)</li>
    <li>Sikap yang Seharusnya Saat Mendengar Hoax</li>
    <li>Pembersihan Nama Aisyah RA</li>
    <li>Hukuman bagi Penyebar Fitnah</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas peristiwa Hadits Ifki, yaitu fitnah keji yang dituduhkan kepada Ummul Mukminin Aisyah RA pasca perang Bani Musthaliq. Allah menurunkan ayat-ayat ini untuk membersihkan nama beliau dan mengajarkan adab menerima berita.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Jangan Mengira Buruk Bagi Kamu</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya orang-orang yang membawa berita bohong itu adalah dari golonganmu juga. Janganlah kamu kira bahwa berita bohong itu buruk bagimu bahkan ia adalah baik bagimu...</p>
        <span class="source">Surat An Nuur Ayat: 11</span>
    </div>
    <p>Di balik musibah fitnah ini, Allah menyingkap siapa yang munafik dan siapa yang mukmin sejati, serta menetapkan hukum-hukum syariat.</p>
</div>

<div class="content-section">
    <h3>2. Adab Mendengar Berita (Husnuzhan)</h3>
    <div class="quran-quote">
        
        <p class="translation">Mengapa pada waktu kamu mendengar berita bohong itu kaum mukminin dan mukminat tidak bersangka baik terhadap diri mereka, dan (mengapa tidak) berkata: "Ini berita bohong yang nyata."</p>
        <span class="source">Surat An Nuur Ayat: 12</span>
    </div>
</div>

<div class="content-section">
    <h3>3. Bahaya Menyebarkan Berita Tanpa Ilmu</h3>
    <div class="quran-quote">
        
        <p class="translation">(Ingatlah) di waktu kamu menerima berita bohong itu dari mulut ke mulut dan kamu katakan dengan mulutmu apa yang tidak kamu ketahui sedikit juga, dan kamu menganggapnya suatu yang ringan saja. Padahal dia pada sisi Allah adalah besar.</p>
        <span class="source">Surat An Nuur Ayat: 15</span>
    </div>
</div>

<div class="content-section">
    <h3>4. Peringatan Allah</h3>
    <div class="quran-quote">
        
        <p class="translation">Allah memperingatkan kamu agar (jangan) kembali berbuat seperti itu selama-lamanya, jika kamu orang-orang yang beriman.</p>
        <span class="source">Surat An Nuur Ayat: 17</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Fitnah kepada keluarga Nabi adalah ujian berat. Pelajarannya: wajib Tabayyun, Husnuzhan kepada sesama mukmin, dan menjaga lisan dari menyebarkan berita yang belum jelas kebenarannya.</p>
        `,
                        quiz: [
                            {
                                question: "Siapakah Ummul Mukminin yang menjadi korban fitnah Hadits Ifki?",
                                options: ["Khadijah binti Khuwailid", "Aisyah binti Abu Bakar", "Hafshah binti Umar", "Zainab binti Jahsy"],
                                correct: 1,
                                explanation: "Berita bohong ini mengenai 'Aisyah Ra. Ummul Mu'minin, pasca perang dengan Bani Mushtaliq."
                            },
                            {
                                question: "Apa sikap yang seharusnya dilakukan mukmin saat mendengar berita buruk tentang saudaranya (An Nuur 12)?",
                                options: ["Langsung menyebarkannya", "Diam saja", "Bersangka baik (Husnuzhan)", "Mencari bukti kesalahan"],
                                correct: 2,
                                explanation: "...kaum mukminin dan mukminat (seharusnya) bersangka baik terhadap diri mereka."
                            },
                            {
                                question: "Mengapa menyebarkan berita bohong dianggap dosa besar (An Nuur 15)?",
                                options: ["Karena menyakiti hati", "Karena kamu menganggapnya ringan padahal di sisi Allah besar", "Karena tidak ada saksi", "Karena dilarang pemerintah"],
                                correct: 1,
                                explanation: "...dan kamu menganggapnya suatu yang ringan saja. Padahal dia pada sisi Allah adalah besar."
                            },
                            {
                                question: "Berapa saksi yang harus didatangkan untuk tuduhan zina (An Nuur 13)?",
                                options: ["2 saksi", "3 saksi", "4 saksi", "10 saksi"],
                                correct: 2,
                                explanation: "Mengapa mereka (yang menuduh) tidak mendatangkan 4 orang saksi atas berita bohong itu?"
                            },
                            {
                                question: "Siapakah tokoh munafik yang menjadi dalang penyebar Hadits Ifki?",
                                options: ["Abdullah bin Ubay bin Salul", "Musailamah Al-Kazzab", "Abu Jahal", "Ka'ab bin Asyraf"],
                                correct: 0,
                                explanation: "Siapa di antara mereka yang mengambil bagian yang terbesar... (merujuk pada Abdullah bin Ubay)."
                            }
                        ]
                    },
                    {
                        id: 121,
                        title: "Perang Khandaq (Ahzab)",
                        file: "topic_121.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Datangnya Pasukan Sekutu (Ahzab)</li>
    <li>Goncangan Jiwa Mukminin</li>
    <li>Sikap Munafik Menghadapi Pengepungan</li>
    <li>Pertolongan Allah (Angin & Malaikat)</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas Perang Khandaq (Parit) atau Perang Ahzab (Sekutu). Madinah dikepung dari segala penjuru oleh 10.000 pasukan gabungan (Quraisy, Ghatafan, Yahudi, dll). Allah menguji orang beriman dengan ketakutan yang sangat, namun akhirnya memberikan kemenangan melalui pertolongan gaib.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Goncangan yang Dahsyat</h3>
    <div class="quran-quote">
        
        <p class="translation">(Yaitu) ketika mereka datang kepadamu dari atas dan dari bawahmu, dan ketika tidak tetap lagi penglihatan-(mu) dan hatimu naik menyesak sampai ke tenggorokan dan kamu menyangka terhadap Allah dengan bermacam-macam prasangka.</p>
        <span class="source">Surat Al Ahzaab Ayat: 10</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Sikap Munafik dan Orang Berpenyakit Hati</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan (ingatlah) ketika orang-orang munafik dan orang-orang yang berpenyakit dalam hatinya berkata: "Allah dan Rasul-Nya tidak menjanjikan kepada kami melainkan tipu daya."</p>
        <span class="source">Surat Al Ahzaab Ayat: 12</span>
    </div>
    <p>Mereka ketakutan dan ingin lari, bahkan berkata "Rumah kami tidak aman".</p>
</div>

<div class="content-section">
    <h3>3. Sikap Mukmin Sejati</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan tatkala orang-orang mukmin melihat golongan-golongan yang bersekutu itu, mereka berkata: "Inilah yang dijanjikan Allah dan Rasul-Nya kepada kita." Dan benarlah Allah dan Rasul-Nya. Dan yang demikian itu tidaklah menambah kepada mereka kecuali iman dan ketundukan.</p>
        <span class="source">Surat Al Ahzaab Ayat: 22</span>
    </div>
</div>

<div class="content-section">
    <h3>4. Pertolongan Allah</h3>
    <div class="quran-quote">
        
        <p class="translation">Hai orang-orang yang beriman, ingatlah nikmat Allah atasmu ketika datang kepadamu tentara-tentara, lalu Kami kirimkan kepada mereka angin topan dan tentara yang tidak dapat kamu melihatnya (malaikat).</p>
        <span class="source">Surat Al Ahzaab Ayat: 9</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Perang Ahzab membuktikan bahwa jumlah pasukan bukan penentu. Ketahanan mental, strategi (parit), dan doa adalah kunci. Allah memecah belah musuh dengan angin dingin yang kencang.</p>
        `,
                        quiz: [
                            {
                                question: "Apa arti 'Ahzab' dalam konteks perang ini?",
                                options: ["Parit", "Pasukan Sekutu (Golongan-golongan)", "Pasukan Berkuda", "Benteng"],
                                correct: 1,
                                explanation: "Ahzab artinya golongan-golongan yang bersekutu (Quraisy, Ghatafan, Yahudi, dll) untuk menyerang Madinah."
                            },
                            {
                                question: "Apa strategi pertahanan umat Islam dalam perang ini?",
                                options: ["Membuat tembok raksasa", "Menggali Parit (Khandaq)", "Menyerang Mekah", "Bersembunyi di gua"],
                                correct: 1,
                                explanation: "Salman Al-Farisi mengusulkan penggalian parit (Khandaq) untuk menghalangi musuh masuk Madinah."
                            },
                            {
                                question: "Bagaimana Allah menghancurkan pasukan Ahzab (Al Ahzaab 9)?",
                                options: ["Dengan gempa bumi", "Dengan banjir", "Dengan angin topan dan tentara malaikat", "Dengan api dari langit"],
                                correct: 2,
                                explanation: "...lalu Kami kirimkan kepada mereka angin topan dan tentara yang tidak dapat kamu melihatnya."
                            },
                            {
                                question: "Apa komentar orang munafik saat melihat pasukan sekutu (Al Ahzaab 12)?",
                                options: ["Kita pasti menang", "Allah dan Rasul-Nya menjanjikan tipu daya", "Hasbunallah Wanikmal Wakil", "Mari kita shalat"],
                                correct: 1,
                                explanation: "Mereka berkata: 'Allah dan Rasul-Nya tidak menjanjikan kepada kami melainkan tipu daya'."
                            },
                            {
                                question: "Apa reaksi orang mukmin saat melihat pasukan sekutu (Al Ahzaab 22)?",
                                options: ["Ketakutan dan lari", "Menambah iman dan ketundukan", "Marah kepada Nabi", "Menyerah"],
                                correct: 1,
                                explanation: "...Dan yang demikian itu tidaklah menambah kepada mereka kecuali iman dan ketundukan."
                            }
                        ]
                    },
                    {
                        id: 122,
                        title: "Perang Melawan Bani Quraizhah",
                        file: "topic_122.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Pengkhianatan Bani Quraizhah</li>
    <li>Pengepungan Benteng Yahudi</li>
    <li>Hukuman Keras bagi Pengkhianat</li>
    <li>Pewarisan Tanah dan Harta</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini adalah kelanjutan langsung dari Perang Ahzab. Bani Quraizhah (Yahudi) mengkhianati perjanjian damai dengan Nabi saat Madinah dikepung. Setelah Ahzab bubar, Jibril memerintahkan Nabi untuk menyerang Bani Quraizhah.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Allah Mengeluarkan Mereka dari Benteng</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan Dia menurunkan orang-orang ahli kitab (Bani Quraizhah) yang membantu golongan yang bersekutu dari benteng-benteng mereka, dan Dia memasukkan rasa takut ke dalam hati mereka.</p>
        <span class="source">Surat Al Ahzaab Ayat: 26</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Hukuman Mati dan Tawanan</h3>
    <div class="quran-quote">
        
        <p class="translation">Sebagian mereka kamu bunuh dan sebagian lainnya kamu tawan.</p>
        <span class="source">Surat Al Ahzaab Ayat: 26 (lanjutan)</span>
    </div>
    <p>Para pengkhianat laki-laki dihukum mati karena pengkhianatan mereka di saat kritis hampir memusnahkan umat Islam.</p>
</div>

<div class="content-section">
    <h3>3. Warisan Tanah dan Harta</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan Dia mewariskan kepada kamu tanah-tanah, rumah-rumah, dan harta benda mereka, dan (begitu pula) tanah yang belum kamu injak.</p>
        <span class="source">Surat Al Ahzaab Ayat: 27</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Hukuman bagi Bani Quraizhah sangat keras karena pengkhianatan dari dalam ("menusuk dari belakang") saat perang Ahzab adalah kejahatan tingkat tinggi yang membahayakan kelangsungan seluruh umat Islam.</p>
        `,
                        quiz: [
                            {
                                question: "Mengapa Bani Quraizhah diperangi setelah Perang Ahzab?",
                                options: ["Karena mereka menolak membayar pajak", "Karena mengkhianati perjanjian dan membantu pasukan Ahzab", "Karena mereka kaya", "Karena mereka orang asing"],
                                correct: 1,
                                explanation: "Dan Dia menurunkan orang-orang ahli kitab yang membantu golongan yang bersekutu (berkhianat)."
                            },
                            {
                                question: "Apa arti 'Shoyashihim' dalam ayat 26?",
                                options: ["Rumah mereka", "Benteng-benteng mereka", "Kebun mereka", "Pasar mereka"],
                                correct: 1,
                                explanation: "Min Shoyashihim = dari benteng-benteng mereka."
                            },
                            {
                                question: "Bagaimana nasib para pengkhianat laki-laki Bani Quraizhah (Al Ahzaab 26)?",
                                options: ["Diusir saja", "Sebagian dibunuh (dihukum mati)", "Dimaafkan", "Dijasikan budak"],
                                correct: 1,
                                explanation: "Sebagian mereka kamu bunuh..."
                            },
                            {
                                question: "Apa bentuk pertolongan Allah dalam menaklukkan benteng Quraizhah?",
                                options: ["Menghancurkan tembok dengan petir", "Memasukkan rasa takut (Ar-Ru'bu) ke hati mereka", "Mengirim banjir", "Pasukan muslim bisa terbang"],
                                correct: 1,
                                explanation: "Dan Dia memasukkan rasa takut ke dalam hati mereka."
                            },
                            {
                                question: "Apa yang dimaksud 'tanah yang belum kamu injak' (Al Ahzaab 27)?",
                                options: ["Tanah Madinah", "Tanah Mekah", "Tanah Khaibar atau Persia/Romawi (penaklukan masa depan)", "Bulan"],
                                correct: 2,
                                explanation: "Tanah yang belum diinjak: tanah-tanah yang akan dimasuki tentara Islam di masa depan (misal: Khaibar)."
                            }
                        ]
                    },
                    {
                        id: 123,
                        title: "Perjanjian Hudaibiyah dan Bai'at Ridwan",
                        file: "topic_123.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Kemenangan Nyata (Fathan Mubina)</li>
    <li>Kabar Gembira dan Pertolongan Allah</li>
    <li>Bai'at Ridwan (Janji Setia di Bawah Pohon)</li>
    <li>Penghalang Menuju Masjidil Haram</li>
    <li>Mimpi Rasulullah Memasuki Mekah</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas peristiwa Hudaibiyah (6 H), di mana kaum muslimin dilarang masuk Mekah untuk umrah. Meski terlihat merugikan, Allah menyebutnya sebagai "Kemenangan yang Nyata". Di sini juga terjadi Bai'at Ridwan yang sangat diridhai Allah.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Kemenangan yang Nyata</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya Kami telah memberikan kepadamu kemenangan yang nyata.</p>
        <span class="source">Surat Al Fath Ayat: 1</span>
    </div>
    <p>Para ulama tafsir menyatakan kemenanga ini merujuk pada Perjanjian Hudaibiyah, yang menjadi pembuka bagi Fathu Makkah.</p>
</div>

<div class="content-section">
    <h3>2. Bai'at Ridwan</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya Allah telah ridha terhadap orang-orang mukmin ketika mereka berjanji setia kepadamu di bawah pohon, maka Allah mengetahui apa yang ada dalam hati mereka lalu menurunkan ketenangan atas mereka...</p>
        <span class="source">Surat Al Fath Ayat: 18</span>
    </div>
    <p>Baiat ini dilakukan karena isu Utsman bin Affan dibunuh di Mekah. Mereka bersumpah setia untuk berperang sampai mati (Baiat Mati) atau tidak lari.</p>
</div>

<div class="content-section">
    <h3>3. Halangan Orang Kafir</h3>
    <div class="quran-quote">
        
        <p class="translation">Merekalah orang-orang kafir yang menghalangi kamu dari (masuk) Masjidil Haram dan menghalangi hewan korban sampai ke tempat (penyembelihan)-nya.</p>
        <span class="source">Surat Al Fath Ayat: 25</span>
    </div>
</div>

<div class="content-section">
    <h3>4. Kebenaran Mimpi Rasul</h3>
    <div class="quran-quote">
        
        <p class="translation">Sungguh Allah akan membuktikan kepada Rasul-Nya kebenaran mimpinya dengan sebenarnya, bahwa sungguh kamu pasti akan memasuki Masjidil Haram, Insya Allah dalam keadaan aman, dengan mencukur rambut kepala dan mengguntingnya...</p>
        <span class="source">Surat Al Fath Ayat: 27</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Hudaibiyah mengajarkan kesabaran strategis. Apa yang tampak sebagai "mengalah" ternyata adalah strategi Allah untuk kemenangan yang lebih besar (Fathum Mubina).</p>
        `,
                        quiz: [
                            {
                                question: "Surat apa yang turun berkaitan dengan Perjanjian Hudaibiyah?",
                                options: ["Al Hujuraat", "Al Fath", "Al Hadid", "Al Hasyr"],
                                correct: 1,
                                explanation: "Surat Al Fath dimulai dengan ayat 'Inna fatahna laka fathan mubina' yang merujuk pada Hudaibiyah."
                            },
                            {
                                question: "Apa nama sumpah setia yang dilakukan di bawah pohon saat Hudaibiyah?",
                                options: ["Bai'at Aqabah", "Bai'at Ridwan", "Bai'at Nisa", "Hilful Fudhul"],
                                correct: 1,
                                explanation: "Laqad radhiyallahu 'anil mu'minina idz yubayi'unaka tahtas syajarah (Bai'at Ridwan)."
                            },
                            {
                                question: "Apa isi mimpi Rasulullah sebelum peristiwa Hudaibiyah (Al Fath 27)?",
                                options: ["Melihat kehancuran Mekah", "Memasuki Masjidil Haram dengan aman dan bercukur", "Bertemu para Nabi", "Melihat sungai surga"],
                                correct: 1,
                                explanation: "Sungguh kamu pasti akan memasuki Masjidil Haram... dengan mencukur rambut kepala."
                            },
                            {
                                question: "Mengapa Hudaibiyah disebut 'Kemenangan yang Nyata' (Fathan Mubina)?",
                                options: ["Karena muslimin berhasil membunuh musuh", "Karena mendapat banyak harta", "Karena menjadi pembuka jalan dakwah damai dan Fathu Makkah", "Karena musuh menyerah seketika"],
                                correct: 2,
                                explanation: "Sebagian ulama tafsir mengatakan kemenangan itu adalah perdamaian Hudaibiyah yang membuka jalan dakwah."
                            },
                            {
                                question: "Apa alasan orang kafir menghalangi kaum muslimin saat itu (Al Fath 26)?",
                                options: ["Ketakutan", "Kesombongan Jahiliyah (Hamiyyatul Jahiliyyah)", "Perintah Raja", "Wabah penyakit"],
                                correct: 1,
                                explanation: "Saat orang-orang kafir menanamkan dalam hati mereka kesombongan (yaitu) kesombongan Jahiliyah."
                            }
                        ]
                    },
                    {
                        id: 124,
                        title: "Perang Tabuk",
                        file: "topic_124.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Pemutusan Hubungan dengan Musyrikin (Bara'ah)</li>
    <li>Perintah Perang Total</li>
    <li>Sikap Munafik (Alasan Palsu, Masjid Dhirar)</li>
    <li>Tiga Sahabat yang Ditangguhkan Taubatnya</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Perang Tabuk (9 H) adalah perang terakhir yang diikuti Rasulullah SAW melawan Romawi di musim panas yang terik. Surat At-Taubah membongkar habis sifat-sifat orang munafik dan menegaskan pemutusan hubungan (Bara'ah) dengan kaum musyrikin.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Pemutusan Hubungan (Bara'ah)</h3>
    <div class="quran-quote">
        
        <p class="translation">(Inilah pernyataan) pemutusan hubungan dari Allah dan Rasul-Nya kepada orang-orang musyrikin yang kamu telah mengadakan perjanjian.</p>
        <span class="source">Surat At Taubah Ayat: 1</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Beratnya Ujian Tabuk</h3>
    <div class="quran-quote">
        
        <p class="translation">Hai orang-orang yang beriman, apa sebabnya bila dikatakan kepadamu: "Berangkatlah (untuk berperang) di jalan Allah" kamu merasa berat?</p>
        <span class="source">Surat At Taubah Ayat: 38</span>
    </div>
</div>

<div class="content-section">
    <h3>3. Sifat Orang Munafik</h3>
    <div class="quran-quote">
        
        <p class="translation">Kalau yang kamu serukan itu keuntungan yang mudah diperoleh dan perjalanan yang tidak seberapa jauh, pastilah mereka mengikutimu, tetapi tempat yang dituju itu amat jauh terasa oleh mereka.</p>
        <span class="source">Surat At Taubah Ayat: 42</span>
    </div>
    <p>Mereka beralasan cuaca panas. Padahal "Api neraka Jahanam lebih panas" (At Taubah 81).</p>
</div>

<div class="content-section">
    <h3>4. Masjid Dhirar</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan (di antara orang munafik itu ada) orang yang mendirikan masjid untuk menimbulkan kemudharatan, kekafiran, dan memecah belah antara orang mukmin...</p>
        <span class="source">Surat At Taubah Ayat: 107</span>
    </div>
    <p>Nabi diperintahkan untuk merobohkan masjid ini sepulang dari Tabuk.</p>
</div>

<div class="content-section">
    <h3>5. Penerimaan Taubat</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya Allah telah menerima tobat Nabi, orang-orang Muhajirin, dan orang-orang Anshar...</p>
        <span class="source">Surat At Taubah Ayat: 117</span>
    </div>
    <p>Serta kepada tiga orang (Ka'ab bin Malik dkk) yang sempat dikucilkan karena tidak ikut perang tanpa uzur syar'i.</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Perang Tabuk disebut "Jaishul 'Usrah" (Pasukan Kesulitan). Ujian ini memisahkan mukmin sejati (yang tetap berangkat meski berat) dengan munafik (yang mencari-cari alasan).</p>
        `,
                        quiz: [
                            {
                                question: "Apa nama lain Surat At-Taubah yang berarti 'Pemutusan Hubungan'?",
                                options: ["Al-Fath", "Bara'ah", "Al-Anfal", "Al-Qital"],
                                correct: 1,
                                explanation: "Ayat pertama dimulai dengan 'Bara'atun minallahi wa rasulihi' (Pemutusan hubungan/berlepas diri dari Allah dan Rasul-Nya)."
                            },
                            {
                                question: "Mengapa Perang Tabuk dirasakan sangat berat oleh kaum muslimin?",
                                options: ["Karena musuh lemah", "Karena jarak jauh, cuaca panas terik, dan musim panen kurma", "Karena tidak ada kendaraan", "Karena hujan badai"],
                                correct: 1,
                                explanation: "Di dalam ayat disebutkan 'b'udat 'alaihimus syuqqah' (tempat yang dituju amat jauh terasa), dan terjadi di musim panas."
                            },
                            {
                                question: "Apa tujuan orang munafik mendirikan Masjid Dhirar?",
                                options: ["Untuk beribadah dengan khusyuk", "Untuk memecah belah orang mukmin dan markas makar", "Untuk menampung orang miskin", "Untuk belajar Al-Qur'an"],
                                correct: 1,
                                explanation: "...mendirikan masjid untuk menimbulkan kemudharatan, kekafiran, dan memecah belah antara orang mukmin (tafriqan bainal mu'minin)."
                            },
                            {
                                question: "Siapakah 3 sahabat yang ditangguhkan tobatnya (dikucilkan) karena tidak ikut Perang Tabuk?",
                                options: ["Abu Bakar, Umar, Utsman", "Ka'ab bin Malik, Hilal bin Umayyah, Murarah bin Rabi'", "Khalid bin Walid, Amr bin Ash, Ikrimah", "Hassan bin Tsabit, Abdullah bin Rawahah, Ka'ab bin Zubair"],
                                correct: 1,
                                explanation: "Di ayat 118: 'Dan terhadap tiga orang yang ditangguhkan...' (Mereka adalah Ka'ab, Hilal, dan Murarah)."
                            },
                            {
                                question: "Apa alasan orang munafik tidak mau berangkat perang (At Taubah 81)?",
                                options: ["Takut mati", "Tidak punya uang", "Jangan berangkat dalam panas terik ini", "Sakit"],
                                correct: 2,
                                explanation: "Mereka berkata: 'La tanfiru fil harr' (Jangan berangkat dalam panas terik ini)."
                            }
                        ]
                    },
                    {
                        id: 125,
                        title: "Perang Hunain",
                        file: "topic_125.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Rasa Bangga akan Jumlah Yang Banyak</li>
    <li>Kekalahan Awal dan Sempitnya Bumi</li>
    <li>Pertolongan Allah dan Kemenangan</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas Perang Hunain (8 H) setelah Fathu Makkah. Umat Islam dengan jumlah besar (12.000) sempat merasa jumawa ("Kami tidak akan kalah karena jumlah sedikit"). Namun mereka justru dipukul mundur di awal, sebelum Allah menurunkan ketenangan (Sakinah) dan bantuan Malaikat.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Jangan Congkak Karena Jumlah</h3>
    <div class="quran-quote">
        
        <p class="translation">...dan (ingatlah) perang Hunain, yaitu di waktu kamu menjadi congkak karena banyaknya jumlah-(mu), maka jumlah yang banyak itu tidak memberi manfaat kepadamu sedikitpun...</p>
        <span class="source">Surat At Taubah Ayat: 25</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Bumi Terasa Sempit</h3>
    <div class="quran-quote">
        
        <p class="translation">...dan bumi yang luas itu telah terasa sempit olehmu, kemudian kamu lari kebelakang dengan bercerai-berai.</p>
        <span class="source">Surat At Taubah Ayat: 25 (lanjutan)</span>
    </div>
    <p>Pasukan Hawazin dan Tsaqif menyerang tiba-tiba (penyergapan) yang membuat barisan muslim kocar-kacir.</p>
</div>

<div class="content-section">
    <h3>3. Turunnya Sakinah dan Bantuan Ghaib</h3>
    <div class="quran-quote">
        
        <p class="translation">Lalu Allah menurunkan ketenangan kepada Rasul-Nya dan kepada orang-orang yang beriman, dan Allah menurunkan tentara yang kamu tiada melihatnya...</p>
        <span class="source">Surat At Taubah Ayat: 26</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Pelajaran utama Hunain: Kemenangan bukan karena jumlah (kuantitas), tapi karena pertolongan Allah. Rasa 'ujub (bangga diri) bisa menjadi sebab kekalahan.</p>
    `,
                        quiz: [
                            {
                                question: "Apa penyebab kekalahan awal umat Islam di Perang Hunain?",
                                options: ["Musuh terlalu kuat", "Rasa ujub/congkak karena jumlah pasukan yang banyak", "Pengkhianatan munafik", "Tidak membawa senjata"],
                                correct: 1,
                                explanation: "...di waktu kamu menjadi congkak karena banyaknya jumlah-(mu)."
                            },
                            {
                                question: "Berapa jumlah pasukan muslimin di Hunain?",
                                options: ["313 orang", "1000 orang", "10.000 orang", "12.000 orang (terbanyak saat itu)"],
                                correct: 3,
                                explanation: "Merupakan jumlah terbesar saat itu, gabungan pasukan Madinah dan Makkah (Thulaqa), sekitar 12.000."
                            },
                            {
                                question: "Apa yang Allah turunkan untuk membalikkan keadaan menjadi kemenangan?",
                                options: ["Harta karun", "Sakinah (Ketenangan) dan Junud (Tentara Malaikat)", "Makanan dari langit", "Senjata api"],
                                correct: 1,
                                explanation: "Lalu Allah menurunkan ketenangan (Sakinah) kepada Rasul-Nya... dan menurunkan tentara yang kamu tiada melihatnya."
                            },
                            {
                                question: "Apa arti 'Dan bumi yang luas itu terasa sempit olehmu'?",
                                options: ["Bumi menyusut", "Perasaan terdesak dan panik yang luar biasa", "Jalanan macet", "Banyak bangunan"],
                                correct: 1,
                                explanation: "Menggambarkan kepanikan dan rasa tidak ada tempat berlindung saat disergap musuh."
                            },
                            {
                                question: "Perang Hunain terjadi setelah peristiwa apa?",
                                options: ["Perang Badar", "Perang Uhud", "Fathu Makkah", "Haji Wada"],
                                correct: 2,
                                explanation: "Terjadi pada tahun 8 H tak lama setelah Penaklukan Kota Mekah."
                            }
                        ]
                    },
                    {
                        id: 126,
                        title: "Penaklukan Kota Mekah (Fathu Makkah)",
                        file: "topic_126.pdf",
                        content: `
    < h2 > Daftar Isi</h2 >
<ul class="toc-list">
    <li>Janji Kepulangan ke Mekah</li>
    <li>Datangnya Pertolongan Allah (An-Nashr)</li>
    <li>Masuk Islam Berbondong-bondong</li>
    <li>Tasbih dan Istighfar</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas puncak kemenangan perjuangan Nabi Muhammad SAW yaitu Penaklukan Kota Mekah (Fathu Makkah). Allah memenuhi janji-Nya untuk mengembalikan Nabi ke tempat kelahirannya (Ma'ad) dan manusia masuk Islam dalam jumlah besar.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Janji Pengembalian ke Mekah</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya yang mewajibkan atasmu (melaksanakan hukum-hukum) Alquran benar-benar akan mengembalikan kamu ke tempat kembali (Mekah).</p>
        <span class="source">Surat Al Qashash Ayat: 85</span>
    </div>
    <p>Ayat ini turun saat Nabi berhijrah meninggalkan Mekah dengan sedih, menghibur beliau bahwa beliau akan kembali sebagai pemenang.</p>
</div>

<div class="content-section">
    <h3>2. Pertolongan dan Kemenangan</h3>
    <div class="quran-quote">
        
        <p class="translation">Apabila telah datang pertolongan Allah dan kemenangan...</p>
        <span class="source">Surat An Nashr Ayat: 1</span>
    </div>
</div>

<div class="content-section">
    <h3>3. Berbondong-bondong Masuk Islam</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan kamu lihat manusia masuk agama Allah dengan berbondong-bondong</p>
        <span class="source">Surat An Nashr Ayat: 2</span>
    </div>
</div>

<div class="content-section">
    <h3>4. Perintah Bertasbih dan Istighfar</h3>
    <div class="quran-quote">
        
        <p class="translation">Maka bertasbihlah dengan memuji Tuhanmu dan mohonlah ampun kepada-Nya. Sesungguhnya Dia adalah Maha Penerima taubat.</p>
        <span class="source">Surat An Nashr Ayat: 3</span>
    </div>
    <p>Ini adalah isyarat bahwa tugas Nabi hampir selesai dan ajal beliau semakin dekat.</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Fathu Makkah adalah bukti kebenaran janji Allah. Kemenangan disambut bukan dengan pesta pora, melainkan dengan tasbih, tahmid, dan istighfar.</p>
        `,
                        quiz: [
                            {
                                question: "Apa arti 'Al-Fath' dalam konteks ini?",
                                options: ["Pembuka / Kemenangan (Penaklukan)", "Perdamaian", "Kekalahan", "Perjanjian"],
                                correct: 0,
                                explanation: "Al-Fath artinya kemenangan atau penaklukan (kota Mekah)."
                            },
                            {
                                question: "Surat apa yang mengabarkan tentang terjadinya Fathu Makkah?",
                                options: ["Al-Lahab", "An-Nashr", "Al-Kautsar", "Al-Ikhlas"],
                                correct: 1,
                                explanation: "Apabila telah datang pertolongan Allah dan kemenangan (Surat An-Nashr)."
                            },
                            {
                                question: "Apa yang diperintahkan Allah saat kemenangan tiba (An Nashr 3)?",
                                options: ["Berpesta dan makan-makan", "Membunuh semua musuh", "Bertasbih, Memuji Allah, dan Beristighfar", "Membangun istana"],
                                correct: 2,
                                explanation: "Fasabbih bihamdi rabbika wastaghfirhu (Maka bertasbihlah dengan memuji Tuhanmu dan mohonlah ampun)."
                            },
                            {
                                question: "Apa makna 'Ma'ad' dalam Surat Al Qashash ayat 85?",
                                options: ["Akhirat", "Tempat kembali (Kota Mekah)", "Madinah", "Palestina"],
                                correct: 1,
                                explanation: "La raadduka ila ma'ad (benar-benar akan mengembalikan kamu ke tempat kembali/Mekah)."
                            },
                            {
                                question: "Bagaimana kondisi manusia masuk Islam saat Fathu Makkah (An Nashr 2)?",
                                options: ["Satu persatu", "Diam-diam", "Berbondong-bondong (Afwaja)", "Terpaksa"],
                                correct: 2,
                                explanation: "...masuk agama Allah dengan berbondong-bondong (Afwaja)."
                            }
                        ]
                    }]
            }, {
                id: "subject-6",
                title: "Pokok Bahasan 6: Sifat Rasulullah SAW & Etika Terhadap Beliau",
                topics: [
                    {
                        id: 127,
                        title: "Akhlak & Rumah Tangga Rasulullah SAW",
                        file: "topic_127.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Akhlak Rasulullah SAW</li>
    <li>Rumah Tangga Rasulullah SAW</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Materi ini membahas kemuliaan akhlak baginda Nabi Muhammad SAW yang dipuji langsung oleh Allah, kasih sayangnya yang mendalam kepada umat, serta etika dan dinamika dalam kehidupan rumah tangga beliau.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Akhlak Rasulullah SAW</h3>
    <div class="quran-quote">
        
        <p class="translation">Dan sesungguhnya kamu benar-benar berbudi pekerti yang agung.</p>
        <span class="source">Surat Al Qalam Ayat: 4</span>
    </div>
    <div class="quran-quote">
        
        <p class="translation">Sungguh telah datang kepadamu seorang Rasul dari kaummu sendiri, berat terasa olehnya penderitaanmu, sangat menginginkan (keimanan dan keselamatan) bagimu, amat belas kasihan lagi penyayang terhadap orang-orang mukmin.</p>
        <span class="source">Surat At Taubah Ayat: 128</span>
    </div>
    <div class="quran-quote">
        
        <p class="translation">Muhammad itu adalah utusan Allah dan orang-orang yang bersamanya adalah keras terhadap orang-orang kafir, tetapi berkasih sayang sesama mereka...</p>
        <span class="source">Surat Al Fath Ayat: 29</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Rumah Tangga Rasulullah SAW</h3>
    <p>Allah memberikan bimbingan khusus kepada istri-istri Nabi agar mereka menjadi teladan (ummahatul mukminin) yang menjaga kehormatan dan ketaatan.</p>
    <div class="quran-quote">
        
        <p class="translation">Hai isteri-isteri Nabi, kamu sekalian tidaklah seperti wanita yang lain, jika kamu bertakwa, maka janganlah kamu tunduk dalam berbicara sehingga berkeinginanlah orang yang ada penyakit dalam hatinya dan ucapkanlah perkataan yang baik.</p>
        <span class="source">Surat Al Ahzaab Ayat: 32</span>
    </div>
    <div class="quran-quote">
        
        <p class="translation">Dan hendaklah kamu tetap di rumahmu dan janganlah kamu berhias dan bertingkah laku seperti orang-orang Jahiliyah yang dahulu...</p>
        <span class="source">Surat Al Ahzaab Ayat: 33</span>
    </div>
    <p>Ayat-ayat ini mengajarkan kemuliaan ahlul bait dan pentingnya menjaga adab serta kesucian hati.</p>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Akhlak Nabi adalah Al-Qur'an. Beliau adalah pribadi yang lembut, penyayang, namun tegas dalam prinsip. Rumah tangga beliau dibangun di atas pondasi ketakwaan, kedermawanan, dan kesederhanaan.</p>
            `,
                        quiz: [
                            {
                                question: "Sifat apakah yang Allah puji dari Nabi dalam Surat Al Qalam ayat 4?",
                                options: ["Kekuatannya", "Kecerdasannya", "Budi pekertinya yang agung", "Kekayaannya"],
                                correct: 2,
                                explanation: "Wa innaka la'alaa khuluqin 'azhiim (Dan sesungguhnya kamu benar-benar berbudi pekerti yang agung)."
                            },
                            {
                                question: "Menurut Surat At Taubah ayat 128, bagaimana perasaan Nabi terhadap penderitaan umatnya?",
                                options: ["Tidak peduli", "Berat terasa olehnya (ikut merasakan sakit)", "Biasanya saja", "Menyukainya"],
                                correct: 1,
                                explanation: "Ayat ini menyatakan '...‘aziizun ‘alaihi maa ‘anittum...' yang artinya berat terasa olehnya penderitaanmu."
                            },
                            {
                                question: "Di dalam Surat Al Fath ayat 29, bagaimana sikap orang mukmin terhadap orang kafir (dalam konteks perang/permusuhan)?",
                                options: ["Lemah lembut", "Keras/Tegas (Asyidda')", "Takut", "Ragu-ragu"],
                                correct: 1,
                                explanation: "Muhammadur rasulullah walladzina ma'ahu asyiddaa'u 'alal kuffaar (keras terhadap orang-orang kafir)."
                            },
                            {
                                question: "Apa nasihat Allah kepada istri-istri Nabi agar tidak memancing fitnah (Al Ahzaab 32)?",
                                options: ["Jangan keluar rumah sama sekali", "Jangan tunduk (melembut-lembutkan suara) dalam berbicara", "Harus memakai emas", "Harus diam membisu"],
                                correct: 1,
                                explanation: "...falaa takhdha'na bil qauli (janganlah kamu tunduk dalam berbicara) sehingga berkeinginanlah orang yang ada penyakit dalam hatinya."
                            },
                            {
                                question: "Apa tujuan perintah Allah dalam Al Ahzaab ayat 33 kepada Ahlul Bait?",
                                options: ["Memberatkan mereka", "Menghilangkan dosa dan membersihkan mereka sebersih-bersihnya", "Membatasi kebebasan", "Tidak ada tujuan"],
                                correct: 1,
                                explanation: "Sesungguhnya Allah bermaksud menghilangkan dosa dari kamu, hai ahlul bait dan membersihkan kamu sebersih-bersihnya."
                            }
                        ]
                    },
                    {
                        id: 128,
                        title: "Etika Terhadap Rasulullah SAW",
                        file: "topic_128.pdf",
                        content: `
<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>Etika Memanggil Nabi SAW</li>
    <li>Etika Berbicara dengan Nabi SAW</li>
    <li>Pembicaraan Khusus (Privat)</li>
    <li>Etika Meninggalkan Majelis</li>
    <li>Bershalawat kepada Nabi SAW</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<p>Sebagai wujud penghormatan dan kecintaan kepada Rasulullah SAW, Allah menetapkan etika dan adab khusus bagi para sahabat (dan umatnya) dalam berinteraksi dengan beliau, baik dalam memanggil, berbicara, maupun bermajelis.</p>
<hr class="divider">

<div class="content-section">
    <h3>1. Etika Memanggil dan Berbicara</h3>
    <div class="quran-quote">
        
        <p class="translation">Janganlah kamu menjadikan panggilan Rasul di antara kamu seperti panggilan sebagian kamu pada sebagian (yang lain)...</p>
        <span class="source">Surat An Nuur Ayat: 63</span>
    </div>
    <div class="quran-quote">
        
        <p class="translation">Hai orang-orang yang beriman, janganlah kamu meninggikan suaramu melebihi suara Nabi...</p>
        <span class="source">Surat Al Hujuraat Ayat: 2</span>
    </div>
</div>

<div class="content-section">
    <h3>2. Etika Majelis dan Konsultasi Khusus</h3>
    <p>Menghormati majelis ilmu bersama Nabi penting. Jika ada keperluan mendesak, harus meminta izin. Untuk pembicaraan empat mata (konsultasi privat), dianjurkan bersedekah sebelumnya (sebagai ujian kejujuran niat).</p>
    <div class="quran-quote">
        
        <p class="translation">...dan apabila mereka berada bersama-sama Rasulullah dalam sesuatu urusan yang memerlukan pertemuan, mereka tidak meninggalkan (Rasulullah) sebelum meminta izin kepadanya.</p>
        <span class="source">Surat An Nuur Ayat: 62</span>
    </div>
    <div class="quran-quote">
        
        <p class="translation">Hai orang-orang beriman, apabila kamu mengadakan pembicaraan khusus dengan Rasul hendaklah kamu mengeluarkan sedekah (kepada orang miskin) sebelum pembicaraan itu.</p>
        <span class="source">Surat Al Mujaadilah Ayat: 12</span>
    </div>
</div>

<div class="content-section">
    <h3>3. Perintah Bershalawat</h3>
    <div class="quran-quote">
        
        <p class="translation">Sesungguhnya Allah dan malaikat-malaikat-Nya bershalawat untuk Nabi. Hai orang-orang yang beriman, bershalawatlah kamu untuk Nabi dan ucapkanlah salam penghormatan kepadanya.</p>
        <span class="source">Surat Al Ahzaab Ayat: 56</span>
    </div>
</div>

<hr class="divider">
<h2>Penutup</h2>
<p>Memuliakan Rasulullah SAW tidak hanya semasa hidup beliau, tetapi juga dengan memuliakan ajaran, sunnah, dan menyebut nama beliau dengan Shalawat. Adab lahir dan batin kepada Nabi adalah cermin keimanan yang sempurna.</p>
            `,
                        quiz: [
                            {
                                question: "Bagaimana etika memanggil Rasulullah menurut Surat An Nuur ayat 63?",
                                options: ["Sama seperti memanggil teman", "Dengan suara keras", "Jangan seperti panggilan sebagian kamu pada sebagian yang lain (Harus hormat)", "Dengan nama kecilnya"],
                                correct: 2,
                                explanation: "Allah melarang memanggil Rasul dengan sebutan 'Hai Muhammad' seperti memanggil teman, melainkan 'Wahai Rasulullah/Nabi Allah' dengan lembut dan hormat."
                            },
                            {
                                question: "Apa larangan dalam Surat Al Hujuraat ayat 2 saat berbicara dengan Nabi?",
                                options: ["Jangan berbicara bahasa asing", "Jangan meninggikan suara melebihi suara Nabi", "Jangan menunduk", "Jangan tersenyum"],
                                correct: 1,
                                explanation: "Janganlah kamu meninggikan suaramu melebihi suara Nabi... agar tidak gugur pahala amalmu."
                            },
                            {
                                question: "Apa anjuran sebelum melakukan konsultasi privat (pembicaraan khusus) dengan Nabi dalam Al Mujaadilah ayat 12?",
                                options: ["Berpuasa", "Mandi besar", "Mengeluarkan sedekah", "Membawa hadiah"],
                                correct: 2,
                                explanation: "...hendaklah kamu mengeluarkan sedekah (kepada orang miskin) sebelum pembicaraan itu."
                            },
                            {
                                question: "Siapa yang bershalawat untuk Nabi menurut Surat Al Ahzaab ayat 56?",
                                options: ["Hanya manusia", "Allah dan Malaikat-Nya", "Hanya Jin", "Alam semesta"],
                                correct: 1,
                                explanation: "Sesungguhnya Allah dan malaikat-malaikat-Nya bershalawat untuk Nabi."
                            },
                            {
                                question: "Apa arti shalawat dari Allah?",
                                options: ["Memohon ampunan", "Memberi rahmat", "Memuji", "Memberi rezeki"],
                                correct: 1,
                                explanation: "Shalawat dari Allah berarti pemberian Rahmat. (Dari malaikat berarti permohonan ampunan)."
                            }
                        ]
                    }
                ]
            }

        ]
    }
    ,

    {
        id: "theme-6",
        title: "Tema 6: Kisah Dalam Alquran",
        description: "Kisah para Nabi dan Rasul",
        subjects: [

            {
                id: "subject-6-1",
                title: "Pokok Bahasan 1: ADAM AS.",
                topics: [

                    {
                        id: 129,
                        title: "Penciptaan Adam AS",
                        file: "topic_129.pdf",
                        content: `<h2>Daftar Isi</h2>
<ul class="toc-list">
<li>Penciptaan Adam As. sebagai Bapak Manusia</li>
<li>Allah Mengajari Adam As. Semua Benda</li>
<li>Seluruh Malaikat Sujud kepada Adam As. kecuali Iblis</li>
<li>Kesombongan Iblis</li>
<li>Iblis Diusir dari Surga</li>
<li>Permintaan Iblis untuk Ditangguhkan</li>
<li>Sumpah Iblis untuk Menggoda Keturunan Adam As.</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<h3>Penciptaan Adam As. sebagai Bapak Manusia</h3>
<div class="quran-quote">

<p class="translation">Dan (ingatlah) ketika Tuhanmu berfirman kepada para malaikat: berkata: "Mengapa hendak Engkau jadikan di dalamnya yang akan berbuat kerusakan padanya dan menumpahkan darah, padahal kami senantiasa bertasbih dengan memuji-Mu dan menyucikan-Mu?" Dia berfirman: “Sesungguhnya Aku tahu apa yang tidak kamu ketahui.”{30}</p>
<span class="source">Surat Al Baqarah  Ayat: 30</span>
</div>
<div class="quran-quote">


<p class="translation">Dan (ingatlah), ketika Tuhanmu berfirman kepada para malaikat: kering (yang berasal) dari lumpur hitam yang diberi bentuk”.{28} Lalu jika Aku telah sempurnakan kejadiannya, dan telah Aku tiupkan ke dalamnya ruh (ciptaan)-Ku, maka tunduklah kamu kepadanya dengan bersujud.{29} </p>
<span class="source">Surat Al Hijr  Ayat: 28 – 29</span>
</div>
<h3>Allah Mengajari Adam As. Semua Benda</h3>
<div class="quran-quote">



<p class="translation">Dan Dia mengajarkan kepada Adam nama-nama (benda) seluruhnya, kemudian mengemukakannya kepada para malaikat lalu berfirman: "Sebutkanlah kepada-Ku nama benda-benda itu jika kamu memang golongan yang benar!"{31} Mereka menjawab: "Maha Suci Engkau, tidak ada yang kami ketahui selain apa yang telah Engkau ajarkan kepada kami; sesungguhnya Engkau-lah Yang Maha Mengetahui lagi Maha Bijaksana."{32} Allah berfirman: "Hai Adam, beritahukan kepada mereka nama-nama benda ini." Maka setelah ia beritahukan kepada mereka nama-nama benda itu, Allah berfirman: "Bukankah sudah Kukatakan padamu, bahwasanya Aku mengetahui rahasia langit dan bumi dan mengetahui apa yang kamu lahirkan dan apa yang kamu sembunyikan?"{33}</p>
<span class="source">Surat Al Baqarah  Ayat: 31 – 33</span>
</div>
<h3>Seluruh Malaikat Sujud kepada Adam As. kecuali Iblis</h3>
<div class="quran-quote">

<p class="translation">Dan (ingatlah) ketika Kami berfirman kepada para malaikat: "Sujudlah kamu kepada Adam," maka sujudlah mereka kecuali iblis; ia enggan dan takabur dan ia adalah termasuk golongan yang kafir.{34}</p>
<span class="source">Surat Al Baqarah  Ayat: 34</span>
</div>
<div class="quran-quote">

<p class="translation">Sesungguhnya Kami telah menciptakanmu (Adam), lalu Kami bentuk tubuhmu, kemudian Kami katakan kepada para malaikat: "Sujudlah kamu kepada Adam", maka merekapun sujud kecuali iblis, ia tidak termasuk mereka yang bersujud .{11}</p>
<span class="source">Surat Al A’raaf  Ayat: 11</span>
</div>
<div class="quran-quote">

<p class="translation">Dan (ingatlah) ketika Kami berkata kepada malaikat: "Sujudlah kamu kepada Adam", maka mereka sujud kecuali iblis, ia enggan.{116} </p>
<span class="source">Surat Thaahaa  Ayat: 116</span>
</div>
<h3>Kesombongan Iblis</h3>
<div class="quran-quote">

<p class="translation">Allah berfirman: "Apakah yang menghalangimu untuk bersujud (kepada Adam) di waktu Aku menyuruhmu?" Menjawab iblis "Saya lebih baik daripadanya: Engkau ciptakan saya dari api sedang dia Engkau ciptakan dari tanah".{12}</p>
<span class="source">Surat Al A'raaf Ayat: 12</span>
</div>
<h3>Iblis Diusir dari Surga</h3>
<div class="quran-quote">

<p class="translation">Allah berfirman: "Turunlah kamu dari surga itu; karena tidaklah kamu sepatutnya menyombongkan maka keluarlah, sesungguhnya kamu termasuk golongan yang hina”.{13} </p>
<span class="source">Surat Al A’raaf  Ayat: 13</span>
</div>
<h3>Permintaan Iblis untuk Ditangguhkan</h3>
<p>Iblis menjawab: "Beri tangguhlah aku sampai waktu mereka tangguh." {15}</p>
<div class="quran-quote">



<p class="translation">Iblis berkata: "Ya Tuhanku, beri tangguhlah aku sampai hari mereka dibangkitkan.”{79} Allah berfirman: “Sesungguhnya kamu termasuk mereka yang diberi tangguh,{80} Sampai kepada hari yang telah ditentukan waktunya (hari kiamat).”{81} </p>
<span class="source">Surat Shaad  Ayat: 79 – 81</span>
</div>
<p>Iblis menjawab: "Karena Engkau telah menghukumku sesat, aku benar- benar akan (menghalangi) mereka dari jalan-Mu yang lurus,{16} Kemudian aku akan mendatangi mereka dari muka dan dari belakang mereka, dari kanan dan dari kiri mereka. Dan Engkau tidak akan mendapati kebanyakan mereka bersyukur (taat).{17} Allah berfirman: "Keluarlah kamu dari surga itu dalam keadaan terhina lagi terusir. Sesungguhnya siapa di antara mereka mengikutimu, sungguh</p>
<h3>Sumpah Iblis untuk Menggoda Keturunan Adam As.</h3>
<div class="quran-quote">


<p class="translation">Iblis berkata: "Demi kekuasaan-Mu, akan aku sesatkan mereka semuanya,{82} Kecuali hamba-hamba-Mu yang ikhlash di antara mereka.{83} </p>
<span class="source">Surat Shaad  Ayat: 82 – 83</span>
</div>
<hr class="divider">
<h2>Penutup</h2>
<p>Demikianlah kisah Adam AS berdasarkan dalil-dalil Al-Qur'an.</p>`,
                        quiz: [
                            {
                                question: "Mengapa Malaikat mempertanyakan penciptaan manusia (Adam) di bumi?",
                                options: ["Karena manusia akan menggantikan Malaikat", "Karena khawatir manusia akan berbuat kerusakan dan menumpahkan darah", "Karena Malaikat ingin tinggal di bumi", "Karena manusia lebih kuat"],
                                correct: 1,
                                explanation: "Malaikat bertanya: 'Mengapa Engkau hendak menjadikan (khalifah) di bumi itu orang yang akan membuat kerusakan padanya dan menumpahkan darah...' (Al Baqarah: 30)"
                            },
                            {
                                question: "Apa alasan Iblis menolak sujud kepada Adam?",
                                options: ["Karena Iblis sedang shalat", "Karena Adam belum bisa bicara", "Karena Iblis merasa lebih baik (diciptakan dari api) dibanding Adam (dari tanah)", "Karena Iblis takut pada Malaikat"],
                                correct: 2,
                                explanation: "Iblis berkata: 'Aku lebih baik daripadanya: Engkau ciptakan aku dari api sedang dia Engkau ciptakan dari tanah.' (Al A'raaf: 12)"
                            },
                            {
                                question: "Apa kelebihan Adam yang ditunjukkan Allah kepada Malaikat?",
                                options: ["Kekuatan fisik", "Sayap yang indah", "Pengetahuan tentang nama-nama benda", "Umur yang panjang"],
                                correct: 2,
                                explanation: "Dan Dia mengajarkan kepada Adam nama-nama (benda) seluruhnya... (Al Baqarah: 31)"
                            },
                            {
                                question: "Apa janji Iblis setelah diusir dari Surga?",
                                options: ["Akan bertaubat", "Akan berdiam diri", "Akan menyesatkan manusia (anak cucu Adam) dari jalan yang lurus", "Akan membuat surga sendiri"],
                                correct: 2,
                                explanation: "Iblis menjawab: '...aku benar-benar akan (menghalangi) mereka dari jalan-Mu yang lurus.' (Al A'raaf: 16)"
                            },
                            {
                                question: "Siapakah golongan yang tidak dapat disesatkan oleh Iblis?",
                                options: ["Orang kaya", "Hamba-hamba Allah yang ikhlas (mukhlis)", "Para raja", "Orang yang kuat"],
                                correct: 1,
                                explanation: "Kecuali hamba-hamba-Mu yang ikhlas di antara mereka. (Shaad: 83)"
                            }
                        ]
                    },

                    {
                        id: 130,
                        title: "Adam AS di Surga",
                        file: "topic_130.pdf",
                        content: `<h2>Daftar Isi</h2>
<ul class="toc-list">
<li>Kehidupan Adam As. di Surga</li>
<li>Setan Menggoda Adam As.</li>
<li>Allah Menerima Taubat Adam As. Dan Memilihnya</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<h3>Kehidupan Adam As. di Surga</h3>
<div class="quran-quote">

<p class="translation">Dan Kami berfirman: "Hai Adam, tinggallah kamu dan istrimu di surga dan makanlah olehmu berdua makanannya yang banyak lagi baik di mana saja kamu berdua sukai, dan jangan kamu berdua dekati pohon ini, yang menyebabkan kamu berdua termasuk golongan zalim.{35}</p>
<span class="source">Surat Al Baqarah  Ayat: 35</span>
</div>
<div class="quran-quote">



<p class="translation">Maka Kami berkata: "Hai Adam, sesungguhnya ini (iblis) adalah musuh Pohon yang dilarang Allah mendekatinya tidak dapat dipastikan, sebab Alquran dan Hadis tidak menerangkan. Ada yang menamakan pohon Khuldi sebagaimana tersebut dalam surat Thaha ayat 120, tapi itu adalah nama yang diberikan setan.</p>
<span class="source">Surat Thaahaa  Ayat: 117 – 119</span>
</div>
<h3>Setan Menggoda Adam As.</h3>
<div class="quran-quote">

<p class="translation">Lalu keduanya digelincirkan oleh setan dari surga itu dan dikeluarkan dari keadaan semula dan Kami berfirman: "Turunlah kalian, sebagian kamu menjadi musuh bagi yang lain, dan bagimu ada tempat kediaman di bumi, dan kesenangan hidup sampai waktu yang ditentukan."{36}</p>
<span class="source">Surat Al Baqarah  Ayat: 36</span>
</div>
<p>Maka setan membisikkan pikiran jahat kepada keduanya untuk menampakkan kepada keduanya apa yang tertutup dari mereka yaitu auratnya dan setan berkata: "Tuhanmu tidak melarangmu dari pohon ini, melainkan supaya kamu berdua tidak menjadi malaikat atau tidak menjadi termasuk yang memberi nasehat kepada kamu berdua",{21} Maka setan membujuk keduanya (untuk memakan buah itu) dengan tipu daya. Tatkala keduanya telah merasai (buah) kayu itu, nampaklah bagi keduanya aurat-auratnya, dan mulailah keduanya menutupinya dengan daun-daun surga. Kemudian Tuhan mereka menyeru mereka: "Bukankah Aku telah melarang kamu berdua dari pohon itu dan Aku katakan kamu berdua?"{22}</p>
<div class="quran-quote">


<p class="translation"> Kemudian setan membisikkan pikiran jahat kepadanya, dengan berkata: "Hai Adam, maukah aku tunjukkan kepadamu pohon keabadian dan kerajaan yang tidak akan binasa?"{120} Maka keduanya memakan dari buah pohon itu, lalu nampaklah bagi keduanya aurat-auratnya dan mulailah keduanya menutupinya dengan daun-daun (yang ada di) surga, dan durhakalah Adam kepada Tuhan dan sesatlah ia.{121}</p>
<span class="source">Surat Thaahaa  Ayat: 120 – 121</span>
</div>
<h3>Allah Menerima Taubat Adam As. Dan Memilihnya</h3>
<div class="quran-quote">

<p class="translation">Kemudian Adam menerima beberapa kalimat dari Tuhannya, maka Allah menerima taubatnya. Sesungguhnya Allah Maha Penerima taubat lagi Maha Penyayang.{37}</p>
<span class="source">Surat Al Baqarah  Ayat: 37</span>
</div>
<div class="quran-quote">

<p class="translation">Keduanya berkata: "Ya Tuhan kami, kami telah menganiaya diri kami sendiri, dan jika Engkau tidak mengampuni kami dan memberi rahmat kepada kami, niscaya kami termasuk orang-orang yang merugi.{23}</p>
<span class="source">Surat Al A'raaf Ayat: 23</span>
</div>
<div class="quran-quote">

<p class="translation">Kemudian Tuhannya memilihnya maka Dia menerima taubatnya dan memberinya petunjuk.{122} </p>
<span class="source">Surat Thaahaa  Ayat: 122</span>
</div>
<hr class="divider">
<h2>Penutup</h2>
<p>Demikianlah kisah Adam AS berdasarkan dalil-dalil Al-Qur'an.</p>`,
                        quiz: [
                            {
                                question: "Apa larangan Allah kepada Adam dan Hawa di Surga?",
                                options: ["Jangan tidur malam", "Jangan makan buah-buahan", "Jangan mendekati pohon tertentu ini", "Jangan berbicara dengan Malaikat"],
                                correct: 2,
                                explanation: "...dan jangan kamu berdua dekati pohon ini, yang menyebabkan kamu berdua termasuk golongan zalim. (Al Baqarah: 35)"
                            },
                            {
                                question: "Bagaimana cara setan (Iblis) menggoda Adam dan Hawa?",
                                options: ["Dengan kekerasan", "Dengan tipu daya dan sumpah palsu (mengatakan sebagai pemberi nasehat)", "Dengan memberi emas", "Dengan ancaman"],
                                correct: 1,
                                explanation: "Dan dia (setan) bersumpah kepada keduanya: 'Sesungguhnya saya adalah termasuk orang yang memberi nasehat kepada kamu berdua'. (Al A'raaf: 21)"
                            },
                            {
                                question: "Apa nama pohon yang disebut setan untuk menipu Adam?",
                                options: ["Pohon Zaitun", "Pohon Tin", "Pohon Khuldi (Keabadian)", "Pohon Kurma"],
                                correct: 2,
                                explanation: "Setan berkata: 'Hai Adam, maukah aku tunjukkan kepadamu pohon khuldi (keabadian) dan kerajaan yang tidak akan binasa?' (Thaahaa: 120)"
                            },
                            {
                                question: "Apa yang terjadi setelah Adam dan Hawa memakan buah terlarang tersebut?",
                                options: ["Mereka menjadi Malaikat", "Terbuka auratnya dan mereka menutupinya dengan daun surga", "Mereka menjadi abadi", "Mereka langsung tertidur"],
                                correct: 1,
                                explanation: "...nampaklah bagi keduanya aurat-auratnya dan mulailah keduanya menutupinya dengan daun-daun (yang ada di) surga... (Thaahaa: 121)"
                            },
                            {
                                question: "Apa doa taubat Adam dan Hawa?",
                                options: ["Rabbana aatina fid dunya hasanah", "Rabbana zhalamna anfusana wa illam taghfir lana wa tarhamna lanakunanna minal khaasirin", "Subhanallah wal hamdulillah", "La ilaha illa anta subhanaka inni kuntu minaz zhalimin"],
                                correct: 1,
                                explanation: "Keduanya berkata: 'Ya Tuhan kami, kami telah menganiaya diri kami sendiri, dan jika Engkau tidak mengampuni kami...' (Al A'raaf: 23)"
                            }
                        ]
                    },

                    {
                        id: 131,
                        title: "Adam AS Turun ke Bumi",
                        file: "topic_131.pdf",
                        content: `<h2>Daftar Isi</h2>
<ul class="toc-list">
<li>Kehidupan Adam As. di Bumi</li>
<li>Perjanjian Adam As. dan Keturunannya dengan Allah</li>
</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<h3>Kehidupan Adam As. di Bumi</h3>
<div class="quran-quote">


<p class="translation">Kami berfirman: "Turunlah kamu semua dari surga itu, kemudian jika datang petunjuk-Ku kepadamu, maka siapa yang mengikuti petunjuk-Ku, niscaya tidak ada kekhawatiran atas mereka, dan tidak (pula) mereka bersedih hati.”{38}</p>
<span class="source">Surat Al Baqarah  Ayat: 38 – 39</span>
</div>
<div class="quran-quote">


<p class="translation">Allah berfirman: "Turunlah kamu semua, sebagian kamu menjadi musuh bagi sebagian yang lain. Dan bagimu tempat kediaman dan kesenangan (tempat mencari kehidupan) di muka bumi sampai waktu tertentu.”{24} Allah berfirman: "Di bumi itu kamu hidup dan di bumi itu kamu mati, dan dari bumi itu (pula) kamu akan dibangkitkan.{25}</p>
<span class="source">Surat Al A\`raaf  Ayat: 24 – 25</span>
</div>
<div class="quran-quote">

<span class="source">Surat Thaahaa  Ayat: 123</span>
</div>
<p>Allah berfirman: "Turunlah kamu berdua dari surga bersama-sama, sebagian kamu menjadi musuh bagi sebagian yang lain. Maka jika datang kepadamu petunjuk dari-Ku, lalu siapa yang mengikut petunjuk-Ku, ia tidak akan sesat dan tidak akan celaka.{123}</p>
<h3>Perjanjian Adam As. dan Keturunannya dengan Allah</h3>
<div class="quran-quote">



<p class="translation">Dan (ingatlah), ketika Tuhanmu mengeluarkan keturunan anak-anak Adam dari sulbi mereka dan Allah mengambil kesaksian terhadap jiwa mereka (seraya berfirman): "Bukankah Aku ini Tuhanmu?" mereka menjawab: "Betul (Engkau Tuhan kami), kami menjadi saksi". (Kami lakukan yang demikian itu) agar di hari kiamat kamu tidak mengatakan: "Sesungguhnya kami (Bani Adam) adalah orang-orang yang lengah terhadap ini (keesaan Tuhan)",{172} Atau agar kamu tidak mengatakan: "Sesungguhnya orang tua kami telah mempersekutukan Tuhan sejak dahulu, sedang kami ini adalah anak-anak keturunan yang (datang) sesudah mereka. Maka apakah Engkau akan membinasakan kami karena perbuatan orang-orang yang sesat dahulu?"{173} Dan demikianlah Kami menjelaskan ayat-ayat itu, agar mereka kembali (kepada kebenaran).{174}</p>
<span class="source">Surat Al A'raaf Ayat: 172 – 174</span>
</div>
<div class="quran-quote">

<p class="translation">Dan sungguh telah Kami perintahkan kepada Adam dahulu, maka ia lupa (perintah itu), dan tidak Kami dapati padanya kemauan kuat.{115}</p>
<span class="source">Surat Thaahaa  Ayat: 115</span>
</div>
<div class="quran-quote">



<p class="translation">Bukankah Aku telah memerintahkan kepadamu Hai Bani Adam supaya kamu tidak mengabdi kepada setan? Sesungguhnya setan itu adalah musuh yang nyata bagi kamu",{60} Dan hendaklah kamu mengabdi kepada-Ku. Inilah jalan yang lurus.{61} Sesungguhnya setan itu telah menyesatkan sebagian besar di antara mu, maka apakah kamu tidak memikirkan ?.{62} </p>
<span class="source">Surat Yaasiin  Ayat: 60 – 62</span>
</div>
<hr class="divider">
<h2>Penutup</h2>
<p>Demikianlah kisah Adam AS berdasarkan dalil-dalil Al-Qur'an.</p>`,
                        quiz: [
                            {
                                question: "Apa konsekuensi dari pelanggaran yang dilakukan Adam dan Hawa?",
                                options: ["Tetap di surga", "Turun ke bumi", "Menjadi Malaikat", "Dihukum penjara"],
                                correct: 1,
                                explanation: "Kami berfirman: 'Turunlah kamu semua dari surga itu...' (Al Baqarah: 38)"
                            },
                            {
                                question: "Apa jaminan Allah bagi mereka yang mengikuti petunjuk-Nya saat di bumi?",
                                options: ["Akan menjadi kaya raya", "Tidak ada kekhawatiran atas mereka dan tidak bersedih hati", "Akan hidup selamanya", "Akan menjadi raja"],
                                correct: 1,
                                explanation: "...maka siapa yang mengikuti petunjuk-Ku, niscaya tidak ada kekhawatiran atas mereka, dan tidak (pula) mereka bersedih hati. (Al Baqarah: 38)"
                            },
                            {
                                question: "Kapan Allah mengambil kesaksian (perjanjian) terhadap jiwa keturunan Adam?",
                                options: ["Saat mereka dewasa", "Saat mereka lahir", "Saat masih di alam sulbi (sebelum dilahirkan ke dunia)", "Saat mereka mati"],
                                correct: 2,
                                explanation: "Dan (ingatlah), ketika Tuhanmu mengeluarkan keturunan anak-anak Adam dari sulbi mereka... (Al A'raaf: 172)"
                            },
                            {
                                question: "Apa isi kesaksian jiwa manusia kepada Allah?",
                                options: ["Bahwa Allah adalah Tuhan mereka", "Bahwa mereka akan kaya", "Bahwa mereka akan sukses", "Bahwa dunia itu abadi"],
                                correct: 0,
                                explanation: "...Bukankah Aku ini Tuhanmu? mereka menjawab: Betul (Engkau Tuhan kami)... (Al A'raaf: 172)"
                            },
                            {
                                question: "Siapakah musuh yang nyata bagi manusia menurut Al Quran?",
                                options: ["Manusia lain", "Hewan buas", "Setan / Iblis", "Alam semesta"],
                                correct: 2,
                                explanation: "Sesungguhnya setan itu adalah musuh yang nyata bagi kamu. (Yaasiin: 60)"
                            }
                        ]
                    }
                ]
            }

            ,
            {
                id: "subject-6-2",
                title: "Pokok Bahasan 2: IDRIS AS.",
                topics: [

                    {
                        id: 132,
                        title: "Keutamaan Idris AS",
                        file: "topic_132.pdf",
                        content: `<h2>Daftar Isi</h2>
<ul class="toc-list">
    <li>KEUTAMAAN IDRIS AS</li>

</ul>
<hr class="divider">
<h2>Isi Materi</h2>
<div class="content-section">
<h3>KEUTAMAAN IDRIS AS</h3>

<div class="quran-quote">


<p class="translation">Dan ceritakanlah (Hai Muhammad kepada mereka, kisah) Idris (yang tersebut) di dalam Alquran. Sesungguhnya ia adalah seorang yang sangat membenarkan dan seorang nabi.{56} Dan Kami telah mengangkatnya ke martabat yang tinggi.{57}</p>
<span class="source">Surat Maryam  Ayat: 56 – 57</span>
</div>
<hr class="divider">
<h2>Penutup</h2>
<p>Demikianlah kisah Idris AS berdasarkan dalil-dalil Al-Qur'an.</p>`,
                        quiz: [
                            {
                                question: "Nabi Idris AS dikenal sebagai nabi yang...",
                                options: ["Sangat pembohong", "Sangat membenarkan (Shiddiq)", "Sangat kaya", "Sangat kuat"],
                                correct: 1,
                                explanation: "Sesungguhnya ia adalah seorang yang sangat membenarkan dan seorang nabi. (Maryam: 56)"
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-6-3",
                title: "Pokok Bahasan 3: NUH AS.",
                topics: [
                    {
                        id: 133,
                        title: "Dakwah Nuh AS",
                        file: "topic_133.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><h3>3.1 DAKWAH NUH AS</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya Kami telah mengutus Nuh kepada kaumnya, maka ia tinggal di antara mereka seribu tahun kurang lima puluh tahun. Maka mereka ditimpa banjir besar, dan mereka adalah orang-orang yang zalim.</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 14</span>
                </div>

                <h3>3.1.1 Berdakwah Siang Malam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Nuh berkata: "Ya Tuhanku sesungguhnya aku telah menyeru kaumku malam dan siang, maka seruanku itu hanyalah menambah mereka lari (dari kebenaran)."</p>
                    <span class="source">Surat Nuh Ayat: 5-6</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan sesungguhnya setiap kali aku menyeru mereka (kepada iman)... mereka memasukkan anak jari mereka ke dalam telinganya dan menutupkan bajunya (ke mukanya) dan mereka tetap (mengingkari) dan menyombongkan diri dengan sangat.</p>
                    <span class="source">Surat Nuh Ayat: 7</span>
                </div>

                <h3>3.1.2 Berdakwah Secara Terang-terangan dan Diam-diam</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Kemudian sesungguhnya aku telah menyeru mereka (dengan suara) keras. Kemudian sesungguhnya aku telah (menyeru) mereka dengan terang-terangan dan dengan diam-diam.</p>
                    <span class="source">Surat Nuh Ayat: 8-9</span>
                </div>

                <h3>3.1.3 Berdakwah (Menyeru) Kaumnya kepada Tauhidullah</h3>
                <div class="quran-quote">
                     
                     <p class="translation">...Hendaklah kamu mengabdi kepada Allah, bertakwalah kepada-Nya dan taatilah aku.</p>
                     <span class="source">Surat Nuh Ayat: 1-3</span>
                </div>

                <h3>3.1.4 Berdakwah (Menyeru) Kaumnya untuk Bersyukur</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka aku katakan kepada mereka: 'Mohonlah ampun kepada Tuhanmu, -sesungguhnya Dia adalah Maha Pengampun-, niscaya Dia akan mengirimkan hujan kepadamu dengan lebat,</p>
                    <span class="source">Surat Nuh Ayat: 10-11</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">dan membanyakkan harta dan anak-anakmu, dan mengadakan untukmu kebun-kebun dan mengadakan (pula di dalamnya) untukmu sungai-sungai.</p>
                    <span class="source">Surat Nuh Ayat: 12</span>
                </div>
            </div>`,
                        quiz: [
                            {
                                question: "Berapa lama Nabi Nuh AS berdakwah kepada kaumnya menurut Al-'Ankabut ayat 14?",
                                options: ["100 tahun", "500 tahun", "950 tahun", "1000 tahun"],
                                correct: 2,
                                explanation: "...maka ia tinggal di antara mereka seribu tahun kurang lima puluh tahun (950 tahun)."
                            },
                            {
                                question: "Bagaimana respon kaum Nuh saat diseru kepada iman (Surat Nuh ayat 7)?",
                                options: ["Mereka mendengarkan dengan baik", "Mereka menutup telinga dan menyombongkan diri", "Mereka langsung beriman", "Mereka meminta bukti mukjizat"],
                                correct: 1,
                                explanation: "...mereka memasukkan anak jari mereka ke dalam telinganya... dan menyombongkan diri dengan sangat."
                            },
                            {
                                question: "Metode dakwah apa yang digunakan Nabi Nuh?",
                                options: ["Hanya diam-diam", "Hanya terang-terangan", "Siang dan malam, diam-diam dan terang-terangan", "Melalui surat"],
                                correct: 2,
                                explanation: "Nuh menyeru mereka malam dan siang, dengan suara keras (terang-terangan) dan diam-diam (Surat Nuh 5, 8-9)."
                            },
                            {
                                question: "Apa janji Allah jika kaum Nuh mau memohon ampun (Surat Nuh 10-12)?",
                                options: ["Dijadikan penguasa dunia", "Diberi hujan lebat, harta, dan anak-anak", "Diberi umur panjang", "Diberi kekuatan fisik"],
                                correct: 1,
                                explanation: "Niscaya Dia akan mengirimkan hujan lebat, membanyakkan harta dan anak-anakmu..."
                            },
                            {
                                question: "Apa inti seruan dakwah Nabi Nuh (Surat Nuh ayat 3)?",
                                options: ["Berdagang dengan jujur", "Menyembah Allah, bertakwa, dan taat", "Membangun kota", "Berperang melawan musuh"],
                                correct: 1,
                                explanation: "...Hendaklah kamu mengabdi kepada Allah, bertakwalah kepada-Nya dan taatilah aku."
                            }
                        ]
                    },
                    {
                        id: 134,
                        title: "Banjir Besar",
                        file: "topic_134.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><h3>3.2 SIKAP KAUM NUH AS TERHADAP DAKWAHNYA</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Pemuka-pemuka dari kaumnya berkata: "Sesungguhnya kami memandang kamu berada dalam kesesatan yang nyata".</p>
                    <span class="source">Surat Al A'raf Ayat: 60</span>
                </div>
                
                <h3>3.2.1 Nuh As. Dianggap Sesat, Pendusta, dan Gila</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Nuh menjawab: "Hai kaumku, tak ada padaku kesesatan sedikitpun tetapi aku adalah utusan dari Tuhan semesta alam".</p>
                    <span class="source">Surat Al A'raf Ayat: 61-62</span>
                </div>
                <div class="quran-quote">
                     
                     <p class="translation">Maka berkatalah pemuka-pemuka orang kafir... "Orang ini tidak lain hanyalah manusia sepertimu... Ia tidak lain hanyalah seorang laki-laki yang berpenyakit gila..."</p>
                     <span class="source">Surat Al Mu'minuun Ayat: 24-25</span>
                </div>

                <h3>3.2.2 Ejekan terhadap Pengikut Nuh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">"...dan kami tidak melihat orang-orang yang mengikutimu, kecuali orang-orang yang hina dina di antara kami..."</p>
                    <span class="source">Surat Hud Ayat: 27</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka berkata: "Apakah kami akan beriman kepadamu, padahal yang mengikuti kamu ialah orang-orang yang hina?"</p>
                    <span class="source">Surat Asy Syu'araa Ayat: 111</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Nuh menjawab: "...Dan tidaklah aku akan mengusir orang-orang yang beriman."</p>
                    <span class="source">Surat Asy Syu'araa Ayat: 114</span>
                </div>

                <h3>3.2.3 Tantangan Kaum Nuh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Mereka berkata: "Hai Nuh, sesungguhnya kamu telah berbantah dengan kami... maka datangkanlah kepada kami azab yang kamu ancamkan kepada kami, jika kamu termasuk orang-orang yang benar".</p>
                    <span class="source">Surat Hud Ayat: 32</span>
                </div>

                <h3>3.2.4 Makar dan Berhala Kaum Nuh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mereka melakukan tipu daya yang besar. Dan mereka berkata: "Jangan sekali-kali kamu meninggalkan (pen penyembahan) tuhan-tuhan kamu dan jangan pula sekali-kali kamu meninggalkan (penyembahan) Wadd, dan jangan pula Suwa', Yaghuts, Ya'uq dan Nasr".</p>
                    <span class="source">Surat Nuh Ayat: 22-23</span>
                </div>

                <h3>3.2.5 Doa Nabi Nuh</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka dia mengadu kepada Tuhannya: "bahwasanya aku ini adalah orang yang dikalahkan, oleh sebab itu tolonglah (aku)".</p>
                    <span class="source">Surat Al Qamar Ayat: 10</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">Nuh berkata: "Ya Tuhanku, janganlah Engkau biarkan seorangpun di antara orang-orang kafir itu tinggal di atas bumi."</p>
                    <span class="source">Surat Nuh Ayat: 26</span>
                </div>
            </div>`,
                        quiz: [
                            {
                                question: "Apa tuduhan kaumnya kepada Nabi Nuh AS?",
                                options: ["Seorang raja yang adil", "Seorang penyair", "Orang yang sesat, pendusta, dan gila", "Orang kaya yang sombong"],
                                correct: 2,
                                explanation: "Mereka menyebutnya sesat (Al A'raf 60), pendusta (Hud 27), dan gila (Al Mu'minun 25)."
                            },
                            {
                                question: "Bagaimana tanggapan kaum Nuh terhadap pengikut Nabi Nuh?",
                                options: ["Mereka menghormatinya", "Mereka menganggap pengikut Nuh adalah orang-orang hina dina", "Mereka ingin bergabung", "Mereka memberi hadiah"],
                                correct: 1,
                                explanation: "...padahal yang mengikuti kamu ialah orang-orang yang hina? (Asy Syu'araa 111)"
                            },
                            {
                                question: "Nama-nama berhala kaum Nuh yang Disebut dalam Al-Qur'an adalah...",
                                options: ["Latta, Uzza, Manat", "Wadd, Suwa', Yaghuts, Ya'uq, Nasr", "Baal, Hubal", "Zeus, Apollo"],
                                correct: 1,
                                explanation: "...jangan pula sekali-kali kamu meninggalkan (penyembahan) Wadd, Suwa', Yaghuts, Ya'uq dan Nasr (Nuh 23)."
                            },
                            {
                                question: "Apa tantangan kaum Nuh ketika bosan didebat?",
                                options: ["Minta didatangkan azab segera", "Minta harta kekayaan", "Minta menjadi pemimpin", "Minta kitab suci"],
                                correct: 0,
                                explanation: "...maka datangkanlah kepada kami azab yang kamu ancamkan kepada kami (Hud 32)."
                            },
                            {
                                question: "Apa doa Nabi Nuh setelah kaumnya terus membangkang?",
                                options: ["Ya Tuhan, berilah mereka petunjuk", "Ya Tuhan, jangan biarkan seorang kafirpun tinggal di bumi", "Ya Tuhan, kayakanlah aku", "Ya Tuhan, pindahkan aku ke negeri lain"],
                                correct: 1,
                                explanation: "Nuh berkata: Ya Tuhanku, janganlah Engkau biarkan seorangpun di antara orang-orang kafir itu tinggal di atas bumi (Nuh 26)."
                            }
                        ]
                    },
                    {
                        id: 135,
                        title: "Keselamatan Nuh AS",
                        file: "topic_135.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><h3>3.3 AZAB DAN BALASAN TERHADAP KAUM NUH AS</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan diwahyukan kepada Nuh, bahwasanya sekali-kali tidak akan beriman di antara kaummu, kecuali orang yang telah beriman (saja), karena itu janganlah kamu bersedih hati tentang apa yang selalu mereka kerjakan.</p>
                    <span class="source">Surat Hud Ayat: 36</span>
                </div>
                
                <h3>3.3.1 Perintah Membuat Perahu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan buatlah bahtera itu dengan pengawasan dan petunjuk wahyu Kami...</p>
                    <span class="source">Surat Hud Ayat: 37</span>
                </div>

                <h3>3.3.2 Nuh As. Diejek oleh Kaumnya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan mulailah Nuh membuat bahtera... Nuh berkata: "Jika kamu mengejek kami, maka sesungguhnya kami (pun) mengejekmu sebagaimana kamu sekalian mengejek (kami)."</p>
                    <span class="source">Surat Hud Ayat: 38</span>
                </div>

                <h3>3.3.3 Kaum Beriman dan Tiap Pasang Binatang Menaiki Perahu</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...Kami berfirman: "Muatkanlah ke dalam bahtera itu dari masing-masing binatang sepasang (jantan dan betina), dan keluargamu..."</p>
                    <span class="source">Surat Hud Ayat: 40</span>
                </div>

                <h3>3.3.4 Terjadinya Taufan (Banjir Besar)</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka Kami bukakan pintu-pintu langit dengan (menurunkan) air yang tercurah.</p>
                    <span class="source">Surat Al Qamar Ayat: 11</span>
                </div>
                <div class="quran-quote">
                    
                    <p class="translation">Dan Kami jadikan bumi memancarkan mata air-mata air...</p>
                    <span class="source">Surat Al Qamar Ayat: 12</span>
                </div>

                <h3>3.3.5 Nuh As. dan Anaknya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">"Hai anakku, naiklah (ke kapal) bersama kami dan janganlah kamu bersama orang-orang yang kafir".</p>
                    <span class="source">Surat Hud Ayat: 42</span>
                </div>
                 <div class="quran-quote">
                    
                    <p class="translation">Anaknya menjawab: "Aku akan mencari perlindungan ke gunung yang dapat memeliharaku dari air bah!"...</p>
                    <span class="source">Surat Hud Ayat: 43</span>
                </div>

                <h3>3.3.6 Nuh As. Selamat serta Kehancuran Kaumnya</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Maka Kami selamatkan Nuh dan penumpang-penumpang bahtera itu...</p>
                    <span class="source">Surat Al 'Ankabuut Ayat: 15</span>
                </div>

                <h3>3.3.7 Perintah Berdoa agar Mendarat di Tempat yang Diberkati</h3>
                <div class="quran-quote">
                    
                    <p class="translation">Dan berdoalah: Ya Tuhanku, tempatkanlah aku pada tempat yang diberkati...</p>
                    <span class="source">Surat Al Mu'minuun Ayat: 29</span>
                </div>

                <h3>3.3.8 Banjir Reda dan Perahu Mendarat di Bukit Judi</h3>
                <div class="quran-quote">
                    
                    <p class="translation">...dan bahtera itupun berlabuh di atas bukit Judi...</p>
                    <span class="source">Surat Hud Ayat: 44</span>
                </div>
            </div>`,
                        quiz: [
                            {
                                question: "Siapakah Nabi yang berdakwah selama 950 tahun?",
                                options: ["Adam AS", "Idris AS", "Nuh AS", "Hud AS"],
                                correct: 2,
                                explanation: "Nabi Nuh AS berdakwah kepada kaumnya selama 950 tahun (Lihat Al-Ankabut: 14)."
                            },
                            {
                                question: "Apa azab yang menimpa kaum Nuh yang ingkar?",
                                options: ["Gempa bumi", "Hujan batu", "Banjir besar (Taufan)", "Angin kencang"],
                                correct: 2,
                                explanation: "Maka mereka ditimpa banjir besar, dan mereka adalah orang-orang yang zalim."
                            },
                            {
                                question: "Di manakah bahtera Nuh berlabuh setelah banjir surut?",
                                options: ["Bukit Sinai", "Bukit Judi", "Bukit Shafa", "Gua Hira"],
                                correct: 1,
                                explanation: "...dan bahtera itupun berlabuh di atas bukit Judi."
                            },
                            {
                                question: "Siapakah anak Nabi Nuh yang tenggelam karena enggan naik bahtera?",
                                options: ["Ismail", "Yusuf", "Qan'aan (Anak yang durhaka)", "Ibrahim"],
                                correct: 2,
                                explanation: "Anak Nuh memilih mencari perlindungan ke gunung dan akhirnya tenggelam."
                            },
                            {
                                question: "Apa doa yang diajarkan Allah kepada Nuh saat mendarat (Al Mu'minuun 29)?",
                                options: ["Ya Tuhanku, tambahkanlah ilmuku", "Ya Tuhanku, berilah aku rezeki", "Ya Tuhanku, tempatkanlah aku pada tempat yang diberkati", "Ya Tuhanku, ampunilah dosaku"],
                                correct: 2,
                                explanation: "Dan berdoalah: Ya Tuhanku, tempatkanlah aku pada tempat yang diberkati..."
                            }
                        ]
                    }



                ]
            },
            {
                id: "subject-6-4",
                title: "Pokok Bahasan 4: HUD AS.",
                topics: [
                    {
                        id: 136,
                        title: "DAKWAH HUD AS",
                        file: "topic_136.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><h3>4.1 DAKWAH HUD AS</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Apakah kamu tidak memperhatikan bagaimana Tuhanmu berbuat terhadap kaum 'Aad? (yaitu) penduduk Iram yang mempunyai bangunan-bangunan yang tinggi, yang belum pernah dibangun (suatu kota) seperti itu, di negeri-negeri lain.</p>
                            <span class="source">Surat Al Fajr Ayat: 6-8</span>
                        </div>

                        <h3>4.1.1 Peringatan kepada Kaum 'Aad</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">...Dan ingatlah olehmu di waktu Allah menjadikan kamu pengganti-pengganti (yang berkuasa) sesudah kaum Nuh, dan Tuhan telah melebihkan kekuatan tubuh dan perawakanmu (daripada kaum Nuh itu). Maka ingatlah nikmat-nikmat Allah supaya kamu mendapat keberuntungan.</p>
                            <span class="source">Surat Al A'raf Ayat: 69</span>
                        </div>

                        <h3>4.1.2 Seruan Tauhid</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Dan kepada kaum 'Aad (Kami utus) saudara mereka, Hud. Ia berkata: "Hai kaumku, sembahlah Allah, sekali-kali tidak ada bagimu Tuhan selain Dia. Kamu hanyalah mengada-adakan saja."</p>
                            <span class="source">Surat Hud Ayat: 50</span>
                        </div>
                        <div class="quran-quote">
                            
                            <p class="translation">"Dan (dia berkata): "Hai kaumku, mohonlah ampun kepada Tuhanmu lalu bertobatlah kepada-Nya, niscaya Dia menurunkan hujan yang sangat deras atasmu, dan Dia akan menambahkan kekuatan kepada kekuatanmu, dan janganlah kamu berpaling dengan berbuat dosa"."</p>
                            <span class="source">Surat Hud Ayat: 52</span>
                        </div>

                        <h3>4.1.3 Peringatan akan Azab</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">...Sesungguhnya aku takut kamu akan ditimpa azab hari yang besar.</p>
                            <span class="source">Surat Asy Syu'araa Ayat: 135</span>
                        </div>
                        </div>`,
                        quiz: [
                            {
                                question: "Kaum 'Aad dikenal sebagai penduduk kota apa menurut Surat Al-Fajr?",
                                options: ["Babilonia", "Iram", "Petra", "Madyan"],
                                correct: 1,
                                explanation: "(yaitu) penduduk Iram yang mempunyai bangunan-bangunan yang tinggi (Al-Fajr: 7)."
                            },
                            {
                                question: "Apa kelebihan fisik yang diberikan Allah kepada kaum 'Aad (Al-A'raf 69)?",
                                options: ["Umur yang sangat panjang", "Kekuatan tubuh dan perawakan besar", "Kecerdasan luar biasa", "Kemampuan terbang"],
                                correct: 1,
                                explanation: "...dan Tuhan telah melebihkan kekuatan tubuh dan perawakanmu (daripada kaum Nuh itu)."
                            },
                            {
                                question: "Apa janji Allah jika kaum 'Aad mau memohon ampun (Surat Hud 52)?",
                                options: ["Diberi kekuasaan dunia", "Diberi hujan deras dan tambahan kekuatan", "Diberi emas dan perak", "Diberi kendaraan cepat"],
                                correct: 1,
                                explanation: "...niscaya Dia menurunkan hujan yang sangat deras atasmu, dan Dia akan menambahkan kekuatan kepada kekuatanmu..."
                            },
                            {
                                question: "Siapakah Nabi yang diutus kepada kaum 'Aad?",
                                options: ["Nuh AS", "Hud AS", "Shaleh AS", "Luth AS"],
                                correct: 1,
                                explanation: "Dan kepada kaum 'Aad (Kami utus) saudara mereka, Hud (Hud: 50)."
                            },
                            {
                                question: "Apa tuduhan utama Nabi Hud kepada kaumnya (Hud 50)?",
                                options: ["Mereka pelit", "Mereka mengada-adakan tuhan selain Allah", "Mereka suka berperang", "Mereka tidak mau bekerja"],
                                correct: 1,
                                explanation: "...Kamu hanyalah mengada-adakan saja (dalam menyembah selain Allah)."
                            }
                        ]
                    },
                    {
                        id: 137,
                        title: "SIKAP KAUM 'AAD TERHADAP KAUM HUD AS",
                        file: "topic_137.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><h3>4.2 SIKAP KAUM 'AAD</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Mereka berkata: "Apakah kamu datang kepada kami, agar kami hanya menyembah Allah saja dan meninggalkan apa yang biasa disembah oleh bapak-bapak kami? maka datangkanlah azab yang kamu ancamkan kepada kami jika kamu termasuk orang-orang yang benar".</p>
                            <span class="source">Surat Al A'raf Ayat: 70</span>
                        </div>

                        <h3>4.2.1 Penolakan dan Kesombongan</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Maka berkatalah pemuka-pemuka orang kafir dari kaumnya: "Orang ini tidak lain hanyalah manusia sepertimu..."</p>
                            <span class="source">Surat Al Mu'minuun Ayat: 24</span>
                        </div>
                        <div class="quran-quote">
                             
                             <p class="translation">Kaum 'Aad berkata: "Hai Hud, kamu tidak mendatangkan kepada kami suatu bukti yang nyata, dan kami sekali-kali tidak akan meninggalkan sembahan-sembahan kami karena perkataanmu, dan kami sekali-kali tidak akan mempercayai kamu".</p>
                             <span class="source">Surat Hud Ayat: 53</span>
                        </div>
                        <div class="quran-quote">
                            
                            <p class="translation">"Kami tidak mengatakan melainkan bahwa sebagian sembahan kami telah menimpakan penyakit gila atas dirimu"...</p>
                            <span class="source">Surat Hud Ayat: 54</span>
                        </div>

                        <h3>4.2.2 Tantangan Kaum 'Aad</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Adapun kaum 'Aad maka mereka menyombongkan diri di muka bumi tanpa alasan yang benar dan berkata: "Siapakah yang lebih besar kekuatannya dari kami?"...</p>
                            <span class="source">Surat Fussilat Ayat: 15</span>
                        </div>

                        <h3>4.2.3 Jawaban Nabi Hud</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">...Hud menjawab: "Sesungguhnya aku bersaksi kepada Allah dan saksikanlah olehmu sekalian bahwa sesungguhnya aku berlepas diri dari apa yang kamu persekutukan,"</p>
                            <span class="source">Surat Hud Ayat: 54</span>
                        </div>
                        <div class="quran-quote">
                            
                            <p class="translation">"...maka jalanlankanlah tipu dayamu semuanya terhadapku dan janganlah kamu memberi tangguh kepadaku."</p>
                            <span class="source">Surat Hud Ayat: 55</span>
                        </div>
                        </div>`,
                        quiz: [
                            {
                                question: "Mengapa kaum 'Aad menolak ajakan Nabi Hud (Al A'raf 70)?",
                                options: ["Mereka ingin harta", "Mereka tidak mau meninggalkan sesembahan nenek moyang", "Mereka ingin nabi dari golongan malaikat", "Mereka sibuk bekerja"],
                                correct: 1,
                                explanation: "...agar kami hanya menyembah Allah saja dan meninggalkan apa yang biasa disembah oleh bapak-bapak kami?"
                            },
                            {
                                question: "Apa tuduhan kaum 'Aad terhadap Nabi Hud terkait sembahan mereka (Hud 54)?",
                                options: ["Hud mencuri berhala mereka", "Sembahan mereka telah menimpakan penyakit gila pada Hud", "Hud menghancurkan berhala mereka", "Hud menjual berhala mereka"],
                                correct: 1,
                                explanation: "...sebagian sembahan kami telah menimpakan penyakit gila atas dirimu."
                            },
                            {
                                question: "Bagaimana kesombongan kaum 'Aad digambarkan dalam Surat Fussilat ayat 15?",
                                options: ["Mereka merasa paling kaya", "Mereka merasa paling pintar", "Mereka berkata: 'Siapakah yang lebih besar kekuatannya dari kami?'", "Mereka membangun istana emas"],
                                correct: 2,
                                explanation: "...dan berkata: Siapakah yang lebih besar kekuatannya dari kami?"
                            },
                            {
                                question: "Apa respon Nabi Hud terhadap ancaman kaumnya (Hud 55)?",
                                options: ["Dia lari ketakutan", "Dia meminta damai", "Dia menantang balik: 'Jalankanlah tipu dayamu semuanya'", "Dia meminta bantuan raja lain"],
                                correct: 2,
                                explanation: "...maka jalanlankanlah tipu dayamu semuanya terhadapku dan janganlah kamu memberi tangguh kepadaku."
                            },
                            {
                                question: "Apa alasan lain kaum 'Aad menolak Hud (Hud 53)?",
                                options: ["Hud tidak membawa bukti nyata (menurut mereka)", "Hud meminta bayaran", "Hud bukan orang Arab", "Hud terlalu muda"],
                                correct: 0,
                                explanation: "Hai Hud, kamu tidak mendatangkan kepada kami suatu bukti yang nyata..."
                            }
                        ]
                    },
                    {
                        id: 138,
                        title: "AZAB DAN BALASAN TERHADAP KAUM 'AAD",
                        file: "topic_138.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><h3>4.3 AZAB DAN BALASAN TERHADAP KAUM AD</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Dan juga pada (kisah) 'Aad ketika Kami kirimkan kepada mereka angin yang membinasakan,</p>
                            <span class="source">Surat Adz Dzariyat Ayat: 41</span>
                        </div>
                        <div class="quran-quote">
                            
                            <p class="translation">angin itu tidak membiarkan satupun yang dilaluinya, melainkan dijadikannya seperti serbuk.</p>
                            <span class="source">Surat Adz Dzariyat Ayat: 42</span>
                        </div>

                        <h3>4.3.1 Angin Sarkhar (Sangat Dingin dan Kencang)</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Adapun kaum 'Aad maka mereka telah dibinasakan dengan angin yang sangat dingin lagi amat kencang,</p>
                            <span class="source">Surat Al Haaqqah Ayat: 6</span>
                        </div>
                        <div class="quran-quote">
                            
                            <p class="translation">yang Allah menimpakan angin itu kepada mereka selama tujuh malam dan delapan hari terus menerus...</p>
                            <span class="source">Surat Al Haaqqah Ayat: 7</span>
                        </div>
                        <div class="quran-quote">
                             
                             <p class="translation">...maka kamu lihat kaum 'Aad pada waktu itu mati bergelimpangan seakan-akan mereka tunggul pohon kurma yang telah kosong (lapuk).</p>
                             <span class="source">Surat Al Haaqqah Ayat: 7</span>
                        </div>

                        <h3>4.3.2 Keselamatan Nabi Hud AS</h3>
                        <div class="quran-quote">
                            
                            <p class="translation">Dan tatkala datang azab Kami, Kami selamatkan Hud dan orang-orang yang beriman bersama dia dengan rahmat dari Kami; dan Kami selamatkan (pula) mereka (di akhirat) dari azab yang berat.</p>
                            <span class="source">Surat Hud Ayat: 58</span>
                        </div>
                        </div>`,
                        quiz: [
                            {
                                question: "Azab apa yang ditimpakan kepada kaum 'Aad?",
                                options: ["Banjir besar", "Angin yang sangat dingin dan kencang", "Hujan batu", "Suara menggelegar"],
                                correct: 1,
                                explanation: "...maka mereka telah dibinasakan dengan angin yang sangat dingin lagi amat kencang (Al Haaqqah: 6)."
                            },
                            {
                                question: "Berapa lama angin tersebut menimpa kaum 'Aad (Al Haaqqah 7)?",
                                options: ["3 hari 3 malam", "7 malam 8 hari", "40 hari 40 malam", "1 hari penuh"],
                                correct: 1,
                                explanation: "...selama tujuh malam dan delapan hari terus menerus..."
                            },
                            {
                                question: "Bagaimana kondisi kaum 'Aad setelah azab tersebut?",
                                options: ["Mereka tertidur pulas", "Mati bergelimpangan seperti tunggul pohon kurma lapuk", "Menjadi batu", "Tenggelam di laut"],
                                correct: 1,
                                explanation: "...mati bergelimpangan seakan-akan mereka tunggul pohon kurma yang telah kosong (lapuk)."
                            },
                            {
                                question: "Siapakah yang selamat dari azab tersebut?",
                                options: ["Hanya Raja 'Aad", "Nabi Hud dan orang-orang yang beriman bersamanya", "Penduduk kota tetangga", "Hewan ternak saja"],
                                correct: 1,
                                explanation: "Kami selamatkan Hud dan orang-orang yang beriman bersama dia dengan rahmat dari Kami (Hud: 58)."
                            },
                            {
                                question: "Apa istilah yang digunakan Al-Qur'an untuk menggambarkan angin yang membinasakan tersebut (Adz Dzariyat 41)?",
                                options: ["Ar-Rih Al-'Aqiim", "As-Shaihah", "At-Thufan", "Ar-Rajfah"],
                                correct: 0,
                                explanation: "...ketika Kami kirimkan kepada mereka angin yang membinasakan (Ar-Rih Al-'Aqiim)."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-6-5",
                title: "Pokok Bahasan 5: SALEH AS.",
                topics: [
                    {
                        id: 139,
                        title: "Dakwah Shaleh AS",
                        file: "topic_139.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><p>5.1</p>
<h4>TERHADAP</h4>
<div class="quran-quote">


<p class="translation">Dan (kami telah mengutus) kepada kaum Tsamud saudara mereka Shaleh. Ia berkata: "Hai kaumku, sembahlah Allah, sekali-kali tidak ada Tuhan bagimu selain-Nya. Sesungguhnya telah datang bukti yang nyata kepadamu dari Tuhammu. Unta betina Allah ini menjadi tanda bagimu, maka biarkanlah ia makan di bumi Allah, dan janganlah kamu mengganggunya dengan gangguan apapun, (yang karenanya) kamu akan ditimpa siksaan yang pedih."{ 73 } Dan ingatlah olehmu di waktu Tuhan menjadikam kamu pengganti- pengganti (yang berkuasa) sesudah kaum 'Aad dan memberikan tempat bagimu di bumi. Kamu dirikan istana-istana di tanah-tanahnya yang datar dan kamu pahat gunung-gunungnya untuk dijadikan rumah; maka ingatlah nikmat-nikmat Allah dan janganlah kamu merajalela di muka bumi membuat kerusakan.{ 74 }</p>
<span class="source">Referensi: Ayat 73  – 74</span>
</div>
<div class="quran-quote">

<h4>Nikmat Allah bagi Kaum Tsamud</h4>
<h4>Dan  mereka  memahat  rumah-rumah  dari  gunung-gunung  batu  (yang</h4>
<p>didiami)  dengan  aman.</p>
<div class="quran-quote">

<p class="translation">Dan kaum Tsamud yang memotong batu-batu besar di lembah 36 ,{ 9}</p>
<span class="source">Referensi: Ayat 9</span>
</div>
<div class="quran-quote">







<div class="quran-quote">












<p class="translation">Mereka memotong-motong batu gunung untuk membangun g edung-gedung tempat tinggal mereka dan ada pula yang melubangi gunung-gun ung untuk tempat tinggal mereka dan tempat berlindung.</p>
<span class="source">Referensi: Ayat 141  – 152</span>
</div>
<h4>Dakwah Shaleh As.</h4>
<h4>Kaum  Tsamud  telah  mendustakan  rasul-rasul.{141 }</h4>
<h4>Ketika  saudara  mereka; Shaleh,  berkata  kepada  mereka:  "Mengapa  kamu</h4>
<p>tidak  bertakwa?</p>
<h4>Sesungguhnya  aku  adalah  seorang  rasul  kepercayaan  (yang  diutus)</h4>
<p>kepadamu,</p>
<h4>Maka  bertakwalah  kepada  Allah  dan  taatlah  kepadaku.{144 }</h4>
<p>Dan  aku  sekali-kali  tidak  minta  upah  kepadamu  atas  ajakan  itu,  upahku tidak  lain  hanyalah  dari  Tuhan  semesta  alam. Akankah  kamu  dibiarkan  tinggal  di  sini  (negerimu)  dengan  aman,</p>
<h4>Di  dalam  kebun-kebun  serta  mata  air,{147 }</h4>
<h4>Dan  tanaman  dan  pohon-pohon  korma  yang  mayangnya  lembut.{148 }</h4>
<h4>Dan  kamu  pahat  sebagian  dari  gunung-gunung  untuk  dijadikan  rumah-</h4>
<p>rumah  dengan  rajin;</p>
<h4>Maka  bertakwalah  kepada  Allah  dan  taatlah  kepadaku;{150 }</h4>
<p>Dan  kamu jangan  menaati  perintah  mereka  yang  melewati  batas, Yang  berbuat  rusak  di  bumi  dan  tidak  mengadakan  perbaikan".</p>
<div class="quran-quote">


<p class="translation">Dan sesungguhnya Kami telah mengutus kepada (kaum) Tsamud saudara mereka Shaleh (yang berseru): "Hendaklah kamu mengabdi kepada Allah". Tetapi tiba-tiba mereka (jadi) dua golongan yang bermusuhan.{ 45 } Dia berkata: "Hai kaumku mengapa kamu minta disegerakan keburukan sebelum (kamu minta) kebaikan?, hendaklah kamu meminta ampun kepada Allah, agar kamu mendapat rahmat".{ 46 }</p>
<span class="source">Referensi: Ayat 45  – 46</span>
</div>
<div class="quran-quote">


</div>`,
                        quiz: [
                            {
                                question: "Nabi Shaleh AS diutus kepada kaum...",
                                options: ["'Aad", "Tsamud", "Madyan", "Bani Israil"],
                                correct: 1,
                                explanation: "Dan (kami telah mengutus) kepada kaum Tsamud saudara mereka Shaleh (Al-A'raaf: 73)."
                            },
                            {
                                question: "Apa mukjizat yang diberikan Allah kepada Nabi Shaleh?",
                                options: ["Tongkat menjadi ular", "Membelah lautan", "Unta betina", "Menghidupkan orang mati"],
                                correct: 2,
                                explanation: "Hai kaumku, inilah unta betina dari Allah, sebagai mukjizat... (Huud: 64)."
                            },
                            {
                                question: "Kaum Tsamud memahat gunung untuk dijadikan...",
                                options: ["Patung berhala", "Rumah-rumah", "Benteng pertahanan", "Kuil pemujaan"],
                                correct: 1,
                                explanation: "Dan kamu pahat sebagian dari gunung-gunung untuk dijadikan rumah-rumah dengan rajin (Asy-Syu'araa': 149)."
                            },
                            {
                                question: "Apa perintah Nabi Shaleh terkait unta betina tersebut?",
                                options: ["Boleh disembelih", "Biarkan makan di bumi Allah dan jangan diganggu", "Gunakan sebagai kendaraan perang", "Serahkan kepada penguasa"],
                                correct: 1,
                                explanation: "...biarkanlah ia makan di bumi Allah, dan janganlah kamu mengganggunya dengan gangguan apapun... (Huud: 64)."
                            },
                            {
                                question: "Dalam surat Asy-Syu'araa' ayat 153, kaum Tsamud menuduh Nabi Shaleh sebagai...",
                                options: ["Orang gila", "Orang yang kena sihir", "Tukang syair", "Raja yang zalim"],
                                correct: 1,
                                explanation: "Mereka berkata: Sesungguhnya kamu adalah salah seorang dari orang-orang yang kena sihir (Asy-Syu'araa': 153)."
                            }
                        ]
                    },
                    {
                        id: 140,
                        title: "Sikap Kaum Tsamud",
                        file: "topic_140.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><p>5.2</p>
<h4>TERHADAP</h4>
<div class="quran-quote">


<p class="translation">Shaleh berkata: "Hai kaumku, bagaimana pikiranmu jika aku memiliki bukti yang nyata dari Tuhanku dan Dia memberiku rahmat (kenabian) dari-Nya, maka siapakah yang akan menolong aku dari (azab) Allah jika aku mendurhakai-Nya. Sebab itu kamu tidak menambah apapun kepadaku selain kerugian.{ 63 }</p>
<span class="source">Referensi: Ayat 62  – 63</span>
</div>
<div class="quran-quote">


<h4>Kaum Tsamud Meragukan Seruan Shaleh As.</h4>
<h4>Kaum Tsamud Mendustakan Seruan Shaleh As.</h4>
<h4>Dan sesungguhnya  penduduk-penduduk  Al  Hijr 37  telah  mendustakan</h4>
<p>rasul-rasul 38 ,</p>
<h4>Dan  Kami  telah  datangkan  kepada  mereka  tanda-tanda  (kekuasaan)</h4>
<h4>Kami,  tetapi  mereka  selalu  berpaling  daripadanya,{ 81 }</h4>
<div class="quran-quote">





<p class="translation">Ketika bangkit orang yang paling celaka di antara mereka,{ 12 } Lalu Rasul Allah (Shaleh) berkata kepada mereka: ("Biarkanlah) unta betina Allah dan minumannya".{ 13 } Lalu mereka mendustakannya dan menyembelih unta itu, maka Tuhan mereka membinasakan mereka disebabkan dosa mereka, lalu Allah meratakan mereka (dengan tanah),{ 14 } Dan Allah tidak takut terhadap akibat tindakan-Nya itu.{ 15 }</p>
<span class="source">Referensi: Ayat 11  – 15</span>
</div>
<div class="quran-quote">



<p class="translation">Para pemuka yang menyombongkan diri di antara kaumnya berkata kepada orang-orang yang dianggap lemah yang telah beriman di antara mereka: "Tahukah kamu bahwa Shaleh diutus (menjadi rasul) oleh Tuhannya?". Mereka menjawab: "Sesungguhnya kami beriman kepada wahyu, yang Shaleh diutus untuk menyampaikannya".{ 75 } Orang-orang yang menyombongkan diri berkata: "Sesungguhnya kami adalah orang yang tidak percaya kepada apa yang kamu imani itu".{ 76 } Kemudian mereka sembelih unta betina itu, dan mereka berlaku angkuh terhadap perintah Tuhan. Dan mereka berkata: "Hai Shaleh, datangkanlah apa yang kamu ancamkan itu kepada kami, jika (betul) kamu termasuk orang-orang yang diutus (Allah)".{ 77 }</p>
<span class="source">Referensi: Ayat 75  – 77</span>
</div>
<div class="quran-quote">


<h4>Kaum Tsamud Mengingkari Seruan Shaleh As.</h4>
<h4>Karena  itu  mereka  ditimpa  gempa, maka  jadilah  mereka  mayat-mayat</h4>
<p>yang  bergelimpangan  di  tempat  tinggal  mereka.</p>
<h4>Maka  Shaleh  meninggalkan  mereka  seraya  berkata:  "Hai  kaumku</h4>
<p>sesungguhnya  aku  telah  menyampaikan  kepadamu  risalah  Tuhanku,  dan aku  telah  memberi  nasehat  kepadamu,  tetapi  kamu  tidak  menyukai orang-orang  yang  memberi  nasehat".</p>
<div class="quran-quote">

<p class="translation">Mereka menjawab: "Kami mendapat nasib yang malang, disebabkan kamu dan orang-orang yang besertamu". Shaleh berkata: "Nasibmu ada pada sisi Allah, (bukan kami yang menjadi sebab), tetapi kamu kaum yang diuji".{ 47 }</p>
<span class="source">Referensi: Ayat 47</span>
</div>
<div class="quran-quote">




<p class="translation">Kaum Tsamud pun telah mendustakan ancaman-ancaman (itu).{ 23 }</p>
<span class="source">Referensi: Ayat 23  – 26</span>
</div>
<h4>Kaum Tsamud Menganggap Shaleh As. Pembawa Sial</h4>
<h4>Kaum Tsamud Menganggap Shaleh As.Pendusta</h4>
<h4>Maka  mereka  berkata:  "Bagaimana  kita  akan  mengikuti  seorang  manusia</h4>
<p>(biasa)  di  antara  kita?". Sesungguhnya  kalau  kita  begitu  benar-benar berada  dalam  keadaan  sesat  dan  gila". Apakah  wahyu  itu  diturunkan  kepadanya  di  antara  kita?, sebenarnya  ia adalah  seorang  yang  amat  pendusta  lagi  sombong.</p>
<h4>Kelak  mereka  akan  mengetahui  siapakah  yang  sebenarnya  amat</h4>
<p>pendusta  lagi  sombong.</p>
<div class="quran-quote">


<p class="translation">Mereka berkata: “Sesungguhnya kamu adalah salah seorang dari orang- orang yang kena sihir;{ 153 } Kamu tidak lain melainkan seorang manusia seperti kami; maka datangkanlah sesuatu mukjizat, jika kamu memang termasuk orang- orang yang benar.”{ 154 }</p>
<span class="source">Referensi: Ayat 153  – 154</span>
</div>
<div class="quran-quote">



<h4>Kaum Tsamud Menganggap Shaleh As.Tersihir</h4>
<h4>Kaum Tsamud Merencanakan Membunuh Shaleh As.</h4>
<p>Dan  adalah  di  kota  itu 39  sembilan  orang  laki-laki  yang  membuat  kerusakan di  muka  bumi,  dan  mereka  tidak  berbuat  kebaikan.</p>
<h4>Mereka  berkata:  "Bersumpahlah  kamu  dengan  nama  Allah,  bahwa  kita</h4>
<p>sungguh-sungguh  akan  menyerangnya  dengan  tiba-tiba  beserta keluarganya  di  malam  hari,  kemudian  kita  katakan  kepada  warisnya (bahwa)  kita  tidak  menyaksikan  kematian  keluarganya  itu,  dan sesungguhnya  kita  adalah  orang-orang  yang  benar".</p>
<h4>Dan  merekapun  merencanakan  makar  dengan  sungguh-sungguh  dan</h4>
<h4>Kamipun  merencanakan  makar,  sedang  mereka  tidak  menyadari.{ 50 }</h4>
<div class="quran-quote">


<p class="translation">Hai kaumku, inilah unta betina dari Allah, sebagai mukjizat (yang menunjukkan kebenaran) untukmu, sebab itu biarkanlah ia makan di bumi Allah, dan janganlah kamu mengganggunya dengan gangguan apapun yang akan menyebabkan kamu ditimpa azab yang dekat."{ 64} Mereka membunuh unta itu, maka berkata Shaleh: "Bersukarialah kamu</p>
<span class="source">Referensi: Ayat 64  – 65</span>
</div>
<h4>Mukjizat Shaleh As. dan Sikap Kaum Tsamud</h4>
<p>sekalian  di  rumahmu  selama  tiga  hari 40 , itu  adalah  janji  yang  tidak  dapat didustakan."</p>
<div class="quran-quote">



<p class="translation">Shaleh menjawab: "Ini seekor unta betina, ia mempunyai giliran untuk mendapatkan air, dan kamu memiliki giliran pula untuk mendapatkan air di hari yang tertentu.{ 155 } Dan janganlah kamu sentuh unta betina itu dengan suatu kejahatan, yang menyebabkan kamu ditimpa oleh azab hari yang besar".{ 156 } Kemudian mereka membunuhnya, lalu mereka menjadi menyesal,{ 157 }</p>
<span class="source">Referensi: Ayat 155  – 157</span>
</div>
<div class="quran-quote">



<p class="translation">Sesungguhnya Kami akan mengirimkan unta betina sebagai cobaan bagi mereka, maka tunggulah (tindakan) mereka dan bersabarlah.{ 27 } Dan beritakanlah kepada mereka bahwa sesungguhnya air itu terbagi antara mereka (dengan unta betina itu); tiap-tiap giliran minum dihadiri Nabi Shaleh As. Oleh sebab itu Allah menjatuhkan ke pada mereka hukuman, yaitu membatasi hidup mereka hanya dalam tempo tiga hari, m aka sebagai ejekan mereka disuruh bersuka ria selama tiga hari itu. (oleh yang punya giliran) 41 {28 } Maka mereka memanggil kawannya, lalu kawannya menangkap (unta itu) dan membunuhnya.{ 29 }</p>
<span class="source">Referensi: Ayat 27  – 29</span>
</div>
<div class="quran-quote">

<p class="translation">Asy Syu'araa' ayat 154-155.</p>
<span class="source">Referensi: Ayat 59</span>
</div>
</div>`,
                        quiz: [
                            {
                                question: "Bagaimana respon mayoritas kaum Tsamud terhadap dakwah Nabi Shaleh?",
                                options: ["Menerima dengan baik", "Mendustakan dan sombong", "Ragu-ragu namun patuh", "Meminta waktu untuk berpikir"],
                                correct: 1,
                                explanation: "Kaum Tsamud telah mendustakan rasul-rasul (Asy-Syu'araa': 141)."
                            },
                            {
                                question: "Siapakah yang pertama kali menyembelih unta betina tersebut?",
                                options: ["Seluruh penduduk kota", "Sembilan orang laki-laki", "Salah seorang yang paling celaka di antara mereka (Qudar bin Salif)", "Raja Tsamud"],
                                correct: 2,
                                explanation: "Ketika bangkit orang yang paling celaka di antara mereka... Lalu mereka mendustakannya dan menyembelih unta itu (Asy-Syams: 12-14)."
                            },
                            {
                                question: "Berapa jumlah orang yang merencanakan makar untuk membunuh Nabi Shaleh?",
                                options: ["3 orang", "7 orang", "9 orang", "40 orang"],
                                correct: 2,
                                explanation: "Dan adalah di kota itu sembilan orang laki-laki yang membuat kerusakan di muka bumi... (An-Naml: 48)."
                            },
                            {
                                question: "Apa rencana jahat sembilan orang tersebut (An-Naml 49)?",
                                options: ["Mengusir Nabi Shaleh", "Membakar rumah Nabi Shaleh", "Menyerang Shaleh dan keluarganya di malam hari", "Memenjarakan pengikut Nabi Shaleh"],
                                correct: 2,
                                explanation: "...kita sungguh-sungguh akan menyerangnya dengan tiba-tiba beserta keluarganya di malam hari... (An-Naml: 49)."
                            },
                            {
                                question: "Bagaimana sikap pemuka kaum Tsamud kepada pengikut Nabi Shaleh yang lemah?",
                                options: ["Melindungi mereka", "Menyombongkan diri dan merendahkan", "Mengajak berdiskusi", "Memberikan harta"],
                                correct: 1,
                                explanation: "Para pemuka yang menyombongkan diri... berkata kepada orang-orang yang dianggap lemah... (Al-A'raaf: 75)."
                            }
                        ]
                    },

                    {
                        id: 140,
                        title: "",
                        file: "topic_140.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><p>Shaleh As.</p><p>5.2</p><h3>SIKAP KAUM TSAMUD</h3><h3>TERHADAP</h3><h3>DAKWAH SHALEH AS</h3><p>Shaleh As.</p><p>5.2.1 Kaum Tsamud Meragukan Seruan Shaleh As.</p><p>◙ Huud [11]: 62 – 63</p><p>‰7èΡ β& $Ζ γΨ?& #‹≈δ ≅6% #θ_Β $ΖŠù MΨ. ‰% x=≈Á≈ƒ #θ9$%</p><p>y ç ÷ ¯ r ! u y ÷ s r ( ! x y Ÿ ö s v ã ö t u Ï | ä ô s ß Î | t ( ä s</p><p>∩∉⊄∪ =ƒ÷∆ µ‹9) $Ρθã‰? $ϑΒ 7© ’∀9 $ΖΡ)ρ $Ρτ$/# ‰7èƒ $Β</p><p>5 Í ß Ï ø s Î ! t ã ô s £ Ïi 7e x Å s u ¯ Î u t ä ! t u ß ç ÷ t t</p><p>µΖΒ _ ?#ρ ’1‘ Β πΨ/ ’?ã MΖ2 β) ΟFƒ‘& Θθ)≈ƒ Α$%</p><p>ç ÷ Ï Í s u u În § Ïi 7 o Éi t 4 n t à à Î ó ç ÷ u u r É ö s t t s</p><p>î _Ρρ‰ƒ“? $ϑù …µFŠÁã β) !# ∅Β ’ΤÁΖƒ ϑù πΗq‘</p><p>u ö x Í t ß Ì s y s ( ç ç ø | t ÷ Î « $ š Ï Î ã Ý t y s Z t ô y</p><p>∩∉⊂∪ ¡ƒB</p><p>9 Å ø r</p><p>Kaum Tsamud berkata: "Hai shaleh, sungguh kamu sebelum ini adalah</p><p>seorang di antara kami yang kami harapkan, apakah kamu melarang kami</p><p>untuk menyembah apa yang disembah oleh bapak-bapak kami?, dan</p><p>sesungguhnya kami betul-betul dalam keraguan yang menggelisahkan</p><p>terhadap apa yang kamu serukan kepada kami."{62}</p><p>Shaleh berkata: "Hai kaumku, bagaimana pikiranmu jika aku memiliki</p><p>bukti yang nyata dari Tuhanku dan Dia memberiku rahmat (kenabian)</p><p>dari-Nya, maka siapakah yang akan menolong aku dari (azab) Allah jika</p><p>aku mendurhakai-Nya. Sebab itu kamu tidak menambah apapun</p><p>kepadaku selain kerugian.{63}</p><p>5.2.2 Kaum Tsamud Mendustakan Seruan Shaleh As.</p><p>◙ Al Hijr [15]: 80 – 81</p><p>$ΖF≈ƒ# Νγ≈Ψ?#ρ ∩∇⊃∪ =™ϑ9# ft:# =≈t¾& >‹. ‰)9ρ</p><p>u Ï t u ö ß o ÷ s u u t Î y ö ß ø $ Ì ô Ï ø $ Ü p õ r z ¤ x ô s s u</p><p>Shaleh As.</p><p>∩∇⊇∪ ÊèΒ $κ]ã #θΡ%3ù</p><p>t Å Ì ÷ ã p ÷ t ( ç s s</p><p>Dan sesungguhnya penduduk-penduduk Al Hijr37 telah mendustakan</p><p>rasul-rasul38,{80}</p><p>Dan Kami telah datangkan kepada mereka tanda-tanda (kekuasaan)</p><p>Kami, tetapi mereka selalu berpaling daripadanya,{81}</p><p>◙ Asy Syams [91]: 11 – 15</p><p>$γ8 $γ1</p><p>Αθ™‘ Νλ; Α$)ù ∩⊇⊄∪ )©& ]è7Ρ# Œ) ∩⊇⊇∪ θóÜ/ ŠθϑO M/‹.</p><p>ã ß u ö ç m t s s y s ô r y y t / $ Ï Î ! y u ø s Î ß ß r ô t ¤ x</p><p>Ογ/‘ ΟγŠ=æ Π‰Β‰ù $δρ)èù νθ/‹3ù ∩⊇⊂∪ $γ≈Š)™ρ !# π%$Ρ !#</p><p>ß š u ó Î ø n t t y ø y s y ã s y s ç ç ¤ s s y u ø ß u « $ s s t « $</p><p>$γ1</p><p>∩⊇∈∪ $γ≈6)ã ∃$ƒ† ωρ ∩⊇⊆∪ θ¡ù Νγ6Ρ‹/</p><p>y t ø ã ß s s Ÿ u y § | s ö Î Î / x Î</p><p>(Kaum) Tsamud telah mendustakan (rasulnya) karena mereka</p><p>melampaui batas,{11}</p><p>Ketika bangkit orang yang paling celaka di antara mereka,{12}</p><p>Lalu Rasul Allah (Shaleh) berkata kepada mereka: ("Biarkanlah) unta</p><p>betina Allah dan minumannya".{13}</p><p>Lalu mereka mendustakannya dan menyembelih unta itu, maka Tuhan</p><p>mereka membinasakan mereka disebabkan dosa mereka, lalu Allah</p><p>meratakan mereka (dengan tanah),{14}</p><p>Dan Allah tidak takut terhadap akibat tindakan-Nya itu.{15}</p><p>◙ Al A'raaf [7]: 75 – 77</p><p>%# %!</p><p>#θ(cid:12)èÒG™#  9 µΒθ% ∅Β #ρ96F™#  # |ϑ9# Α$%</p><p>( à Ï ô ç ó $ t Ï © Ï Ï Ï ö s Ï ( ç y ò t ó $ t Ï © $ _ y ø $ t s</p><p>37) Penduduk Al-Hijr ialah kaum Tsamud. Al-Hijr adalah tempat yang terletak di Wadi</p><p>Qura antara Madinah dan Syria.</p><p>38) Yang dimaksud rasul-rasul di sini ialah shaleh. Mestinya di sini disebut rasul, tetapi</p><p>disebut rasul-rasul (Jamak), karena mendustakan seorang rasul sama dengan</p><p>mendustakan semua rasul.</p><p>Shaleh As.</p><p>#θ9$% µ/‘ Β≅™÷∆$s=≈¹ χ& χθϑ=è?& Νκ]ΒΒ# ϑ9</p><p>( þ ä s 4 Ï În § Ïi × y ó ‘ [ Î | ā r š ß n ÷ s r ö å ÷ Ï z t u ô y Ï</p><p>%!</p><p>$Ρ) #ρ96F™#  # Α$% ∩∠∈∪ χθΖΒσΒ µ/ ≅™‘& $ϑ/ $Ρ)</p><p>¯ Î ( ÿ ç y ò t ó $ š Ï © $ t s š ã Ï ÷ ã Ï Î Ÿ Å ö é ! y Î ¯ Î</p><p>%!</p><p>÷∆& ã #θGãρ π%$Ψ9# #ρ)èù ∩∠∉∪ χρ(cid:12)≈. µ/ ΝGΖΒ# “ $/</p><p>Í ö r ô t ( ö t t u s s ¨ $ ( ã s y s š ã Ï x Ï Î ç t u ü Ï © $ Î</p><p>∩∠∠∪=™ϑ9#ΒMΨ.β)$Ρ‰è?$ϑ/$ΨK~#x=≈Á≈ƒ#θ9$%ρΟγ/‘</p><p>t Î y ö ß ø $ z Ï | ä Î ! t ß Ï s y Î o Ï ø $ ß Î | t ( ä s u ó Î În u</p><p>Para pemuka yang menyombongkan diri di antara kaumnya berkata</p><p>kepada orang-orang yang dianggap lemah yang telah beriman di antara</p><p>mereka: "Tahukah kamu bahwa Shaleh diutus (menjadi rasul) oleh</p><p>Tuhannya?". Mereka menjawab: "Sesungguhnya kami beriman kepada</p><p>wahyu, yang Shaleh diutus untuk menyampaikannya".{75}</p><p>Orang-orang yang menyombongkan diri berkata: "Sesungguhnya kami</p><p>adalah orang yang tidak percaya kepada apa yang kamu imani itu".{76}</p><p>Kemudian mereka sembelih unta betina itu, dan mereka berlaku angkuh</p><p>terhadap perintah Tuhan. Dan mereka berkata: "Hai Shaleh,</p><p>datangkanlah apa yang kamu ancamkan itu kepada kami, jika (betul)</p><p>kamu termasuk orang-orang yang diutus (Allah)".{77}</p><p>5.2.3 Kaum Tsamud Mengingkari Seruan Shaleh As.</p><p>◙ Al A'raaf [7]: 78 – 79</p><p>’<θFù ∩∠∇∪ ϑW≈_ Νδ‘#Š ’û #θs7¹'ù π(cid:12)_9# Ογ?‹{'ù</p><p>4 ¯ u t s t Ï Ï y ö Ï Í y Î ( ß t ô r s è x ô § $ Þ ß ø x s r s</p><p>'!</p><p>Ν39 MsÁΡρ ’1‘ $™‘ Ν6Gó=/& ‰)9 Θθ)≈ƒ Α$%ρ Νκ]ã</p><p>ö ä s à ó | t u În u s s y Í ö à ç ø n ö r ô s s É ö s t t s u ö å ÷ t</p><p>∩∠∪ ⇔Á≈Ψ9# βθ7tB ω 3≈9ρ</p><p>š Ï Å ¨ $ t ™ Ï é ā Å s u</p><p>Shaleh As.</p><p>Karena itu mereka ditimpa gempa, maka jadilah mereka mayat-mayat</p><p>yang bergelimpangan di tempat tinggal mereka.{78}</p><p>Maka Shaleh meninggalkan mereka seraya berkata: "Hai kaumku</p><p>sesungguhnya aku telah menyampaikan kepadamu risalah Tuhanku, dan</p><p>aku telah memberi nasehat kepadamu, tetapi kamu tidak menyukai</p><p>orang-orang yang memberi nasehat".{79}</p><p>5.2.4 Kaum Tsamud Menganggap Shaleh As. Pembawa Sial</p><p>◙ An Naml [27]: 47</p><p>ΟFΡ& ≅/ !# ‰Ζã Ν.∝≈Û Α$% 7èΒ ϑ/ρ 7/ $ΡÛ# #θ9$%</p><p>ó ç r ö t ( « $ y Ï ö ä ç È ¯ s t s 4 y t ¨ y Î u y Î t ÷ ¨ © $ ( ä s</p><p>∩⊆∠∪ βθΖF(cid:12)? Πθ%</p><p>t ã t ø è × ö s</p><p>Mereka menjawab: "Kami mendapat nasib yang malang, disebabkan</p><p>kamu dan orang-orang yang besertamu". Shaleh berkata: "Nasibmu ada</p><p>pada sisi Allah, (bukan kami yang menjadi sebab), tetapi kamu kaum yang</p><p>diuji".{47}</p><p>5.2.5 Kaum Tsamud Menganggap Shaleh As.Pendusta</p><p>◙ Al Qamar [54]: 23 – 26</p><p>#Œ) $Ρ) …µè7KΡ #‰n≡ρ $ΖΒ #³0& #θ9$)ù ∩⊄⊂∪ ‘‹Ζ9$/ ŠθϑO M/‹.</p><p>] Î ! ¯ Î ÿ ç ã Î ® ¯ Y Ï u ¨ Ïi Z | o r ( þ ä s s Í ä ‘ $ Î ß ß r ô t ¤ x</p><p>%!</p><p>>#‹. θδ ≅/ $ΖΨ/ Β µ‹=ã . # ’+9& ∩⊄⊆∪ è™ρ ≅≈=Ê ’∀9</p><p>ë ¤ x u è ö t u Ï ÷ t . Ï Ï ø n t ã ø Ïe $ u Å ø â r @ ã ß u 9 n | Å ©</p><h3>U</h3><p>∩⊄∉∪ °{# #‹39# Β #‰î βθΗ>è‹™ ∩⊄∈∪ °&</p><p>ç Å F $ Û ¤ s ø $ Ç ¨ Y x t ç s ÷ u y × Å r</p><p>Kaum Tsamud pun telah mendustakan ancaman-ancaman (itu).{23}</p><p>Shaleh As.</p><p>Maka mereka berkata: "Bagaimana kita akan mengikuti seorang manusia</p><p>(biasa) di antara kita?". Sesungguhnya kalau kita begitu benar-benar</p><p>berada dalam keadaan sesat dan gila".{24}</p><p>Apakah wahyu itu diturunkan kepadanya di antara kita?, sebenarnya ia</p><p>adalah seorang yang amat pendusta lagi sombong.{25}</p><p>Kelak mereka akan mengetahui siapakah yang sebenarnya amat</p><p>pendusta lagi sombong.{26}</p><p>5.2.6 Kaum Tsamud Menganggap Shaleh As.Tersihir</p><p>◙ Asy Syu'araa' [26]: 153 – 154</p><p>N'ù $Ψ=WΒ ³0 ω) MΡ& $Β ∩⊇∈⊂∪ s¡ϑ9# Β MΡ& $ϑΡ) #θ9$%</p><p>Ï ù s o è ÷ Ïi × | o ā Î | r ! t t Ì − | ß ø $ z Ï | r ! y ¯ Î ( þ ä s</p><p>∩⊇∈⊆∪ %‰≈Á9# Β MΖ. β) πƒ$↔/</p><p>š Ï Ï ¢ $ z Ï | ä Î > t t Î</p><p>Mereka berkata: “Sesungguhnya kamu adalah salah seorang dari orang-</p><p>orang yang kena sihir;{153}</p><p>Kamu tidak lain melainkan seorang manusia seperti kami; maka</p><p>datangkanlah sesuatu mukjizat, jika kamu memang termasuk orang-</p><p>orang yang benar.”{154}</p><p>5.2.7 Kaum Tsamud Merencanakan Membunuh Shaleh As.</p><p>◙ An Naml [27]: 48 – 50</p><p>ωρ Ú‘{# ’û χρ‰¡(cid:12)ƒ Ýδ‘ πè¡@ πΖƒ‰ϑ9# ’û χ%.ρ</p><p>Ÿ u Ç ö F $ Î š ß Å ø ã 7 ÷ u è y ó Î Ï u Ï y ø $ Î š x u</p><p>&#</p><p>ΟO … δ&ρ …µΖGŠ;Ψ9 !$/ #θϑ™$)? #θ9$% ∩⊆∇∪ χθs=Áƒ</p><p>¢ è ã s ÷ r u ç ¨ t Íh u ã s « $ Î ( ß y s s ( ä s š ß Î ó ã</p><p>&#</p><p>∩⊆∪ χθ%‰≈Á9 $Ρ)ρ  δ& 7=γΒ $Ρ‰κ− $Β µ‹9θ9 9θ)Ζ9</p><p>š è Ï | s ¯ Î u Ï Î ÷ r y Î ô t t ô Í y t Ï Íh Ï u Ï £ s à u s</p><p>Shaleh As.</p><p>∩∈⊃∪ χρè±„ ω Νδρ #6Β $Ρ3Βρ #6Β #ρ3Βρ</p><p>š ã ã ô o Ÿ ö è u \ ò t t ö s t u \ ò t ( ã s t u</p><p>Dan adalah di kota itu39 sembilan orang laki-laki yang membuat kerusakan</p><p>di muka bumi, dan mereka tidak berbuat kebaikan.{48}</p><p>Mereka berkata: "Bersumpahlah kamu dengan nama Allah, bahwa kita</p><p>sungguh-sungguh akan menyerangnya dengan tiba-tiba beserta</p><p>keluarganya di malam hari, kemudian kita katakan kepada warisnya</p><p>(bahwa) kita tidak menyaksikan kematian keluarganya itu, dan</p><p>sesungguhnya kita adalah orang-orang yang benar".{49}</p><p>Dan merekapun merencanakan makar dengan sungguh-sungguh dan</p><p>Kamipun merencanakan makar, sedang mereka tidak menyadari.{50}</p><p>5.2.8 Mukjizat Shaleh As. dan Sikap Kaum Tsamud</p><p>◙ Huud [11]: 64 – 65</p><p>Ú‘& ’û ≅2'? $δρ‘‹ù πƒ# Ν69 !# π%$Ρ ν‹≈δ Θθ)≈ƒρ</p><p>Ç ö r þ Î ö à ù s y â x s Z t u ö à s « $ è s t Í É y Ï ö s t u</p><p>/</p><p>$δρ)èù ∩∉⊆∪ =ƒ% >#‹ã .‹{'‹ù θ¡0 $δθ¡ϑ? ωρ !#</p><p>y ã s y s Ò Ì s Ò x t ö ä x è ù u s & þ Ý Î y  y s Ÿ u « $</p><p></p><p>î ‰ãρ 9≡Œ Θ$ƒ& πW≈=O Ν2‘#Š ’û #θèGϑ? Α$)ù</p><p>ç ö x î ô u š Ï s ( 5 − r s s n r ö à Í y Î ( ã − y s t s s</p><p>∩∉∈∪ >ρ‹3Β</p><p>5 ä õ t</p><p>Hai kaumku, inilah unta betina dari Allah, sebagai mukjizat (yang</p><p>menunjukkan kebenaran) untukmu, sebab itu biarkanlah ia makan di bumi</p><p>Allah, dan janganlah kamu mengganggunya dengan gangguan apapun</p><p>yang akan menyebabkan kamu ditimpa azab yang dekat."{64}</p><p>Mereka membunuh unta itu, maka berkata Shaleh: "Bersukarialah kamu</p><p>39) Menurut Agli Tafsir yang dimaksud “kota ini”: kota kaum Tsamud yaitu kota Al Hijr.</p><p>Shaleh As.</p><p>sekalian di rumahmu selama tiga hari40, itu adalah janji yang tidak dapat</p><p>didustakan."{65}</p><p>◙ Asy Syu'araa' [26]: 155 – 157</p><p>/</p><p>ωρ ∩⊇∈∈∪ Θθ=èΒ Θθƒ >° 39ρ >° $λ; π%$Ρ ν‹≈δ Α$%</p><p>Ÿ u 5 è ÷ ¨ 5 ö t Ü ÷ Å ö ä s u Ò ÷ Å o ° × s t Í É y t s</p><p>$δρ)èù ∩⊇∈∉∪ ΟŠàã Θθƒ >#‹ã Ν.‹{'‹ù θ¡0 $δθ¡ϑ?</p><p>y ã s y s 5 Ï t B ö t Ü x t ö ä x è ù u s & þ Ý Î y  y s</p><p>∩⊇∈∠∪ Β‰≈Ρ #θs7¹'ù</p><p>t Ï Ï t ( ß t ô r s</p><p>Shaleh menjawab: "Ini seekor unta betina, ia mempunyai giliran untuk</p><p>mendapatkan air, dan kamu memiliki giliran pula untuk mendapatkan air</p><p>di hari yang tertentu.{155}</p><p>Dan janganlah kamu sentuh unta betina itu dengan suatu kejahatan, yang</p><p>menyebabkan kamu ditimpa oleh azab hari yang besar".{156}</p><p>Kemudian mereka membunuhnya, lalu mereka menjadi menyesal,{157}</p><p>◙ Al Qamar [54]: 27 – 29</p><p>β& Νη∞;Ρρ ∩⊄∠∪ 9Ü¹#ρ Νκ:)?‘$ù Νλ; πΖFù π%$Ζ9# #θ=™Β $Ρ)</p><p>¨ r ö æ ÷ Îm t u ÷ É s ô $ u ö å ö É s ö $ s ö ç ° Z u ÷ Ï Ï s ¨ $ ( è Å ö ã ¯ Î</p><p>Λι7m$¹ #ρŠ$Ζù ∩⊄∇∪ ØGtΧ >° ≅. ΝηΖ/ πϑ¡% $ϑ9#</p><p>÷ à t Ï | ( ÷ y u s × | t ø ’ 5 ÷ Å ‘ ä ( ö æ u ÷ t 8 y ó Ï u ! y ø $</p><p>∩⊄∪ )èù ‘Û$èGù</p><p>t s y s 4 s y t s</p><p>Sesungguhnya Kami akan mengirimkan unta betina sebagai cobaan bagi</p><p>mereka, maka tunggulah (tindakan) mereka dan bersabarlah.{27}</p><p>Dan beritakanlah kepada mereka bahwa sesungguhnya air itu terbagi</p><p>antara mereka (dengan unta betina itu); tiap-tiap giliran minum dihadiri</p><p>40) Perbuatan mereka menusuk unta itu adalah suatu pelanggaran terhadap larangan</p><p>Nabi Shaleh As. Oleh sebab itu Allah menjatuhkan kepada mereka hukuman, yaitu</p><p>membatasi hidup mereka hanya dalam tempo tiga hari, maka sebagai ejekan mereka</p><p>disuruh bersuka ria selama tiga hari itu.</p><p>Shaleh As.</p><p>(oleh yang punya giliran)41{28}</p><p>Maka mereka memanggil kawannya, lalu kawannya menangkap (unta itu)</p><p>dan membunuhnya.{29}</p><p>◙</p><p>Lihat juga: Al Israa’ [17]: 59, Al A'raaf [7]: 77, Asy Syams [91]: 11 – 115</p><p>41) Unta betina ini sebagai mukjizat Nabi saleh As. Lihat surat Hud ayat 64 dan surat</p><p>Asy Syu'araa' ayat 154-155.</p></div>`,
                        quiz: [
                            { "question": "Siapakah nama ibu Nabi Ya'qub AS?", "options": ["Ribka (Rifiqah)", "Sarah", "Hajar", "Rahmah"], "answer": 0 },
                            { "question": "Siapakah saudara kembar Nabi Ya'qub AS?", "options": ["'Aishu' (Esau)", "Yusuf", "Bunyamin", "Luth"], "answer": 0 },
                            { "question": "Nabi Ya'qub adalah putera dari Nabi siapa?", "options": ["Ishaq", "Ismail", "Ibrahim", "Luth"], "answer": 0 },
                            { "question": "Dimanakah Nabi Ya'qub dilahirkan?", "options": ["Palestina", "Mesir", "Babilonia", "Mekah"], "answer": 0 },
                            { "question": "Dalam surat Huud ayat 71, kelahiran Ya'qub dikabarkan setelah kelahiran siapa?", "options": ["Ishak", "Ismail", "Yusuf", "Musa"], "answer": 0 }
                        ]
                    },
                    {
                        id: 141,
                        title: "Azab Kaum Tsamud",
                        file: "topic_141.pdf",
                        content: `<h2>Isi Materi</h2><div class="content-section"><p>5.3</p>
<h4>AZAB DAN BALASAN</h4>
<h4>TERHADAP</h4>
<div class="quran-quote">

<p class="translation">Adapun kaum Tsamud, maka mereka telah dibinasakan dengan kejadian yang luar biasa 42 .{ 5}</p>
<span class="source">Referensi: Ayat 5</span>
</div>
<div class="quran-quote">


<p class="translation">Maka mereka ditimpa azab. Sesungguhnya pada yang demikian itu benar-benar terdapat bukti yang nyata. Dan adalah kebanyakan mereka tidak beriman.{158 } Dan sesungguhnya Tuhanmu benar-benar Dia-lah Yang Maha Perkasa lagi Maha Penyayang.{159 }</p>
<span class="source">Referensi: Ayat 158  – 159</span>
</div>
<div class="quran-quote">


<p class="translation">Dan satu suara keras yang mengguntur menimpa orang-orang yang zalim itu, lalu mereka mati bergelimpangan di rumahnya,{67 } menyebabkan suara yang mengguntur yang dapat menghancurkan.</p>
<span class="source">Referensi: Ayat 67  – 68</span>
</div>
<h4>Turunnya Azab kepada  Kaum Tsamud</h4>
<p>Seolah-olah  mereka  belum  pernah  berdiam 43  di  tempat  itu.  Ingatlah, sesungguhnya  kaum  Tsamud  mengingkari  Tuhan  mereka.  Ingatlah, kebinasaanlah  bagi  kaum  Tsamud.</p>
<div class="quran-quote">


<p class="translation">Maka mereka dibinasakan oleh suara keras yang mengguntur di waktu pagi 44 ,{83 } Maka tidak dapat menolong mereka apa yang telah mereka usahakan.{84 }</p>
<span class="source">Referensi: Ayat 83  – 84</span>
</div>
<div class="quran-quote">



<p class="translation">Sesungguhnya Kami menimpakan atas mereka satu suara yang keras mengguntur, maka jadilah mereka seperti rumput kering (yang dikumpulkan oleh) yang punya kandang binatang.{31 } Dan sesungguhnya telah Kami mudahkan Alquran untuk pelajaran, maka adakah orang yang mengambil pelajaran?{32 } lebur oleh guntur itu, tanpa bekas, seakan-akan mereka tidak pernah ada. kepada mereka.</p>
<span class="source">Referensi: Ayat 30  – 32</span>
</div>
<div class="quran-quote">



<p class="translation">Dan pada (kisah) kaum Tsamud ketika dikatakan kepada mereka: "Bersenang-senanglah kalian sampai suatu waktu."{ 43 } Maka mereka berlaku angkuh terhadap perintah Tuhannya, lalu mereka disambar petir dan mereka melihatnya.{ 44 } Maka mereka sekali-kali tidak dapat bangun dan tidak pula mendapat pertolongan,{ 45 }</p>
<span class="source">Referensi: Ayat 43  – 45</span>
</div>
<div class="quran-quote">


<p class="translation">Maka perhatikanlah betapa akibat makar mereka itu, bahwasanya Kami membinasakan mereka dan kaum mereka semuanya.{ 51 } Maka itulah rumah-rumah mereka dalam keadaan runtuh disebabkan kezaliman mereka. Sesungguhnya pada yang demikian itu (terdapat) pelajaran bagi kaum yang mengetahui.{ 52 }</p>
<span class="source">Referensi: Ayat 51  – 52</span>
</div>
<div class="quran-quote">

<p class="translation">Dzaariyaat [51]: 43-45, Al Haaqqah [69]: 5, Asy Syams [91]: 13 – 15</p>
<span class="source">Referensi: Ayat 78</span>
</div>
<div class="quran-quote">

<p class="translation">Maka tatkala datang azab Kami, Kami selamatkan Shaleh beserta orang- orang yang beriman bersamanya dengan rahmat dari Kami dan dari kehinaan di hari itu. Sesungguhnya Tuhanmu Dia-lah Yang Maha Kuat lagi Maha Perkasa.{ 66 }</p>
<span class="source">Referensi: Ayat 66</span>
</div>
<div class="quran-quote">

<p class="translation">Dan telah Kami selamatkan orang-orang yang beriman 45 dan mereka itu selalu bertakwa.{53 }</p>
<span class="source">Referensi: Ayat 53</span>
</div>
<div class="quran-quote">


<p class="translation">Dan adapun kaum Tsamud, maka mereka telah Kami beri petunjuk tetapi dengan dia.</p>
<span class="source">Referensi: Ayat 17  – 18</span>
</div>
<h4>Shaleh As. dan Kaumnya yang Beriman Selamat</h4>
<p>mereka  lebih  menyukai  buta  (kesesatan)  daripada  petunjuk, maka mereka  disambar  petir  azab  yang  menghinakan  disebabkan  apa  yang telah  mereka  kerjakan.</p>
<h4>Dan  Kami  selamatkan  orang-orang  yang  beriman  dan  mereka  adalah</h4>
<p>orang-orang  yang  bertakwa.</p>
<div class="quran-quote">

</div>`,
                        quiz: [
                            {
                                question: "Berapa lama tangguh waktu yang diberikan kepada kaum Tsamud sebelum azab datang?",
                                options: ["1 hari", "3 hari", "7 hari", "40 hari"],
                                correct: 1,
                                explanation: "...Bersukarialah kamu sekalian di rumahmu selama tiga hari... (Huud: 65)."
                            },
                            {
                                question: "Azab apa yang menimpa kaum Tsamud (berdasarkan Al-Haaqqah: 5 & Huud: 67)?",
                                options: ["Banjir besar", "Angin topan", "Kejadian luar biasa (petir/suara keras yang mengguntur)", "Hujan batu"],
                                correct: 2,
                                explanation: "Adapun kaum Tsamud, maka mereka telah dibinasakan dengan kejadian yang luar biasa (Al-Haaqqah: 5)."
                            },
                            {
                                question: "Kapan waktu terjadinya azab suara menggelegar tersebut (Al-Hijr 83)?",
                                options: ["Tengah malam", "Siang bolong", "Waktu dhuha (pagi)", "Waktu ashar"],
                                correct: 2,
                                explanation: "Maka mereka dibinasakan oleh suara keras yang mengguntur di waktu pagi (Al-Hijr: 83)."
                            },
                            {
                                question: "Siapakah yang diselamatkan Allah dari azab tersebut?",
                                options: ["Hanya Nabi Shaleh", "Nabi Shaleh dan keluarganya", "Shaleh beserta orang-orang yang beriman bersamanya", "Hewan-hewan ternak"],
                                correct: 2,
                                explanation: "Maka tatkala datang azab Kami, Kami selamatkan Shaleh beserta orang-orang yang beriman bersamanya... (Huud: 66)."
                            },
                            {
                                question: "Bagaimana kondisi kaum Tsamud setelah azab menimpa?",
                                options: ["Mati bergelimpangan di rumah mereka", "Hanyut terbawa air", "Terkubur pasir hidup-hidup", "Berubah menjadi kera"],
                                correct: 0,
                                explanation: "...maka jadilah mereka mayat-mayat yang bergelimpangan di tempat tinggal mereka (Huud: 67)."
                            }
                        ]
                    }
                ]
            }
            ,
            {
                "id": "subject-6-6",
                "title": "Pokok Bahasan 6: Luth AS",
                "topics": [
                    {
                        "id": 142,
                        "title": "Dakwah Luth AS Terhadap Kaum Sodom",
                        "file": "topic_142.pdf",
                        "content": `<p>6.1</p><h3>DAKWAH LUTH AS</h3><h3>TERHADAP</h3><h3>KAUM SODOM</h3><div class="quran-quote" id="verse-11:77-80"><p class="translation">Dan tatkala datang utusan-utusan Kami (para malaikat) itu kepada Luth, dia merasa susah dan merasa sempit dadanya karena kedatangan mereka, dan dia berkata: "Ini adalah hari yang amat sulit". Dan datanglah kepadanya kaumnya dengan bergegas-gegas. Dan sejak dahulu mereka selalu melakukan perbuatan-perbuatan yang keji. Luth berkata: "Hai kaumku, inilah puteri-puteriku, mereka lebih suci bagimu, maka bertakwalah kepada Allah dan janganlah kamu mencemarkan (nama)ku terhadap tamuku ini. Tidak adakah di antaramu seorang yang berakal?" Mereka menjawab: "Sesungguhnya kamu telah tahu bahwa kami tidak mempunyai keinginan terhadap puteri-puterimu; dan sesungguhnya kamu tentu mengetahui apa yang sebenarnya kami kehendaki". Luth berkata: "Seandainya aku ada mempunyai kekuatan (untuk menolakmu) atau kalau aku dapat berlindung kepada keluarga yang kuat (tentu aku lakukan)".</p><span class="source">Surat 11 Ayat: 77 - 80</span></div><div class="quran-quote" id="verse-15:67-72"><p class="translation">Dan datanglah penduduk kota itu (ke rumah Luth) dengan gembira (karena) kedatangan tamu-tamu itu. Luth berkata: "Sesungguhnya mereka adalah tamuku; maka janganlah kamu memberi malu (kepadaku), dan bertakwalah kepada Allah dan janganlah kamu membuat aku terhina". Mereka berkata: "Dan bukankah kami telah melarangmu dari (melindungi) manusia?" Luth berkata: "Inilah puteri-puteriku (kawinlah dengan mereka), jika kamu hendak berbuat (secara yang halal)". (Allah berfirman): "Demi umurmu (Muhammad), sesungguhnya mereka terombang-ambing di dalam kemabukan (kesesatan)".</p><span class="source">Surat 15 Ayat: 67 - 72</span></div><div class="quran-quote" id="verse-7:80-81"><p class="translation">Dan (Kami juga telah mengutus) Luth (kepada kaumnya). (Ingatlah) tatkala dia berkata kepada mereka: "Mengapa kamu mengerjakan perbuatan faahisyah itu, yang belum pernah dikerjakan oleh seorangpun (di dunia ini) sebelummu?" Sesungguhnya kamu mendatangi lelaki untuk melepaskan nafsumu (kepada mereka), bukan kepada wanita, malah kamu ini adalah kaum yang melampaui batas.</p><span class="source">Surat 7 Ayat: 80 - 81</span></div><div class="quran-quote" id="verse-26:160-166"><p class="translation">Kaum Luth telah mendustakan rasul-rasul, ketika saudara mereka, Luth, berkata kepada mereka: mengapa kamu tidak bertakwa?" Sesungguhnya aku adalah seorang rasul kepercayaan (yang diutus) kepadamu, maka bertakwalah kepada Allah dan taatlah kepadaku. Dan aku sekali-kali tidak minta upah kepadamu atas ajakan itu; upahku tidak lain hanyalah dari Tuhan semeta alam. Mengapa kamu mendatangi jenis lelaki di antara manusia, dan kamu tinggalkan isteri-isteri yang dijadikan oleh Tuhanmu untukmu, bahkan kamu adalah orang-orang yang melampaui batas".</p><span class="source">Surat 26 Ayat: 160 - 166</span></div><div class="quran-quote" id="verse-27:54-55"><p class="translation">Dan (ingatlah kisah) Luth, ketika dia berkata kepada kaumnya: "Mengapa kamu mengerjakan perbuatan fahisyah itu sedang kamu memperlihatkan(nya)?" "Mengapa kamu mendatangi laki-laki untuk (memenuhi) nafsu(mu), bukan (mendatangi) wanita? Sebenarnya kamu adalah kaum yang tidak mengetahui (akibat perbuatanmu)".</p><span class="source">Surat 27 Ayat: 54 - 55</span></div><div class="quran-quote" id="verse-29:28-29"><p class="translation">Dan (ingatlah) ketika Luth berkata pepada kaumnya: "Sesungguhnya kamu benar-benar mengerjakan perbuatan yang amat keji yang belum pernah dikerjakan oleh seorangpun dari umat-umat sebelum kamu". Apakah sesungguhnya kamu patut mendatangi laki-laki, menyamun dan mengerjakan kemungkaran di tempat-tempat pertemuanmu? Maka jawaban kaumnya tidak lain hanya mengatakan: "Datangkanlah kepada kami azab Allah, jika kamu termasuk orang-orang yang benar".</p><span class="source">Surat 29 Ayat: 28 - 29</span></div><p>Dan tatkala datang utusan-utusan Kami (para malaikat) itu kepada Luth, ia merasa susah dan merasa sempit dadanya karena kedatangan mereka, dan ia berkata: "Ini adalah hari yang amat sulit."</p><p>Dan datanglah kepadanya kaumnya dengan bergegas. Dan sejak dulu mereka selalu melakukan perbuatan keji. Luth berkata: "Hai kaumku, inilah putri-putriku, mereka lebih suci bagimu, maka bertakwalah kepada Allah dan janganlah kamu mencemarkan (nama)-ku terhadap tamuku ini. Tidak adakah di antaramu seorang yang berakal?"</p><p>Mereka menjawab: "Sesungguhnya kamu telah tahu bahwa kami tidak mempunyai keinginan terhadap putri-putrimu; dan sesungguhnya kamu tentu mengetahui apa yang sebenarnya kami kehendaki."</p><p>Luth berkata: "Kalau aku memiliki kekuatan (menolakmu) atau aku dapat berlindung kepada keluarga yang kuat (tentu aku lakukan)."</p><p>6.1.1 Tabiat Penduduk Sodom</p><p>Kaum Luth telah mendustakan rasul-rasul, Ketika saudara mereka; Luth berkata kepada mereka: “Mengapa kamu tidak bertakwa?" Sesungguhnya aku adalah seorang rasul kepercayaan (yang diutus) kepadamu, Maka bertakwalah kepada Allah dan taatlah kepadaku. Dan aku sekali-kali tidak minta upah kepadamu atas ajakan itu; upahku tidak lain hanyalah dari Tuhan semeta alam. Mengapa kamu mendatangi jenis lelaki di antara manusia, Dan kamu tinggalkan istri-istri yang dijadikan oleh Tuhanmu untukmu, bahkan kamu adalah orang-orang yang melampaui batas".</p><p>6.1.2 Dakwah Luth As. kepada Penduduk Sodom</p><p>Dan (kisah) Luth, ketika ia berkata kepada kaumnya: "Mengapa kamu mengerjakan fahisyah itu sedang kamu memperlihatkan-(nya)?" "Mengapa kamu mendatangi laki-laki untuk (memenuhi) nafsu -(mu), bukan (mendatangi) wanita? sebenarnya kamu adalah kaum yang tidak mengetahui (akibat perbuatanmu)".</p><p>Dan (ingatlah) ketika Luth berkata kepada kaumnya: "Sesungguhnya kamu benar-benar mengerjakan perbuatan yang amat keji yang belum pernah dikerjakan oleh seorangpun dari umat-umat sebelum kamu". Apakah sesungguhnya kamu patut mendatangi laki-laki, menyamun, dan mengerjakan kemungkaran di tempat-tempat pertemuanmu?. Maka jawaban kaumnya tidak lain hanya mengatakan: "Datangkanlah kepada kami azab Allah, jika kamu termasuk orang-orang benar".</p>`,
                        "quiz": [
                            {
                                "question": "Siapakah Nabi yang diutus kepada kaum Sodom?",
                                "options": [
                                    "Nabi Ibrahim AS",
                                    "Nabi Luth AS",
                                    "Nabi Ismail AS",
                                    "Nabi Musa AS"
                                ],
                                "correct": 1,
                                "explanation": "Nabi Luth AS diutus kepada kaum Sodom untuk mendakwahkan tauhid dan melarang perbuatan keji mereka."
                            },
                            {
                                "question": "Perbuatan keji apa yang dilakukan oleh kaum Sodom?",
                                "options": [
                                    "Menyembah berhala batu",
                                    "Homoseksual",
                                    "Mengubur bayi hidup-hidup",
                                    "Mengurangi timbangan"
                                ],
                                "correct": 1,
                                "explanation": "Kaum Sodom melakukan perbuatan keji yang belum pernah dilakukan sebelumnya, yaitu homoseksual (mendatangi sesama jenis)."
                            },
                            {
                                "question": "Bagaimana sikap kaum Sodom terhadap dakwah Nabi Luth AS?",
                                "options": [
                                    "Menerima dengan baik",
                                    "Sebagian menerima",
                                    "Mendustakan dan mengusir",
                                    "Ragu-ragu"
                                ],
                                "correct": 2,
                                "explanation": "Mereka mendustakan Nabi Luth dan bahkan mengancam akan mengusirnya."
                            },
                            {
                                "question": "Siapakah anggota keluarga Nabi Luth yang ikut dibinasakan?",
                                "options": [
                                    "Anaknya",
                                    "Ayahnya",
                                    "Istrinya",
                                    "Paman"
                                ],
                                "correct": 2,
                                "explanation": "Istri Nabi Luth termasuk golongan yang tertinggal dan dibinasakan karena ia mendukung perbuatan kaumnya."
                            },
                            {
                                "question": "Azab apa yang menimpa kaum Sodom?",
                                "options": [
                                    "Banjir bandang",
                                    "Tanah longsor",
                                    "Negeri dibalik dan dihujani batu",
                                    "Angin topan"
                                ],
                                "correct": 2,
                                "explanation": "Negeri mereka dijungkirbalikkan dan dihujani dengan batu dari tanah yang terbakar."
                            }
                        ]
                    },
                    {
                        "id": 143,
                        "title": "Sikap Kaum Sodom Terhadap Dakwah",
                        "file": "topic_143.pdf",
                        "content": `<p>6.2</p><h3>SIKAP KAUM SODOM</h3><h3>TERHADAP</h3><h3>DAKWAH LUTH AS</h3><div class="quran-quote" id="verse-7:82-82"><p class="translation">Jawab kaumnya tidak lain hanya mengatakan: "Usirlah mereka (Luth dan pengikut-pengikutnya) dari kotamu ini; sesungguhnya mereka adalah orang-orang yang berpura-pura mensucikan diri".</p><span class="source">Surat 7 Ayat: 82 - 82</span></div><div class="quran-quote" id="verse-27:56-56"><p class="translation">Maka tidak lain jawaban kaumnya melainkan mengatakan: "Usirlah Luth beserta keluarganya dari negerimu; karena sesungguhnya mereka itu orang-orang yang (mendakwakan dirinya) bersih".</p><span class="source">Surat 27 Ayat: 56 - 56</span></div><div class="quran-quote" id="verse-26:167-168"><p class="translation">Mereka menjawab: "Hai Luth, sesungguhnya jika kamu tidak berhenti, benar-benar kamu termasuk orang-orang yang diusir" Luth berkata: "Sesungguhnya aku sangat benci kepada perbuatanmu".</p><span class="source">Surat 26 Ayat: 167 - 168</span></div><p>Jawab kaumnya tidak lain hanya mengatakan: "Usirlah mereka (Luth dan pengikut-pengikutnya) dari kotamu ini; Sesungguhnya mereka adalah orang-orang yang berpura-pura menyucikan diri."</p><p>Maka tidak lain jawaban kaumnya melainkan mengatakan: "Usirlah Luth beserta keluarganya dari negerimu; karena sesungguhnya mereka itu orang-orang yang (mendakwakan dirinya) bersih".</p><p>6.2.1 Kaum Sodom Mengingkari Seruan Luth As.</p><p>Mereka menjawab: "Hai Luth, sesungguhnya jika kamu tidak berhenti, benar-benar kamu termasuk orang-orang yang diusir"</p><p>Luth berkata: “Sesungguhnya aku kepada perbuatanmu sangat benci..”</p>`,
                        "quiz": [
                            {
                                "question": "Siapakah Nabi yang diutus kepada kaum Sodom?",
                                "options": [
                                    "Nabi Ibrahim AS",
                                    "Nabi Luth AS",
                                    "Nabi Ismail AS",
                                    "Nabi Musa AS"
                                ],
                                "correct": 1,
                                "explanation": "Nabi Luth AS diutus kepada kaum Sodom untuk mendakwahkan tauhid dan melarang perbuatan keji mereka."
                            },
                            {
                                "question": "Perbuatan keji apa yang dilakukan oleh kaum Sodom?",
                                "options": [
                                    "Menyembah berhala batu",
                                    "Homoseksual",
                                    "Mengubur bayi hidup-hidup",
                                    "Mengurangi timbangan"
                                ],
                                "correct": 1,
                                "explanation": "Kaum Sodom melakukan perbuatan keji yang belum pernah dilakukan sebelumnya, yaitu homoseksual (mendatangi sesama jenis)."
                            },
                            {
                                "question": "Bagaimana sikap kaum Sodom terhadap dakwah Nabi Luth AS?",
                                "options": [
                                    "Menerima dengan baik",
                                    "Sebagian menerima",
                                    "Mendustakan dan mengusir",
                                    "Ragu-ragu"
                                ],
                                "correct": 2,
                                "explanation": "Mereka mendustakan Nabi Luth dan bahkan mengancam akan mengusirnya."
                            },
                            {
                                "question": "Siapakah anggota keluarga Nabi Luth yang ikut dibinasakan?",
                                "options": [
                                    "Anaknya",
                                    "Ayahnya",
                                    "Istrinya",
                                    "Paman"
                                ],
                                "correct": 2,
                                "explanation": "Istri Nabi Luth termasuk golongan yang tertinggal dan dibinasakan karena ia mendukung perbuatan kaumnya."
                            },
                            {
                                "question": "Azab apa yang menimpa kaum Sodom?",
                                "options": [
                                    "Banjir bandang",
                                    "Tanah longsor",
                                    "Negeri dibalik dan dihujani batu",
                                    "Angin topan"
                                ],
                                "correct": 2,
                                "explanation": "Negeri mereka dijungkirbalikkan dan dihujani dengan batu dari tanah yang terbakar."
                            }
                        ]
                    },
                    {
                        "id": 144,
                        "title": "Azab dan Balasan Kaum Sodom",
                        "file": "topic_144.pdf",
                        "content": `<p>6.3</p><h3>AZAB DAN BALASAN</h3><h3>TERHADAP</h3><h3>KAUM SODOM</h3><div class="quran-quote" id="verse-7:83-83"><p class="translation">Kemudian Kami selamatkan dia dan pengikut-pengikutnya kecuali isterinya; dia termasuk orang-orang yang tertinggal (dibinasakan).</p><span class="source">Surat 7 Ayat: 83 - 83</span></div><div class="quran-quote" id="verse-11:81-81"><p class="translation">Para utusan (malaikat) berkata: "Hai Luth, sesungguhnya kami adalah utusan-utusan Tuhanmu, sekali-kali mereka tidak akan dapat mengganggu kamu, sebab itu pergilah dengan membawa keluarga dan pengikut-pengikut kamu di akhir malam dan janganlah ada seorangpun di antara kamu yang tertinggal, kecuali isterimu. Sesungguhnya dia akan ditimpa azab yang menimpa mereka karena sesungguhnya saat jatuhnya azab kepada mereka ialah di waktu subuh; bukankah subuh itu sudah dekat?".</p><span class="source">Surat 11 Ayat: 81 - 81</span></div><p>Kemudian Kami selamatkan dia dan pengikut-pengikutnya kecuali istrinya; ia termasuk orang-orang yang tertinggal (dibinasakan).</p><div class="quran-quote" id="verse-15:59-66"><p class="translation">kecuali Luth beserta pengikut-pengikutnya. Sesungguhnya Kami akan menyelamatkan mereka semuanya, kecuali istrinya. Kami telah menentukan, bahwa sesungguhnya ia itu termasuk orang-orang yang tertinggal (bersama-sama dengan orang kafir lainnya)". Maka tatkala para utusan itu datang kepada kaum Luth, beserta pengikut pengikutnya, ia berkata: "Sesungguhnya kamu adalah orang-orang yang tidak dikenal". Para utusan menjawab: "Sebenarnya kami ini datang kepadamu dengan membawa azab yang selalu mereka dustakan. Dan kami datang kepadamu membawa kebenaran dan sesungguhnya kami betul-betul orang-orang benar. Maka pergilah kamu di akhir malam dengan membawa keluargamu, dan ikutlah mereka dari belakang dan janganlah seorangpun di antara kamu menoleh kebelakang dan teruskanlah perjalanan ke tempat yang di perintahkan kepadamu". Dan telah Kami wahyukan kepadanya (Luth) perkara itu, yaitu bahwa mereka akan ditumpas habis di waktu subuh.</p><span class="source">Surat 15 Ayat: 59 - 66</span></div><div class="quran-quote" id="verse-21:74-75"><p class="translation">dan kepada Luth, Kami telah berikan hikmah dan ilmu, dan telah Kami selamatkan dia dari (azab yang telah menimpa penduduk) kota yang mengerjakan perbuatan keji. Sesungguhnya mereka adalah kaum yang jahat lagi fasik, dan Kami masukkan dia ke dalam rahmat Kami; karena sesungguhnya dia termasuk orang-orang yang saleh.</p><span class="source">Surat 21 Ayat: 74 - 75</span></div><div class="quran-quote" id="verse-26:169-171"><p class="translation">(Luth berdoa): "Ya Tuhanku selamatkanlah aku beserta keluargaku dari (akibat) perbuatan yang mereka kerjakan". Lalu Kami selamatkan ia beserta keluarganya semua, kecuali seorang perempuan tua (isterinya), yang termasuk dalam golongan yang tinggal.</p><span class="source">Surat 26 Ayat: 169 - 171</span></div><div class="quran-quote" id="verse-27:57-57"><p class="translation">Maka Kami selamatkan dia beserta keluarganya, kecuali isterinya. Kami telah mentakdirkan dia termasuk orang-orang yang tertinggal (dibinasakan).</p><span class="source">Surat 27 Ayat: 57 - 57</span></div><p>Para utusan (malaikat) berkata: "Hai Luth, sesungguhnya kami adalah utusan-utusan Tuhanmu, sekali-kali mereka tidak dapat mengganggu kamu, sebab itu pergilah dengan membawa keluarga dan pengikut-pengikutmu di akhir malam dan janganlah ada seorangpun di antara kamu yang tertinggal, kecuali istrimu. Sesungguhnya ia akan ditimpa azab yang menimpa mereka karena sesungguhnya saat jatuhnya azab kepada mereka ialah waktu subuh; bukankah subuh sudah dekat?".</p><div class="quran-quote" id="verse-29:30-33"><p class="translation">Luth berdoa: "Ya Tuhanku, tolonglah aku (dengan menimpakan azab) atas kaum yang berbuat kerusakan itu". Dan tatkala utusan Kami (para malaikat) datang kepada Ibrahim membawa kabar gembira, mereka mengatakan: "Sesungguhnya kami akan menghancurkan penduduk negeri (Sodom) ini; sesungguhnya penduduknya adalah orang-orang yang zalim". Berkata Ibrahim: "Sesungguhnya di kota itu ada Luth". Para malaikat berkata: "Kami lebih mengetahui siapa yang ada di kota itu. Kami sungguh-sungguh akan menyelamatkan dia dan pengikut-pengikutnya kecuali isterinya. Dia adalah termasuk orang-orang yang tertinggal (dibinasakan). Dan tatkala datang utusan-utusan Kami (para malaikat) itu kepada Luth, dia merasa susah karena (kedatangan) mereka, dan (merasa) tidak punya kekuatan untuk melindungi mereka dan mereka berkata: "Janganlah kamu takut dan jangan (pula) susah. Sesungguhnya kami akan menyelamatkan kamu dan pengikut-pengikutmu, kecuali isterimu, dia adalah termasuk orang-orang yang tertinggal (dibinasakan)".</p><span class="source">Surat 29 Ayat: 30 - 33</span></div><div class="quran-quote" id="verse-37:133-135"><p class="translation">Sesungguhnya Luth benar-benar salah seorang rasul. (Ingatlah) ketika Kami selamatkan dia dan keluarganya (pengikut-pengikutnya) semua, kecuali seorang perempuan tua (isterinya yang berada) bersama-sama orang yang tinggal.</p><span class="source">Surat 37 Ayat: 133 - 135</span></div><div class="quran-quote" id="verse-7:84-84"><p class="translation">Dan Kami turunkan kepada mereka hujan (batu); maka perhatikanlah bagaimana kesudahan orang-orang yang berdosa itu.</p><span class="source">Surat 7 Ayat: 84 - 84</span></div><div class="quran-quote" id="verse-11:82-83"><p class="translation">Maka tatkala datang azab Kami, Kami jadikan negeri kaum Luth itu yang di atas ke bawah (Kami balikkan), dan Kami hujani mereka dengan batu dari tanah yang terbakar dengan bertubi-tubi, Yang diberi tanda oleh Tuhanmu, dan siksaan itu tiadalah jauh dari orang-orang yang zalim.</p><span class="source">Surat 11 Ayat: 82 - 83</span></div><p>6.3.1 Luth As. dan Pengikutnya Selamat Kecuali Isterinya</p><div class="quran-quote" id="verse-15:73-77"><p class="translation">Maka mereka dibinasakan oleh suara keras yang mengguntur, ketika matahari akan terbit. Maka Kami jadikan bahagian atas kota itu terbalik ke bawah dan Kami hujani mereka dengan batu dari tanah yang keras. Sesungguhnya pada yang demikian itu benar-benar terdapat tanda-tanda (kekuasaan Allah) bagi orang-orang yang memperhatikan tanda-tanda. Dan sesungguhnya kota itu benar-benar terletak di jalan yang masih tetap (dilalui manusia). Sesungguhnya pada yang demikian itu benar-benar terdapat tanda-tanda (kekuasaan Allah) bagi orang-orang yang beriman.</p><span class="source">Surat 15 Ayat: 73 - 77</span></div><div class="quran-quote" id="verse-26:172-175"><p class="translation">Kemudian Kami binasakan yang lain. Dan Kami hujani mereka dengan hujan (batu) maka amat jeleklah hujan yang menimpa orang-orang yang telah diberi peringatan itu. Sesunguhnya pada yang demikian itu benar-benar terdapat bukti-bukti yang nyata. Dan adalah kebanyakan mereka tidak beriman. Dan sesungguhnya Tuhanmu, benar-benar Dialah Yang Maha Perkasa lagi Maha Penyayang.</p><span class="source">Surat 26 Ayat: 172 - 175</span></div><div class="quran-quote" id="verse-27:58-58"><p class="translation">Dan Kami turunkan hujan atas mereka (hujan batu), maka amat buruklah hujan yang ditimpakan atas orang-orang yang diberi peringatan itu.</p><span class="source">Surat 27 Ayat: 58 - 58</span></div><div class="quran-quote" id="verse-29:34-35"><p class="translation">Sesungguhnya Kami akan menurunkan azab dari langit atas penduduk kota ini karena mereka berbuat fasik. Dan sesungguhnya Kami tinggalkan daripadanya satu tanda yang nyata bagi orang-orang yang berakal.</p><span class="source">Surat 29 Ayat: 34 - 35</span></div><div class="quran-quote" id="verse-37:136-138"><p class="translation">Kemudian Kami binasakan orang-orang yang lain. Dan sesungguhnya kamu (hai penduduk Mekah) benar-benar akan melalui (bekas-bekas) mereka di waktu pagi, dan di waktu malam. Maka apakah kamu tidak memikirkan?</p><span class="source">Surat 37 Ayat: 136 - 138</span></div><div class="quran-quote" id="verse-51:31-37"><p class="translation">Ibrahim bertanya: "Apakah urusanmu hai para utusan?" Mereka menjawab: "Sesungguhnya kami diutus kepada kaum yang berdosa (kaum Luth), agar kami timpakan kepada mereka batu-batu dari tanah, yang ditandai di sisi Tuhanmu untuk membinasakan orang-orang yang melampaui batas". Lalu Kami keluarkan orang-orang yang beriman yang berada di negeri kaum Luth itu. Dan Kami tidak mendapati negeri itu, kecuali sebuah rumah dari orang yang berserah diri. Dan Kami tinggalkan pada negeri itu suatu tanda bagi orang-orang yang takut kepada siksa yang pedih.</p><span class="source">Surat 51 Ayat: 31 - 37</span></div><p>Kecuali Luth beserta pengikut-pengikutnya. Sesungguhnya Kami akan menyelamatkan mereka semuanya, Kecuali istrinya. Kami telah menentukan, bahwa sesungguhnya ia termasuk golongan yang tertinggal (bersama orang kafir lainnya)".</p><p>Maka ketika para utusan datang kepada keluarga (pengikut) Luth, Ia (Luth) berkata: "Sesungguhnya kamu adalah orang-orang yang tidak dikenal". Para utusan itu menjawab: "Sebenarnya kami ini datang kepadamu dengan membawa azab yang selalu mereka dustakan. Dan Kami datang kepadamu membawa kebenaran dan sesungguhnya Kami betul-betul golongan yang benar.</p><p>Maka pergilah kamu di akhir malam dengan membawa keluargamu, dan ikutlah mereka dari belakang dan janganlah seorangpun di antara kamu menoleh ke belakang dan teruskanlah perjalanan ke tempat yang di perintahkan kepadamu".</p><p>Dan telah Kami wahyukan kepadanya (Luth) perkara itu, yaitu bahwa mereka akan ditumpas habis di waktu subuh.</p><div class="quran-quote" id="verse-54:33-40"><p class="translation">Kaum Luth-pun telah mendustakan ancaman-ancaman (nabinya). Sesungguhnya Kami telah menghembuskan kepada mereka angin yang membawa batu-batu (yang menimpa mereka), kecuali keluarga Luth. Mereka Kami selamatkan sebelum fajar menyingsing, sebagai nikmat dari Kami. Demikianlah Kami memberi balasan kepada orang-orang yang bersyukur, Dan sesungguhnya dia (Luth) telah memperingatkan mereka akan azab-azab Kami, maka mereka mendustakan ancaman-ancaman itu. Dan sesungguhnya mereka telah membujuknya (agar menyerahkan) tamunya (kepada mereka), lalu Kami butakan mata mereka, maka rasakanlah azab-Ku dan ancaman-ancaman-Ku. Dan sesungguhnya pada esok harinya mereka ditimpa azab yang kekal. Maka rasakanlah azab-Ku dan ancaman-ancaman-Ku. Dan sesungguhnya telah Kami mudahkan Al Quran untuk pelajaran, maka adakah orang yang mengambil pelajaran?</p><span class="source">Surat 54 Ayat: 33 - 40</span></div><p>Dan kepada Luth, Kami telah berikan hikmah dan ilmu, dan telah Kami selamatkan dia dari (azab yang telah menimpa penduduk) kota yang mengerjakan perbuatan keji. Sesungguhnya mereka adalah kaum yang jahat lagi fasik, Dan Kami masukkan ia ke dalam rahmat kami; karena sesungguhnya ia termasuk orang-orang yang saleh.</p><p>(Luth berdoa): "Ya Tuhanku selamatkanlah aku beserta keluargaku dari (akibat) perbuatan yang mereka kerjakan.” Lalu Kami selamatkan ia beserta keluarganya semua, Kecuali seorang perempuan tua (istrinya) yang termasuk dalam golongan yang tinggal.</p><p>Maka Kami selamatkan dia dan keluarganya, kecuali istrinya. Kami telah menakdirkannya termasuk golongan tertinggal (dibinasakan).</p><p>Luth berdoa: "Ya Tuhanku, tolonglah aku (dengan menimpakan azab) atas kaum yang berbuat kerusakan itu".</p><p>Dan tatkala utusan Kami (para malaikat) datang kepada Ibrahim membawa kabar gembira, mereka mengatakan: "Sesungguhnya kami akan menghancurkan penduduk negeri (Sodom) ini; sesungguhnya penduduknya adalah orang-orang yang zalim".</p><p>Berkata Ibrahim: "Sesungguhnya di kota itu ada Luth". Para malaikat berkata: "Kami lebih mengetahui siapa yang ada di kota itu. Kami sungguh akan menyelamatkannya dan pengikut-pengikutnya kecuali istrinya, ia termasuk orang-orang yang tertinggal (dibinasakan).</p><p>Dan tatkala datang utusan-utusan Kami (para malaikat) itu kepada Luth, dia merasa susah karena (kedatangan) mereka, dan (merasa) tidak punya kekuatan untuk melindungi mereka dan mereka berkata: "Janganlah kamu takut dan jangan (pula) susah. Sesungguhnya kami akan menyelamatkanmu dan pengikut-pengikutmu, kecuali istrimu, ia adalah termasuk orang-orang yang tertinggal (dibinasakan)".</p><p>Sesungguhnya Luth benar-benar salah seorang rasul. (Ingatlah) ketika Kami selamatkan dia dan kelurganya (pengikutnya) semua, Kecuali seorang perempuan tua (istrinya yang berada) bersama-sama orang yang tinggal.</p><p>Dan Kami turunkan kepada mereka hujan (batu); maka perhatikanlah bagaimana kesudahan orang-orang yang berdosa itu.</p><p>Maka tatkala datang azab Kami, Kami jadikan negeri kaum Luth itu yang di atas ke bawah (kami balikkan), dan Kami hujani mereka dengan batu dari tanah yang terbakar dengan bertubi-tubi, Yang diberi tanda oleh Tuhanmu, dan siksaan itu tidaklah jauh dari orang-orang yang zalim.</p><p>Maka mereka dibinasakan oleh suara keras yang mengguntur, ketika matahari akan terbit. Maka Kami jadikan bagian atas kota itu terbalik ke bawah dan Kami hujani mereka dengan batu dari tanah yang keras. Sesungguhnya pada yang demikian benar-benar terdapat tanda-tanda (kekuasaan Allah) bagi orang-orang yang memperhatikan tanda.</p><p>Dan sesungguhnya kota itu benar-benar terletak di jalan yang masih tetap (dilalui manusia). Sesungguhnya pada yang demikian itu benar-benar terdapat tanda-tanda (kekuasaan Allah) bagi orang-orang yang beriman.</p><p>Kemudian Kami binasakan yang lain. Dan Kami hujani mereka dengan hujan (batu), maka amat jeleklah hujan yang menimpa orang-orang yang telah diberi peringatan itu.</p><p>Sesunguhnya pada yang demikian itu benar-benar terdapat bukti-bukti yang nyata. Dan adalah kebanyakan mereka tidak beriman. Dan sesungguhnya Tuhanmu, benar-benar Dialah Yang Maha Perkasa lagi Maha Penyayang.</p><p>Dan Kami turunkan hujan atas mereka (hujan batu), maka amat buruk hujan yang ditimpakan atas orang-orang yang diberi peringatan itu.</p><p>Sesungguhnya Kami akan menurunkan azab dari langit atas penduduk kota ini karena mereka berbuat fasik. Dan sesungguhnya Kami tinggalkan daripadanya satu tanda yang nyata bagi orang-orang yang berakal.</p><p>Kemudian Kami binasakan orang-orang yang lain. Dan sesungguhnya kamu (hai penduduk Mekah) benar-benar akan melalui (bekas-bekas) mereka di waktu pagi, Dan di waktu malam. Maka apakah kamu tidak memikirkan?</p><p>Ibrahim bertanya: "Apakah urusanmu hai para utusan?" Mereka menjawab: "Sesungguhnya kami diutus kepada kaum yang berdosa (kaum Luth), Agar Kami timpakan kepada mereka batu-batu dari tanah, Yang ditandai di sisi Tuhanmu untuk membinasakan orang-orang yang melampaui batas".</p><p>Lalu Kami keluarkan orang-orang yang beriman yang berada di negeri kaum Luth itu. Dan Kami tidak mendapati negeri itu, kecuali sebuah rumah dari orang yang berserah diri. Dan Kami tinggalkan pada negeri itu suatu tanda bagi orang-orang yang takut kepada siksa yang pedih.</p><p>Kaum Luth-pun telah mendustakan ancaman-ancaman (nabinya). Sesungguhnya Kami telah menghembuskan kepada mereka angin yang membawa batu-batu (yang menimpa mereka), kecuali keluarga Luth. Mereka Kami selamatkan sebelum fajar menyingsing, Sebagai nikmat dari kami. Demikianlah Kami memberi balasan kepada orang-orang yang bersyukur,</p><p>Dan sungguh dia (Luth) telah memperingatkan mereka akan azab-azab Kami, maka mereka mendustakan ancaman-ancaman itu. Dan sungguh mereka telah membujuknya (agar menyerahkan) tamunya (kepada mereka), lalu Kami butakan mata mereka, maka rasakanlah azab-Ku dan ancaman-ancaman-Ku. Dan sungguh pada esok harinya mereka ditimpa azab yang kekal. Maka rasakanlah azab-Ku dan ancaman-ancaman-Ku. Dan sesungguhnya telah Kami mudahkan Alquran untuk pelajaran, maka adakah orang yang mengambil pelajaran?</p>`,
                        "quiz": [
                            {
                                "question": "Siapakah Nabi yang diutus kepada kaum Sodom?",
                                "options": [
                                    "Nabi Ibrahim AS",
                                    "Nabi Luth AS",
                                    "Nabi Ismail AS",
                                    "Nabi Musa AS"
                                ],
                                "correct": 1,
                                "explanation": "Nabi Luth AS diutus kepada kaum Sodom untuk mendakwahkan tauhid dan melarang perbuatan keji mereka."
                            },
                            {
                                "question": "Perbuatan keji apa yang dilakukan oleh kaum Sodom?",
                                "options": [
                                    "Menyembah berhala batu",
                                    "Homoseksual",
                                    "Mengubur bayi hidup-hidup",
                                    "Mengurangi timbangan"
                                ],
                                "correct": 1,
                                "explanation": "Kaum Sodom melakukan perbuatan keji yang belum pernah dilakukan sebelumnya, yaitu homoseksual (mendatangi sesama jenis)."
                            },
                            {
                                "question": "Bagaimana sikap kaum Sodom terhadap dakwah Nabi Luth AS?",
                                "options": [
                                    "Menerima dengan baik",
                                    "Sebagian menerima",
                                    "Mendustakan dan mengusir",
                                    "Ragu-ragu"
                                ],
                                "correct": 2,
                                "explanation": "Mereka mendustakan Nabi Luth dan bahkan mengancam akan mengusirnya."
                            },
                            {
                                "question": "Siapakah anggota keluarga Nabi Luth yang ikut dibinasakan?",
                                "options": [
                                    "Anaknya",
                                    "Ayahnya",
                                    "Istrinya",
                                    "Paman"
                                ],
                                "correct": 2,
                                "explanation": "Istri Nabi Luth termasuk golongan yang tertinggal dan dibinasakan karena ia mendukung perbuatan kaumnya."
                            },
                            {
                                "question": "Azab apa yang menimpa kaum Sodom?",
                                "options": [
                                    "Banjir bandang",
                                    "Tanah longsor",
                                    "Negeri dibalik dan dihujani batu",
                                    "Angin topan"
                                ],
                                "correct": 2,
                                "explanation": "Negeri mereka dijungkirbalikkan dan dihujani dengan batu dari tanah yang terbakar."
                            }
                        ]
                    }
                ]
            },
            {
                id: "subject-6-7",
                title: "Pokok Bahasan 7: Ibrahim As., Ismail As., dan Ishak As.",
                topics: [
                    {
                        id: 145,
                        title: "Keutamaan Keluarga Ibrahim As.",
                        file: "topic_145.pdf",
                        content: `<h3>KEUTAMAAN KELUARGA</h3>
<h3>IBRAHIM AS</h3>
<div class="quran-quote">
  <h4>Al Mumtahanah : 4-6</h4>
  <div class="verse">
    
    <p class="translation">Sesungguhnya telah ada suri tauladan yang baik bagimu pada Ibrahim dan orang-orang yang bersama dengan dia; ketika mereka berkata kepada kaum mereka: "Sesungguhnya kami berlepas diri daripada kamu dari daripada apa yang kamu sembah selain Allah, kami ingkari (kekafiran)mu dan telah nyata antara kami dan kamu permusuhan dan kebencian buat selama-lamanya sampai kamu beriman kepada Allah saja. Kecuali perkataan Ibrahim kepada bapaknya: "Sesungguhnya aku akan memohonkan ampunan bagi kamu dan aku tiada dapat menolak sesuatupun dari kamu (siksaan) Allah". (Ibrahim berkata): "Ya Tuhan kami hanya kepada Engkaulah kami bertawakkal dan hanya kepada Engkaulah kami bertaubat dan hanya kepada Engkaulah kami kembali". <span class="verse-num">(4)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">"Ya Tuhan kami, janganlah Engkau jadikan kami (sasaran) fitnah bagi orang-orang kafir. Dan ampunilah kami ya Tuhan kami. Sesungguhnya Engkaulah Yang Maha Perkasa lagi Maha Bijaksana". <span class="verse-num">(5)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya pada mereka itu (Ibrahim dan umatnya) ada teladan yang baik bagimu; (yaitu) bagi orang-orang yang mengharap (pahala) Allah dan (keselamatan pada) Hari Kemudian. Dan barangsiapa yang berpaling, maka sesungguhnya Allah Dialah yang Maha kaya lagi Maha Terpuji. <span class="verse-num">(6)</span></p>
  </div>
</div>
<p>Sungguh telah  ada  teladan  yang  baik  bagimu  pada  Ibrahim  dan  orang-</p>
<p>orang  yang  bersamanya; ketika  mereka  berkata  kepada  kaum  mereka:</p>
<p>“Sesungguhnya  kami  berlepas  diri  dari  kamu  dan dari  apa  yang  kamu</p>
<p>ibadahi  selain  Allah,  kami  ingkari  (kekafiran)-mu  dan  telah  nyata  antara</p>
<p>kami  dan  kamu  permusuhan  dan  kebencian  untuk  selamanya  sampai</p>
<p>kamu  beriman  kepada  Allah  saja.  Kecuali  perkataan  Ibrahim  kepada</p>
<p>bapaknya 66 : “Sesungguhnya  aku  akan  memohonkan  ampun  bagimu  dan</p>
<p class="footnote"><em>66) Nabi Ibrahim pernah memintakan ampunan bagi bapakn ya yang musyrik kepada</em></p>
<p>Allah: ini tidak boleh ditiru, karena Allah tidak me mbenarkan orang mukmin memintakan</p>
<p>ampun untuk orang-orang kafir (Lihat surat An Nisa ayat 48).</p>
<p>Keluarga Ibrahim As. sebagai Uswah Hasanah</p>
<p>aku  tidak dapat  menolak  sesuatupun  bagimu dari  (siksa) Allah.”  (Ibrahim</p>
<p>berkata):  "Ya  Tuhan  kami  hanya  kepada  Engkau  kami  bertawakkal  dan</p>
<p>hanya  kepada  Engkau  kami  bertaubat  dan  hanya  kepada  Engkau  kami</p>
<p>kembali."{ 4}</p>
<p>"Ya  Tuhan  kami,  janganlah  Engkau  jadikan  kami  (sasaran)  fitnah  bagi</p>
<p>orang-orang  kafir.  Dan  ampunilah  kami  Ya  Tuhan  kami.  Sesungguhnya</p>
<p>Engkau-lah  Yang  Maha  Perkasa  lagi  Maha  Bijaksana.”{ 5}</p>
<p>Sesungguhnya  pada  mereka  itu  (Ibrahim  dan  umatnya)  ada  teladan  yang</p>
<p>baik  bagimu;  (yaitu)  bagi  orang-orang  yang  mengharap  (pahala)  Allah</p>
<p>dan  (keselamatan  pada)  hari  Akhir. Dan  siapa  yang  berpaling,  maka</p>
<p>sesungguhnya  Allahlah  Yang  Maha  Kaya  lagi  Maha  Terpuji.{ 6}</p>
<div class="quran-quote">
  <h4>Al  Baqarah : 130-131</h4>
  <div class="verse">
    
    <p class="translation">Dan tidak ada yang benci kepada agama Ibrahim, melainkan orang yang memperbodoh dirinya sendiri, dan sungguh Kami telah memilihnya di dunia dan sesungguhnya dia di akhirat benar-benar termasuk orang-orang yang saleh. <span class="verse-num">(130)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ketika Tuhannya berfirman kepadanya: "Tunduk patuhlah!" Ibrahim menjawab: "Aku tunduk patuh kepada Tuhan semesta alam". <span class="verse-num">(131)</span></p>
  </div>
</div>
<p>Dan  tidak  ada  yang  benci  kepada  agama  Ibrahim,  melainkan  orang  yang</p>
<p>memperbodoh  dirinya  sendiri,  dan  sungguh  Kami  telah  memilihnya 67  di</p>
<p>dunia  dan  sesungguhnya  dia  di  akhirat  benar-benar  termasuk  orang-</p>
<p>orang  yang  saleh.{ 130 }</p>
<p>Ketika  Tuhannya  berfirman  kepadanya:  "Tunduk  patuhlah!"  Ibrahim</p>
<p>menjawab:  "Aku  tunduk  patuh  kepada  Tuhan  semesta  alam.”{ 131 }</p>
<p>◙ Ali  ‘Imraan  [3]:  67</p>
<p class="footnote"><em>67) Di antaranya menjadi; imam, rasul, banyak keturunan nya yang menjadi nabi, dan</em></p>
<p>diberi gelar  Khalilullah  (Kekasih Allah).</p>
<h3>Sifat-Sifat Ibrahim As.</h3>
<p>Ibrahim  bukan  seorang  Yahudi  dan  bukan  (pula)  seorang  Nasrani,  akan</p>
<p>tetapi  ia  adalah  seorang  yang hanif  (lurus)68  lagi  berserah  diri  dan  sekali-</p>
<p>kali  bukanlah  ia  termasuk  golongan  orang-orang  musyrik.{ 67 }</p>
<p>◙ Ali  ‘Imraan  [3]:  95</p>
<p>Katakanlah:  "Benarlah  (firman) Allah".  Maka  ikutilah  agama  Ibrahim  yang</p>
<p>lurus,  dan  bukanlah  ia  termasuk  orang-orang  yang  musyrik.{ 95 }</p>
<div class="quran-quote">
  <h4>An  Nahl : 120-123</h4>
  <div class="verse">
    
    <p class="translation">Sesungguhnya Ibrahim adalah seorang imam yang dapat dijadikan teladan lagi patuh kepada Allah dan hanif. Dan sekali-kali bukanlah dia termasuk orang-orang yang mempersekutukan (Tuhan), <span class="verse-num">(120)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">(lagi) yang mensyukuri nikmat-nikmat Allah. Allah telah memilihnya dan menunjukinya kepada jalan yang lurus. <span class="verse-num">(121)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan Kami berikan kepadanya kebaikan di dunia. Dan sesungguhnya dia di akhirat benar-benar termasuk orang-orang yang saleh. <span class="verse-num">(122)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kemudian Kami wahyukan kepadamu (Muhammad): "Ikutilah agama Ibrahim seorang yang hanif" dan bukanlah dia termasuk orang-orang yang mempersekutukan Tuhan. <span class="verse-num">(123)</span></p>
  </div>
</div>
<p>Sesungguhnya  Ibrahim  adalah  seorang  imam  yang  dapat  dijadikan</p>
<p class="footnote"><em>68) Hanif  (lurus) maksudnya: seorang yang selalu berpegang kepad a kebenaran dan</em></p>
<p>tidak pernah meninggalkannya, jauh dari syirik dan jauh dari kesesatan.</p>
<p>teladan  lagi  patuh  kepada  Allah  dan  hanif.  Dan  sekali-kali  bukanlah  dia</p>
<p>termasuk  orang-orang  yang  mempersekutukan  (Tuhan),{120 }</p>
<p>(Lagi)  yang  mensyukuri  nikmat-nikmat  Allah.  Allah  telah  memilihnya  dan</p>
<p>menunjukinya  kepada  jalan  yang  lurus.{121 }</p>
<p>Dan  Kami  berikan  kepadanya  kebaikan  di  dunia.  Dan  sesungguhnya  dia</p>
<p>di  akhirat  benar-benar  termasuk  orang-orang  yang  saleh.{122 }</p>
<p>Lalu  Kami  wahyukan  kepadamu  (Muhammad):  "Ikutilah  agama  Ibrahim</p>
<p>seorang  yang  hanif," dan  ia bukan  termasuk  orang-orang  musyrik.{123 }</p>
<p>◙ Lihat juga: Maryam [19]: 41</p>
<div class="quran-quote">
  <h4>Al An’aam : 84-90</h4>
  <div class="verse">
    
    <p class="translation">Dan Kami telah menganugerahkan Ishak dan Ya'qub kepadanya. Kepada keduanya masing-masing telah Kami beri petunjuk; dan kepada Nuh sebelum itu (juga) telah Kami beri petunjuk, dan kepada sebahagian dari keturunannya (Nuh) yaitu Daud, Sulaiman, Ayyub, Yusuf, Musa dan Harun. Demikianlah Kami memberi balasan kepada orang-orang yang berbuat baik. <span class="verse-num">(84)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan Zakaria, Yahya, Isa dan Ilyas. Semuanya termasuk orang-orang yang shaleh. <span class="verse-num">(85)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan Ismail, Alyasa', Yunus dan Luth. Masing-masing Kami lebihkan derajatnya di atas umat (di masanya), <span class="verse-num">(86)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan Kami lebihkan (pula) derajat sebahagian dari bapak-bapak mereka, keturunan dan saudara-saudara mereka. Dan Kami telah memilih mereka (untuk menjadi nabi-nabi dan rasul-rasul) dan Kami menunjuki mereka ke jalan yang lurus. <span class="verse-num">(87)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Itulah petunjuk Allah, yang dengannya Dia memberi petunjuk kepada siapa yang dikehendaki-Nya di antara hamba-hamba-Nya. Seandainya mereka mempersekutukan Allah, niscaya lenyaplah dari mereka amalan yang telah mereka kerjakan. <span class="verse-num">(88)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Mereka itulah orang-orang yang telah Kami berikan kitab, hikmat dan kenabian Jika orang-orang (Quraisy) itu mengingkarinya, maka sesungguhnya Kami akan menyerahkannya kepada kaum yang sekali-kali tidak akan mengingkarinya. <span class="verse-num">(89)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Mereka itulah orang-orang yang telah diberi petunjuk oleh Allah, maka ikutilah petunjuk mereka. Katakanlah: "Aku tidak meminta upah kepadamu dalam menyampaikan (Al-Quran)". Al-Quran itu tidak lain hanyalah peringatan untuk seluruh ummat. <span class="verse-num">(90)</span></p>
  </div>
</div>
<p>Ibrahim As. sebagai Bapak Para Nabi (Abu al Anbiya)</p>
<p>Dan  Kami  telah  menganugerahkan  Ishak  dan  Yaqub  kepadanya.  Kepada</p>
<p>tiap-tiap  keduanya  telah  Kami  beri  petunjuk;  dan  kepada  Nuh  sebelum  itu</p>
<p>telah  Kami  beri  petunjuk,  dan  kepada  sebagian  dari  keturunannya, yaitu</p>
<p>Daud,  Sulaiman,  Ayyub,  Yusuf,  Musa, dan  Harun.  Demikian  Kami</p>
<p>membalas  orang-orang  yang  berbuat  baik.{ 84 }</p>
<p>Dan  Zakaria,  Yahya,  Isa, dan  Ilyas.  Semuanya  termasuk  orang-orang</p>
<p>yang  shaleh.{ 85 }</p>
<p>Dan  Ismail,  Ilyasa',  Yunus, dan  Luth.  Masing-masing  Kami  lebihkan</p>
<p>derajatnya  di  atas  umat  (di  masanya),{ 86 }</p>
<p>Dan  Kami  lebihkan  (pula)  derajat  sebagian  dari  bapak-bapak  mereka,</p>
<p>keturunan  dan  saudara-saudara  mereka.  Dan  Kami  telah  memilih  mereka</p>
<p>(untuk  menjadi  nabi dan  rasul) dan  Kami  menunjuki  mereka  ke  jalan  yang</p>
<p>lurus.{ 87 }</p>
<p>Itulah  petunjuk  Allah,  yang  dengannya  Dia  memberi  petunjuk  kepada</p>
<p>siapa  yang  Dia kehendaki  di  antara  hamba-hamba-Nya.  Seandainya</p>
<p>mereka  mempersekutukan  Allah,  niscaya  lenyaplah  dari  mereka  amalan</p>
<p>yang  telah  mereka  kerjakan.{ 88 }</p>
<p>Itulah mereka  yang  telah  Kami  beri  kitab,  hikmah,  dan  kenabian, jika</p>
<p>orang-orang  (Quraisy)  itu  mengingkarinya,  maka  sungguh Kami  akan</p>
<p>menyerahkannya  kepada  kaum  yang  tidak  akan  mengingkarinya.{ 89 }</p>
<p>Mereka  itulah  orang-orang  yang  telah  diberi  petunjuk  oleh  Allah, maka</p>
<p>ikutilah  petunjuk  mereka.  Katakanlah:  "Aku  tidak  meminta  upah</p>
<p>kepadamu  dalam  menyampaikan  (Alquran)."  Alquran  itu  tidak  lain</p>
<p>hanyalah  peringatan  untuk  seluruh  ummat.{ 90 }</p>
<div class="quran-quote">
  <h4>Al An’aam : 125-125</h4>
  <div class="verse">
    
    <p class="translation">Dan siapakah yang lebih baik agamanya dari pada orang yang ikhlas menyerahkan dirinya kepada Allah, sedang diapun mengerjakan kebaikan, dan ia mengikuti agama Ibrahim yang lurus? Dan Allah mengambil Ibrahim menjadi kesayangan-Nya. <span class="verse-num">(125)</span></p>
  </div>
</div>
<p>Dan siapa yang lebih baik agamanya daripada orang y ang ikhlas</p>
<p>menyerahkan dirinya kepada Allah, sedang diapun men gerjakan</p>
<p>kebaikan, dan ia mengikuti agama Ibrahim yang lurus ? dan Allah</p>
<p>mengambil Ibrahim menjadi kesayangan-Nya.{ 125 }</p>
<p>Ibrahim As. sebagai Khalilullah (Kekasih Allah)</p>
`,
                        quiz: [
                            { "question": "Apa gelar yang diberikan Allah kepada Nabi Ibrahim As?", "options": ["Khalilullah", "Habibullah", "Kalimullah", "Ruhullah"], "answer": 0 },
                            { "question": "Apa arti dari 'Hanif' yang disematkan pada Nabi Ibrahim?", "options": ["Lurus/Bertauhid", "Sabar", "Kuat", "Penyayang"], "answer": 0 },
                            { "question": "Surat apa yang menceritakan doa Nabi Ibrahim memohon anak yang shaleh?", "options": ["Ash-Shaffaat: 100", "Al-Baqarah: 124", "Ibrahim: 35", "Maryam: 41"], "answer": 0 },
                            { "question": "Apa hukum memintakan ampun bagi orang musyrik menurut kisah Ibrahim dan bapaknya?", "options": ["Wajib", "Sunnah", "Mubah", "Dilarang Allah"], "answer": 3 },
                            { "question": "Siapakah anak yang dikabarkan sebagai 'anak yang amat sabar' dalam surat Ash-Shaffaat: 101?", "options": ["Ismail", "Ishaq", "Ya'qub", "Yusuf"], "answer": 0 }
                        ]
                    },
                    {
                        id: 146,
                        title: "Proses Pencarian Kebenaran",
                        file: "topic_146.pdf",
                        content: `<h3>PROSES PENCARIAN</h3>
<h3>KEBENARAN</h3>
<div class="quran-quote">
  <h4>Al  An'aam : 74-79</h4>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah) di waktu Ibrahim berkata kepada bapaknya, Aazar, "Pantaskah kamu menjadikan berhala-berhala sebagai tuhan-tuhan? Sesungguhnya aku melihat kamu dan kaummu dalam kesesatan yang nyata". <span class="verse-num">(74)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan demikianlah Kami perlihatkan kepada Ibrahim tanda-tanda keagungan (Kami yang terdapat) di langit dan bumi dan (Kami memperlihatkannya) agar dia termasuk orang yang yakin. <span class="verse-num">(75)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ketika malam telah gelap, dia melihat sebuah bintang (lalu) dia berkata: "Inilah Tuhanku", tetapi tatkala bintang itu tenggelam dia berkata: "Saya tidak suka kepada yang tenggelam". <span class="verse-num">(76)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kemudian tatkala dia melihat bulan terbit dia berkata: "Inilah Tuhanku". Tetapi setelah bulan itu terbenam, dia berkata: "Sesungguhnya jika Tuhanku tidak memberi petunjuk kepadaku, pastilah aku termasuk orang yang sesat". <span class="verse-num">(77)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kemudian tatkala ia melihat matahari terbit, dia berkata: "Inilah Tuhanku, ini yang lebih besar". Maka tatkala matahari itu terbenam, dia berkata: "Hai kaumku, sesungguhnya aku berlepas diri dari apa yang kamu persekutukan. <span class="verse-num">(78)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya aku menghadapkan diriku kepada Rabb yang menciptakan langit dan bumi, dengan cenderung kepada agama yang benar, dan aku bukanlah termasuk orang-orang yang mempersekutukan Tuhan. <span class="verse-num">(79)</span></p>
  </div>
</div>
<p>Dan  (ingatlah)  ketika  Ibrahim  berkata kepada  bapaknya,  Azar,69</p>
<p>"Patutkah  kamu  menjadikan  berhala-berhala  sebagai  tuhan-tuhan?</p>
<p class="footnote"><em>69) Di antara ahli tafsir ada yang berpendapat bahwa y ang dimaksud dengan Abiihi</em></p>
<p>(bapaknya) ialah pamannya.</p>
<p>Ibrahim As. dan Alam</p>
<p>sesungguhnya  aku  melihat  kamu  dan  kaummu  dalam  kesesatan  yang</p>
<p>nyata."{ 74 }</p>
<p>Dan  demikianlah  Kami  perlihatkan  kepada  Ibrahim  tanda-tanda</p>
<p>keagungan  di  langit  dan  bumi  dan  (Kami  memperlihatkannya)  agar  dia</p>
<p>termasuk  orang  yang  yakin.{ 75 }</p>
<p>Ketika  malam  telah  gelap,  dia  melihat  sebuah  bintang  (lalu)  dia  berkata:</p>
<p>"Inilah  Tuhanku",  tetapi  tatkala  bintang  itu  tenggelam  dia  berkata:  "Aku</p>
<p>tidak  suka  kepada  yang  tenggelam."{ 76 }</p>
<p>Kemudian  tatkala  dia  melihat  bulan  terbit  dia  berkata:  "Inilah  Tuhanku.”</p>
<p>tetapi  setelah  bulan  itu  terbenam,  dia  berkata:  “Sesungguhnya  jika</p>
<p>Tuhanku  tidak  memberi  petunjuk  kepadaku,  pastilah  aku  termasuk  orang</p>
<p>yang  sesat."{ 77 }</p>
<p>Lalu  ketika  ia  melihat  matahari  terbit,  ia  berkata:  "Inilah  Tuhanku,  ini  lebih</p>
<p>besar.”  Maka  ketika  matahari  terbenam,  ia  berkata:  "Hai  kaumku,</p>
<p>sesungguhnya  aku  berlepas  diri  dari  apa  yang  kamu  sekutukan.{78 }</p>
<p>Sesungguhnya  aku  menghadapkan  diriku  kepada  Tuhan  yang</p>
<p>menciptakan  langit  dan  bumi,  dengan  cenderung  kepada  agama  yang</p>
<p>benar,  dan  aku  bukanlah  termasuk  orang-orang  musyrik. { 79 }</p>
<div class="quran-quote">
  <h4>Al  Baqarah : 260-260</h4>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah) ketika Ibrahim berkata: "Ya Tuhanku, perlihatkanlah kepadaku bagaimana Engkau menghidupkan orang-orang mati". Allah berfirman: "Belum yakinkah kamu?" Ibrahim menjawab: "Aku telah meyakinkannya, akan tetapi agar hatiku tetap mantap (dengan imanku) Allah berfirman: "(Kalau demikian) ambillah empat ekor burung, lalu cincanglah semuanya olehmu. (Allah berfirman): "Lalu letakkan diatas tiap-tiap satu bukit satu bagian dari bagian-bagian itu, kemudian panggillah mereka, niscaya mereka datang kepadamu dengan segera". Dan ketahuilah bahwa Allah Maha Perkasa lagi Maha Bijaksana. <span class="verse-num">(260)</span></p>
  </div>
</div>
<p>Ibrahim As. dan Burung</p>
<p>Dan  (ingatlah)  ketika  Ibrahim  berkata:  "Ya  Tuhanku,  perlihatkanlah</p>
<p>kepadaku  bagaimana  Engkau  menghidupkan  orang-orang  mati."  Allah</p>
<p>berfirman:  "Belum  yakinkah  kamu?"  Ibrahim  menjawab:  "Aku  telah</p>
<p>meyakininya,  tetapi  agar  hatiku  tetap  mantap. Allah  berfirman:  "(Kalau</p>
<p>demikian)  ambillah  empat  ekor  burung,  lalu  cincanglah 70  semuanya</p>
<p>olehmu.  (Allah  berfirman):  "Lalu  letakkan  di atas  tiap-tiap  satu  bukit  satu</p>
<p>bagian  dari  bagian-bagian  itu,  kemudian  panggillah  mereka,  niscaya</p>
<p>mereka  datang  kepadamu  dengan  segera.”  Dan  ketahuilah  bahwa  Allah</p>
<p>Maha  Perkasa  lagi  Maha  Bijaksana.{ 260 }</p>
<p class="footnote"><em>70) Pendapat di atas adalah menurut At-Thabari dan Ibnu  Katsir, sedang menurut Abu</em></p>
<p>Muslim Al Ashfahani pengertian ayat ini bahwa Allah menjelasankan kepada Ibrahim</p>
<p>tentang cara Dia menghidupkan yang mati. Disuruh-Nya Ibrahim mengambil 4 ekor</p>
<p>burung, lalu memeliharanya dan menjinakkannya hingga burung itu dapat datang</p>
<p>seketika, jika dipanggil. Kemudian, burung-burung yan g sudah pandai itu, diletakkan di</p>
<p>atas tiap bukit seekor, lalu burung-burung itu dipanggi l dengan satu tepukan/seruan,</p>
<p>niscaya burung-burung itu akan datang dengan segera, walaupun tempatnya terpisah-</p>
<p>pisah dan berjauhan. Maka demikian pula Allah mengh idupkan orang mati yang</p>
<p>tersebar di mana-mana, dengan satu kalimat cipta “hid uplah kamu semua” pastilah</p>
<p>mereka hidup kembali. Jadi menurut Abu Muslim “ sighat amr ” (bentuk kata perintah)</p>
<p>dalam ayat ini, pengertiannya khabar  (bentuk berita) sebagai cara penjelasan. Pendapat</p>
<p>beliau ini dianut pula oleh Ar Razy dan Rasyid Ridha.</p>
`,
                        quiz: [
                            { "question": "Apa yang pertama kali dikira Tuhan oleh Ibrahim saat mencari kebenaran?", "options": ["Bintang", "Bulan", "Matahari", "Api"], "answer": 0 },
                            { "question": "Siapakah raja yang mendebat Nabi Ibrahim tentang Tuhan?", "options": ["Namrud", "Firaun", "Abrahah", "Qarun"], "answer": 0 },
                            { "question": "Mengapa Nabi Ibrahim tidak menyukai bintang, bulan, dan matahari sebagai Tuhan?", "options": ["Karena mereka kecil", "Karena mereka terbenam/hilang", "Karena mereka panas", "Karena mereka jauh"], "answer": 1 },
                            { "question": "Bagaimana cara Allah meyakinkan Nabi Ibrahim tentang menghidupkan orang mati (Al-Baqarah: 260)?", "options": ["Menghidupkan manusia", "Mencincang 4 burung dan memanggilnya", "Menumbuhkan tanaman", "Menerbitkan matahari dari barat"], "answer": 1 },
                            { "question": "Apa jawaban Nabi Ibrahim ketika melihat matahari terbit?", "options": ["Ini Tuhanku, ini yang lebih besar", "Ini terlalu panas", "Ini ciptaan Tuhan", "Ini cahaya abadi"], "answer": 0 }
                        ]
                    },
                    {
                        id: 147,
                        title: "Dakwah Ibrahim As.",
                        file: "topic_147.pdf",
                        content: `<h3>DAKWAH IBRAHIM AS</h3>
<div class="quran-quote">
  <h4>Maryam : 41-47</h4>
  <div class="verse">
    
    <p class="translation">Ceritakanlah (Hai Muhammad) kisah Ibrahim di dalam Al Kitab (Al Quran) ini. Sesungguhnya ia adalah seorang yang sangat membenarkan lagi seorang Nabi. <span class="verse-num">(41)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ingatlah ketika ia berkata kepada bapaknya; "Wahai bapakku, mengapa kamu menyembah sesuatu yang tidak mendengar, tidak melihat dan tidak dapat menolong kamu sedikitpun? <span class="verse-num">(42)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Wahai bapakku, sesungguhnya telah datang kepadaku sebahagian ilmu pengetahuan yang tidak datang kepadamu, maka ikutilah aku, niscaya aku akan menunjukkan kepadamu jalan yang lurus. <span class="verse-num">(43)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Wahai bapakku, janganlah kamu menyembah syaitan. Sesungguhnya syaitan itu durhaka kepada Tuhan Yang Maha Pemurah. <span class="verse-num">(44)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Wahai bapakku, sesungguhnya aku khawatir bahwa kamu akan ditimpa azab dari Tuhan Yang Maha Pemurah, maka kamu menjadi kawan bagi syaitan". <span class="verse-num">(45)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Berkata bapaknya: "Bencikah kamu kepada tuhan-tuhanku, hai Ibrahim? Jika kamu tidak berhenti, maka niscaya kamu akan kurajam, dan tinggalkanlah aku buat waktu yang lama". <span class="verse-num">(46)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Berkata Ibrahim: "Semoga keselamatan dilimpahkan kepadamu, aku akan memintakan ampun bagimu kepada Tuhanku. Sesungguhnya Dia sangat baik kepadaku. <span class="verse-num">(47)</span></p>
  </div>
</div>
<p>Ceritakanlah  (Muhammad)  kisah  Ibrahim  di  dalam  Alkitab  (Alquran)  ini.</p>
<p>Sesungguhnya  ia  seorang  yang  sangat  membenarkan 71  lagi  seorang</p>
<p>nabi.{ 41 }</p>
<p>Ingatlah  ketika  ia  berkata  kepada  bapaknya;  "Wahai  bapakku,  mengapa</p>
<p>kamu  mengabdi kepada  sesuatu  yang  tidak  mendengar,  tidak  melihat,</p>
<p>dan  tidak  dapat  menolongmu  sedikitpun?{ 42 }</p>
<p>Wahai  bapakku,  sesungguhnya  telah  datang  kepadaku  sebagian  ilmu</p>
<p>pengetahuan  yang  tidak  datang  kepadamu,  maka  ikutilah  aku,  niscaya</p>
<p class="footnote"><em>71) Maksudnya: Ibrahim As. adalah seorang nabi yang am at cepat membenarkan</em></p>
<p>semua hal yang ghaib yang datang dari Allah.</p>
<p>Dakwah Ibrahim As. kepada Ayahnya</p>
<p>aku  akan  menunjukkan  kepadamu  jalan  yang  lurus.{ 43 }</p>
<p>Wahai  bapakku,  janganlah  kamu  menyembah  setan.  Sesungguhnya</p>
<p>setan  itu  durhaka  kepada  Tuhan  Yang  Maha  Pemurah.{ 44 }</p>
<p>Wahai  bapakku,  sesungguhnya  aku  khawatir  bahwa  kamu  akan  ditimpa</p>
<p>azab  dari  Yang  Maha  Pemurah,  lalu  kamu  menjadi  kawan  bagi  setan.”{ 45 }</p>
<p>Berkata  bapaknya:  "Bencikah  kamu  kepada  Tuhan-tuhanku,  hai</p>
<p>Ibrahim?, jika  kamu  tidak  berhenti,  niscaya  kamu  akan  kurajam,  dan</p>
<p>tinggalkanlah  aku  buat  waktu  yang  lama.”{ 46 }</p>
<p>Berkata  Ibrahim:  "Semoga  keselamatan  dilimpahkan  kepadamu,  aku</p>
<p>akan  memintakan  ampun  bagimu  kepada  Tuhanku.  Sesungguhnya  Dia</p>
<p>sangat  baik  kepadaku.{ 47 }</p>
<div class="quran-quote">
  <h4>Al  Baqarah : 258-258</h4>
  <div class="verse">
    
    <p class="translation">Apakah kamu tidak memperhatikan orang yang mendebat Ibrahim tentang Tuhannya (Allah) karena Allah telah memberikan kepada orang itu pemerintahan (kekuasaan). Ketika Ibrahim mengatakan: "Tuhanku ialah Yang menghidupkan dan mematikan," orang itu berkata: "Saya dapat menghidupkan dan mematikan". Ibrahim berkata: "Sesungguhnya Allah menerbitkan matahari dari timur, maka terbitkanlah dia dari barat," lalu terdiamlah orang kafir itu; dan Allah tidak memberi petunjuk kepada orang-orang yang zalim. <span class="verse-num">(258)</span></p>
  </div>
</div>
<p>Tidakkah  kamu  perhatikan  orang 72  yang  mendebat  Ibrahim  tentang</p>
<p>Tuhannya, karena  Dia telah  memberinya  pemerintahan  (kekuasaan).</p>
<p>Ketika  Ibrahim  berkata:  "Tuhanku  yang  menghidupkan  dan  memati-kan,"</p>
<p>orang  itu  berkata:  "Aku 73  dapat  menghidupkan  dan  mematikan.”  Ibrahim</p>
<p class="footnote"><em>72) Yaitu Namrudz dari Babilonia.</em></p>
<p class="footnote"><em>73) Yang dimaksud raja Namrudz dengan menghidupkan  ialah membiarkan hidup, dan</em></p>
<p>yang dimaksudnya dengan mematikan  ialah membunuh. Perkataan itu untuk mengejek</p>
<h3>nabi Ibrahim As.</h3>
<p>Perdebatan Ibrahim As. dengan Raja Namrud</p>
<p>berkata:  “Sesungguhnya  Allah  menerbitkan  matahari  dari  Timur,  maka</p>
<p>terbitkanlah  ia  dari  Barat,"  lalu  terdiamlah  orang  kafir  itu;  dan  Allah  tidak</p>
<p>memberi  petunjuk  kepada  orang-orang  zalim.{ 258 }</p>
<p>◙ Al  Anbiyaa\`  [21]:  51  – 56</p>
<p>Dan  sungguh telah  Kami  anugerahkan  kepada  Ibrahim  hidayah</p>
<p>kebenaran  sebelum  (Musa  dan  Harun),  dan  Kami  mengetahuinya{51 }</p>
<p>(Ingatlah),  ketika  Ibrahim  berkata  kepada  bapaknya  dan  kaumnya:</p>
<p>"Patung-patung  apakah  ini  yang  kamu  tekun  menyembahnya?"{ 52 }</p>
<p>Mereka  menjawab:  "Telah kami  mendapati  bapak-bapak  kami  mengabdi</p>
<p>kepadanya.”{ 53 }</p>
<p>Ibrahim  berkata:  “Sesungguhnya  kamu  dan  bapak-bapakmu  berada</p>
<p>dalam  kesesatan  yang  nyata.”{ 54 }</p>
<p>Mereka  menjawab:  “Apakah  kamu  datang  kepada  kami  dengan</p>
<p>kebenaran  ataukah  kamu  termasuk  yang  bermain-main?"{ 55 }</p>
<p>Dakwah Ibrahim As. kepada Kaumnya</p>
<p>Ibrahim  berkata:  "Sebenarnya  Tuhan  kamu  ialah  Tuhan  langit  dan  bumi</p>
<p>yang  telah  menciptakannya;  dan  aku  termasuk  orang-orang  yang  dapat</p>
<p>memberikan  bukti  atas  yang  demikian  itu.”{ 56 }</p>
<div class="quran-quote">
  <h4>Al An’aam : 80-83</h4>
  <div class="verse">
    
    <p class="translation">Dan dia dibantah oleh kaumnya. Dia berkata: "Apakah kamu hendak membantah tentang Allah, padahal sesungguhnya Allah telah memberi petunjuk kepadaku". Dan aku tidak takut kepada (malapetaka dari) sembahan-sembahan yang kamu persekutukan dengan Allah, kecuali di kala Tuhanku menghendaki sesuatu (dari malapetaka) itu. Pengetahuan Tuhanku meliputi segala sesuatu. Maka apakah kamu tidak dapat mengambil pelajaran (daripadanya)?" <span class="verse-num">(80)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Bagaimana aku takut kepada sembahan-sembahan yang kamu persekutukan (dengan Allah), padahal kamu tidak mempersekutukan Allah dengan sembahan-sembahan yang Allah sendiri tidak menurunkan hujjah kepadamu untuk mempersekutukan-Nya. Maka manakah di antara dua golongan itu yang lebih berhak memperoleh keamanan (dari malapetaka), jika kamu mengetahui? <span class="verse-num">(81)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Orang-orang yang beriman dan tidak mencampuradukkan iman mereka dengan kezaliman (syirik), mereka itulah yang mendapat keamanan dan mereka itu adalah orang-orang yang mendapat petunjuk. <span class="verse-num">(82)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan itulah hujjah Kami yang Kami berikan kepada Ibrahim untuk menghadapi kaumnya. Kami tinggikan siapa yang Kami kehendaki beberapa derajat. Sesungguhnya Tuhanmu Maha Bijaksana lagi Maha Mengetahui. <span class="verse-num">(83)</span></p>
  </div>
</div>
<p>Dan  ia  dibantah  oleh  kaumnya.  Ia berkata:  "Akankah  kamu  membantah</p>
<p>tentang  Allah, sungguh  Allah  telah  memberi  petunjuk  kepadaku".  Dan  aku</p>
<p>tidak  takut  kepada  (malapetaka  dari)  sembahan  yang  kamu  persekutukan</p>
<p>dengan  Allah,  kecuali  jika  Tuhanku  menghendaki  sesuatu  (malapetaka)</p>
<p>itu.  Pengetahuan  Tuhanku  meliputi  segala  sesuatu.  Maka  tidakkah  kamu</p>
<p>mengambil  pelajaran?"{ 80 }</p>
<p>Bagaimana  aku  takut  kepada  sembahan  yang  kamu  persekutukan,</p>
<p>padahal kamu tidak  takut mempersekutukan  Allah  dengan  sembahan-</p>
<p>sembahan, yang  Allah  sendiri  tidak  menurunkan  hujjah  padamu  untuk  hal</p>
<p>itu. Maka  manakah  di  antara  dua  golongan  itu  yang  lebih  berhak</p>
<p>memperoleh  keamanan,  jika  kamu  mengetahui? 74 {81 }</p>
<p>Orang-orang  yang  beriman  dan  tidak  mencampuradukkan  iman  mereka</p>
<p>dengan  kezaliman  (syirik),  mereka  itulah  yang  mendapat  keamanan  dan</p>
<p>mereka  itulah  yang  mendapat  petunjuk.{ 82 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 83-90</h4>
  <div class="verse">
    
    <p class="translation">Dan sesungguhnya Ibrahim benar-benar termasuk golongannya (Nuh). <span class="verse-num">(83)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">(lngatlah) ketika ia datang kepada Tuhannya dengan hati yang suci: <span class="verse-num">(84)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">(Ingatlah) ketika ia berkata kepada bapaknya dan kaumnya: "Apakah yang kamu sembah itu? <span class="verse-num">(85)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Apakah kamu menghendaki sembahan-sembahan selain Allah dengan jalan berbohong? <span class="verse-num">(86)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Maka apakah anggapanmu terhadap Tuhan semesta alam?" <span class="verse-num">(87)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Lalu ia memandang sekali pandang ke bintang-bintang. <span class="verse-num">(88)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kemudian ia berkata: "Sesungguhnya aku sakit". <span class="verse-num">(89)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Lalu mereka berpaling daripadanya dengan membelakang. <span class="verse-num">(90)</span></p>
  </div>
</div>
<p>Dan  sesungguhnya  termasuk  golongannya  (Nuh) ialah Ibrahim  75 .{ 83 }</p>
<p>(lngatlah)  ketika  ia  datang  kepada  Tuhannya  dengan  hati  suci:{ 84 }</p>
<p>(Ingatlah)  ketika  ia  berkata  kepada  bapaknya  dan  kaumnya:  “Apakah</p>
<p>yang  kamu  sembah  itu  ?{ 85 }</p>
<p>Apakah  kamu  menghendaki  sembahan-sembahan  selain  Allah  dengan</p>
<p>jalan  berbohong?{ 86 }</p>
<p>Maka  apakah  anggapanmu  terhadap  Tuhan  semesta  alam?"{ 87 }</p>
<p>Lalu  ia  memandang  sekali  pandang  ke  bintang-bintang.{ 88 }</p>
<p>Kemudian  ia  berkata:  “Sesungguhnya  aku  sakit.”{ 89 }</p>
<p>Lalu  mereka  berpaling  daripadanya  dengan  membelakang.{ 90 }</p>
<div class="quran-quote">
  <h4>Asy  Syu'araa' : 69-82</h4>
  <div class="verse">
    
    <p class="translation">Dan bacakanlah kepada mereka kisah Ibrahim. <span class="verse-num">(69)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ketika ia berkata kepada bapaknya dan kaumnya: "Apakah yang kamu sembah?" <span class="verse-num">(70)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Mereka menjawab: "Kami menyembah berhala-berhala dan kami senantiasa tekun menyembahnya". <span class="verse-num">(71)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Berkata Ibrahim: "Apakah berhala-berhala itu mendengar (doa)mu sewaktu kamu berdoa (kepadanya)?, <span class="verse-num">(72)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">atau (dapatkah) mereka memberi manfaat kepadamu atau memberi mudharat?" <span class="verse-num">(73)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Mereka menjawab: "(Bukan karena itu) sebenarnya kami mendapati nenek moyang kami berbuat demikian". <span class="verse-num">(74)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ibrahim berkata: "Maka apakah kamu telah memperhatikan apa yang selalu kamu sembah, <span class="verse-num">(75)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">kamu dan nenek moyang kamu yang dahulu?, <span class="verse-num">(76)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">karena sesungguhnya apa yang kamu sembah itu adalah musuhku, kecuali Tuhan Semesta Alam, <span class="verse-num">(77)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">(yaitu Tuhan) Yang telah menciptakan aku, maka Dialah yang menunjuki aku, <span class="verse-num">(78)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan Tuhanku, Yang Dia memberi makan dan minum kepadaku, <span class="verse-num">(79)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan apabila aku sakit, Dialah Yang menyembuhkan aku, <span class="verse-num">(80)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan Yang akan mematikan aku, kemudian akan menghidupkan aku (kembali), <span class="verse-num">(81)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan Yang amat kuinginkan akan mengampuni kesalahanku pada hari kiamat". <span class="verse-num">(82)</span></p>
  </div>
</div>
<p class="footnote"><em>74) Setelah diperlihatkan kepada Ibrahim tanda-tanda keagungan-Nya dan dengan itu</em></p>
<p>teguhlah imannya kepada Allah (ayat 75), maka Ibrahim,  memimpin kaumnya kepada</p>
<p>tauhid dengan mengikuti alam pikiran mereka untuk kemudian dibantahnya.</p>
<p class="footnote"><em>75) Maksudnya: Ibrahim termasuk golongan Nuh As. dala m keimanan kepada Allah</em></p>
<p>dan pokok-pokok pelajaran agama.</p>
<p>Dan  bacakanlah  kepada  mereka  kisah  Ibrahim.{ 69 }</p>
<p>Ketika  ia  berkata  kepada  bapaknya  dan  kaumnya:  "Kepada apakah  kamu</p>
<p>mengabdi?"{ 70 }</p>
<p>Mereka  menjawab:  "Kami  mengabdi kepada  berhala-berhala  dan  Kami</p>
<p>senantiasa  tekun  mengabdi kepadanya".{ 71 }</p>
<p>Berkata  Ibrahim:  "Apakah  berhala-berhala  itu  mendengar  (doa)-mu</p>
<p>sewaktu  kamu  berdoa  (kepadanya)?,{ 72 }</p>
<p>Atau  (dapatkah)  mereka  memberi  manfaat  kepadamu  atau  memberi</p>
<p>mudharat?"{ 73 }</p>
<p>Mereka  menjawab:  "(Bukan  karena  itu)  sebenarnya  kami  mendapati</p>
<p>nenek  moyang  kami  berbuat  demikian".{ 74 }</p>
<p>Ibrahim  berkata:  "Maka  apakah  kamu  telah  memperhatikan  kepada apa</p>
<p>yang  selalu  kamu  ibadahi,{ 75 }</p>
<p>Kamu  dan  nenek  moyang  kamu  yang  dahulu?,{ 76 }</p>
<p>Karena  sesungguhnya  apa  yang  kamu  ibadahi  itu  adalah  musuhku,</p>
<p>kecuali  Tuhan  semesta  alam,{ 77 }</p>
<p>Yang  telah menciptakanku, maka  Dialah  yang  menunjukiku,{ 78 }</p>
<p>Dan  yang  memberi  makan  dan  minum  kepadaku,{ 79 }</p>
<p>Dan  apabila  aku  sakit,  Dialah  yang  menyembuhkanku,{ 80 }</p>
<p>Dan  yang  akan  mematikanku,  lalu  akan  menghidupkanku  kembali,{ 81 }</p>
<p>Dan  yang  amat  kuinginkan  akan  mengampuni  kesalahanku  pada  hari</p>
<p>kiamat".{ 82 }</p>
<div class="quran-quote">
  <h4>Al  'Ankabuut : 16-23</h4>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah) Ibrahim, ketika ia berkata kepada kaumnya: "Sembahlah olehmu Allah dan bertakwalah kepada-Nya. Yang demikian itu adalah lebih baik bagimu, jika kamu mengetahui. <span class="verse-num">(16)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya apa yang kamu sembah selain Allah itu adalah berhala, dan kamu membuat dusta. Sesungguhnya yang kamu sembah selain Allah itu tidak mampu memberikan rezeki kepadamu; maka mintalah rezeki itu di sisi Allah, dan sembahlah Dia dan bersyukurlah kepada-Nya. Hanya kepada-Nya-lah kamu akan dikembalikan. <span class="verse-num">(17)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan jika kamu (orang kafir) mendustakan, maka umat yang sebelum kamu juga telah mendustakan. Dan kewajiban rasul itu, tidak lain hanyalah menyampaikan (agama Allah) dengan seterang-terangnya". <span class="verse-num">(18)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan apakah mereka tidak memperhatikan bagaimana Allah menciptakan (manusia) dari permulaannya, kemudian mengulanginya (kembali). Sesungguhnya yang demikian itu adalah mudah bagi Allah. <span class="verse-num">(19)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Katakanlah: "Berjalanlah di (muka) bumi, maka perhatikanlah bagaimana Allah menciptakan (manusia) dari permulaannya, kemudian Allah menjadikannya sekali lagi. Sesungguhnya Allah Maha Kuasa atas segala sesuatu. <span class="verse-num">(20)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Allah mengazab siapa yang dikehendaki-Nya, dan memberi rahmat kepada siapa yang dikehendaki-Nya, dan hanya kepada-Nya-lah kamu akan dikembalikan. <span class="verse-num">(21)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan kamu sekali-kali tidak dapat melepaskan diri (dari azab Allah) di bumi dan tidak (pula) di langit dan sekali-kali tiadalah bagimu pelindung dan penolong selain Allah. <span class="verse-num">(22)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan orang-orang yang kafir terhadap ayat-ayat Allah dan pertemuan dengan Dia, mereka putus asa dari rahmat-Ku, dan mereka itu mendapat azab yang pedih. <span class="verse-num">(23)</span></p>
  </div>
</div>
<p>Dan  (ingatlah kisah)  Ibrahim,  ketika  ia  berkata  kepada  kaumnya:</p>
<p>"Hendaklah kamu mengabdi kepada  Allah  dan  bertakwalah  kepada-Nya.</p>
<p>Hal  itu  adalah  lebih  baik  bagimu,  jika  kamu  mengetahui.{ 16 }</p>
<p>Sesungguhnya  apa  yang  kamu  ibadahi  selain  Allah  itu  adalah  berhala,</p>
<p>dan  kamu  membuat  dusta 76 . Sesungguhnya  yang  kamu  ibadahi  selain</p>
<p>Allah  itu  tidak  mampu  memberikan  rezeki  kepadamu;  Maka  mintalah</p>
<p>rezeki  itu  di  sisi  Allah,  dan  mengabdilah kepada-Nya  dan  bersyukurlah</p>
<p>kepada-Nya.  Hanya  kepada-Nya  kamu  akan  dikembalikan.{ 17 }</p>
<p>Dan  jika  kamu  (orang  kafir)  mendustakan, maka  umat  yang  sebelum</p>
<p>kamu  juga  telah  mendustakan.  Dan  kewajiban  Rasul  itu,  tidak  lain</p>
<p>hanyalah  menyampaikan  dengan  seterang-terangnya."{ 18 }</p>
<p>Dan  tidakkah  mereka  memperhatikan  bagaimana  Allah  menciptakan</p>
<p>(manusia)  dari  permulaannya,  kemudian  mengulanginya  (kembali).</p>
<p>Sesungguhnya  yang  demikian  itu  adalah  mudah  bagi  Allah.{ 19 }</p>
<p>Katakan: "Berjalanlah  di  bumi, maka  perhatikan bagaimana  Allah</p>
<p>ciptakan  (manusia)  dari  permulaan, lalu  Allah  menjadikannya  sekali  lagi 77 .</p>
<p>Sesungguhnya  Allah  Maha  Kuasa  atas  segala  sesuatu.{ 20 }</p>
<p class="footnote"><em>76) Maksudnya: mereka menyatakan bahwa berhala-berhala  itu dapat memberi</em></p>
<p>syafaat kepada mereka di sisi Allah dan ini adalah dusta.</p>
<p class="footnote"><em>77) Maksudnya: Allah membangkitkan manusia sesudah m ati kelak di akhirat</em></p>
<p>Allah  mengazab  siapa  yang  dikehendaki-Nya,  dan  memberi  rahmat</p>
<p>kepada  siapa  yang  dikehendaki-Nya,  dan  hanya  kepada-Nya-lah  kamu</p>
<p>akan  dikembalikan.{ 21 }</p>
<p>Dan  kamu  sekali-kali  tidak  dapat  melepaskan  diri  (dari  azab  Allah)  di  bumi</p>
<p>dan  tidak  (pula)  di  langit  dan  sekali-kali  tiadalah  bagimu  pelindung  dan</p>
<p>penolong  selain  Allah.{ 22 }</p>
<p>Dan  orang-orang  yang  kafir  terhadap  ayat-ayat  Allah  dan  pertemuan</p>
<p>dengan  Dia,  mereka  putus  asa  dari  rahmat-Ku,  dan  mereka  itu  mendapat</p>
<p>azab  yang  pedih.{ 23 }</p>
<p>◙ Al  Anbiyaa\`  [21]:  57  – 58</p>
<p>Demi  Allah,  sesungguhnya  aku  akan  melakukan  tipu  daya  terhadap</p>
<p>berhala-berhalamu  sesudah  kamu  pergi  meninggalkannya 78 .{ 57 }</p>
<p>Maka  Ibrahim  membuat  berhala-berhala  itu  hancur  berpotong-potong,</p>
<p>kecuali  yang  terbesar  (induk)  dari  patung-patung  yang  lain;  agar  mereka</p>
<p>kembali  (untuk  bertanya)  kepadanya.{ 58 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 91-93</h4>
  <div class="verse">
    
    <p class="translation">Kemudian ia pergi dengan diam-diam kepada berhala-berhala mereka; lalu ia berkata: "Apakah kamu tidak makan? <span class="verse-num">(91)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kenapa kamu tidak menjawab?" <span class="verse-num">(92)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Lalu dihadapinya berhala-berhala itu sambil memukulnya dengan tangan kanannya (dengan kuat). <span class="verse-num">(93)</span></p>
  </div>
</div>
<p class="footnote"><em>78) Ucapan-ucapan itu diucapkan Ibrahim As. dalam hat inya saja. Maksudnya: nabi</em></p>
<p>Ibrahim As. akan menjalankan tipu dayanya untuk meng hancurkan berhala-berhala</p>
<p>mereka, sesudah mereka meninggalkan tempat-tempat berhala itu.</p>
<p>Ibrahim As. Menghancurkan Patung-patung</p>
<p>Kemudian  ia  pergi  dengan  diam-diam  kepada  berhala-berhala  mereka;</p>
<p>lalu  ia  berkata:  "Mengapa  kamu  tidak  makan 79 ?{ 91 }</p>
<p>Mengapa  kamu  tidak  menjawab?"{ 92 }</p>
<p>Lalu  dihadapinya  berhala-berhala  itu  sambil  memukulnya  dengan  tangan</p>
<p>kanannya  (dengan  kuat).{ 93 }</p>
<p>◙ Al  Anbiyaa\`  [21]:  59  – 67</p>
<p class="footnote"><em>79) Maksud Ibrahim dengan perkataan itu, ialah mengej ek berhala-berhala itu, karena</em></p>
<p>dekat berhala itu banyak diletakkan makanan yang baik sebagai sesajian.</p>
<p>Sikap Kaumnya Setelah Patung-patung Dihancurkan</p>
<p>Mereka  berkata:  "Siapakah  yang  melakukan  ini  terhadap  Tuhan-tuhan</p>
<p>kami,  sesungguhnya  dia  termasuk  orang-orang  yang  zalim."{ 59 }</p>
<p>Mereka  berkata:  "Kami  dengar  ada  seorang  pemuda  yang  mencela</p>
<p>berhala-berhala  ini  yang  bernama  Ibrahim.”{ 60 }</p>
<p>Mereka  berkata:  "(Kalau  demikian)  bawalah  dia  dengan  cara  yang  dapat</p>
<p>dilihat  orang  banyak,  agar  mereka  menyaksikan.”{ 61 }</p>
<p>Mereka  bertanya:  “Kamukah  yang  melakukan  ini  terhadap  Tuhan-tuhan</p>
<p>kami,  hai  Ibrahim?"{ 62 }</p>
<p>Ibrahim  menjawab:  "Sebenarnya  patung  yang  besar  itulah  yang</p>
<p>melakukannya,  maka  tanyakanlah  kepada  berhala  itu,  jika  mereka  dapat</p>
<p>berbicara.”{ 63 }</p>
<p>Maka  mereka  telah  kembali  kepada  kesadaran  dan  lalu  berkata:</p>
<p>“Sesungguhnya  kalianlah yang  menganiaya  (diri  sendiri)",{ 64 }</p>
<p>Lalu  kepala  mereka  tertunduk 80  (dan  berkata):  “Sungguh kamu  telah</p>
<p>mengetahui  bahwa  berhala-berhala  itu  tidak  dapat  berbicara."{ 65 }</p>
<p>Ibrahim  berkata: “Maka  mengapa  kamu  menyembah  selain  Allah  sesuatu</p>
<p>yang  tidak  dapat  memberi  manfaat  sedikitpun  dan  tidak  (pula)  memberi</p>
<p>mudharat  kepada  kamu?"{ 66 }</p>
<p>Ah  (celakalah)  kamu  dan  apa  yang  kamu  ibadahi  selain  Allah.  Maka</p>
<p>apakah  kamu  tidak  memahami?{ 67 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 94-96</h4>
  <div class="verse">
    
    <p class="translation">Kemudian kaumnya datang kepadanya dengan bergegas. <span class="verse-num">(94)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ibrahim berkata: "Apakah kamu menyembah patung-patung yang kamu pahat itu? <span class="verse-num">(95)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Padahal Allah-lah yang menciptakan kamu dan apa yang kamu perbuat itu". <span class="verse-num">(96)</span></p>
  </div>
</div>
<p class="footnote"><em>80) Maksudnya; mereka kembali membangkang setelah sad ar.</em></p>
<p>Kemudian  kaumnya  datang  kepadanya  dengan  bergegas.{ 94 }</p>
<p>Ibrahim  berkata:  “Apakah  kamu  menyembah  patung-patung  yang  kamu</p>
<p>pahat  itu  ?{ 95 }</p>
<p>Padahal  Allahlah  yang  menciptakanmu  dan  apa  yang  kamu  buat.”{ 96 }</p>
<p>◙ Al  Anbiyaa\`  [21]:  68  – 71</p>
<p>Mereka  berkata:  "Bakarlah  dia  dan  bantulah  Tuhan-tuhan  kamu,  jika</p>
<p>kamu  benar-benar  hendak  bertindak.”{ 68 }</p>
<p>Kami  berfirman:  "Hai  api  menjadi  dinginlah,  dan  jadilah  keselamatan  bagi</p>
<p>Ibrahim",{ 69 }</p>
<p>Mereka  hendak  berbuat  makar  terhadap  Ibrahim,  maka  Kami  menjadikan</p>
<p>mereka  itu  orang-orang  yang  paling  merugi.{ 70 }</p>
<p>Dan  Kami  seIamatkan  Ibrahim  dan  Luth  ke  sebuah  negeri  yang  Kami</p>
<p>telah  memberkahinya  untuk  sekalian  manusia 81 .{ 71 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 97-98</h4>
  <div class="verse">
    
    <p class="translation">Mereka berkata: "Dirikanlah suatu bangunan untuk (membakar) Ibrahim; lalu lemparkanlah dia ke dalam api yang menyala-nyala itu". <span class="verse-num">(97)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Mereka hendak melakukan tipu muslihat kepadanya, maka Kami jadikan mereka orang-orang yang hina. <span class="verse-num">(98)</span></p>
  </div>
</div>
<p class="footnote"><em>81) Yang dimaksud dengan “negeri” di sini ialah negeri S yam, termasuk di dalamnya</em></p>
<p>Palestina. Tuhan memberkahi negeri itu artinya: keban yakan nabi berasal dan negeri ini</p>
<p>dan tanahnyapun subur.</p>
<p>Ibrahim As. Dilemparkan ke dalam Api</p>
<p>Mereka  berkata:  "Dirikanlah  suatu  bangunan  untuk  (membakar)  Ibrahim;</p>
<p>lalu  lemparkanlah  dia  ke  dalam  api  yang  menyala-nyala.”{ 97 }</p>
<p>Mereka  hendak  melakukan  tipu  muslihat  kepadanya,  maka  Kami  jadikan</p>
<p>mereka  orang-orang  yang  hina.{ 98 }</p>
<div class="quran-quote">
  <h4>Al  'Ankabuut : 24-25</h4>
  <div class="verse">
    
    <p class="translation">Maka tidak adalah jawaban kaum Ibrahim, selain mengatakan: "Bunuhlah atau bakarlah dia", lalu Allah menyelamatkannya dari api. Sesungguhnya pada yang demikian itu benar-benar terdapat tanda-tanda kebesaran Allah bagi orang-orang yang beriman. <span class="verse-num">(24)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan berkata Ibrahim: "Sesungguhnya berhala-berhala yang kamu sembah selain Allah adalah untuk menciptakan perasaan kasih sayang di antara kamu dalam kehidupan dunia ini kemudian di hari kiamat sebahagian kamu mengingkari sebahagian (yang lain) dan sebahagian kamu melaknati sebahagian (yang lain); dan tempat kembalimu ialah neraka, dan sekali-kali tak ada bagimu para penolongpun. <span class="verse-num">(25)</span></p>
  </div>
</div>
<p>Maka  tidaklah  ada  jawaban  kaum  Ibrahim,  selain  mengatakan:  "Bunuhlah</p>
<p>atau  bakarlah  dia",  lalu  Allah  menyelamatkannya  dari  api.  Sesungguhnya</p>
<p>pada  yang  demikian  itu  benar-benar  terdapat  tanda-tanda  kebesaran</p>
<p>Allah  bagi  orang-orang  yang  beriman.{ 24 }</p>
<p>Dan  berkata  Ibrahim:  "Sesungguhnya  berhala-berhala  yang  kamu  ibadahi</p>
<p>selain  Allah  adalah  untuk  menciptakan  perasaan  kasih  sayang  di  antara</p>
<p>kamu  dalam  kehidupan  dunia  ini, kemudian  di  hari  kiamat  sebagian  kamu</p>
<p>mengingkari  sebagian  (yang  lain)  dan  sebagian  kamu  melaknat  sebagian</p>
<p>(yang  lain);  dan  tempat  kembalimu  ialah  neraka,  dan  sekali-kali  tidak  ada</p>
<p>bagimu  seorang  penolongpun.{ 25 }</p>
<p>Ibrahim As. Hijrah dari Kaumnya</p>
<div class="quran-quote">
  <h4>Maryam : 48-48</h4>
  <div class="verse">
    
    <p class="translation">Dan aku akan menjauhkan diri darimu dan dari apa yang kamu seru selain Allah, dan aku akan berdoa kepada Tuhanku, mudah-mudahan aku tidak akan kecewa dengan berdoa kepada Tuhanku". <span class="verse-num">(48)</span></p>
  </div>
</div>
<p>Dan  aku  akan  menjauhkan  diri  darimu  dan  dari  apa  yang  kamu  seru  selain</p>
<p>Allah,  dan  aku  akan  berdoa  kepada  Tuhanku,  mudah-mudahan  aku  tidak</p>
<p>akan  kecewa  dengan  berdoa  kepada  Tuhanku.”{ 48 }</p>
<p>◙ Al  ‘Ankabuut  [29]:  28</p>
<p>Maka  Luth  membenarkan  (kenabian)-nya.  Dan  berkatalah  Ibrahim:</p>
<p>“Sesungguhnya  aku  akan  berpindah  ke  (tempat  yang  diperintahkan)</p>
<p>Tuhanku  (kepadaku);  sesungguhnya  Dia-lah  Yang  Maha  Perkasa  lagi</p>
<p>Maha  Bijaksana.{ 26 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 99-99</h4>
  <div class="verse">
    
    <p class="translation">Dan Ibrahim berkata: "Sesungguhnya aku pergi menghadap kepada Tuhanku, dan Dia akan memberi petunjuk kepadaku. <span class="verse-num">(99)</span></p>
  </div>
</div>
<p>Dan  Ibrahim  berkata:  “Sesungguhnya  aku  pergi  menghadap  kepada</p>
<p>Tuhanku,  dan  Dia  akan  memberi  petunjuk  kepadaku 82 .”{ 99 }</p>
<div class="quran-quote">
  <h4>Az  Zukhruf : 26-28</h4>
  <div class="verse">
    
    <p class="translation">Dan ingatlah ketika Ibrahim berkata kepada bapaknya dan kaumnya: "Sesungguhnya aku tidak bertanggung jawab terhadap apa yang kamu sembah, <span class="verse-num">(26)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">tetapi (aku menyembah) Tuhan Yang menjadikanku; karena sesungguhnya Dia akan memberi hidayah kepadaku". <span class="verse-num">(27)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan (lbrahim a. s.) menjadikan kalimat tauhid itu kalimat yang kekal pada keturunannya supaya mereka kembali kepada kalimat tauhid itu. <span class="verse-num">(28)</span></p>
  </div>
</div>
<p class="footnote"><em>82) Ibrahim pergi ke suatu negeri untuk menyembah Alla h dan berdakwah.</em></p>
<p>Dan  (ingatlah)  ketika  Ibrahim  berkata  kepada  bapaknya  dan  kaumnya:</p>
<p>"Sesungguhnya  aku  berlepas diri dari  apa  yang  kamu  ibadahi,{ 26 }</p>
<p>Tetapi  (aku  mengabdi) kepada  Tuhan  yang  menjadikanku;  karena</p>
<p>sesungguhnya  Dia  akan  memberi  hidayah  kepadaku".{ 27 }</p>
<p>Dan  (lbrahim)  menjadikan  kalimat  tauhid  itu  kalimat  yang  kekal  pada</p>
<p>keturunannya  supaya  mereka  kembali  kepada  kalimat  tauhid  itu.{ 28 }</p>
`,
                        quiz: [
                            { "question": "Siapakah nama ayah Nabi Ibrahim As?", "options": ["Azar", "Taruh", "Nahur", "Ismail"], "answer": 0 },
                            { "question": "Apa hukuman yang diberikan kaumnya kepada Nabi Ibrahim?", "options": ["Dibakar", "Dipenjara", "Diasingkan", "Disalib"], "answer": 0 },
                            { "question": "Apa alasan utama kaum Nabi Ibrahim menyembah berhala?", "options": ["Perintah raja", "Mengikuti nenek moyang", "Wahyu Tuhan", "Logika akal"], "answer": 1 },
                            { "question": "Apa yang dilakukan Nabi Ibrahim terhadap berhala-berhala kaumnya?", "options": ["Menghancurkannya kecuali yang terbesar", "Menyembunyikannya", "Mewarnainya", "Membuangnya ke sungai"], "answer": 0 },
                            { "question": "Bagaimana kondisi api saat Nabi Ibrahim dibakar?", "options": ["Sangat panas", "Padam terkena hujan", "Menjadi dingin dan menyelamatkan", "Membakar tali pengikat saja"], "answer": 2 }
                        ]
                    },
                    {
                        id: 148,
                        title: "Ibrahim As. dan Ismail As.",
                        file: "topic_148.pdf",
                        content: `<h3>IBRAHIM AS</h3>
<h3>DAN ISMAIL AS</h3>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 100-101</h4>
  <div class="verse">
    
    <p class="translation">Ya Tuhanku, anugrahkanlah kepadaku (seorang anak) yang termasuk orang-orang yang saleh. <span class="verse-num">(100)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Maka Kami beri dia khabar gembira dengan seorang anak yang amat sabar. <span class="verse-num">(101)</span></p>
  </div>
</div>
<p>Ya  Tuhanku,  anugrahilah  aku  (anak)  yang  termasuk  orang  saleh.{ 100 }</p>
<p>Maka  Kami  gembirakan dia  dengan  anak  yang  amat  sabar (Ismail){101 }</p>
<div class="quran-quote">
  <h4>Maryam : 54-55</h4>
  <div class="verse">
    
    <p class="translation">Dan ceritakanlah (hai Muhammad kepada mereka) kisah Ismail (yang tersebut) di dalam Al Quran. Sesungguhnya ia adalah seorang yang benar janjinya, dan dia adalah seorang rasul dan nabi. <span class="verse-num">(54)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan ia menyuruh ahlinya untuk bersembahyang dan menunaikan zakat, dan ia adalah seorang yang diridhai di sisi Tuhannya. <span class="verse-num">(55)</span></p>
  </div>
</div>
<p>Dan  ceritakanlah  (hai  Muhammad)  kisah  Ismail  (yang  tersebut)  di  dalam</p>
<p>Alquran. Sesungguhnya  ia  adalah  seorang  yang  benar  janjinya,  dan  dia</p>
<p>adalah  seorang  rasul  dan  nabi.{ 54 }</p>
<p>Dan  ia  menyuruh  ahlinya (keluarga atau umatnya)  untuk  shalat  dan</p>
<p>menunaikan  zakat,  dan  ia  seorang  yang  diridhai  di  sisi  Tuhannya.{ 55 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 102-103</h4>
  <div class="verse">
    
    <p class="translation">Maka tatkala anak itu sampai (pada umur sanggup) berusaha bersama-sama Ibrahim, Ibrahim berkata: "Hai anakku sesungguhnya aku melihat dalam mimpi bahwa aku menyembelihmu. Maka fikirkanlah apa pendapatmu!" Ia menjawab: "Hai bapakku, kerjakanlah apa yang diperintahkan kepadamu; insya Allah kamu akan mendapatiku termasuk orang-orang yang sabar". <span class="verse-num">(102)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Tatkala keduanya telah berserah diri dan Ibrahim membaringkan anaknya atas pelipis(nya), (nyatalah kesabaran keduanya). <span class="verse-num">(103)</span></p>
  </div>
</div>
<p>Ibrahim As. Dianugerahi Putera Pertama; Ismail</p>
<h3>Keutamaan Ismail As.</h3>
<p>Ibrahim As. Diuji untuk Menyembelih Ismail</p>
<p>Maka  tatkala  anak  itu  sampai  (pada  umur  yang sanggup)  berusaha</p>
<p>bersamanya,  Ibrahim  berkata:  "Hai  anakku, sesungguhnya  aku  melihat</p>
<p>dalam  mimpi  bahwa  aku  menyembelihmu.  Maka  pikirkanlah  apa</p>
<p>pendapatmu!"  ia  menjawab:  "Hai  bapakku,  kerjakan  apa  yang</p>
<p>diperintahkan  padamu;  insya  Allah  kamu  akan  mendapatiku  termasuk</p>
<p>orang-orang  yang  sabar".{ 102 }</p>
<p>Tatkala  keduanya  telah  berserah  diri  dan  Ibrahim  membaringkan  anaknya</p>
<p>atas  pelipis-(nya),  (nyatalah  kesabaran  keduanya).{ 103 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 104-111</h4>
  <div class="verse">
    
    <p class="translation">Dan Kami panggillah dia: "Hai Ibrahim, <span class="verse-num">(104)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">sesungguhnya kamu telah membenarkan mimpi itu sesungguhnya demikianlah Kami memberi balasan kepada orang-orang yang berbuat baik. <span class="verse-num">(105)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya ini benar-benar suatu ujian yang nyata. <span class="verse-num">(106)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan Kami tebus anak itu dengan seekor sembelihan yang besar. <span class="verse-num">(107)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kami abadikan untuk Ibrahim itu (pujian yang baik) di kalangan orang-orang yang datang kemudian, <span class="verse-num">(108)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">(yaitu)"Kesejahteraan dilimpahkan atas Ibrahim". <span class="verse-num">(109)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Demikianlah Kami memberi balasan kepada orang-orang yang berbuat baik. <span class="verse-num">(110)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya ia termasuk hamba-hamba Kami yang beriman. <span class="verse-num">(111)</span></p>
  </div>
</div>
<p>Dan  Kami  panggil  dia:  "Hai  Ibrahim,{ 104 }</p>
<p>Ibrahim As. Lulus dari Ujian dan Hikmahnya</p>
<p>Sungguh  kamu  telah  membenarkan  mimpi  itu,83  sesungguhnya</p>
<p>demikianlah  Kami  membalas  orang-orang  yang  berbuat  baik.{ 105 }</p>
<p>Sesungguhnya  ini  benar-benar  suatu  ujian  yang  nyata.{ 106 }</p>
<p>Dan  Kami  tebus  anak  itu  dengan  seekor  sembelihan  yang  besar 84 .{ 107 }</p>
<p>Kami  abadikan  untuk  Ibrahim  itu  (pujian  yang  baik)  di  kalangan  orang-</p>
<p>orang  yang  datang  kemudian,{ 108 }</p>
<p>(Yaitu)  "Kesejahteraan  dilimpahkan  atas  Ibrahim.”{ 109 }</p>
<p>Demikian  Kami  membalas  orang-orang  yang  berbuat  baik.{ 110 }</p>
<p>Sesungguhnya  ia  termasuk  hamba-hamba  Kami  yang  beriman.{ 111 }</p>
<div class="quran-quote">
  <h4>Al  Baqarah : 124-129</h4>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah), ketika Ibrahim diuji Tuhannya dengan beberapa kalimat (perintah dan larangan), lalu Ibrahim menunaikannya. Allah berfirman: "Sesungguhnya Aku akan menjadikanmu imam bagi seluruh manusia". Ibrahim berkata: "(Dan saya mohon juga) dari keturunanku". Allah berfirman: "Janji-Ku (ini) tidak mengenai orang yang zalim". <span class="verse-num">(124)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah), ketika Kami menjadikan rumah itu (Baitullah) tempat berkumpul bagi manusia dan tempat yang aman. Dan jadikanlah sebahagian maqam Ibrahim tempat shalat. Dan telah Kami perintahkan kepada Ibrahim dan Ismail: "Bersihkanlah rumah-Ku untuk orang-orang yang thawaf, yang i'tikaf, yang ruku' dan yang sujud". <span class="verse-num">(125)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah), ketika Ibrahim berdoa: "Ya Tuhanku, jadikanlah negeri ini, negeri yang aman sentosa, dan berikanlah rezeki dari buah-buahan kepada penduduknya yang beriman diantara mereka kepada Allah dan hari kemudian. Allah berfirman: "Dan kepada orang yang kafirpun Aku beri kesenangan sementara, kemudian Aku paksa ia menjalani siksa neraka dan itulah seburuk-buruk tempat kembali". <span class="verse-num">(126)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah), ketika Ibrahim meninggikan (membina) dasar-dasar Baitullah bersama Ismail (seraya berdoa): "Ya Tuhan kami terimalah daripada kami (amalan kami), sesungguhnya Engkaulah Yang Maha Mendengar lagi Maha Mengetahui". <span class="verse-num">(127)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ya Tuhan kami, jadikanlah kami berdua orang yang tunduk patuh kepada Engkau dan (jadikanlah) diantara anak cucu kami umat yang tunduk patuh kepada Engkau dan tunjukkanlah kepada kami cara-cara dan tempat-tempat ibadat haji kami, dan terimalah taubat kami. Sesungguhnya Engkaulah Yang Maha Penerima taubat lagi Maha Penyayang. <span class="verse-num">(128)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ya Tuhan kami, utuslah untuk mereka sesorang Rasul dari kalangan mereka, yang akan membacakan kepada mereka ayat-ayat Engkau, dan mengajarkan kepada mereka Al Kitab (Al Quran) dan Al-Hikmah (As-Sunnah) serta mensucikan mereka. Sesungguhnya Engkaulah yang Maha Kuasa lagi Maha Bijaksana. <span class="verse-num">(129)</span></p>
  </div>
</div>
<p class="footnote"><em>83) Yang dimaksud dengan membenarkan mimpi ialah mem percayai bahwa mimpi itu</em></p>
<p>benar dari Allah Swt. dan wajib melaksanakannya.</p>
<p class="footnote"><em>84) Setelah nyata Ibrahim dan Ismail sabar dan taat, m aka Allah melarang</em></p>
<p>menyembelih Ismail. Untuk meneruskan korban, Allah ganti dengan seekor kambing.</p>
<p>Ibrahim As. dan Ismail As. Membina Ka'bah</p>
<p>Dan  (ingatlah),  ketika  Ibrahim  diuji 85  Tuhannya  dengan  beberapa  kalimat,</p>
<p>lalu  Ibrahim  menunaikannya.  Allah  berfirman:  “Sesungguhnya  Aku  akan</p>
<p>menjadikanmu  imam  bagi  seluruh  manusia.”  Ibrahim  berkata:  "(Dan  saya</p>
<p>mohon  juga)  dari  keturunanku" 86 . Allah  berfirman:  "Janji-Ku  (ini)  tidak</p>
<p>mengenai  orang-orang  yang  zalim.”{ 124 }</p>
<p>Dan  (ingatlah),  ketika  Kami  menjadikan  rumah  itu  (Baitullah)  tempat</p>
<p>berkumpul  bagi  manusia  dan  tempat  yang  aman.  Dan  jadikanlah</p>
<p class="footnote"><em>85) Ujian terhadap Ibrahim di antaranya: membangun Ka' bah, membersihkannya dari</em></p>
<p>kemusyrikan, mengorbankan anaknya, menghadapi raja Namrudz dan lain-lain.</p>
<p class="footnote"><em>86) Allah telah mengabulkan doa nabi Ibrahim As., ka rena banyak di antara rasul-rasul</em></p>
<h3>itu adalah keturunan nabi Ibrahim As.</h3>
<p>sebagian  maqam  Ibrahim 87  tempat  shalat.  Dan  telah  Kami  perintahkan</p>
<p>kepada  Ibrahim  dan  Ismail:  "Bersihkanlah  rumah-Ku  untuk  orang-orang</p>
<p>yang  thawaf,  yang  i'tikaf,  yang  ruku' , dan  yang  sujud.”{ 125 }</p>
<p>Dan  (ingatlah),  ketika  Ibrahim  berdoa:  "Ya  Tuhanku,  jadikanlah  negeri  ini,</p>
<p>negeri  yang  aman  sentosa,  dan  berikanlah  rezeki  dari  buah-buahan</p>
<p>kepada  penduduknya  yang  beriman  di  antara  mereka  kepada  Allah  dan</p>
<p>hari  Akhir. Allah  berfirman:  "Dan  kepada  orang  yang  kafirpun  Aku  beri</p>
<p>kesenangan  sementara,  kemudian  Aku  paksa  ia  menjalani  siksa  neraka</p>
<p>dan  itulah  seburuk-buruk  tempat  kembali.”{ 126 }</p>
<p>Dan  (ingatlah),  ketika  Ibrahim  meninggikan  (membina)  dasar-dasar</p>
<p>Baitullah  bersama  Ismail  (seraya  berdoa):  "Ya  Tuhan  kami  terimalah  dari</p>
<p>kami  (amal  kami),  sesungguhnya  Engkau-lah  Yang  Maha  Mendengar  lagi</p>
<p>Maha  Mengetahui.”{ 127 }</p>
<p>Ya  Tuhan  kami,  jadikanlah  kami  berdua  orang  yang  tunduk  patuh kepada-</p>
<p>Mu dan  (jadikanlah)  di  antara  anak  cucu  kami  umat  yang  tunduk  patuh</p>
<p>kepada-Mu dan  tunjukkanlah  kepada  kami  cara  dan  tempat  ibadat  haji</p>
<p>kami,  dan  terimalah  tobat  kami.  Sesungguhnya  Engkau-lah  Yang  Maha</p>
<p>Penerima  tobat  lagi  Maha  Penyayang.{ 128 }</p>
<p>Ya  Tuhan  kami,  utuslah  untuk  mereka  sesorang  rasul  dari  kalangan</p>
<p>mereka,  yang  akan  membacakan  kepada  mereka  ayat-ayat-Mu, dan</p>
<p>mengajarkan  kepada  mereka  Alkitab  (Alquran)  dan  hikmah  (As-Sunnah)</p>
<p>serta  menyucikan  mereka.  Sesungguhnya  Engkau-lah  Yang  Maha  Kuasa</p>
<p>lagi  Maha  Bijaksana.{ 129 }</p>
<div class="quran-quote">
  <h4>Ibraahiim : 35-41</h4>
  <div class="verse">
    
    <p class="translation">Dan (ingatlah), ketika Ibrahim berkata: "Ya Tuhanku, jadikanlah negeri ini (Mekah), negeri yang aman, dan jauhkanlah aku beserta anak cucuku daripada menyembah berhala-berhala. <span class="verse-num">(35)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ya Tuhanku, sesungguhnya berhala-berhala itu telah menyesatkan kebanyakan daripada manusia, maka barangsiapa yang mengikutiku, maka sesungguhnya orang itu termasuk golonganku, dan barangsiapa yang mendurhakai aku, maka sesungguhnya Engkau, Maha Pengampun lagi Maha Penyayang. <span class="verse-num">(36)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ya Tuhan kami, sesungguhnya aku telah menempatkan sebahagian keturunanku di lembah yang tidak mempunyai tanam-tanaman di dekat rumah Engkau (Baitullah) yang dihormati, ya Tuhan kami (yang demikian itu) agar mereka mendirikan shalat, maka jadikanlah hati sebagian manusia cenderung kepada mereka dan beri rezekilah mereka dari buah-buahan, mudah-mudahan mereka bersyukur. <span class="verse-num">(37)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ya Tuhan kami, sesungguhnya Engkau mengetahui apa yang kami sembunyikan dan apa yang kami lahirkan; dan tidak ada sesuatupun yang tersembunyi bagi Allah, baik yang ada di bumi maupun yang ada di langit. <span class="verse-num">(38)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Segala puji bagi Allah yang telah menganugerahkan kepadaku di hari tua(ku) Ismail dan Ishaq. Sesungguhnya Tuhanku, benar-benar Maha Mendengar (memperkenankan) doa. <span class="verse-num">(39)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ya Tuhanku, jadikanlah aku dan anak cucuku orang-orang yang tetap mendirikan shalat, ya Tuhan kami, perkenankanlah doaku. <span class="verse-num">(40)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ya Tuhan kami, beri ampunlah aku dan kedua ibu bapaku dan sekalian orang-orang mukmin pada hari terjadinya hisab (hari kiamat)". <span class="verse-num">(41)</span></p>
  </div>
</div>
<p class="footnote"><em>87) Ialah tempat berdiri nabi Ibrahim As. pada waktu me mbuat Ka'bah.</em></p>
<h3>Doa Ibrahim As. dan Ismail As.</h3>
<p>Dan  (ingatlah),  ketika  Ibrahim  berkata:  "Ya  Tuhanku,  jadikanlah  negeri  ini</p>
<p>(Mekah),  negeri  yang  aman,  dan  jauhkanlah  aku  beserta  anak  cucuku</p>
<p>daripada  mengabdi kepada  berhala-berhala.{ 35 }</p>
<p>Ya  Tuhanku,  sesungguhnya  berhala-berhala  itu  telah  menyesatkan</p>
<p>kebanyakan  dari  manusia,  maka  siapa  mengikutiku,  maka  sungguh  ia</p>
<p>termasuk  golonganku,  dan  siapa  yang  mendurhakaiku,  maka</p>
<p>sesungguhnya  Engkau  Maha  Pengampun  lagi  Maha  Penyayang.{ 36 }</p>
<p>Ya  Tuhan  kami,  sesungguhnya  aku  telah  menempatkan  sebagian</p>
<p>keturunanku  di  lembah  yang  tidak  mempunyai  tanam-tanaman  di  dekat</p>
<p>rumah-Mu (Baitullah)  yang  dihormati,  Ya  Tuhan  kami  (yang  demikian  itu)</p>
<p>agar  mereka  mendirikan  shalat,  maka  jadikanlah  hati  sebagian  manusia</p>
<p>cenderung  kepada  mereka  dan  beri  rezekilah  mereka  dari  buah-buahan,</p>
<p>mudah-mudahan  mereka  bersyukur.{ 37 }</p>
<p>Ya  Tuhan  kami,  sesungguhnya  Engkau  mengetahui  apa  yang  kami</p>
<p>sembunyikan  dan  apa  yang  kami  lahirkan;  dan  tidak  ada  sesuatupun</p>
<p>yang  tersembunyi  bagi  Allah,  baik  yang  ada  di  bumi  maupun  yang  ada  di</p>
<p>langit.{ 38 }</p>
<p>Segala  puji  bagi  Allah  yang  telah  menganugerahkan  kepadaku  di  hari  tua -</p>
<p>(ku)  Ismail  dan  Ishaq.  Sesungguhnya  Tuhanku,  benar-benar  Maha</p>
<p>Mendengar  (Memperkenankan)  doa.{ 39 }</p>
<p>Ya  Tuhanku,  jadikanlah  aku  dan  anak  cucuku  orang-orang  yang  tetap</p>
<p>mendirikan  shalat,  Ya  Tuhan  kami,  perkenankanlah  doaku.{ 40 }</p>
<p>Ya  Tuhan  kami,  beri  ampunlah  aku  dan  kedua  ibu -bapaku  dan  segenap</p>
<p>orang  mukmin  pada  hari  terjadinya  hisab  (hari  kiamat).”{ 41 }</p>
<div class="quran-quote">
  <h4>Asy  Syu'araa' : 83-89</h4>
  <div class="verse">
    
    <p class="translation">(Ibrahim berdoa): "Ya Tuhanku, berikanlah kepadaku hikmah dan masukkanlah aku ke dalam golongan orang-orang yang saleh, <span class="verse-num">(83)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan jadikanlah aku buah tutur yang baik bagi orang-orang (yang datang) kemudian, <span class="verse-num">(84)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan jadikanlah aku termasuk orang-orang yang mempusakai surga yang penuh kenikmatan, <span class="verse-num">(85)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan ampunilah bapakku, karena sesungguhnya ia adalah termasuk golongan orang-orang yang sesat, <span class="verse-num">(86)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">dan janganlah Engkau hinakan aku pada hari mereka dibangkitkan, <span class="verse-num">(87)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">(yaitu) di hari harta dan anak-anak laki-laki tidak berguna, <span class="verse-num">(88)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">kecuali orang-orang yang menghadap Allah dengan hati yang bersih, <span class="verse-num">(89)</span></p>
  </div>
</div>
<p>(Ibrahim  berdoa):  "Ya  Tuhanku,  berikanlah  kepadaku  hikmah  dan</p>
<p>masukkanlah  aku  ke  dalam  golongan  orang-orang  yang  saleh,{ 83 }</p>
<p>Dan  jadikanlah  aku  buah  tutur  yang  baik  bagi  orang-orang  (yang  datang)</p>
<p>kemudian,{ 84 }</p>
<p>Dan  jadikanlah  aku  termasuk  orang-orang  yang  mempusakai  surga  yang</p>
<p>penuh  kenikmatan,{ 85 }</p>
<p>Dan  ampunilah  bapakku,  karena  sesungguhnya  ia  adalah  termasuk</p>
<p>golongan  orang-orang  yang  sesat,{ 86 }</p>
<p>Dan  janganlah  Engkau  hinakan  aku  pada  hari  mereka  dibangkitkan,{ 87 }</p>
<p>(Yaitu)  di  hari  harta  dan  anak-anak  laki-laki  tidak  berguna,{ 88 }</p>
<p>Kecuali  orang-orang  yang  menghadap  Allah  dengan  hati  yang  bersih,{ 89 }</p>
<p>◙ Lihat juga: Al Baqarah [2]: 126 – 129</p>
`,
                        quiz: [
                            { "question": "Siapakah putera pertama Nabi Ibrahim As?", "options": ["Ismail", "Ishak", "Yakub", "Yusuf"], "answer": 0 },
                            { "question": "Apa yang diperintahkan Allah kepada Ibrahim melalui mimpi?", "options": ["Menyembelih Ismail", "Membangun Kabah", "Berhijrah", "Berpuasa"], "answer": 0 },
                            { "question": "Apa gelar Nabi Ismail yang disebutkan dalam surat Maryam ayat 54?", "options": ["Shadiqul Wa'di", "Ulul Azmi", "Khatamun Nabiyyin", "Kalimullah"], "answer": 0 },
                            { "question": "Apa yang dibangun oleh Nabi Ibrahim dan Ismail di Mekah?", "options": ["Ka'bah (Baitullah)", "Masjid Nabawi", "Istana", "Menara"], "answer": 0 },
                            { "question": "Apa doa Nabi Ibrahim untuk negeri Mekah (Al-Baqarah: 126)?", "options": ["Negeri yang aman dan berbuah-buahan", "Negeri yang kaya emas", "Negeri yang luas", "Negeri yang sejuk"], "answer": 0 }
                        ]
                    },
                    {
                        id: 149,
                        title: "Ibrahim As. dan Tamunya (Malaikat)",
                        file: "topic_149.pdf",
                        content: `<h3>IBRAHIM AS</h3>
<h3>DAN</h3>
<h3>TAMUNYA (MALAIKAT)</h3>
<div class="quran-quote">
  <h4>Huud : 69-76</h4>
  <div class="verse">
    
    <p class="translation">Dan sesungguhnya utusan-utusan Kami (malaikat-malaikat) telah datang kepada lbrahim dengan membawa kabar gembira, mereka mengucapkan: "Selamat". Ibrahim menjawab: "Selamatlah," maka tidak lama kemudian Ibrahim menyuguhkan daging anak sapi yang dipanggang. <span class="verse-num">(69)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Maka tatkala dilihatnya tangan mereka tidak menjamahnya, Ibrahim memandang aneh perbuatan mereka, dan merasa takut kepada mereka. Malaikat itu berkata: "Jangan kamu takut, sesungguhnya kami adalah (malaikat-ma]aikat) yang diutus kepada kaum Luth". <span class="verse-num">(70)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan isterinya berdiri (dibalik tirai) lalu dia tersenyum, maka Kami sampaikan kepadanya berita gembira tentang (kelahiran) Ishak dan dari Ishak (akan lahir puteranya) Ya'qub. <span class="verse-num">(71)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Isterinya berkata: "Sungguh mengherankan, apakah aku akan melahirkan anak padahal aku adalah seorang perempuan tua, dan ini suamikupun dalam keadaan yang sudah tua pula?. Sesungguhnya ini benar-benar suatu yang sangat aneh". <span class="verse-num">(72)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Para malaikat itu berkata: "Apakah kamu merasa heran tentang ketetapan Allah? (Itu adalah) rahmat Allah dan keberkatan-Nya, dicurahkan atas kamu, hai ahlulbait! Sesungguhnya Allah Maha Terpuji lagi Maha Pemurah". <span class="verse-num">(73)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Maka tatkala rasa takut hilang dari Ibrahim dan berita gembira telah datang kepadanya, diapun bersoal jawab dengan (malaikat-malaikat) Kami tentang kaum Luth. <span class="verse-num">(74)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya Ibrahim itu benar-benar seorang yang penyantun lagi penghiba dan suka kembali kepada Allah. <span class="verse-num">(75)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Hai Ibrahim, tinggalkanlah soal jawab ini, sesungguhnya telah datang ketetapan Tuhanmu, dan sesungguhnya mereka itu akan didatangi azab yang tidak dapat ditolak. <span class="verse-num">(76)</span></p>
  </div>
</div>
<p>Dan  sungguh utusan-utusan  Kami  (malaikat-malaikat)  telah  datang</p>
<p>kepada  lbrahim  dengan  kabar  gembira,  mereka  mengucapkan:</p>
<p>"Selamat."  Ibrahim  menjawab:  "Selamat,"  maka  tidak  lama  kemudian</p>
<p>Ibrahim  menyuguhkan  daging  anak  sapi  yang  dipanggang.{ 69 }</p>
<p>Maka  tatkala  dilihatnya  tangan  mereka  tidak  menjamahnya,  Ibrahim</p>
<p>memandang  aneh  perbuatan  mereka,  dan  merasa  takut  kepada  mereka.</p>
<p>Malaikat  itu  berkata:  "Jangan  kamu  takut,  sesungguhnya  kami  adalah</p>
<p>(malaikat-malaikat)  yang  diutus  kepada  kaum  Luth."{ 70 }</p>
<div class="quran-quote">
  <h4>Al  Hijr : 51-52</h4>
  <div class="verse">
    
    <p class="translation">Dan kabarkanlah kepada mereka tentang tamu-tamu Ibrahim. <span class="verse-num">(51)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ketika mereka masuk ke tempatnya, lalu mereka mengucapkan: "Salaam". Berkata Ibrahim: "Sesungguhnya kami merasa takut kepadamu". <span class="verse-num">(52)</span></p>
  </div>
</div>
<p>Dan  kabarkanlah  kepada  mereka  tentang  tamu-tamu  Ibrahim.{ 51 }</p>
<p>Ketika  mereka  masuk  ke  tempatnya,  lalu  mereka  mengucapkan:</p>
<p>"Selamat".  Berkata  Ibrahim:  "Sesungguhnya  kami  takut  padamu".{ 52 }</p>
<p>◙ Lihat juga: Adz Dzaariyaat [51]: 24-27</p>
<p>Ibrahim As. Menyuguhi Para Tamunya (Malaikat)</p>
<div class="quran-quote">
  <h4>Huud : 71-73</h4>
  <div class="verse">
    
    <p class="translation">Dan isterinya berdiri (dibalik tirai) lalu dia tersenyum, maka Kami sampaikan kepadanya berita gembira tentang (kelahiran) Ishak dan dari Ishak (akan lahir puteranya) Ya'qub. <span class="verse-num">(71)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Isterinya berkata: "Sungguh mengherankan, apakah aku akan melahirkan anak padahal aku adalah seorang perempuan tua, dan ini suamikupun dalam keadaan yang sudah tua pula?. Sesungguhnya ini benar-benar suatu yang sangat aneh". <span class="verse-num">(72)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Para malaikat itu berkata: "Apakah kamu merasa heran tentang ketetapan Allah? (Itu adalah) rahmat Allah dan keberkatan-Nya, dicurahkan atas kamu, hai ahlulbait! Sesungguhnya Allah Maha Terpuji lagi Maha Pemurah". <span class="verse-num">(73)</span></p>
  </div>
</div>
<p>Dan  istrinya  berdiri  (di balik  tirai)  lalu  ia  tersenyum, maka  kami  sampaikan</p>
<p>kepadanya  berita  gembira  tentang  (kelahiran)  Ishak  dan  dari  Ishak  (akan</p>
<p>lahir  putranya)  Ya'qub.{ 71 }</p>
<p>Istrinya  berkata:  "Sungguh  mengherankan,  akankah  aku  melahirkan</p>
<p>anak, padahal  aku  seorang  perempuan  tua,  dan  ini  suamiku  dalam</p>
<p>keadaan  sudah  tua  pula?.  Sesungguhnya  ini  benar-benar  suatu  yang</p>
<p>sangat  aneh."{ 72 }</p>
<p>Para  malaikat  itu  berkata:  "Apakah  kamu  merasa  heran  tentang</p>
<p>ketetapan  Allah?  (Itu  adalah)  rahmat  Allah  dan  keberkatan-Nya,</p>
<p>dicurahkan  atasmu,  hai  ahlulbait!  Sesungguhnya  Allah  Maha  Terpuji  lagi</p>
<p>Maha  Pemurah."{ 73 }</p>
<div class="quran-quote">
  <h4>Al  Hijr : 53-56</h4>
  <div class="verse">
    
    <p class="translation">Mereka berkata: "Janganlah kamu merasa takut, sesungguhnya kami memberi kabar gembira kepadamu dengan (kelahiran seorang) anak laki-laki (yang akan menjadi) orang yang alim". <span class="verse-num">(53)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Berkata Ibrahim: "Apakah kamu memberi kabar gembira kepadaku padahal usiaku telah lanjut, maka dengan cara bagaimanakah (terlaksananya) berita gembira yang kamu kabarkan ini?" <span class="verse-num">(54)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Mereka menjawab: "Kami menyampaikan kabar gembira kepadamu dengan benar, maka janganlah kamu termasuk orang-orang yang berputus asa". <span class="verse-num">(55)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ibrahim berkata: "Tidak ada orang yang berputus asa dari rahmat Tuhan-nya, kecuali orang-orang yang sesat". <span class="verse-num">(56)</span></p>
  </div>
</div>
<p>Tamu Membawa Kabar tentang Kelahiran Ishak dan Ya'qub</p>
<p>Mereka  berkata:  "Janganlah  kamu  merasa  takut,  sesungguhnya  kami</p>
<p>memberi  kabar  gembira  kepadamu  dengan  (kelahiran  seorang)  anak  laki-</p>
<p>laki  (yang  akan  menjadi)  orang  yang  alim (Ishak) ".{ 53 }</p>
<p>Berkata  Ibrahim:  "Apakah  kamu  memberi  kabar  gembira  kepadaku,</p>
<p>padahal  usiaku  telah  lanjut, maka  bagaimana  (terlaksananya)  berita</p>
<p>gembira  yang  kamu  kabarkan  ini?"{ 54 }</p>
<p>Mereka  menjawab:  "Kami  menyampaikan  kabar  gembira  kepadamu</p>
<p>dengan  benar, maka  janganlah  kamu  termasuk  orang-orang  yang</p>
<p>berputus  asa".{ 55 }</p>
<p>Ibrahim  berkata:  "tidak  ada  orang  yang  berputus  asa  dari  rahmat  Tuhan-</p>
<p>nya,  kecuali  orang-orang  yang  sesat".{ 56 }</p>
<p>◙ Lihat juga: Adz Dzaariyaat [51]: 28-30</p>
<div class="quran-quote">
  <h4>Huud : 74-76</h4>
  <div class="verse">
    
    <p class="translation">Maka tatkala rasa takut hilang dari Ibrahim dan berita gembira telah datang kepadanya, diapun bersoal jawab dengan (malaikat-malaikat) Kami tentang kaum Luth. <span class="verse-num">(74)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya Ibrahim itu benar-benar seorang yang penyantun lagi penghiba dan suka kembali kepada Allah. <span class="verse-num">(75)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Hai Ibrahim, tinggalkanlah soal jawab ini, sesungguhnya telah datang ketetapan Tuhanmu, dan sesungguhnya mereka itu akan didatangi azab yang tidak dapat ditolak. <span class="verse-num">(76)</span></p>
  </div>
</div>
<p>Maka  tatkala  rasa  takut  hilang  dari  Ibrahim  dan  berita  gembira  telah</p>
<p>datang  kepadanya,  diapun  bersoal  jawab  dengan  (malaikat-malaikat)</p>
<p>Kami  tentang  kaum  Luth.{ 74 }</p>
<h3>Ibrahim As. Berdialog dengan Tamu tentang Kaum Luth As.</h3>
<p>Sesungguhnya  Ibrahim  itu  benar-benar  seorang  yang  penyantun  lagi</p>
<p>penghiba  dan  suka  kembali  kepada  Allah.{ 75 }</p>
<p>Hai  Ibrahim,  tinggalkanlah  soal  jawab  ini,  sesungguhnya  telah  datang</p>
<p>ketetapan  Tuhanmu,  dan  sesungguhnya  mereka  itu  akan  didatangi  azab</p>
<p>yang  tidak  dapat  ditolak.{ 76 }</p>
<div class="quran-quote">
  <h4>Al  Hijr : 57-60</h4>
  <div class="verse">
    
    <p class="translation">Berkata (pula) Ibrahim: "Apakah urusanmu yang penting (selain itu), hai para utusan?" <span class="verse-num">(57)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Mereka menjawab: "Kami sesungguhnya diutus kepada kaum yang berdosa, <span class="verse-num">(58)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">kecuali Luth beserta pengikut-pengikutnya. Sesungguhnya Kami akan menyelamatkan mereka semuanya, <span class="verse-num">(59)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">kecuali istrinya. Kami telah menentukan, bahwa sesungguhnya ia itu termasuk orang-orang yang tertinggal (bersama-sama dengan orang kafir lainnya)". <span class="verse-num">(60)</span></p>
  </div>
</div>
<p>Berkata  (pula)  Ibrahim:  "Apakah  urusanmu  yang  penting  (selain  itu),  Hai</p>
<p>para  utusan?"{ 57 }</p>
<p>Mereka  menjawab:  "Kami  sesungguhnya  diutus  kepada  kaum  yang</p>
<p>berdosa,{ 58 }</p>
<p>◙ Lihat juga: Adz Dzaariyaat [51]: 31-37</p>
`,
                        quiz: [
                            { "question": "Siapakah tamu yang mengunjungi Nabi Ibrahim?", "options": ["Malaikat", "Raja", "Pengemis", "Saudara"], "answer": 0 },
                            { "question": "Kabar gembira apa yang dibawa para tamu tersebut?", "options": ["Kelahiran Ishak", "Kemenangan perang", "Turunnya hujan", "Harta melimpah"], "answer": 0 },
                            { "question": "Apa yang disuguhkan Nabi Ibrahim kepada tamu-tamunya?", "options": ["Daging anak sapi panggang", "Roti gandum", "Buah kurma", "Susu unta"], "answer": 0 },
                            { "question": "Mengapa Nabi Ibrahim merasa takut kepada tamu-tamunya?", "options": ["Wajah mereka seram", "Mereka membawa senjata", "Tangan mereka tidak menjamah makanan", "Mereka datang malam hari"], "answer": 2 },
                            { "question": "Selain kabar gembira anak, apa tujuan lain para malaikat datang?", "options": ["Mengabarkan azab kaum Luth", "Menguji Ibrahim", "Mencari jalan", "Meminta sumbangan"], "answer": 0 }
                        ]
                    },
                    {
                        id: 150,
                        title: "Ibrahim As. dan Ishak As.",
                        file: "topic_150.pdf",
                        content: `<h3>IBRAHIM AS</h3>
<h3>DAN</h3>
<h3>ISHAK AS</h3>
<div class="quran-quote">
  <h4>Al  Anbiyaa' : 72-73</h4>
  <div class="verse">
    
    <p class="translation">Dan Kami telah memberikan kepada-nya (Ibrahim) lshak dan Ya'qub, sebagai suatu anugerah (daripada Kami). Dan masing-masingnya Kami jadikan orang-orang yang saleh <span class="verse-num">(72)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kami telah menjadikan mereka itu sebagai pemimpin-pemimpin yang memberi petunjuk dengan perintah Kami dan telah Kami wahyukan kepada, mereka mengerjakan kebajikan, mendirikan sembahyang, menunaikan zakat, dan hanya kepada Kamilah mereka selalu menyembah, <span class="verse-num">(73)</span></p>
  </div>
</div>
<p>Dan  Kami  telah  memberikan  kepada-Nya  (Ibrahim)  lshak  dan  Ya'qub,</p>
<p>sebagai  suatu  anugerah  (dari  Kami).  Dan  masing-masing  Kami  jadikan</p>
<p>orang-orang  yang  saleh.{72 }</p>
<p>Kami  telah  jadikan  mereka  pemimpin-pemimpin  yang  memberi  petunjuk</p>
<p>dengan  perintah  Kami  dan  telah  Kami  wahyukan  kepada  mereka</p>
<p>mengerjakan  kebaikan,  mendirikan  shalat, menunaikan  zakat,  dan  hanya</p>
<p>kepada  Kami  mereka  selalu  menngabdi,{ 73 }</p>
<div class="quran-quote">
  <h4>Ash  Shaaffaat : 112-113</h4>
  <div class="verse">
    
    <p class="translation">Dan Kami beri dia kabar gembira dengan (kelahiran) Ishaq seorang nabi yang termasuk orang-orang yang saleh. <span class="verse-num">(112)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Kami limpahkan keberkatan atasnya dan atas Ishaq. Dan diantara anak cucunya ada yang berbuat baik dan ada (pula) yang Zalim terhadap dirinya sendiri dengan nyata. <span class="verse-num">(113)</span></p>
  </div>
</div>
<p>Dan  Kami  beri  dia  kabar  gembira  dengan  (kelahiran)  Ishaq  seorang  nabi</p>
<p>yang  termasuk  orang-orang  yang  saleh.{ 112 }</p>
<p>Kami  limpahkan  keberkatan  atasnya  dan  atas  Ishaq.  Dan  di  antara  anak</p>
<p>cucunya  ada  yang  berbuat  baik  dan  ada  (pula)  yang  zalim  terhadap</p>
<p>dirinya  sendiri  dengan  nyata.{ 113 }</p>
<p>◙ Al\`Ankabuut  [29]:  27</p>
<h3>Ibrahim As. Dianugerahi Ishaq As. dan Ya'qub As.</h3>
<p>Dan  Kami  anugerahkan  kepada  Ibrahim,  Ishak,  dan  Ya'qub,  dan  Kami</p>
<p>jadikan  kenabian  dan  Alkitab  pada  keturunannya,  dan  Kami  berikan</p>
<p>kepadanya  balasannya  di  dunia;  dan  sesungguhnya  mereka  di  akhirat,</p>
<p>benar-benar  termasuk  orang-orang  yang  saleh.{27 }</p>
<div class="quran-quote">
  <h4>Maryam : 49-50</h4>
  <div class="verse">
    
    <p class="translation">Maka ketika Ibrahim sudah menjauhkan diri dari mereka dan dari apa yang mereka sembah selain Allah, Kami anugerahkan kepadanya Ishak, dan Ya'qub. Dan masing-masingnya Kami angkat menjadi nabi. <span class="verse-num">(49)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan Kami anugerahkan kepada mereka sebagian dari rahmat Kami dan Kami jadikan mereka buah tutur yang baik lagi tinggi. <span class="verse-num">(50)</span></p>
  </div>
</div>
<p>Maka  ketika  Ibrahim  sudah  menjauhkan  diri  dari  mereka  dan  dari  apa</p>
<p>yang  mereka  ibadahi  selain  Allah,  Kami  anugerahkan  padanya  Ishak,  dan</p>
<p>Ya'qub.  Dan  masing-masing  Kami  angkat  menjadi  nabi.{ 49 }</p>
<p>Dan  Kami  anugerahkan  kepada  mereka  sebagian  dari  rahmat  Kami  dan</p>
<p>Kami  jadikan  mereka  buah  tutur  yang  baik  lagi  tinggi.{ 50 }</p>
<div class="quran-quote">
  <h4>Shaad : 45-49</h4>
  <div class="verse">
    
    <p class="translation">Dan ingatlah hamba-hamba Kami: Ibrahim, Ishaq dan Ya'qub yang mempunyai perbuatan-perbuatan yang besar dan ilmu-ilmu yang tinggi. <span class="verse-num">(45)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Sesungguhnya Kami telah mensucikan mereka dengan (menganugerahkan kepada mereka) akhlak yang tinggi yaitu selalu mengingatkan (manusia) kepada negeri akhirat. <span class="verse-num">(46)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan sesungguhnya mereka pada sisi Kami benar-benar termasuk orang-orang pilihan yang paling baik. <span class="verse-num">(47)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Dan ingatlah akan Ismail, Ilyasa' dan Zulkifli. Semuanya termasuk orang-orang yang paling baik. <span class="verse-num">(48)</span></p>
  </div>
  <div class="verse">
    
    <p class="translation">Ini adalah kehormatan (bagi mereka). Dan sesungguhnya bagi orang-orang yang bertakwa benar-benar (disediakan) tempat kembali yang baik, <span class="verse-num">(49)</span></p>
  </div>
</div>
<h3>Keutamaan Ibrahim As., Ishaq As., dan Ya'qub As.</h3>
<p>Dan  ingatlah  hamba-hamba  Kami:  Ibrahim,  Ishaq, dan  Ya'qub  yang</p>
<p>memiliki  karya-karya  yang  besar  dan  ilmu-ilmu  yang  tinggi.{ 45 }</p>
<p>Sesungguhnya  Kami  telah  menyucikan  mereka  dengan  akhlak  yang</p>
<p>tinggi  yaitu  selalu  mengingatkan  (manusia)  kepada  negeri  akhirat.{ 46 }</p>
<p>Dan  sesungguhnya  mereka  pada  sisi  Kami  benar-benar  termasuk  orang-</p>
<p>orang  pilihan  yang  paling  baik.{ 47 }</p>
`,
                        quiz: [
                            { "question": "Siapakah putera kedua Nabi Ibrahim dari Siti Sarah?", "options": ["Ishak", "Ismail", "Yakub", "Yusuf"], "answer": 0 },
                            { "question": "Siapakah anak dari Nabi Ishak yang juga menjadi Nabi?", "options": ["Yakub", "Yusuf", "Musa", "Harun"], "answer": 0 },
                            { "question": "Siapakah ibu dari Nabi Ishak?", "options": ["Sarah", "Hajar", "Ribka", "Rahmah"], "answer": 0 },
                            { "question": "Dalam surat Ash-Shaffaat ayat 113, keberkahan dilimpahkan kepada siapa?", "options": ["Ibrahim dan Ishak", "Musa dan Harun", "Daud dan Sulaiman", "Yusuf dan Bunyamin"], "answer": 0 },
                            { "question": "Sifat apa yang dimiliki Ibrahim, Ishak, dan Ya'qub menurut surat Shaad: 45?", "options": ["Punya kekuatan besar dan ilmu tinggi", "Kaya raya", "Berumur panjang", "Ahli perang"], "answer": 0 }
                        ]
                    },
                ]
            },
            {
                "id": "subject-6-8",
                "title": "Pokok Bahasan 8: Ya'qub AS",
                "topics": [
                    {
                        "id": 151,
                        "title": "Kelahiran Ya'qub As.",
                        "file": "topic_151.pdf",
                        "content": "<h3>KELAHIRAN YA'QUB AS.</h3><p>Nabi  Ishaq  dikabarkan  tidak  mempunyai  anak  dalam  waktu  yang  lama, tapi dia dan istrinya Ribka (Rifiqah) terus berdoa kepada Allah Swt.. Setelah usia Ishaq  mencapai  60 tahun, barulah  Ribka  hamil  dan  melahirkan  anak  kembar.</p><p>Anak pertama diberi nama ‘Aishu’ (Esau) dan anak kedua diberi nama ‘Ya’qub’. Nabi  Ya’qub  dilahirkan  di  Palestina.  Ia  adalah  putra  Nabi  Ishaq  dan  ibunya bernama  Ribka  binti  Azar.  Ayahnya  (Ishaq)  adalah  anak  Nabi  Ibrahim.</p><div class=\"quran-quote\">  <h4>Huud : 71-73</h4>  <div class=\"verse\">        <p class=\"translation\">Dan isterinya berdiri (dibalik tirai) lalu dia tersenyum, maka Kami sampaikan kepadanya berita gembira tentang (kelahiran) Ishak dan dari Ishak (akan lahir puteranya) Ya'qub. <span class=\"verse-num\">(71)</span></p>  </div>  <div class=\"verse\">        <p class=\"translation\">Isterinya berkata: \"Sungguh mengherankan, apakah aku akan melahirkan anak padahal aku adalah seorang perempuan tua, dan ini suamikupun dalam keadaan yang sudah tua pula?. Sesungguhnya ini benar-benar suatu yang sangat aneh\". <span class=\"verse-num\">(72)</span></p>  </div>  <div class=\"verse\">        <p class=\"translation\">Para malaikat itu berkata: \"Apakah kamu merasa heran tentang ketetapan Allah? (Itu adalah) rahmat Allah dan keberkatan-Nya, dicurahkan atas kamu, hai ahlulbait! Sesungguhnya Allah Maha Terpuji lagi Maha Pemurah\". <span class=\"verse-num\">(73)</span></p>  </div></div><p>Dan isterinya  berdiri  (dibalik  tirai)  lalu  dia  tersenyum, maka  Kami  sampaikan kepadanya  berita  gembira  tentang  (kelahiran)  Ishak  dan  dari  Ishak  (akan  lahir puteranya)  Ya'qub.{ 71 }.</p><p>Isterinya  berkata:  \"Sungguh  mengherankan,  apakah  aku  akan  melahirkan anak  padahal  aku  adalah  seorang  perempuan  tua,  dan  ini  suamikupun  dalam keadaan  yang  sudah  tua  pula?.  Sesungguhnya  ini  benar-benar  suatu  yang sangat  aneh\".{ 72 }.</p><p>Para  malaikat  itu  berkata:  \"Apakah  kamu  merasa  heran  tentang  ketetapan Allah?  (Itu  adalah)  rahmat  Allah  dan  keberkatan-Nya,  dicurahkan  atas  kamu, hai  ahlulbait!  Sesungguhnya  Allah  Maha  Terpuji  lagi  Maha  Pemurah\".{ 73 }.</p>",
                        "quiz": [
                            { "question": "Siapakah nama ibu Nabi Ya'qub AS?", "options": ["Ribka (Rifiqah)", "Sarah", "Hajar", "Rahmah"], "answer": 0 },
                            { "question": "Siapakah saudara kembar Nabi Ya'qub AS?", "options": ["'Aishu' (Esau)", "Yusuf", "Bunyamin", "Luth"], "answer": 0 },
                            { "question": "Nabi Ya'qub adalah putera dari Nabi siapa?", "options": ["Ishaq", "Ismail", "Ibrahim", "Luth"], "answer": 0 },
                            { "question": "Dimanakah Nabi Ya'qub dilahirkan?", "options": ["Palestina", "Mesir", "Babilonia", "Mekah"], "answer": 0 },
                            { "question": "Dalam surat Huud ayat 71, kelahiran Ya'qub dikabarkan setelah kelahiran siapa?", "options": ["Ishak", "Ismail", "Yusuf", "Musa"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 152,
                        "title": "Kehidupan Ya'qub As.",
                        "file": "topic_152.pdf",
                        "content": "<h3>KEHIDUPAN YA'QUB AS.</h3><p>Nabi  Ya’qub  tumbuh  bersama  saudaranya  ‘Aishu’  di  bawah  asuhan orang tuanya.  Akan  tetapi  ada  perbedaan  perlakuan  orang  tua  terhadap  kedua anaknya.</p><p>Ishaq lebih menyayangi ‘Aishu’ karena ia pandai berburu dan sering memberikan  hasil  buruannya  kepada  ayahnya.  Sedangkan  Ribka  lebih menyayangi  Ya’qub  karena  ia  penurut  dan  sering  membantu  pekerjaan  rumah.</p><p>Suatu  hari  Ishaq  meminta  ‘Aishu’  untuk  berburu  dan  membuatkan  makanan kesukaannya.  Mendengar  hal  itu,  Ribka  menyuruh  Ya’qub  untuk  mendahului saudaranya  membuatkan  makanan  untuk  ayahnya.  Ya’qub  pun  melakukan perintah  ibunya  dan  mendapatkan  doa  keberkahan  dari  ayahnya.</p><div class=\"quran-quote\">  <h4>Al  Anbiyaa' : 72-73</h4>  <div class=\"verse\">        <p class=\"translation\">Dan Kami telah memberikan kepada-nya (Ibrahim) lshak dan Ya'qub, sebagai suatu anugerah (daripada Kami). Dan masing-masingnya Kami jadikan orang-orang yang saleh <span class=\"verse-num\">(72)</span></p>  </div>  <div class=\"verse\">        <p class=\"translation\">Kami telah menjadikan mereka itu sebagai pemimpin-pemimpin yang memberi petunjuk dengan perintah Kami dan telah Kami wahyukan kepada, mereka mengerjakan kebajikan, mendirikan sembahyang, menunaikan zakat, dan hanya kepada Kamilah mereka selalu menyembah, <span class=\"verse-num\">(73)</span></p>  </div></div><p>Dan  Kami  telah  memberikan  kepada-nya  (Ibrahim)  lshak  dan  Ya'qub, sebagai  suatu  anugerah  (daripada  Kami).  Dan  masing-masingnya  Kami jadikan  orang-orang  yang  saleh.{ 72 }.</p><p>Kami  telah  menjadikan  mereka  itu  sebagai  pemimpin-pemimpin  yang  memberi petunjuk  dengan  perintah  Kami  dan  telah  Kami  wahyukan  kepada,  mereka mengerjakan  kebajikan,  mendirikan  sembahyang,  menunaikan  zakat,  dan  hanya kepada  Kamilah  mereka  selalu  menyembah.{ 73 }.</p>",
                        "quiz": [
                            { "question": "Mengapa Nabi Ishaq lebih menyayangi 'Aishu' (Esau)?", "options": ["Karena dia pandai berburu", "Karena dia anak sulung", "Karena dia tampan", "Karena dia kaya"], "answer": 0 },
                            { "question": "Mengapa Ribka lebih menyayangi Ya'qub?", "options": ["Karena penurut dan membantu di rumah", "Karena dia bungsu", "Karena dia sakit-sakitan", "Karena dia gagah"], "answer": 0 },
                            { "question": "Apa yang diminta Nabi Ishaq kepada 'Aishu' sebelum memberkatinya?", "options": ["Berburu dan membuat makanan", "Menggembala kambing", "Mencari kayu bakar", "Berperang"], "answer": 0 },
                            { "question": "Siapa yang akhirnya mendapatkan doa keberkahan utama dari Nabi Ishaq?", "options": ["Ya'qub", "Esau", "Ismail", "Ibrahim"], "answer": 0 },
                            { "question": "Menurut Al-Anbiyaa: 73, Allah menjadikan mereka sebagai pemimpin yang memberi apa?", "options": ["Petunjuk dengan perintah Allah", "Harta kepada fakir miskin", "Kekuasaan politik", "Makanan berlimpah"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 153,
                        "title": "Wasiat Ya'qub As.",
                        "file": "topic_153.pdf",
                        "content": "<h3>WASIAT YA'QUB AS.</h3><p>Nabi Ya’qub hidup sampai usia yang sangat tua. Menjelang wafatnya, ia mengumpulkan  anak-anaknya  untuk  memberikan  wasiat.</p><div class=\"quran-quote\">  <h4>Al  Baqarah : 132-133</h4>  <div class=\"verse\">        <p class=\"translation\">Dan Ibrahim telah mewasiatkan ucapan itu kepada anak-anaknya, demikian pula Ya'qub. (Ibrahim berkata): \"Hai anak-anakku! Sesungguhnya Allah telah memilih agama ini bagimu, maka janganlah kamu mati kecuali dalam memeluk agama Islam\". <span class=\"verse-num\">(132)</span></p>  </div>  <div class=\"verse\">        <p class=\"translation\">Adakah kamu hadir ketika Ya'qub kedatangan (tanda-tanda) maut, ketika ia berkata kepada anak-anaknya: \"Apa yang kamu sembah sepeninggalku?\" Mereka menjawab: \"Kami akan menyembah Tuhanmu dan Tuhan nenek moyangmu, Ibrahim, Ismail dan Ishaq, (yaitu) Tuhan Yang Maha Esa dan kami hanya tunduk patuh kepada-Nya\". <span class=\"verse-num\">(133)</span></p>  </div></div><p>Dan  Ibrahim  telah  mewasiatkan  ucapan  itu  kepada  anak-anaknya,  demikian pula  Ya'qub.  (Ibrahim  berkata):  \"Hai  anak-anakku!  Sesungguhnya  Allah  telah memilih  agama  ini  bagimu, maka  janganlah  kamu  mati  kecuali  dalam  memeluk agama  Islam\".{ 132 }.</p><p>Adakah  kamu  hadir  ketika  Ya'qub  kedatangan  (tanda-tanda)  maut,  ketika  ia berkata  kepada  anak-anaknya:  \"Apa  yang  kamu  sembah  sepeninggalku?\" Mereka  menjawab:  \"Kami  akan  menyembah  Tuhanmu  dan  Tuhan  nenek moyangmu,  Ibrahim,  Ismail  dan  Ishaq,  (yaitu)  Tuhan  Yang  Maha  Esa  dan  kami hanya  tunduk  patuh  kepada-Nya\".{ 133 }.</p>",
                        "quiz": [
                            { "question": "Apa yang ditanyakan Nabi Ya'qub kepada anak-anaknya menjelang wafat?", "options": ["Apa yang kamu sembah sepeninggalku?", "Berapa harta yang tersisa?", "Siapa yang akan menjadi raja?", "Kapan aku akan dikubur?"], "answer": 0 },
                            { "question": "Apa jawaban anak-anak Nabi Ya'qub atas pertanyaan ayahnya?", "options": ["Kami menyembah Tuhanmu dan Tuhan nenek moyangmu", "Kami menyembah berhala", "Kami tidak tahu", "Kami akan mencari Tuhan baru"], "answer": 0 },
                            { "question": "Siapakah nenek moyang yang disebut oleh anak-anak Ya'qub?", "options": ["Ibrahim, Ismail, Ishaq", "Adam, Nuh, Idris", "Musa, Harun, Daud", "Luth, Syu'aib, Shaleh"], "answer": 0 },
                            { "question": "Apa wasiat utama Nabi Ibrahim dan Ya'qub kepada keturunannya (Al-Baqarah: 132)?", "options": ["Jangan mati kecuali dalam keadaan Islam", "Kumpulkan harta sebanyak-banyaknya", "Jadilah penguasa dunia", "Jangan berperang"], "answer": 0 },
                            { "question": "Apa nama agama yang disebutkan dalam wasiat tersebut?", "options": ["Islam", "Yahudi", "Nasrani", "Majusi"], "answer": 0 }
                        ]
                    }
                ]
            },
            {
                "id": "subject-6-9",
                "title": "Pokok Bahasan 9: Ayyub AS",
                "topics": [
                    {
                        "id": 154,
                        "title": "Kisah Nabi Ayyub As.",
                        "file": "topic_154.pdf",
                        "content": `<div class="verse"><p class="translation">Ayyub As. 182 9.1 KENABIAN DAN KESABARAN AYUB AS Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Ayyub As. 183 9.1.1 Kenabian Ayub As.</p></div><div class="verse"><p class="translation">◙ An Nisaa’ [4]: 163</p></div><div class="verse"><p class="translation">Sesungguhnya Kami telah memberI wahyu kepadamu sebagaimana Kami telah memberi wahyu kepada Nuh dan nabi-nabi yang setelahnya, dan Kami telah memberi wahyu (pula) kepada Ibrahim, Ismail, Ishak, Ya'qub dan anak cucunya, Isa, Ayub, Yunus, Harun, dan Sulaiman. Dan Kami berikan Zabur kepada Daud.{163}</p></div><div class="verse"><p class="translation">◙ Lihat juga: Al An\`aam [6]: 84 9.1.2 Kesabaran Ayub As.</p></div><div class="verse"><p class="translation">◙ Al Anbiyaa\` [21]: 83 – 84</p></div><div class="verse"><p class="translation">Dan (ingatlah kisah) Ayub, ketika ia menyeru Tuhannya: "(Ya Tuhanku), sesungguhnya aku telah ditimpa penyakit dan Engkau adalah Tuhan Yang Maha Penyayang di antara semua penyayang.”{83}</p></div><div class="verse"><p class="translation">Maka Kami pun memperkenankan seruannya itu, lalu Kami lenyapkan penyakit yang ada padanya dan Kami kembalikan keluarganya kepadanya, dan Kami lipatgandakan bilangan mereka, sebagai suatu rahmat dari sisi Kami dan untuk menjadi peringatan bagi semua yang menyembah Allah.{84}</p></div><div class="verse"><p class="translation">◙ Shaad [38]: 41 – 44</p></div><div class="verse"><p class="translation">Dan ingatlah hamba Kami Ayub ketika ia menyeru Tuhannya: “Sesungguhnya aku diganggu oleh setan dengan kepayahan dan siksaan.”{41} (Allah berfirman): "Hantamkanlah kakimu; inilah air yang sejuk untuk mandi dan untuk minum.”{42} Dan Kami menganugerahinya (dengan mengumpulkan kembali) keluarganya dan (Kami tambahkan) kepada mereka sebanyak mereka pula sebagai rahmat dari Kami dan pelajaran bagi orang-orang yang mempunyai pikiran.{43} Dan ambillah dengan tanganmu seikat (rumput), maka pukullah dengan itu dan janganlah kamu melanggar sumpah. Sesungguhnya Kami dapati dia (Ayub) seorang yang sabar. Dialah sebaik-baik hamba. Sesungguhnya dia amat taat (kepada Tuhannya)106.{44}</p></div><div class="verse"><p class="translation">106) Nabi Ayub As. menderita penyakit kulit beberapa waktu lamanya dan dia memohon pertolongan kepada Allah Swt., Allah kemudian memperkenankan doanya dan memerintahkan agar dia menghentakkan kakinya ke bumi. Ayub mentaati perintah itu maka keluarlah air dari bekas kakinya atas petunjuk Allah, Ayub pun mandi dan minum dari air itu, sehingga sembuhlah dia dari penyakitnya dan dia dapat berkumpul kembali dengan keluarganya. Maka mereka kemudian berkembang biak sampai jumlah mereka dua kali lipat dari jumlah sebelumnya. Pada suatu ketika Ayub teringat akan sumpahnya, bahwa dia akan memukul istrinya bilamana sakitnya sembuh disebabkan istrinya pernah lalai mengurusinya sewaktu dia masih sakit. Akan tetapi timbul dalam hatinya rasa iba dan sayang kepada istrinya sehingga dia tidak dapat memenuhi sumpahnya. Oleh sebab itu turunlah perintah Allah seperti yang tercantum dalam ayat 44 di atas, agar dia dapat memenuhi sumpahnya dengan tidak menyakiti istrinya yaitu memukulnya dengan seikat rumput.</p></div>`,
                        "quiz": [
                            { "question": "Surat apa yang menyebutkan wahyu kepada Nabi Ayyub sejajar dengan Nabi lainnya?", "options": ["An-Nisa: 163", "Al-Baqarah: 124", "Yusuf: 4", "Hud: 71"], "answer": 0 },
                            { "question": "Apa doa Nabi Ayyub ketika ditimpa penyakit (Al-Anbiyaa: 83)?", "options": ["Sesungguhnya aku telah ditimpa penyakit dan Engkau Tuhan Maha Penyayang", "Ya Tuhanku, sembuhkanlah aku", "Ya Tuhanku, matikanlah aku", "Ya Tuhanku, berikan aku kekayaan"], "answer": 0 },
                            { "question": "Bagaimana cara Allah menyembuhkan penyakit Nabi Ayyub (Shaad: 42)?", "options": ["Hantamkan kaki ke bumi hingga keluar air sejuk", "Minum madu", "Mandi di sungai Nil", "Berpuasa 40 hari"], "answer": 0 },
                            { "question": "Apa yang dilakukan Allah terhadap keluarga Nabi Ayyub setelah beliau sembuh?", "options": ["Mengembalikan dan melipatgandakan jumlahnya", "Memisahkan mereka", "Menjadikan mereka raja", "Tidak ada perubahan"], "answer": 0 },
                            { "question": "Mengapa Nabi Ayyub diperintahkan memukul istrinya dengan seikat rumput?", "options": ["Untuk memenuhi sumpah tanpa menyakiti istri", "Karena istri durhaka", "Karena perintah raja", "Karena tradisi"], "answer": 0 }
                        ]
                    }
                ]
            },
            {
                "id": "subject-6-10",
                "title": "Pokok Bahasan 10: Syu'aib AS",
                "topics": [
                    {
                        "id": 155,
                        "title": "Dakwah Syu'aib AS Terhadap Penduduk Madyan",
                        "file": "topic_155.pdf",
                        "content": `<div class="verse"><p class="translation">Shu’aib As. 186 10.1 DAKWAH SYU'AIB AS TERHADAP PENDUDUK MADYAN Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Shu’aib As. 187 10.1.1 Perintah Untuk Menyempurnakan Takaran dan Timbangan</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 85</p></div><div class="verse"><p class="translation">Dan (Kami telah mengutus) kepada penduduk Madyan107 saudara mereka, Syu'aib. Ia berkata: \"Hai kaumku, sembahlah Allah, sekali-kali tidak ada Tuhan bagimu selain-Nya. Sesungguhnya telah datang kepadamu bukti yang nyata dari Tuhanmu. Maka sempurnakanlah takaran dan timbangan dan janganlah kamu kurangkan bagi manusia barang-barang takaran dan timbangannya, dan janganlah kamu membuat kerusakan di muka bumi sesudah Tuhan memperbaikinya. Yang demikian itu lebih baik bagimu jika betul-betul kamu orang-orang yang beriman\".{85}</p></div><div class="verse"><p class="translation">◙ Huud [11]: 84 – 86</p></div><div class="verse"><p class="translation">Dan kepada (penduduk) Madyan (Kami utus) saudara mereka, Syu'aib. Ia berkata: \"Hai kaumku, sembahlah Allah, sekali-kali tiada Tuhan bagimu selain Dia. Dan janganlah kamu kurangi takaran dan timbangan, sesungguhnya aku melihat kamu dalam keadaan yang baik (mampu) dan sesungguhnya aku khawatir terhadapmu akan azab hari yang membinasakan (kiamat).\"{84}</p></div><div class="verse"><p class="translation">\"Dan Syu'aib berkata: \"Hai kaumku, cukupkanlah takaran dan timbangan dengan adil, dan janganlah kamu merugikan manusia terhadap hak-hak mereka dan janganlah kamu membuat kejahatan di muka bumi dengan membuat kerusakan.{85}</p></div><div class="verse"><p class="translation">Sisa (keuntungan) dari Allah108 adalah lebih baik bagimu jika kamu orang-orang yang beriman. Dan aku bukanlah seorang penjaga atas dirimu\"{86}</p></div><div class="verse"><p class="translation">◙ Al 'Ankabuut [29]: 36</p></div><div class="verse"><p class="translation">Dan (kami telah mengutus) kepada penduduk Madyan, saudara mereka Syu'aib, maka ia berkata: \"Hai kaumku, hendaklah kamu mengabdi kepada Allah, harapkanlah (pahala) hari akhir, dan jangan kamu berkeliaran di muka bumi seraya berbuat kerusakan\".{36}</p></div><div class="verse"><p class="translation">◙ Asy Syu'araa' [26]: 176 – 184</p></div><div class="verse"><p class="translation">Penduduk Aikah109 telah mendustakan rasul-rasul;{176}</p></div><div class="verse"><p class="translation">ketika Syu'aib berkata kepada mereka: \"Mengapa kamu tidak bertakwa?,{177}</p></div><div class="verse"><p class="translation">Sesungguhnya aku adalah seorang rasul kepercayaan (yang diutus) kepadamu.{178}</p></div><div class="verse"><p class="translation">maka bertakwalah kepada Allah dan taatlah kepadaku;{179}</p></div><div class="verse"><p class="translation">Dan aku sekali-kali tidak minta upah kepadamu atas ajakan itu; upahku tidak lain hanyalah dari Tuhan semesta alam.{180}</p></div><div class="verse"><p class="translation">Sempurnakanlah takaran dan janganlah kamu termasuk orang-orang yang merugikan;{181}</p></div><div class="verse"><p class="translation">dan timbanglah dengan timbangan yang lurus.{182}</p></div><div class="verse"><p class="translation">Dan janganlah kamu merugikan manusia pada hak-haknya dan janganlah kamu merajalela di muka bumi dengan membuat kerusakan;{183}</p></div><div class="verse"><p class="translation">dan bertakwalah kepada Allah yang telah menciptakan kamu dan umat-umat yang dahulu\".{184}</p></div><div class="verse"><p class="translation">107) Madyan adalah nama putera Nabi ibrahim a.s. kemudian menjadi nama kabilah (kaum) yang terdiri dari anak cucunya. Kabilah ini diam di suatu tempat yang dinamakan Madyan pula. yang terietak di dekat pantai laut merah di tenggara gunung Sinai.</p></div><div class="verse"><p class="translation">108) Maksudnya: keuntungan yang diberikan Allah yang diperoleh sesudah menyempurnakan takaran dan timbangan.</p></div><div class="verse"><p class="translation">109) Aikah ialah nama sebuah tempat yang berhutan di daerah Madyan.</p></div><div class="verse"><p class="translation">10.1.2 Larangan Menghalang-halangi Orang Beriman</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 86</p></div><div class="verse"><p class="translation">Dan janganlah kamu duduk di tiap-tiap jalan dengan menakut-nakuti dan menghalang-halangi orang yang beriman dari jalan Allah, dan menginginkan agar jalan Allah itu menjadi bengkok. Dan ingatlah di waktu dahulunya kamu berjumlah sedikit, lalu Allah memperbanyak jumlah kamu. Dan perhatikanlah bagaimana kesudahan orang-orang yang berbuat kerusakan.{86}</p></div>`,
                        "quiz": [
                            { "question": "Siapakah Nabi yang diutus kepada penduduk Madyan?", "options": ["Syu'aib AS", "Luth AS", "Hud AS", "Shaleh AS"], "answer": 0 },
                            { "question": "Apa kejahatan utama penduduk Madyan dalam muamalah?", "options": ["Mengurangi takaran dan timbangan", "Mencuri ternak", "Membunuh bayi", "Menyembah api"], "answer": 0 },
                            { "question": "Penduduk Madyan juga disebut sebagai Ashab al-...", "options": ["Aikah", "Hijr", "Rass", "Kahfi"], "answer": 0 },
                            { "question": "Apa yang dilakukan penduduk Madyan di jalan-jalan?", "options": ["Mengancam dan menghalang-halangi orang beriman", "Berdagang dengan jujur", "Membangun pos penjagaan", "Meminta sedekah"], "answer": 0 },
                            { "question": "Apa hubungan kekerabatan Syu'aib dengan penduduk Madyan?", "options": ["Saudara mereka sebangsa", "Orang asing", "Raja mereka", "Budak mereka"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 156,
                        "title": "Sikap Penduduk Madyan Terhadap Dakwah Syu'aib AS",
                        "file": "topic_156.pdf",
                        "content": `<div class="verse"><p class="translation">Shu’aib As. 191 10.2 SIKAP PENDUDUK MADYAN TERHADAP DAKWAH SYU'AIB AS Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Shu’aib As. 192 10.2.1 Penduduk Madyan Meragukan Ajaran Syu'aib As.</p></div><div class="verse"><p class="translation">◙ Huud [11]: 87</p></div><div class="verse"><p class="translation">Mereka berkata: \"Hai Syu'aib, apakah sembahyangmu menyuruh kamu agar kami meninggalkan apa yang disembah oleh bapak-bapak kami atau melarang kami memperbuat apa yang kami kehendaki tentang harta kami. Sesungguhnya kamu adalah orang yang sangat penyantun lagi pandai\".{87}</p></div><div class="verse"><p class="translation">10.2.2 Penduduk Madyan Mengancam Akan Mengusir Syu'aib As.</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 88 – 89</p></div><div class="verse"><p class="translation">Pemuka-pemuka dan kaum Syu'aib yang menyombongkan diri berkata: \"Sesungguhnya kami akan mengusir kamu hai Syu'aib dan orang-orang yang beriman bersamamu dari kota kami, atau kamu kembali kepada agama kami\". Berkata Syu'aib: \"Walau kami tidak menyukainya?\"{88}</p></div><div class="verse"><p class="translation">Sungguh kami mengada-adakan kebohongan yang besar terhadap Allah, jika kami kembali kepada agamamu, sesudah Allah melepaskan kami daripadanya. Dan tidaklah patut kami kembali kepadanya, kecuali jika Allah, Tuhan kami menghendaki(nya). Pengetahuan Tuhan kami meliputi segala sesuatu. Kepada Allah sajalah kami bertawakkal. Ya Tuhan kami, berilah keputusan antara kami dan kaum kami dengan hak (adil) dan Engkaulah Pemberi keputusan yang sebaik-baiknya.{89}</p></div><div class="verse"><p class="translation">10.2.3 Penduduk Madyan Mengancam Akan Merajam Syu'aib As.</p></div><div class="verse"><p class="translation">◙ Huud [11]: 91</p></div><div class="verse"><p class="translation">Mereka berkata: \"Hai Syu'aib, kami tidak banyak mengerti tentang apa yang kamu katakan itu dan sesungguhnya kami benar-benar melihat kamu seorang yang lemah di antara kami; kalau tidaklah karena keluargamu tentulah kami telah merajam kamu, sedang kamupun bukanlah seorang yang berwibawa di sisi kami.\"{91}</p></div><div class="verse"><p class="translation">10.2.4 Penduduk Madyan Menuduh Syu'aib As. Sebagal Pesihir dan Pendusta</p></div><div class="verse"><p class="translation">◙ Asy Syu'araa' [26]: 185 – 188</p></div><div class="verse"><p class="translation">Mereka berkata: \"Sesungguhnya kamu adalah salah seorang dari orang-orang yang kena sihir,{185}</p></div><div class="verse"><p class="translation">Dan kamu tidak lain melainkan seorang manusia seperti kami, dan sesungguhnya kami yakin bahwa kamu benar-benar termasuk orang-orang yang berdusta.{186}</p></div><div class="verse"><p class="translation">Maka jatuhkanlah atas kami gumpalan dari langit, jika kamu termasuk orang-orang yang benar.{187}</p></div><div class="verse"><p class="translation">Syu'aib berkata: \"Tuhanku lebih mengetahui apa yang kamu kerjakan\".{188}</p></div><div class="verse"><p class="translation">10.2.5 Bantahan Syu'aib As. Terhadap Kaumnya</p></div><div class="verse"><p class="translation">◙ Huud [11]: 88 – 90</p></div><div class="verse"><p class="translation">Syu'aib berkata: \"Hai kaumku, bagaimana pikiranmu jika aku mempunyai bukti yang nyata dari Tuhanku dan dianugerahi-Nya aku dari pada-Nya rezeki yang baik (patutkah aku menyalahi perintah-Nya)? Dan aku tidak berkehendak menyalahi kamu (dengan mengerjakan) apa yang aku larang. Aku tidak bermaksud kecuali (mendatangkan) perbaikan selama aku masih berkesanggupan. Dan tidak ada taufik bagiku melainkan dengan (pertolongan) Allah. Hanya kepada Allah aku bertawakkal dan hanya kepada-Nya-lah aku kembali.{88}</p></div><div class="verse"><p class="translation">Hai kaumku, janganlah hendaknya pertentangan antara aku (dengan kamu) menyebabkan kamu menjadi jahat hingga kamu ditimpa azab seperti yang menimpa kaum Nuh atau kaum Hud atau kaum Shaleh, sedang kaum Luth tidak (pula) jauh (tempatnya) dari kamu.{89}</p></div><div class="verse"><p class="translation">Dan mohonlah ampun kepada Tuhanmu kemudian bertobatlah kepada-Nya. Sesungguhnya Tuhanku Maha Penyayang lagi Maha Pengasih.{90}</p></div><div class="verse"><p class="translation">◙ Huud [11]: 92</p></div><div class="verse"><p class="translation">Syu'aib menjawab: \"Hai kaumku, apakah keluargaku lebih terhormat menurut pandanganmu daripada Allah, sedang Allah kamu jadikan sesuatu yang terbuang di belakangmu? Sesungguhnya (pengetahuan) Tuhanku meliputi apa yang kamu kerjakan\".{92}</p></div>`,
                        "quiz": [
                            { "question": "Apa tuduhan pemuka Madyan terhadap Nabi Syu'aib?", "options": ["Tukang sihir / Pendusta", "Pemberontak", "Orang gila", "Pencuri"], "answer": 0 },
                            { "question": "Apa ancaman pemuka Madyan kepada Nabi Syu'aib (Al-A'raaf: 88)?", "options": ["Mengusir dari kota", "Membunuhnya", "Memenjarakannya", "Mendendanya"], "answer": 0 },
                            { "question": "Bagaimana respon kaum Madyan terhadap ajakan beribadah?", "options": ["Menolak dan mengejek", "Menerima dengan baik", "Meminta waktu berpikir", "Diam saja"], "answer": 0 },
                            { "question": "Mereka menganggap Syu'aib sebagai orang yang...", "options": ["Lemah dan tidak berpengaruh", "Kuat dan berkuasa", "Kaya raya", "Sangat pintar"], "answer": 0 },
                            { "question": "Apa tantangan kaum Madyan kepada Syu'aib jika dia benar (Asy-Syu'ara: 187)?", "options": ["Jatuhkan gumpalan dari langit", "Datangkan banjir", "Keluarkan onta dari batu", "Hidupkan orang mati"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 157,
                        "title": "Azab dan Balasan Terhadap Penduduk Madyan",
                        "file": "topic_157.pdf",
                        "content": `<div class="verse"><p class="translation">Syu’aib As. 196 10.3 AZAB DAN BALASAN TERHADAP PENDUDUK MADYAN Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Syu’aib As. 197 10.3.1 Turunnya Azab atas Penduduk Madyan (Ashab al Aikah)</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 91 – 93</p></div><div class="verse"><p class="translation">Kemudian mereka ditimpa gempa, maka jadilah mereka mayat-mayat yang bergelimpangan di dalam rumah-rumah mereka,{91} (Yaitu) orang-orang yang mendustakan Syu'aib seolah-olah mereka belum pernah berdiam di kota itu; orang-orang yang mendustakan Syu'aib mereka itulah orang-orang yang merugi.{92} Maka Syu'aib meninggalkan mereka seraya berkata: \"Hai kaumku, sesungguhnya aku telah menyampaikan kepadamu risalah Tuhanku dan aku telah memberi nasehat kepadamu. Maka bagaimana aku akan bersedih hati terhadap orang-orang yang kafir?\"{93}</p></div><div class="verse"><p class="translation">◙ Huud [11]: 93 – 95</p></div><div class="verse"><p class="translation">Dan (dia berkata): \"Hai kaumku, berbuatlah menurut kemampuanmu, Sesungguhnya akupun berbuat (pula). Kelak kamu akan mengetahui siapa yang akan ditimpa azab yang menghinakannya dan siapa yang berdusta. Dan tunggulah azab (Tuhan), sesungguhnya akupun menunggu bersama kamu.\"{93} Dan tatkala datang azab Kami, Kami selamatkan Syu'aib dan orang- orang yang beriman bersama-sama dengan Dia dengan rahmat dari Kami, dan orang-orang yang zalim dibinasakan oleh satu suara yang mengguntur, lalu jadilah mereka mati bergelimpangan di rumahnya.{94} Seolah-olah mereka belum pernah berdiam di tempat itu. Ingatlah, kebinasaanlah bagi penduduk Madyan sebagaimana kaum Tsamud telah binasa.{95}</p></div><div class="verse"><p class="translation">◙ Al Hijr [15]: 78 – 79</p></div><div class="verse"><p class="translation">Dan sungguh penduduk Aikah111 itu benar-benar kaum yang zalim,{78} Maka Kami membinasakan mereka. Dan sesungguhnya kedua kota112 itu</p></div><div class="verse"><p class="translation">111) Aikah ialah tempat yang berhutan di daerah Madyan. 112) Yakni kota kaum Luth (Sadom) dan Aikah.</p></div><div class="verse"><p class="translation">benar-benar terletak di jalan umum yang terang.{79}</p></div><div class="verse"><p class="translation">◙ Asy Syu'araa' [26]: 189 – 191</p></div><div class="verse"><p class="translation">Kemudian mereka mendustakan Syu'aib, lalu mereka ditimpa 'azab pada hari mereka dinaungi awan. Sesungguhnya azab itu adalah 'azab hari yang besar.{189} Sesungguhnya pada yang demikian itu benar-benar terdapat tanda (kekuasaan Allah), tetapi kebanyakan mereka tidak beriman.{190} Dan sesungguhnya Tuhanmu benar-benar Dialah Yang Maha Perkasa lagi Maha Penyayang.{191}</p></div><div class="verse"><p class="translation">◙ Al 'Ankabuut [29]: 36 – 37</p></div><div class="verse"><p class="translation">Dan (kami telah mengutus) kepada penduduk Madyan, saudara mereka Syu'aib, maka ia berkata: \"Hai kaumku, hendaklah kamu mengabdi kepada Allah, harapkanlah (pahala) hari akhir, dan jangan kamu berkeliaran di muka bumi seraya berbuat kerusakan\".{36} Maka mereka mendustakan Syu'aib, lalu mereka ditimpa gempa yang dahsyat, dan jadilah mereka mayat-mayat yang bergelimpangan di tempat-tempat tinggal mereka.{37}</p></div><div class="verse"><p class="translation">◙ Lihat juga: Al Furqaan [25]: 38 – 39</p></div>`,
                        "quiz": [
                            { "question": "Azab apa yang menimpa penduduk Madyan menurut Al-A'raaf: 91?", "options": ["Gempa dahsyat", "Banjir bandang", "Hujan batu", "Angin topan"], "answer": 0 },
                            { "question": "Azab apa yang menimpa mereka menurut Huud: 94?", "options": ["Suara mengguntur", "Kebakaran besar", "Penyakit kulit", "Kelaparan"], "answer": 0 },
                            { "question": "Azab apa yang menimpa mereka menurut Asy-Syu'ara: 189?", "options": ["Azab hari naungan awan", "Patung emas yang runtuh", "Serangan serangga", "Tenggelam di laut"], "answer": 0 },
                            { "question": "Bagaimana kondisi penduduk Madyan setelah diazab?", "options": ["Mati bergelimpangan di rumahnya", "Hilang tanpa jejak", "Berubah menjadi kera", "Menjadi batu"], "answer": 0 },
                            { "question": "Nasib Madyan disamakan dengan kaum apa dalam surat Huud: 95?", "options": ["Tsamud", "Ad", "Sodom", "Firaun"], "answer": 0 }
                        ]
                    }
                ]
            },
            {
                "id": "subject-6-11",
                "title": "Pokok Bahasan 11: Musa AS & Harun AS",
                "topics": [
                    {
                        "id": 158,
                        "title": "Masa Kecil Musa dan Kekejaman Fir'aun",
                        "file": "topic_158.pdf",
                        "content": `<div class="verse"><p class="translation">Musa As. dan Harun As. 159 11.1 MASA KECIL MUSA, KEKEJAMAN FIR’AUN Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 160 11.1.1 Kesewenang-wenangan Fir’aun</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 3 – 6</p></div><div class="verse"><p class="translation">Kami membacakan kepadamu sebagian dari kisah Musa dan Fir'aun dengan benar untuk orang-orang yang beriman.{3} Sesungguhnya Fir'aun telah berbuat sewenang-wenang di muka bumi dan menjadikan penduduknya berpecah belah, dengan menindas segolongan dari mereka, menyembelih anak laki-laki mereka dan membiarkan hidup anak-anak perempuan mereka. Sesungguhnya Fir'aun termasuk orang-orang yang berbuat kerusakan.{4}</p></div><div class="verse"><p class="translation">Dan Kami hendak memberi karunia kepada orang-orang yang tertindas di bumi (Mesir) itu dan hendak menjadikan mereka pemimpin dan menjadikan mereka orang-orang yang mewarisi (bumi),{5} dan akan Kami teguhkan kedudukan mereka di muka bumi dan akan Kami perlihatkan kepada Fir'aun dan Haman beserta tentaranya apa yang selalu mereka khawatirkan dari mereka itu 196.{6}</p></div><div class="verse"><p class="translation">196) Yang mereka khawatirkan ialah kehancuran kerajaan mereka melalui bani Israel.</p></div><div class="verse"><p class="translation">11.1.2 Kelahiran Musa As. dan Pengasuhannya di Istana Fir'aun</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 7 – 9</p></div><div class="verse"><p class="translation">Dan kami ilhamkan kepada ibu Musa; "Susuilah dia, dan apabila kamu khawatir terhadapnya maka jatuhkahlah dia ke sungai (Nil). Dan janganlah kamu khawatir dan janganlah (pula) bersedih hati, karena sesungguhnya Kami akan mengembalikannya kepadamu, dan menjadikannya salah seorang dari para rasul.{7} Maka dipungutlah ia oleh keluarga Fir'aun yang akibatnya dia menjadi musuh dan kesedihan bagi mereka. Sesungguhnya Fir'aun dan Haman beserta tentaranya adalah orang-orang yang bersalah.{8} Dan berkatalah isteri Fir'aun: "(Ia) adalah penyejuk mata hati bagiku dan bagimu. Janganlah kamu membunuhnya, mudah-mudahan ia bermanfaat kepada kita atau kita ambil ia menjadi anak", sedang mereka tiada menyadari.{9}</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 38 – 39</p></div><div class="verse"><p class="translation">yaitu ketika Kami mengilhamkan kepada ibumu tiap-tiap yang diilhamkan,{38} Yaitu: "Letakkanlah ia (Musa) didalam peti, kemudian lemparkanlah ia ke sungai (Nil), maka pasti sungai itu membawanya ke tepi, supaya diambil oleh (Fir'aun) musuh-Ku dan musuhnya. Dan Aku telah melimpahkan kepadamu kasih sayang yang datang dari-Ku; dan supaya kamu diasuh di atas pengawasan-Ku,{39}</p></div><div class="verse"><p class="translation">11.1.3 Musa As. Kembali ke Pangkuan Ibunya</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 10 – 13</p></div><div class="verse"><p class="translation">Dan menjadi kosonglah hati ibu Musa. Sesungguhnya hampir saja ia menyatakan rahasia tentang Musa, seandainya tidak Kami teguhkan hatinya, supaya ia termasuk orang-orang yang percaya (kepada janji Allah).{10} Dan berkatalah ibu Musa kepada saudara Musa yang perempuan: "Ikutilah dia" Maka kelihatanlah olehnya Musa dari jauh, sedang mereka tidak mengetahuinya.{11} dan Kami cegah Musa menyusu kepada wanita-wanita yang menyusui(nya) sebelum itu; maka berkatalah saudara perempuan Musa: "Maukah kamu aku tunjukkan kepadamu ahlul bait yang akan memeliharanya untukmu dan mereka dapat berlaku baik kepadanya?".{12} Maka kami kembalikan Musa kepada ibunya, supaya senang hatinya dan tidak berduka cita dan supaya ia mengetahui bahwa janji Allah itu adalah benar, tetapi kebanyakan manusia tidak mengetahuinya.{13}</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 40</p></div><div class="verse"><p class="translation">(yaitu) ketika saudara perempuanmu berjalan, lalu ia berkata kepada (keluarga Fir'aun): "Bolehkah saya menunjukkan kepadamu orang yang akan memeliharanya?" Maka Kami mengembalikanmu kepada ibumu, agar senang hatinya dan tidak berduka cita...</p></div>`,
                        "quiz": [
                            { "question": "Apa kezaliman yang dilakukan Fir'aun terhadap Bani Israil (Al-Qashash: 4)?", "options": ["Menyembelih bayi laki-laki", "Menaikkan pajak", "Melarang ibadah", "Mengusir dari Mesir"], "answer": 0 },
                            { "question": "Apa yang diilhamkan Allah kepada ibu Musa saat khawatir bayinya dibunuh?", "options": ["Hanyutkan ke sungai Nil", "Sembunyikan di gua", "Larikan ke negeri lain", "Serahkan ke tetangga"], "answer": 0 },
                            { "question": "Siapakah yang memungut bayi Musa dari sungai?", "options": ["Keluarga Fir'aun", "Nelayan", "Pedagang budak", "Bani Israil"], "answer": 0 },
                            { "question": "Siapakah wanita yang akhirnya menyusui Musa?", "options": ["Ibu kandungnya sendiri", "Istri Fir'aun", "Wanita Mesir", "Saudara perempuannya"], "answer": 0 },
                            { "question": "Apa alasan istri Fir'aun melarang membunuh bayi Musa?", "options": ["Sebagai penyejuk hati dan anak angkat", "Karena kasihan", "Karena perintah raja", "Karena bayinya tampan"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 159,
                        "title": "Pertemuan Musa dengan Keluarga Syu'aib AS",
                        "file": "topic_159.pdf",
                        "content": `<div class="verse"><p class="translation">Musa As. dan Harun As. 168 11.2 PERTEMUAN MUSA DENGAN KELUARGA SYUAIB AS Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 169 11.2.1 Musa Bertemu dengan Dua Puteri Syu’aib As.</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 23 – 24</p></div><div class="verse"><p class="translation">Dan tatkala ia sampai di sumber air negeri Madyan ia menjumpai di sana sekumpulan orang yang sedang meminumkan (ternaknya), dan ia menjumpai di belakang orang banyak itu, dua orang wanita yang sedang menghambat (ternaknya). Musa berkata: "Apakah maksudmu (dengan berbuat begitu)?" Kedua wanita itu menjawab: "Kami tidak dapat meminumkan (ternak kami), sebelum pengembala-pengembala itu memulangkan (ternaknya), sedang bapak kami adalah orang tua yang telah lanjut umurnya".{23} Maka Musa memberi minum ternak itu untuk (menolong) keduanya, kemudian dia kembali ke tempat yang teduh lalu berdoa: "Ya Tuhanku sesungguhnya aku sangat memerlukan sesuatu kebaikan yang Engkau turunkan kepadaku".{24}</p></div><div class="verse"><p class="translation">11.2.2 Musa As. Bertemu dengan Syu’aib As.</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 25</p></div><div class="verse"><p class="translation">Kemudian datanglah kepada Musa salah seorang dari kedua wanita itu berjalan kemalu-maluan, ia berkata: "Sesungguhnya bapakku memanggil kamu agar ia memberikan balasan terhadap (kebaikan)mu memberi minum (ternak) kami". Maka tatkala Musa mendatangi bapaknya (Syu'aib) dan menceritakan kepadanya cerita (mengenai dirinya), Syu'aib berkata: "Janganlah kamu takut. Kamu telah selamat dari orang-orang yang zalim itu".{25}</p></div><div class="verse"><p class="translation">11.2.3 Musa As. Menikah dengan salah Seorang Puteri Syu’aib As.</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 26 – 28</p></div><div class="verse"><p class="translation">Salah seorang dari kedua wanita itu berkata: "Ya bapakku ambillah ia sebagai orang yang bekerja (pada kita), karena sesungguhnya orang yang paling baik yang kamu ambil untuk bekerja (pada kita) ialah orang yang kuat lagi dapat dipercaya".{26} Berkatalah dia (Syu'aib): "Sesungguhnya aku bermaksud menikahkan kamu dengan salah seorang dari kedua anakku ini, atas dasar bahwa kamu bekerja denganku delapan tahun dan jika kamu cukupkan sepuluh tahun maka itu adalah (suatu kebaikan) dari kamu, maka aku tidak hendak memberati kamu. Dan kamu Insya Allah akan mendapatiku termasuk orang-orang yang baik".{27} Dia (Musa) berkata: "Itulah (perjanjian) antara aku dan kamu. Mana saja dari kedua waktu yang ditentukan itu aku sempurnakan, maka tidak ada tuntutan tambahan atas diriku (lagi). Dan Allah adalah saksi atas apa yang kita ucapkan".{28}</p></div>`,
                        "quiz": [
                            { "question": "Mengapa Musa melarikan diri ke negeri Madyan?", "options": ["Karena tidak sengaja membunuh orang Mesir", "Karena diusir Fir'aun", "Mencari ilmu", "Berdagang"], "answer": 0 },
                            { "question": "Apa pertolongan yang diberikan Musa kepada dua wanita di Madyan?", "options": ["Memberi minum ternak mereka", "Mengusir penjahat", "Menunjukkan jalan", "Membawakan air ke rumah"], "answer": 0 },
                            { "question": "Kenapa kedua wanita itu tidak bisa memberi minum ternaknya?", "options": ["Menunggu penggembala lain selesai & ayah lanjut usia", "Sumurnya kering", "Ternaknya sakit", "Dilarang warga"], "answer": 0 },
                            { "question": "Sifat apa yang dipuji oleh putri Syu'aib tentang Musa (Al-Qashash: 26)?", "options": ["Kuat dan dapat dipercaya (Al-Qawiy Al-Amin)", "Kaya dan dermawan", "Pandai dan cerdas", "Sabar dan lemah lembut"], "answer": 0 },
                            { "question": "Apa mahar yang diminta Syu'aib untuk menikahkan putrinya dengan Musa?", "options": ["Bekerja selama 8-10 tahun", "Emas dan perak", "Seratus ekor kambing", "Membangun rumah"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 160,
                        "title": "Kenabian Musa AS",
                        "file": "topic_160.pdf",
                        "content": `<div class="verse"><p class="translation">Musa As. dan Harun As. 172 11.3 KENABIAN MUSA AS Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 173 11.3.1 Musa As. Diangkat Menjadi Nabi dan Rasul</p></div><div class="verse"><p class="translation">◙ Maryam [19]: 51 – 53</p></div><div class="verse"><p class="translation">Dan ceritakanlah (hai Muhammad kepada mereka, kisah) Musa di dalam Al Kitab (Al Quran) ini. Sesungguhnya ia adalah seorang yang dipilih dan seorang rasul dan nabi.{51} Dan Kami telah memanggilnya dari sebelah kanan gunung Thur dan Kami telah mendekatkannya kepada Kami di waktu dia bermunajat (kepada Kami).{52} Dan Kami telah menganugerahkan kepadanya sebagian rahmat Kami, yaitu saudaranya, Harun menjadi seorang nabi.{53}</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 29 – 30</p></div><div class="verse"><p class="translation">Maka tatkala Musa telah menyelesaikan waktu yang ditentukan dan dia berangkat dengan keluarganya, dilihatnyalah api di lereng gunung ia berkata kepada keluarganya: "Tunggulah (di sini), sesungguhnya aku melihat api, mudah-mudahan aku dapat membawa suatu berita kepadamu dari (tempat) api itu atau (membawa) sesuluh api, agar kamu dapat menghangatkan badan".{29} Maka tatkala Musa sampai ke (tempat) api itu, diserulah dia dari (arah) pinggir lembah yang diberkahi, dari sebatang pohon kayu, yaitu: "Ya Musa, sesungguhnya Aku adalah Allah, Tuhan semesta alam.{30}</p></div><div class="verse"><p class="translation">11.3.2 Mukjizat Nabi Musa As.</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 31 – 32</p></div><div class="verse"><p class="translation">dan lemparkanlah tongkatmu. Maka tatkala (tongkat itu) menjadi ular dan bergerak-gerak seolah-olah seekor ular yang gesit, larilah ia berbalik ke belakang tanpa menoleh. "Wahai Musa, datanglah kepada-Ku dan janganlah kamu takut. Sesungguhnya kamu termasuk orang-orang yang aman.{31} Masukkanlah tanganmu ke leher bajumu, niscaya ia keluar putih tidak bercacat bukan karena penyakit, dan dekapkanlah kedua tanganmu (ke dada)mu bila ketakutan..."{32}</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 17 – 23</p></div><div class="verse"><p class="translation">Apakah itu yang di tangan kananmu, hai Musa?{17} Berkata Musa: "Ini adalah tongkatku, aku bertelekan padanya, dan aku pukul (daun) dengannya untuk kambingku, dan bagiku ada lagi keperluan yang lain padanya".{18} Allah berfirman: "Lemparkanlah ia, hai Musa!"{19} Lalu dilemparkannyalah tongkat itu, maka tiba-tiba ia menjadi seekor ular yang merayap dengan cepat.{20} Allah berfirman: "Peganglah ia dan jangan takut, Kami akan mengembalikannya kepada keadaannya semula,{21} Dan kepitkanlah tanganmu ke ketiakmu, niscaya ia keluar menjadi putih cemerlang tanpa cacad, sebagai mukjizat yang lain (pula),{22} untuk Kami perlihatkan kepadamu sebahagian dari tanda-tanda kekuasaan Kami yang sangat besar,{23}</p></div><div class="verse"><p class="translation">11.3.3 Doa Nabi Musa As.</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 25 – 35</p></div><div class="verse"><p class="translation">Berkata Musa: "Ya Tuhanku, lapangkanlah untukku dadaku,{25} dan mudahkanlah untukku urusanku,{26} dan lepaskanlah kekakuan dari lidahku,{27} supaya mereka mengerti perkataanku,{28} dan jadikanlah untukku seorang pembantu dari keluargaku,{29} (yaitu) Harun, saudaraku,{30} teguhkanlah dengan dia kekuatanku,{31} dan jadikankanlah dia sekutu dalam urusanku,{32} supaya kami banyak bertasbih kepada Engkau,{33} dan banyak mengingat Engkau.{34} Sesungguhnya Engkau adalah Maha Melihat (keadaan) kami".{35}</p></div>`,
                        "quiz": [
                            { "question": "Apa yang dilihat Musa di lereng gunung Thur?", "options": ["Api", "Cahaya", "Air", "Malaikat"], "answer": 0 },
                            { "question": "Apa mukjizat pertama yang diberikan Allah kepada Musa?", "options": ["Tongkat menjadi ular", "Membelah laut", "Belalang", "Banjir darah"], "answer": 0 },
                            { "question": "Apa mukjizat kedua yang ada pada tangan Musa?", "options": ["Tangan menjadi putih bercahaya", "Tangan menjadi emas", "Tangan menjadi api", "Tangan menjadi air"], "answer": 0 },
                            { "question": "Siapakah yang diminta Musa menjadi pembantunya dalam berdakwah?", "options": ["Harun saudaranya", "Yusya bin Nun", "Syu'aib", "Istri Fir'aun"], "answer": 0 },
                            { "question": "Apa doa terkenal Nabi Musa saat diangkat menjadi Rasul (Thaahaa: 25)?", "options": ["Rabbishrahli shadri (Ya Tuhanku lapangkanlah dadaku)", "Rabbana aatina fiddunya hasanah", "Rabbi zidni 'ilman", "Allahumma lakal hamdu"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 161,
                        "title": "Dakwah Musa AS Kepada Fir'aun",
                        "file": "topic_161.pdf",
                        "content": `<div class="verse"><p class="translation">Musa As. dan Harun As. 181 11.4 DAKWAH MUSA AS KEPADA FIR’AUN Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 182 11.4.1 Perintah Berdakwah kepada Fir'aun dan Kaumnya</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 103 – 105</p></div><div class="verse"><p class="translation">Kemudian Kami utus Musa sesudah rasul-rasul itu dengan membawa ayat-ayat Kami kepada Fir'aun dan pemuka-pemuka kaumnya, lalu mereka mengingkari ayat-ayat itu. Maka perhatikanlah bagaimana kesudahan orang-orang yang membuat kerusakan.{103} Dan Musa berkata: "Hai Fir'aun, sesungguhnya aku ini adalah seorang utusan dari Tuhan semesta alam,{104} wajib atasku tidak mengatakan sesuatu terhadap Allah, kecuali yang hak. Sesungguhnya aku datang kepadamu dengan membawa bukti yang nyata dari Tuhanmu, maka lepaskanlah Bani Israil (pergi) bersama aku".{105}</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 43 – 44</p></div><div class="verse"><p class="translation">Pergilah kamu berdua kepada Fir'aun, sesungguhnya dia telah melampaui batas;{43} maka berbicaralah kamu berdua kepadanya dengan kata-kata yang lemah lembut, mudah-mudahan ia ingat atau takut".{44}</p></div><div class="verse"><p class="translation">11.4.2 Penolakan Fir’aun terhadap Dakwah Musa As.</p></div><div class="verse"><p class="translation">◙ Al Qashash [28]: 36 – 38</p></div><div class="verse"><p class="translation">Maka tatkala Musa datang kepada mereka dengan (membawa) mukjizat-mukjizat Kami yang nyata, mereka berkata: "Ini tidak lain hanyalah sihir yang dibuat-buat dan kami belum pernah mendengar (seruan) ini pada nenek moyang kami dahulu".{36} Musa menjawab: "Tuhanku lebih mengetahui siapa yang (patut) membawa petunjuk dari sisi-Nya dan siapa yang akan mendapat kesudahan (yang baik) di negeri akhirat. Sesungguhnya orang-orang yang zalim tidak akan mendapat kemenangan".{37} Dan berkata Fir'aun: "Hai pembesar kaumku, aku tidak mengetahui tuhan bagimu selain aku. Maka bakarlah hai Haman untukku tanah liat, kemudian buatkanlah untukku bangunan yang tinggi supaya aku dapat naik melihat Tuhan Musa, dan sesungguhnya aku benar-benar yakin bahwa dia termasuk orang-orang pendusta".{38}</p></div><div class="verse"><p class="translation">11.4.3 Perlawanan Para Ahli Sihir Fir’aun</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 115 – 122</p></div><div class="verse"><p class="translation">Ahli-ahli sihir berkata: "Hai Musa, kamukah yang akan melemparkan lebih dahulu, ataukah kami yang akan melemparkan?"{115} Musa menjawab: "Lemparkanlah (lebih dahulu)!" Maka tatkala mereka melemparkan, mereka menyulap mata orang dan menjadikan orang banyak itu takut, serta mereka mendatangkan sihir yang besar (menakjubkan).{116} Dan Kami wahyukan kepada Musa: "Lemparkanlah tongkatmu!". Maka sekonyong-konyong tongkat itu menelan apa yang mereka sulapkan.{117} Karena itu nyatalah yang benar dan batallah yang selalu mereka kerjakan.{118} Maka mereka kalah di tempat itu dan jadilah mereka orang-orang yang hina.{119} Dan ahli-ahli sihir itu serta merta meniarapkan diri dengan bersujud.{120} Mereka berkata: "Kami beriman kepada Tuhan semesta alam,{121} "(yaitu) Tuhan Musa dan Harun".{122}</p></div><div class="verse"><p class="translation">11.4.4 Azab Bagi Fir’aun dan Kaumnya</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 130</p></div><div class="verse"><p class="translation">Dan sesungguhnya Kami telah menghukum (Fir'aun dan) kaumnya dengan (mendatangkan) musim kemarau yang panjang dan kekurangan buah-buahan, supaya mereka mengambil pelajaran.{130}</p></div>`,
                        "quiz": [
                            { "question": "Bagaimana perintah Allah kepada Musa dan Harun saat berbicara kepada Fir'aun (Thaahaa: 44)?", "options": ["Berbicara dengan lemah lembut", "Berbicara dengan kasar", "Langsung memerangi", "Diam saja"], "answer": 0 },
                            { "question": "Apa permintaan Musa kepada Fir'aun terkait Bani Israil?", "options": ["Lepaskan Bani Israil pergi bersamanya", "Jadikan Bani Israil raja", "Berikan harta kepada Bani Israil", "Bunuh semua Bani Israil"], "answer": 0 },
                            { "question": "Apa yang dilakukan tongkat Musa terhadap sihir para penyihir Fir'aun?", "options": ["Menelan apa yang mereka sulapkan", "Berubah menjadi air", "Terbakar api", "Menjadi patung"], "answer": 0 },
                            { "question": "Bagaimana reaksi para penyihir setelah melihat mukjizat Musa?", "options": ["Langsung bersujud dan beriman", "Marah dan menyerang Musa", "Lari ketakutan", "Meminta bayaran lebih"], "answer": 0 },
                            { "question": "Apa hukuman awal yang ditimpakan Allah kepada kaum Fir'aun (Al-A'raaf: 130)?", "options": ["Kemarau panjang dan kekurangan buah-buahan", "Banjir besar", "Hujan api", "Gempa bumi"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 162,
                        "title": "Dakwah Musa AS Kepada Bani Israil",
                        "file": "topic_162.pdf",
                        "content": `<div class="verse"><p class="translation">Musa As. dan Harun As. 233 11.5 DAKWAH MUSA AS KEPADA BANI ISRAIL Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 234 11.5.1 Karunia dan Nikmat bagi Bani Israil</p></div><div class="verse"><p class="translation">◙ Al Baqarah [2]: 47</p></div><div class="verse"><p class="translation">Hai Bani Israil, ingatlah akan nikmat-Ku yang telah Aku anugerahkan kepadamu dan (ingatlah pula) bahwasanya Aku telah melebihkan kamu atas segala umat.{47}</p></div><div class="verse"><p class="translation">◙ Al Maa'idah [5]: 20</p></div><div class="verse"><p class="translation">Dan (ingatlah) ketika Musa berkata kepada kaumnya: \"Hai kaumku, ingatlah nikmat Allah atasmu ketika Dia mengangkat nabi nabi diantaramu, dan dijadikan-Nya kamu orang-orang merdeka, dan diberikan-Nya kepadamu apa yang belum pernah diberikan-Nya kepada seorangpun diantara umat-umat yang lain\".{20}</p></div><div class="verse"><p class="translation">11.5.2 Penyelamatan Bani Israil dari Kejaran Fir’aun</p></div><div class="verse"><p class="translation">◙ Asy Syu'araa' [26]: 63 – 66</p></div><div class="verse"><p class="translation">Lalu Kami wahyukan kepada Musa: \"Pukullah lautan itu dengan tongkatmu\". Maka terbelahlah lautan itu dan tiap-tiap belahan adalah seperti gunung yang besar.{63} Dan di sanalah Kami dekatkan golongan yang lain.{64} Dan Kami selamatkan Musa dan orang-orang yang besertanya semuanya.{65} Dan Kami tenggelamkan golongan yang lain itu.{66}</p></div><div class="verse"><p class="translation">◙ Al Baqarah [2]: 50</p></div><div class="verse"><p class="translation">Dan (ingatlah), ketika Kami belah laut untukmu, lalu Kami selamatkan kamu dan Kami tenggelamkan (Fir'aun) dan pengikut-pengikutnya sedang kamu sendiri menyaksikan.{50}</p></div><div class="verse"><p class="translation">11.5.3 Perilaku Bani Israil Setelah Diselamatkan</p></div><div class="verse"><p class="translation">◙ Al Baqarah [2]: 61</p></div><div class="verse"><p class="translation">Dan (ingatlah), ketika kamu berkata: \"Hai Musa, kami tidak bisa sabar (tahan) dengan satu macam makanan saja. Sebab itu mohonkanlah untuk kami kepada Tuhanmu, agar Dia mengeluarkan bagi kami dari apa yang ditumbuhkan bumi, yaitu sayur-mayurnya, ketimunnya, bawang putihnya, kacang adasnya, dan bawang merahnya. Musa berkata: \"Maukah kamu mengambil yang rendah sebagai pengganti yang lebih baik? Pergilah kamu ke suatu kota, pasti kamu memperoleh apa yang kamu minta\". Lalu ditimpahkanlah kepada mereka nista dan kehinaan, serta mereka mendapat kemurkaan dari Allah. Hal itu (terjadi) karena mereka selalu mengingkari ayat-ayat Allah dan membunuh para Nabi yang memang tidak dibenarkan. Demikian itu (terjadi) karena mereka selalu berbuat durhaka dan melampaui batas.{61}</p></div>`,
                        "quiz": [
                            { "question": "Apa perintah Allah kepada Musa saat terdesak di depan laut (Asy-Syu'ara: 63)?", "options": ["Pukullah lautan itu dengan tongkatmu", "Berdoalah minta sayap", "Buatlah perahu", "Menyerah saja"], "answer": 0 },
                            { "question": "Bagaimana keadaan laut setelah dipukul tongkat Musa?", "options": ["Terbelah seperti gunung besar", "Menjadi es", "Kering kerontang selamanya", "Mendidih"], "answer": 0 },
                            { "question": "Apa yang terjadi pada Fir'aun dan tentaranya di laut?", "options": ["Tenggelam semuanya", "Berhasil mengejar", "Selamat berenang", "Kembali ke Mesir"], "answer": 0 },
                            { "question": "Makanan apa yang diminta Bani Israil karena bosan dengan Manna dan Salwa?", "options": ["Sayur, ketimun, bawang, kacang adas", "Daging sapi", "Buah-buahan surga", "Ikan laut"], "answer": 0 },
                            { "question": "Apa yang ditimpakan Allah kepada mereka karena ketidaksabaran dan kedurhakaan mereka?", "options": ["Nista, kehinaan, dan kemurkaan Allah", "Kekayaan berlimpah", "Umur panjang", "Kemenangan perang"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 163,
                        "title": "Pengkhianatan Samiri & Penyembahan Anak Sapi",
                        "file": "topic_163.pdf",
                        "content": `< div class= "verse" > <p class="translation">Musa As. dan Harun As. 242 11.6 PENGKHIANATAN SAMIRI, PENYEMBAHAN ANAK SAPI Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 243 11.6.1 Musa As. Mewakilkan Kepemimpinan kepada Harun As.</p></div ><div class="verse"><p class="translation">◙ Al A'raaf [7]: 142</p></div><div class="verse"><p class="translation">Dan Kami telah menjanjikan kepada Musa (memberikan Taurat) sesudah berlalu waktu tiga puluh malam, dan Kami sempurnakan jumlah malam itu dengan sepuluh (malam lagi), maka sempurnalah waktu yang telah ditentukan Tuhannya empat puluh malam. Dan berkata Musa kepada saudaranya yaitu Harun: \"Gantikanlah aku dalam (memimpin) kaumku, dan perbaikilah, dan janganlah kamu mengikuti jalan orang-orang yang membuat kerusakan\".{142}</p></div><div class="verse"><p class="translation">11.6.2 Samiri Membuat Patung Anak Sapi</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 87 – 88</p></div><div class="verse"><p class="translation">Mereka berkata: \"Kami sekali-kali tidak melanggar perjanjianmu dengan kemauan kami sendiri, tetapi kami disuruh membawa beban-beban dari perhiasan kaum itu, maka kami telah melemparkannya, dan demikian pula Samiri melemparkannya\",{87} kemudian Samiri mengeluarkan untuk mereka (dari lobang itu) anak lembu yang bertubuh dan bersuara, maka mereka berkata: \"Inilah Tuhanmu dan Tuhan Musa, tetapi Musa telah lupa\".{88}</p></div><div class="verse"><p class="translation">11.6.3 Kemarahan Musa As.</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 92 – 94</p></div><div class="verse"><p class="translation">Berkata Musa: \"Hai Harun, apa yang menghalangi kamu ketika kamu melihat mereka telah sesat,{92} (sehingga) kamu tidak mengikuti aku? Maka apakah kamu telah (sengaja) mendurhakai perintahku?\"{93} Harun menjawab: \"Hai putera ibuku, janganlah kamu pegang janggutku dan jangan (pula) kepalaku; sesungguhnya aku khawatir bahwa kamu akan berkata (kepadaku): \"Kamu telah memecah antara Bani Israil dan kamu tidak memelihara amanatku\".{94}</p></div><div class="verse"><p class="translation">11.6.4 Hukuman Bagi Samiri</p></div><div class="verse"><p class="translation">◙ Thaahaa [20]: 97</p></div><div class="verse"><p class="translation">Berkata Musa: \"Pergilah kamu, maka sesungguhnya bagimu di dalam kehidupan di dunia ini (hanya dapat) mengatakan: \"Janganlah menyentuh (aku)\". Dan sesungguhnya bagimu hukuman (di akhirat) yang kamu sekali-kali tidak dapat menghindarinya, dan lihatlah tuhanmu itu yang kamu tetap menyembahnya. Sesungguhnya kami akan membakarnya, kemudian kami sungguh-sungguh akan menghamburkannya ke dalam laut (berupa abu yang berserakan).{97}</p></div>`,
                        "quiz": [
                            { "question": "Berapa lama Musa meninggalkan kaumnya untuk bermunajat di gunung bukit (Al-A'raaf: 142)?", "options": ["40 malam", "30 malam", "10 malam", "7 malam"], "answer": 0 },
                            { "question": "Siapakah yang membuat patung anak sapi emas untuk disembah Bani Israil?", "options": ["Samiri", "Qarun", "Haman", "Harun"], "answer": 0 },
                            { "question": "Apa keanehan patung anak sapi buatan Samiri?", "options": ["Bertubuh dan bisa bersuara (melenguh)", "Bisa berjalan", "Bisa terbang", "Bisa makan"], "answer": 0 },
                            { "question": "Apa reaksi Musa kepada Harun saat melihat kaumnya menyembah sapi?", "options": ["Marah dan memegang janggut/kepala Harun", "Memuji Harun", "Diam saja", "Minta maaf"], "answer": 0 },
                            { "question": "Apa hukuman Samiri di dunia menurut perkataan Musa (Thaahaa: 97)?", "options": ["Berkata 'Laa Misaas' (Jangan sentuh aku) seumur hidup", "Dihukum mati", "Dipenjara", "Diasingkan ke hutan"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 164,
                        "title": "Pelanggaran Bani Israil di Hari Sabat",
                        "file": "topic_164.pdf",
                        "content": `< div class= "verse" > <p class="translation">Musa As. dan Harun As. 257 11.7 PELANGGARAN BANI ISRAIL DI HARI SABAT (SABTU) Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 258 11.7.1 Perintah untuk Menghormati Hari Sabat (Sabtu)</p></div ><div class="verse"><p class="translation">◙ An Nahl [16]: 124</p></div><div class="verse"><p class="translation">Sesungguhnya diwajibkan (menghormati) hari Sabtu atas orang-orang (Yahudi) yang berselisih padanya. Dan sesungguhnya Tuhanmu benar-benar akan memberi putusan di antara mereka di hari kiamat terhadap apa yang telah mereka perselisihkan itu.{124}</p></div><div class="verse"><p class="translation">11.7.2 Ujian Allah Bagi Bani Israil di Hari Sabat</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 163</p></div><div class="verse"><p class="translation">Dan tanyakanlah kepada Bani Israil tentang negeri yang terletak di dekat laut ketika mereka melanggar aturan pada hari Sabtu, di waktu datang kepada mereka ikan-ikan (yang berada di sekitar) mereka terapung-apung di permukaan air, dan di hari-hari yang bukan Sabtu, ikan-ikan itu tidak datang kepada mereka. Demikianlah Kami mencoba mereka disebabkan mereka berlaku fasik.{163}</p></div><div class="verse"><p class="translation">11.7.3 Hukuman Bagi Pelanggar Hari Sabat</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 166</p></div><div class="verse"><p class="translation">Maka tatkala mereka bersikap sombong terhadap apa yang dilarang mereka mengerjakannya, Kami katakan kepadanya: \"Jadilah kamu kera yang hina\".{166}</p></div><div class="verse"><p class="translation">◙ Al Baqarah [2]: 65</p></div><div class="verse"><p class="translation">Dan sesungguhnya telah kamu ketahui orang-orang yang melanggar diantaramu pada hari Sabtu, lalu Kami berfirman kepada mereka: \"Jadilah kamu kera yang hina\".{65}</p></div><div class="verse"><p class="translation">◙ An Nisaa' [4]: 47</p></div><div class="verse"><p class="translation">...atau Kami laknat mereka sebagaimana Kami telah melaknat orang-orang (yang berbuat maksiat) pada hari Sabtu, dan ketetapan Allah pasti berlaku.{47}</p></div>`,
                        "quiz": [
                            { "question": "Hati apa yang dikhususkan bagi Bani Israil untuk beribadah dan dilarang bekerja?", "options": ["Sabtu (Sabat)", "Jumat", "Minggu", "Senin"], "answer": 0 },
                            { "question": "Apa ujian yang diberikan Allah pada hari Sabat (Al-A'raaf: 163)?", "options": ["Ikan-ikan muncul terapung banyak sekali", "Hujan emas", "Musuh menyerang", "Tanah menjadi subur"], "answer": 0 },
                            { "question": "Bagaimana kondisi ikan di hari selain Sabtu?", "options": ["Tidak datang kepada mereka", "Sama banyaknya", "Lebih besar", "Mati semua"], "answer": 0 },
                            { "question": "Apa hukuman bagi mereka yang melanggar larangan hari Sabat?", "options": ["Dikutuk menjadi kera yang hina", "Diberi penyakit kusta", "Ditenggelamkan", "Dibutakan matanya"], "answer": 0 },
                            { "question": "Sifat apa yang menyebabkan mereka dicoba dan dihukum (Al-A'raaf: 163, 166)?", "options": ["Fasik dan sombong", "Bodoh", "Miskin", "Lemah"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 165,
                        "title": "Bani Israil dan Penyembelihan Sapi Betina",
                        "file": "topic_165.pdf",
                        "content": `< div class= "verse" > <p class="translation">Musa As. dan Harun As. 262 11.8 BANI ISRAIL DAN PENYEMBELIHAN SAPI BETINA Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 263 11.8.1 Perintah untuk Menyembelih Sapi Betina</p></div ><div class="verse"><p class="translation">◙ Al Baqarah [2]: 67</p></div><div class="verse"><p class="translation">Dan (ingatlah), ketika Musa berkata kepada kaumnya: \"Sesungguhnya Allah menyuruh kamu menyembelih seekor sapi betina\". Mereka berkata: \"Apakah kamu hendak menjadikan kami buah ejekan?\" Musa menjawab: \"Aku berlindung kepada Allah agar tidak menjadi salah seorang dari orang-orang yang jahil\".{67}</p></div><div class="verse"><p class="translation">11.8.2 Bani Israil Mempersulit Diri Sendiri</p></div><div class="verse"><p class="translation">◙ Al Baqarah [2]: 68 – 71</p></div><div class="verse"><p class="translation">Mereka menjawab: \"Mohonkanlah kepada Tuhanmu untuk kami, agar Dia menerangkan kepada kami; sapi betina apakah itu\". Musa menjawab: \"Sesungguhnya Allah berfirman bahwa sapi betina itu adalah sapi betina yang tidak tua dan tidak muda; pertengahan antara itu; maka kerjakanlah apa yang diperintahkan kepadamu\".{68} Mereka berkata: \"Mohonkanlah kepada Tuhanmu untuk kami agar Dia menerangkan kepada kami apa warnanya\". Musa menjawab: \"Sesungguhnya Allah berfirman bahwa sapi betina itu adalah sapi betina yang kuning, yang kuning tua warnanya, lagi menyenangkan orang-orang yang memandangnya\".{69} Mereka berkata: \"Mohonkanlah kepada Tuhanmu untuk kami agar Dia menerangkan kepada kami bagaimana hakikat sapi betina itu, karena sesungguhnya sapi itu (masih) samar bagi kami dan sesungguhnya kami insya Allah akan mendapat petunjuk (untuk memperoleh sapi itu)\".{70} Musa menjawab: \"Sesungguhnya Allah berfirman bahwa sapi betina itu adalah sapi betina yang belum pernah dipakai untuk membajak tanah dan tidak pula untuk mengairi tanaman, tidak bercacat, tidak ada belangnya\". Mereka berkata: \"Sekarang barulah kamu menerangkan hakikat sapi betina yang sebenarnya\". Kemudian mereka menyembelihnya dan hampir saja mereka tidak melaksanakan perintah itu.{71}</p></div><div class="verse"><p class="translation">11.8.3 Terungkapnya Kasus Pembunuhan</p></div><div class="verse"><p class="translation">◙ Al Baqarah [2]: 72 – 73</p></div><div class="verse"><p class="translation">Dan (ingatlah), ketika kamu membunuh seorang manusia lalu kamu saling tuduh menuduh tentang itu. Dan Allah hendak menyingkapkan apa yang selama ini kamu sembunyikan.{72} Lalu Kami berfirman: \"Pukullah mayat itu dengan sebagian anggota sapi betina itu!\" Demikianlah Allah menghidupkan kembali orang-orang yang telah mati, dan memperlihatkan padamu tanda-tanda kekuasaan-Nya agar kamu mengerti.{73}</p></div>`,
                        "quiz": [
                            { "question": "Apa tujuan perintah menyembelih sapi betina dalam surat Al-Baqarah?", "options": ["Untuk mengungkap kasus pembunuhan", "Untuk pesta makan", "Untuk kurban rutin", "Untuk membayar denda"], "answer": 0 },
                            { "question": "Apa respon awal Bani Israil saat diperintah menyembelih sapi?", "options": ["Mengira Musa mengejek mereka", "Langsung menuruti", "Menolak keras", "Tertawa"], "answer": 0 },
                            { "question": "Apa warna sapi yang diminta Allah setelah mereka bertanya-tanya?", "options": ["Kuning tua yang menyenangkan dipandang", "Hitam legam", "Putih bersih", "Merah bata"], "answer": 0 },
                            { "question": "Bagaimana ciri fisik sapi tersebut yang akhirnya dijelaskan?", "options": ["Tidak pernah membajak/mengairi, tidak cacat, tidak belang", "Sapi perah yang gemuk", "Anak sapi yang baru lahir", "Sapi liar dari hutan"], "answer": 0 },
                            { "question": "Bagaimana cara mayat itu dihidupkan kembali untuk memberitahu pembunuhnya?", "options": ["Dipukul dengan sebagian anggota sapi yang disembelih", "Dibacakan mantra", "Diberi minum darah sapi", "Dibakar"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 166,
                        "title": "Penataan Kembali Bani Israil Menjadi 12 Suku",
                        "file": "topic_166.pdf",
                        "content": `< div class= "verse" > <p class="translation">Musa As. dan Harun As. 267 11.9 PENATAAN KEMBALI BANI ISRAIL MENJADI 12 SUKU Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis. Musa As. dan Harun As. 268 11.9.1 12 Mata Air dan Pembagian Bani Israil Menjadi 12 Suku</p></div ><div class="verse"><p class="translation">◙ Al Baqarah [2]: 60</p></div><div class="verse"><p class="translation">Dan (ingatlah) ketika Musa memohon air untuk kaumnya, lalu Kami berfirman: \"Pukullah batu itu dengan tongkatmu\". Lalu memancarlah darinya dua belas mata air. Sungguh tiap-tiap suku telah mengetahui tempat minumnya (masing-masing)200. Makan dan minumlah rezeki (yang diberikan) Allah, dan janganlah kamu berkeliaran di muka bumi dengan berbuat kerusakan.{60}</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 160</p></div><div class="verse"><p class="translation">Dan mereka Kami bagi menjadi dua belas suku yang masing-masing berjumlah besar dan Kami wahyukan kepada Musa ketika kaumnya meminta air kepadanya: \"Pukullah batu itu dengan tongkatmu!.” Maka memancarlah darinya dua belas mata air. Sungguh tiap suku tahu tempat minum masing-masing. Dan Kami naungkan awan di atas mereka dan Kami turunkan kepada mereka manna dan salwa...</p></div><div class="verse"><p class="translation">11.9.2 Bani Israil Terpecah-pecah Menjadi Beberapa Golongan</p></div><div class="verse"><p class="translation">◙ Al A'raaf [7]: 168</p></div><div class="verse"><p class="translation">Dan Kami bagi-bagi mereka di dunia ini menjadi beberapa golongan; di antaranya ada orang-orang yang saleh dan di antaranya ada yang tidak demikian. Dan Kami coba mereka dengan (nikmat) yang baik-baik dan (bencana) yang buruk-buruk, agar mereka kembali.{168}</p></div>`,
                        "quiz": [
                            { "question": "Berapa jumlah suku Bani Israil yang dibagi?", "options": ["12 Suku", "7 Suku", "40 Suku", "3 Suku"], "answer": 0 },
                            { "question": "Apa mukjizat air yang diberikan untuk 12 suku tersebut?", "options": ["12 mata air memancar dari batu", "Sungai Nil terbelah 12", "Hujan turun 12 hari", "Sumur menjadi penuh"], "answer": 0 },
                            { "question": "Makanan apa yang diturunkan Allah dari langit untuk mereka?", "options": ["Manna dan Salwa", "Gandum dan Anggur", "Roti dan Ikan", "Kurma dan Susu"], "answer": 0 },
                            { "question": "Bagaimana kondisi Bani Israil di dunia menurut Al-A'raaf: 168?", "options": ["Terbagi menjadi golongan saleh dan tidak saleh", "Bersatu padu selamanya", "Semuanya menjadi raja", "Semuanya binasa"], "answer": 0 },
                            { "question": "Apa tujuan Allah menguji mereka dengan nikmat dan bencana?", "options": ["Agar mereka kembali (bertaubat)", "Agar mereka menderita", "Agar mereka kaya", "Agar mereka berkuasa"], "answer": 0 }
                        ]
                    }
                ]
            },
            {
                "id": "subject-6-12",
                "title": "Pokok Bahasan 12: Daud AS",
                "topics": [
                    {
                        "id": 167,
                        "title": "Masa Kecil & Keutamaan Daud As.",
                        "file": "topic_167.pdf",
                        "content": `<div class="verse"><p class="translation">Daud As.</p></div><div class="verse"><p class="translation"><em>Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis.</em></p></div><div class="verse"><p class="translation"><strong>Al Baqarah [2]: 251</strong></p></div><div class="verse"><p class="translation">Mereka (tentara Thalut) mengalahkan tentara Jalut dengan izin Allah dan</p></div><div class="verse"><p class="translation">(dalam peperangan itu) Daud membunuh Jalut, lalu Allah memberikan</p></div><div class="verse"><p class="translation">padanya (Daud) pemerintahan dan hikmah (kenabian dan Zabur,</p></div><div class="verse"><p class="translation">sesudah Thalut meninggalnya) dan mengajarinya apa yang Dia</p></div><div class="verse"><p class="translation">kehendaki. Seandainya Allah tidak menolak (keganasan) sebagian umat</p></div><div class="verse"><p class="translation">manusia dengan sebagian yang lain, pasti rusaklah bumi ini, tetapi Allah</p></div><div class="verse"><p class="translation">memiliki karunia (yang dicurahkan) atas semesta alam.{251}</p></div><div class="verse"><p class="translation"><strong>Shaad [38]: 17 – 20</strong></p></div><div class="verse"><p class="translation">Bersabarlah atas apa yang mereka katakan; dan ingatlah hamba Kami</p></div><div class="verse"><p class="translation">12.1.1 Masa Kecil Daud As.</p></div><div class="verse"><p class="translation">12.1.2 Keutamaan Daud As.</p></div><div class="verse"><p class="translation">Daud yang memiilkii kekuatan; sesungguhnya dia amat taat.{17}</p></div><div class="verse"><p class="translation">Sesungguhnya Kami menundukkan gunung-gunung untuk bertasbih</p></div><div class="verse"><p class="translation">bersamanya (Daud) di waktu petang dan pagi,{18}</p></div><div class="verse"><p class="translation">Dan (Kami tundukkan pula) burung-burung dalam keadaan terkumpul,</p></div><div class="verse"><p class="translation">seluruhnya amat taat (kepada Allah).{19}</p></div><div class="verse"><p class="translation">Dan Kami kuatkan kerajaannya dan Kami berikan padanya hikmah</p></div><div class="verse"><p class="translation">(kenabian, ketelitian, kesempurnaan ilmu) dan kebijaksanaan dalam</p></div><div class="verse"><p class="translation">menyelesaikan perselisihan.{20}</p></div><div class="verse"><p class="translation"><strong>Saba' [34]: 10 – 13</strong></p></div><div class="verse"><p class="translation">Dan sungguh telah Kami berikan kepada Daud karunia dari Kami. (Kami</p></div><div class="verse"><p class="translation">berfirman): "Hai gunung-gunung dan burung-burung, bertasbih-lah</p></div><div class="verse"><p class="translation">bersama Daud", dan Kami telah melunakkan besi untuknya,{10}</p></div><div class="verse"><p class="translation">(Yaitu) buatlah baju besi yang besar-besar dan ukurlah anyamannya; dan</p></div><div class="verse"><p class="translation">beramal salehlah. Sesungguhnya Aku melihat apa yang kamu</p></div><div class="verse"><p class="translation">kerjakan.{11}</p></div><div class="verse"><p class="translation"><strong>Al Anbiyaa' [21]: 78 – 82</strong></p></div><div class="verse"><p class="translation">Dan (ingatlah kisah) Daud dan Sulaiman, di waktu keduanya memberikan</p></div><div class="verse"><p class="translation">keputusan mengenai tanaman, karena tanaman itu dirusak oleh kambing-</p></div><div class="verse"><p class="translation">kambing milik kaumnya. Dan adalah Kami menyaksikan keputusan yang</p></div><div class="verse"><p class="translation">mereka berikan,{78}</p></div><div class="verse"><p class="translation">Maka Kami telah memberikan pengertian kepada Sulaiman tentang</p></div><div class="verse"><p class="translation">hukum (yang lebih tepat)204; dan kepada masing-masing mereka telah</p></div><div class="verse"><p class="translation">Kami berikan hikmah dan ilmu dan telah Kami tundukkan gunung-gunung</p></div><div class="verse"><p class="translation">dan burung-burung, semua bertasbih bersama Daud. Dan Kamilah yang</p></div><div class="verse"><p class="translation">melakukannya.{79}</p></div><div class="verse"><p class="translation">Dan telah Kami ajarkan kepada Daud membuat baju besi untukmu, guna</p></div><div class="verse"><p class="translation">memelihara kamu dalam peperanganmu; maka hendaklah kamu</p></div><div class="verse"><p class="translation">bersyukur (kepada Allah).{80}</p></div><div class="verse"><p class="translation"><strong>Shaad [38]: 21 – 24</strong></p></div><div class="verse"><p class="translation">204) Menurut riwayat Ibnu Abbas bahwa sekelompok kambing telah merusak tanaman di waktu malam...</p></div><div class="verse"><p class="translation">12.1.3 Daud As. Diuji Melalui Kasus 2 Orang yang Bersengketa</p></div><div class="verse"><p class="translation">Dan adakah sampai kepadamu berita orang-orang yang berperkara</p></div><div class="verse"><p class="translation">ketika mereka memanjat pagar?{21}</p></div><div class="verse"><p class="translation">Ketika mereka masuk (menemui) Daud, lalu ia terkejut karena mereka.</p></div><div class="verse"><p class="translation">Mereka berkata: "Janganlah kamu takut; (kami) adalah dua orang yang</p></div><div class="verse"><p class="translation">berperkara yang salah satu dari kami berbuat zalim kepada yang lain;</p></div><div class="verse"><p class="translation">maka berilah keputusan antara kami dengan adil dan kamu jangan</p></div><div class="verse"><p class="translation">menyimpang dari kebenaran dan tunjukilah kami ke jalan lurus.{22}</p></div><div class="verse"><p class="translation">Sesungguhnya saudaraku ini mempunyai sembilan puluh sembilan ekor</p></div><div class="verse"><p class="translation">Kambing betina dan aku mempunyai seekor saja. Maka dia berkata:</p></div><div class="verse"><p class="translation">"Serahkanlah kambingmu itu kepadaku dan dia mengalahkan aku dalam</p></div><div class="verse"><p class="translation">perdebatan.”{23}</p></div><div class="verse"><p class="translation">Daud berkata: “Sungguh dia telah berbuat zalim kepadamu dengan</p></div><div class="verse"><p class="translation">meminta kambingmu untuk ditambahkan kepada kambingnya. Dan</p></div><div class="verse"><p class="translation">sesungguhnya kebanyakan dari orang-orang yang berserikat sebagian</p></div><div class="verse"><p class="translation">mereka berbuat zalim kepada sebagian yang lain, kecuali orang-orang</p></div><div class="verse"><p class="translation">yang beriman dan beramal saleh; dan amat sedikitlah mereka ini.” Dan</p></div><div class="verse"><p class="translation">Daud mengetahui bahwa Kami mengujinya; maka ia meminta ampun</p></div><div class="verse"><p class="translation">kepada Tuhannya lalu menyungkur sujud dan bertaubat.{24}</p></div><div class="verse"><p class="translation"><strong>Shaad [38]: 25</strong></p></div><div class="verse"><p class="translation">Maka Kami ampuni baginya kesalahannya. Dan sungguh ia di sisi Kami</p></div><div class="verse"><p class="translation">memiliki kedudukan dekat dan sebaik-baik tempat kembali.{25}</p></div><div class="verse"><p class="translation">12.1.4 Allah Mengampuni Kesalahan Daud As.</p></div>`,
                        "quiz": [
                            { "question": "Siapakah tokoh zalim yang dibunuh oleh Nabi Daud dalam pasukan Thalut?", "options": ["Jalut", "Namrud", "Fir'aun", "Qarun"], "answer": 0 },
                            { "question": "Makhluk apa yang diperintahkan Allah untuk bertasbih bersama Daud (Saba': 10)?", "options": ["Gunung-gunung dan burung-burung", "Matahari dan bulan", "Ikan di laut", "Para Malaikat"], "answer": 0 },
                            { "question": "Apa mukjizat yang diberikan Allah kepada Daud terkait pengolahan logam?", "options": ["Melunakkan besi untuk membuat baju besi", "Mengubah besi menjadi emas", "Membuat pedang api", "Mencairkan tembaga"], "answer": 0 },
                            { "question": "Dalam kisah dua orang yang bersengketa (Shaad: 23), berapa jumlah kambing saudara yang kaya?", "options": ["99 ekor", "100 ekor", "50 ekor", "10 ekor"], "answer": 0 },
                            { "question": "Apa hikmah yang disadari Daud setelah mengadili sengketa tersebut (Shaad: 24)?", "options": ["Bahwa Allah sedang mengujinya", "Bahwa ia sangat pintar", "Bahwa rakyatnya kaya", "Bahwa kambing itu mahal"], "answer": 0 }
                        ]
                    },
                    {
                        "id": 168,
                        "title": "Kenabian Daud As.",
                        "file": "topic_168.pdf",
                        "content": `<div class="verse"><p class="translation">Daud As.</p></div><div class="verse"><p class="translation"><em>Disusun Oleh: DR.Ahsin Sakho Muhammad, Akmaldin Noor, Fuad Mukhlis.</em></p></div><div class="verse"><p class="translation">12.2 KENABIAN DAUD AS</p></div><div class="verse"><p class="translation"><strong>Shaad [38]: 26 – 28</strong></p></div><div class="verse"><p class="translation">Hai Daud, sesungguhnya Kami menjadikan kamu khalifah (penguasa) di</p></div><div class="verse"><p class="translation">muka bumi, maka berilah keputusan (perkara) di antara manusia dengan</p></div><div class="verse"><p class="translation">adil dan janganlah kamu mengikuti hawa nafsu, karena ia akan</p></div><div class="verse"><p class="translation">menyesatkan kamu dari jalan Allah. Sesungguhnya orang-orang yang</p></div><div class="verse"><p class="translation">sesat dari jalan Allah akan mendapat azab yang berat, karena mereka</p></div><div class="verse"><p class="translation">melupakan hari perhitungan.{26}</p></div><div class="verse"><p class="translation">Dan Kami tidak menciptakan langit dan bumi dan apa yang ada antara</p></div><div class="verse"><p class="translation">keduanya tanpa hikmah. Hal itu adalah anggapan orang-orang kafir,</p></div><div class="verse"><p class="translation">maka celakalah orang-orang kafir karena masuk neraka.{27}</p></div><div class="verse"><p class="translation">Patutkah Kami menganggap orang-orang beriman dan beramal saleh</p></div><div class="verse"><p class="translation">sama dengan orang-orang yang berbuat kerusakan di muka bumi?</p></div><div class="verse"><p class="translation">12.2.1 Allah Mengangkat Daud As. sebagai Khalifah di Bumi</p></div><div class="verse"><p class="translation">patutkah (pula) Kami menganggap orang-orang yang bertakwa sama</p></div><div class="verse"><p class="translation">dengan orang-orang yang berbuat maksiat?{28}</p></div><div class="verse"><p class="translation"><strong>Shaad [38]: 29</strong></p></div><div class="verse"><p class="translation">Ini adalah sebuah kitab yang Kami turunkan kepadamu penuh dengan</p></div><div class="verse"><p class="translation">berkah supaya mereka memperhatikan ayat-ayat-Nya dan supaya</p></div><div class="verse"><p class="translation">mendapat pelajaran orang-orang yang mempunyai pikiran.{29}</p></div><div class="verse"><p class="translation"><strong>Lihat juga: Al Israa' [17]: 55</strong></p></div><div class="verse"><p class="translation">12.2.2 Kitab Zabur Diturunkan kepada Daud As.</p></div>`,
                        "quiz": [
                            { "question": "Sebagai apakah Allah mengangkat Daud di muka bumi (Shaad: 26)?", "options": ["Khalifah (Penguasa)", "Pedagang", "Petani", "Penyair"], "answer": 0 },
                            { "question": "Kitab suci apa yang diturunkan Allah kepada Nabi Daud?", "options": ["Zabur", "Taurat", "Injil", "Al-Qur'an"], "answer": 0 },
                            { "question": "Apa peringatan Allah kepada Daud dalam memutuskan perkara (Shaad: 26)?", "options": ["Jangan mengikuti hawa nafsu", "Jangan ragu-ragu", "Jangan meminta upah", "Jangan sendirian"], "answer": 0 },
                            { "question": "Mengapa mengikuti hawa nafsu dilarang keras dalam memimpin?", "options": ["Karena akan menyesatkan dari jalan Allah", "Karena membuat miskin", "Karena tidak populer", "Karena melelahkan"], "answer": 0 },
                            { "question": "Apa tujuan diturunkannya Kitab yang penuh berkah menurut Shaad: 29?", "options": ["Supaya diperhatikan ayat-ayat-Nya dan mendapat pelajaran", "Hanya untuk dipajang", "Untuk diperjualbelikan", "Sebagai mantra"], "answer": 0 }
                        ]
                    }
                ]
            }
        ]
    }
];
export default courseData;
