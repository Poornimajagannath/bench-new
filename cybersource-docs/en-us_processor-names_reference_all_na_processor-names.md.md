Processor Names {#processor-names}
==================================

Many `Cybersource` reports include a payment processor value:

* In XML reports, the name of the element is usually `&lt;PaymentProcessor&gt;`.
* In CSV reports, the name of the field is usually payment_processor.
  {#processor-names_ul_sx2_dhz_qpb}  
  In most reports, a payment processor value is a raw, unmapped value from the `Cybersource` software. A few reports use mapped payment processor values. For information about the main `Cybersource` reports, see the [Business Center Reporting Developer Guide](https://developer.cybersource.com/library/documentation/dev_guides/reporting_and_reconciliation/Reporting_User/html/ "").

Raw Payment Processor Names
---------------------------

| Raw Name               | Processor                                                                                                                |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------|
| aibms                  | `AIBMS`                                                                                                                  |
| amexdirect             | `American Express Direct`                                                                                                |
| barclays               | `Barclays`                                                                                                               |
| barclays2              | `Barclays`                                                                                                               |
| bdftresor              | `Banque de France et Tresor Public`                                                                                      |
| bofaach                | `Bank of America ACH`. This processor is part of the Cybersource ACH Service.                                            |
| cardnet                | `LloydsTSB Cardnet`                                                                                                      |
| cielo                  | `Cielo`                                                                                                                  |
| citimb                 | `Elavon`. This processor was formerly called *Citibank Meerbusch*.                                                       |
| cmcic                  | `Credit Mutuel-CIC`                                                                                                      |
| comerciolatino         | `Comercio Latino`                                                                                                        |
| cybsach                | `Cybersource ACH Service`                                                                                                |
| eftpos                 | `eftpos`                                                                                                                 |
| eibnpp                 | `BNP Paribas France`                                                                                                     |
| elavonamericas         | `Elavon Americas`                                                                                                        |
| fdccompass             | `FDC Compass`                                                                                                            |
| fdiaus                 | `FDI Australia`                                                                                                          |
| fdiglobal              | `FDC Nashville Global`. This processor was formerly called *FDI Global*.                                                 |
| getnet                 | `Getnet`                                                                                                                 |
| gpn                    | `GPN`                                                                                                                    |
| gpx                    | `GPX`                                                                                                                    |
| hbos                   | `HBoS`                                                                                                                   |
| hsbc                   | `HSBC` HSBC is the `Cybersource` name for HSBC U.K. The acquirer is Global Payments U.K.                                 |
| jcngateway             | `JCN Gateway`                                                                                                            |
| moneris                | `Moneris`                                                                                                                |
| opdbams                | `Bank of America Merchant Services`Bank of America Merchant Services on OmniPay Direct                                   |
| opdcardnet             | `LloydsTSB Cardnet International` LloydsTSB Cardnet International                                                        |
| opdfde                 | `First Data Merchant Solutions` (Europe) on OmniPay Direct                                                               |
| omnipayfdi             | `Lloyds-OmniPay`                                                                                                         |
| paymentechtampa        | `Chase Paymentech Tandem`. This processor was formerly called *Paymentech Tampa.*                                        |
| prisma                 | `Prisma`                                                                                                                 |
| prosa                  | `Prosa`                                                                                                                  |
| rede                   | `Rede`                                                                                                                   |
| six                    | `SIX`                                                                                                                    |
| smartfdc               | `FDMS Nashville`                                                                                                         |
| smartpay               | `Chase Paymentech Solutions`. This processor was formerly called *Paymentech New Hampshire.*                             |
| streamline2            | `Streamline`. The acquirer is WorldPay.                                                                                  |
| telecheck              | `TeleCheck`                                                                                                              |
| uatp                   | `UATP`                                                                                                                   |
| vantivcnp              | `Worldpay Relay`                                                                                                           |
| vero                   | `Vero`                                                                                                                   |
| wellsfargoach          | `Wells Fargo ACH`. This processor is part of the `Cybersource ACH Service`.                                              |
| vital                  | `TSYS Acquiring Solutions`. This processor was formerly called *Vital*.                                                  |
| vdcabsa                | Absa Bank on `Platform Connect`                                                                                     |
| vdcdhofar              | Abu Dhabi Commercial Bank (ADCB) in UAE on BankDhofar's Gateway                                                          |
| vdcadcbae              | Abu Dhabi Commercial Bank on `Platform Connect`                                                                     |
| vdcaccessbk            | Access Bank PLC on `Platform Connect`                                                                               |
| vdcabakh               | Advanced Bank of Asia Cambodia (ABA Bank) on `Platform Connect`                                                     |
| vdcaffinbkmy           | Affin Bank on `Platform Connect`                                                                                    |
| vdcagbkchina           | Agricultural Bank of China (ABC) on `Platform Connect`                                                              |
| networkintluae         | Ahli United Bank in Bahrain, BLOM Bank, Network International                                                            |
| vdcacpalinma           | Alinma Bank on `Platform Connect`                                                                                   |
| vdcalipaycn            | Alipay on `Platform Connect`                                                                                        |
| vdcalliancemy          | Alliance Bank Malaysia Berhad on `Platform Connect`                                                                 |
| vdcallinpayhk          | AllinPay Merchant Services Company Ltd. on `Platform Connect`                                                       |
| vdcallinpaynsclcn      | AllinPay Network Services China on `Platform Connect`                                                               |
| vdcalrajhisa           | Al-Rajhi Bank on `Platform Connect`                                                                                 |
| vdcaaib                | Arab African International Bank (AAIB) on `Platform Connect`                                                        |
| vdcarabbankjo          | Arab Bank on `Platform Connect`                                                                                     |
| vdcacbvietnam          | Asia Commercial Bank (ACB) on `Platform Connect`                                                                    |
| vdcatcsablv            | ATC Bank on `Platform Connect`                                                                                      |
| vdcasb                 | Auckland Savings Bank (ASB) on `Platform Connect`                                                                   |
| vdcanzbank             | Australia and New Zealand Banking Group Ltd. (ANZ) on `Platform Connect`                                            |
| vdcaxis                | Axis Bank Ltd. of India on `Platform Connect`                                                                       |
| vdcayabankmm           | AYA Bank on `Platform Connect`                                                                                      |
| vdcayeyarswadymm       | Ayeyarwady Bank Ltd. on `Platform Connect`                                                                          |
| vdcazuldo              | Azul Bank on `Platform Connect`                                                                                     |
| vdcbaccredcr           | BAC Credomatic Cost Rica and BAC Credomatic Panama on `Platform Connect`                                            |
| vdcbaccredsv           | BAC Credomatic El Salvador on `Platform Connect`                                                                    |
| vdcbaccredgt           | BAC Credomatic Guatemala on `Platform Connect`                                                                      |
| vdcbaccredhn           | BAC Credomatic Honduras on `Platform Connect`                                                                       |
| vdcbaccredni           | BAC Credomatic Nicaragua on `Platform Connect`                                                                      |
| vdcbaiduribn           | Baiduri Bank on `Platform Connect`                                                                                  |
| vdcbancocuscatlansv    | Banco Cuscatlan on `Platform Connect`                                                                               |
| vdcbanpaishn           | Banco del País on `Platform Connect`                                                                                |
| vdcbancocaribecw       | Banco di Caribe on `Platform Connect`                                                                               |
| vdcbancogenpa          | Banco General on `Platform Connect`                                                                                 |
| vdcbkguayaquilec       | Banco Guayaquil S.A. on `Platform Connect`                                                                          |
| vdcbancomer            | Bancomer (via eGLobal) on `Platform Connect`                                                                        |
| vdcbanconacionalcr     | Banco Nacional de Costa Rica (BNCR) on `Platform Connect`                                                           |
| vdcbanamex             | Banco Nacional de México (Banamex) on `Platform Connect`                                                            |
| vdcbcosafrabr          | Banco Safra on `Platform Connect`                                                                                   |
| vdcbncsantanderbzl     | Banco Santander on `Platform Connect`                                                                               |
| vdcbanescopn           | Banesco on `Platform Connect`                                                                                       |
| vdcbbl                 | Bangkok Bank Ltd. on `Platform Connect`                                                                             |
| vdcacpbkalbilad        | Bank Albilad on `Platform Connect`                                                                                  |
| vdcacpbaljazira        | Bank AlJazira on `Platform Connect`                                                                                 |
| vdcdhofar              | BankDhofar in Oman                                                                                                       |
| vdcbidvvn              | Bank for Investment and Development in Vietnam (BIDV) on `Platform Connect`                                         |
| vdcbankmuscat          | Bank Muscat of Oman on `Platform Connect`                                                                           |
| vdcabyssiniaet         | Bank of Abyssinia on `Platform Connect`                                                                             |
| vdccostcopay           | Bank of America - CostcoPay on `Platform Connect`                                                                   |
| vdcbay                 | Bank of Ayudhya (BAY) on `Platform Connect`                                                                         |
| vdcbocmacau            | Bank of China in Macau on `Platform Connect`                                                                        |
| vdcbankcommcn          | Bank of Communication on `Platform Connect`                                                                         |
| vdcbocom               | Bank of Communications on `Platform Connect`                                                                        |
| vdcbkeastasiahk        | Bank of East Asia Ltd. on `Platform Connect`                                                                        |
| vdcbanknznz            | Bank of New Zealand on `Platform Connect`                                                                           |
| vdcacpbsn              | Bank Simpanan Nasional (BSN) on `Platform Connect`                                                                  |
| vdcbksinarmasid        | Bank Sinarmas (Omise Ltd.) on `Platform Connect`                                                                    |
| vdcmisreg              | Banque Misr on `Platform Connect`                                                                                   |
| vdcbcellao             | Banque Pour Le Commerce Exterieur Lao (BCEL) on `Platform Connect`                                                  |
| vdcbarclaysbw          | Barclays Bank Botswana on `Platform Connect`                                                                        |
| vdcbarclaysgh          | Barclays Bank Ghana on `Platform Connect`                                                                           |
| vdcbarclaysmu          | Barclays Bank Mauritius Ltd. on `Platform Connect`                                                                  |
| vdcbarclaysghtzug      | Barclays Bank of Ghana Ltd., Barclays Bank of Tanzania Ltd., and Barclays Bank of Uganda Ltd. on `Platform Connect` |
| vdcbarclayske          | Barclays Bank of Kenya on `Platform Connect`                                                                        |
| vdcbarclayszm          | Barclays Bank of Zambia on `Platform Connect`                                                                       |
| vdcbarclayssc          | Barclays Bank Seychelles on `Platform Connect`                                                                      |
| vdcbarclaystz          | Barclays Bank Tanzania on `Platform Connect`                                                                        |
| vdcbarclaysug          | Barclays Bank Uganda on `Platform Connect`                                                                          |
| vdcbccardkr            | BC Card Co., Ltd. on `Platform Connect`                                                                             |
| vdcbdounibkph          | BDO Unibank, Inc. in Philippines on `Platform Connect`                                                              |
| vdcbfvsgsn             | BFV Société Générale on `Platform Connect`                                                                          |
| vdcbocihk              | BOC International Holdings Ltd. (BOCI) on `Platform Connect`                                                        |
| vdcbracbkltdbd         | BRAC Bank Ltd. on `Platform Connect`                                                                                |
| vdcburganbkkw          | Burgan Bank on `Platform Connect`                                                                                   |
| vdccampubkkh           | Cambodian Public Bank on `Platform Connect`                                                                         |
| vdccapitalbkjo         | Capital Bank of Jordan on `Platform Connect`                                                                        |
| vdcplcapone            | Capital One on `Platform Connect`                                                                                   |
| opdcardnet             | Cardnet International on OmniPay Direct                                                                                  |
| vdccaribbeancckn       | Caribbean Credit Card Corporation Ltd. on `Platform Connect`                                                        |
| vdccubtw               | Cathay United Bank (CUB) on `Platform Connect`                                                                      |
| vdcacpcaymannb         | Cayman National Bank Ltd. on `Platform Connect`                                                                     |
| vdcccbhk               | CCBC in Hong Kong on `Platform Connect`                                                                             |
| vdcciticbankcn         | China CITIC Bank Credit Card Center on `Platform Connect`                                                           |
| vdccimbbkmy            | CIMB Bank Berhad on `Platform Connect`                                                                              |
| vdccitihkmo            | Citibank Hongkong and Macau on `Platform Connect`                                                                   |
| vdccitiau              | Citibank in Australia on `Platform Connect`                                                                         |
| vdccitimy              | Citibank Malaysia on `Platform Connect`                                                                             |
| vdccitisg              | Citibank Singapore Ltd. on `Platform Connect`                                                                       |
| vdcacpdominicana       | CMP SA Dominicana on `Platform Connect`                                                                             |
| vdccbocsl              | Commercial Bank of Ceylon on `Platform Connect`                                                                     |
| vdccbduae              | Commercial Bank of Dubai on `Platform Connect`                                                                      |
| vdccommbket            | Commercial Bank of Ethiopia on `Platform Connect`                                                                   |
| vdccbq                 | Commercial Bank of Qatar on `Platform Connect`                                                                      |
| vdccbadxcau            | Commonwealth Bank of Australia DXC on `Platform Connect`                                                            |
| vdccbafisau            | Commonweatlh Bank of Australia FIS on `Platform Connect`                                                            |
| vdcvnperumc            | Compañía Peruana de Medios de Pago on `Platform Connect`                                                            |
| vdccardnetdo           | Consorcio De Tarjetas Dominicanas, S.A. (Cardnet) on `Platform Connect`                                             |
| vdccoopbkke            | Cooperative Bank in Kenya on `Platform Connect`                                                                     |
| vdccrdbbktz            | CRDB Bank PLC on `Platform Connect`                                                                                 |
| vdccredibanco          | Credibanco on `Platform Connect`                                                                                    |
| vdccredicorppn         | Credicorp Bank on `Platform Connect`                                                                                |
| vdccredimax            | CrediMax (Bahrain) on `Platform Connect`                                                                            |
| vdcctbc                | CTBC Bank Ltd. on `Platform Connect`                                                                                |
| vdcdashenbanket        | Dashen Bank Ethiopia (Amole) on `Platform Connect`                                                                  |
| vdcdeltaair            | Delta AIR on `Platform Connect`                                                                                     |
| vdcdohabkqa            | Doha Bank on `Platform Connect`                                                                                     |
| vdcdubaiislamicbankuae | Dubai Islamic Bank on `Platform Connect`                                                                            |
| vdceblbankbd           | Eastern Bank Ltd. on `Platform Connect`                                                                             |
| vdcecobankgh           | Ecobank in Ghana on `Platform Connect`                                                                              |
| vdcelavonie            | Elavon Ireland on `Platform Connect`                                                                                |
| vdcacpelavon           | Elavon on `Platform Connect`                                                                                        |
| vdcequitybkke          | Equity Bank on `Platform Connect`                                                                                   |
| vdcevertecpr           | Evertec, Inc. hybrid on `Platform Connect` and Relay Accelerated Connection Platform (ACP)                           |
| vdcfarelogix           | Farelogix on `Platform Connect` (authorization only)                                                                |
| vdcfdmsau              | FDMS Australia on `Platform Connect`                                                                                |
| vdcficohsahn           | Ficohsa on `Platform Connect`                                                                                       |
| vdcacpcibc             | FirstCaribbean International Bank (FCIB) in Barbados on `Platform Connect`                                          |
| vdcfcbtt               | First Citizens Bank on `Platform Connect`                                                                           |
| vdcfdmsbn              | First Data Merchant Solutions in Brunei on `Platform Connect`                                                       |
| vdcfdmshk              | First Data Merchant Solutions in Hong Kong on `Platform Connect`                                                    |
| vdcfdmsmy              | First Data Merchant Solutions in Malaysia on `Platform Connect`                                                     |
| vdcfdmssg              | First Data Merchant Solutions in Singapore on `Platform Connect`                                                    |
| vdcfnbza               | First National Bank (FNB) on `Platform Connect`                                                                     |
| vdcfnb                 | FirstRand Bank on `Platform Connect`                                                                                |
| vdcftbkh               | Foreign Trade Bank on `Platform Connect`                                                                            |
| vdcfresnous            | Fresno - EPX/NAB on `Platform Connect`                                                                              |
| vdchsbcbank            | Global Payments Asia Pacific on `Platform Connect`                                                                  |
| vdcgpsbh               | Global Payment Services on `Platform Connect`                                                                       |
| vdcgblpayau            | Global Payments in Australia on `Platform Connect`                                                                  |
| omnipaydirect          | Global Payments International Acquiring on `OmniPay Direct`                                                              |
| vdcgpindia             | Global Payments Ltd. in India on `Platform Connect`                                                                 |
| vdcglobalprocar        | Global Processing S.A on `Platform Connect`                                                                         |
| vdcgtbankng            | Guaranty Trust (GT) Bank on `Platform Connect`                                                                      |
| vdcgulfbkkw            | Gulf Bank on `Platform Connect`                                                                                     |
| vdchabibltd            | Habib Bank Ltd. (HBL) on `Platform Connect`                                                                         |
| vdchangsenghk          | Hang Seng Bank Ltd. on `Platform Connect`                                                                           |
| vdchattonlk            | Hatton National Bank on `Platform Connect`                                                                          |
| vdchdfc                | HDFC Bank Ltd. of India on `Platform Connect`                                                                       |
| rupayhdfc              | HDFC Bank on `RuPay`                                                                                                     |
| vdcimbank              | I\&M Bank on `Platform Connect`                                                                                     |
| vdcicepaybvnl          | ICEPAY B.V. Ireland on `Platform Connect`                                                                           |
| vdcicici               | ICICI of India on `Platform Connect`                                                                                |
| vdcindozambiabkzm      | Indo Zambia Bank on `Platform Connect`                                                                              |
| vdcicbcasisahk         | Industrial and Commercial Bank of China (Asia) on `Platform Connect`                                                |
| vdcicbc                | Industrial and Commercial Bank of China (ICBC) on `Platform Connect`                                                |
| vdcinterswitchng       | Interswitch Ltd. on `Platform Connect`                                                                              |
| vdcishtariq            | Ishtar Gate for e-Payment Systems and Services                                                                           |
| vdcmulticajacl         | Iswitch - Multicaja on `Platform Connect`                                                                           |
| vdcconcordprocarduk    | JSCB Concord on `Platform Connect`                                                                                  |
| vdckapitalbkuz         | Kapital Bank on `Platform Connect`                                                                                  |
| vdckbankvn             | Kasikornbank (Kbank) in Vietnam on `Platform Connect`                                                               |
| vdckbank               | Kasikornbank (Kbank) on `Platform Connect`                                                                          |
| vdckbzmm               | KBZ Bank on `Platform Connect`                                                                                      |
| vdckcbank              | Kenya Commercial Bank on `Platform Connect`                                                                         |
| vdckeb                 | Korea Exchange Bank (KEB) on `Platform Connect`                                                                     |
| vdcktbth               | Krungthai Bank Public Company Ltd. on `Platform Connect`                                                            |
| vdckibkw               | Kuwait International Bank on `Platform Connect`                                                                     |
| vdcledgerpayus         | Ledgerpay - Westamerica Bank on `Platform Connect`                                                                  |
| vdclinkserbo           | Linkser Empresa Administradora de Tarjetas on `Platform Connect`                                                    |
| vdclivepymtau          | Live Payments on `Platform Connect`                                                                                 |
| vdcmadfooatjo          | MadfooatCom on `Platform Connect`                                                                                   |
| vdcmashreqbk           | Mashreq on `Platform Connect`                                                                                       |
| vdcmaybankmy           | Maybank on `Platform Connect`                                                                                       |
| vdcmetrobkpa           | MetroBank S.A on `Platform Connect`                                                                                 |
| vdcmetropolitan        | Metropolitan Bank on `Platform Connect`                                                                             |
| vdcmepsjo              | Middle East Payment Services (MEPS) on `Platform Connect`                                                           |
| vdcacpnabau            | National Australia Bank on `Platform Connect`                                                                       |
| vdcnbad                | National Bank of Abu Dhabi (NBAD) on `Platform Connect`                                                             |
| vdcnabdinau            | National Bank of Australia (Diners or Discover) on `Platform Connect`                                               |
| vdcnabau               | National Bank of Australia on `Platform Connect`                                                                    |
| vdcacpnatlcalif        | National Bank of California on `Platform Connect`                                                                   |
| vdcnbctz               | National Bank of Commerce in Tanzania on `Platform Connect`                                                         |
| vdcnationalbkgr        | National Bank of Greece (NBG) on `Platform Connect`                                                                 |
| vdcnbk                 | National Bank of Kuwait (NBK) on `Platform Connect`                                                                 |
| vdcnboom               | National Bank of Oman on `Platform Connect`                                                                         |
| vdcacpncbj             | National Commercial Bank (NCB) Jamaica hybrid on `Platform Connect` and Relay Accelerated Connection Platform (ACP)  |
| vdcnacombk             | National Commercial Bank on `Platform Connect`                                                                      |
| vdcndblk               | National Development Bank on `Platform Connect`                                                                     |
| vdcnayapaypk           | NayaPay on `Platform Connect`                                                                                       |
| vdcncbabkke            | NCBA Bank Kenya on `Platform Connect`                                                                               |
| vdcnijo                | Network International (NI) Jordan on `Platform Connect`                                                             |
| vdcnicnepal            | NIC Asia Bank Ltd. on `Platform Connect`                                                                            |
| vdcnovattiau           | Novatti Australia on `Platform Connect`                                                                             |
| vdcjscoschadbkua       | Oschadbank on `Platform Connect`                                                                                    |
| vdcocbc                | Overseas Chinese Banking Corp (OCBC) on `Platform Connect`                                                          |
| vdcappspk              | PayFast (APPS) on `Platform Connect`                                                                                |
| vdcpayglocalin         | PayGlocal Technologies on `Platform Connect`                                                                        |
| vdcpaymayaph           | PayMaya on `Platform Connect`                                                                                       |
| vdcpymtsnsltdgb        | Paymentsense on `Platform Connect`                                                                                  |
| vdcpayzlius            | Payzli on `Platform Connect`                                                                                        |
| vdcpeoplesbksl         | Peoples Bank on `Platform Connect`                                                                                  |
| vdcpinganbkch          | Ping An Bank in China on `Platform Connect`                                                                         |
| vdcplanetmrchntservuk  | Planet Merchant Services on `Platform Connect`                                                                      |
| vdcprismampar          | Prisma de Pago S.A. on `Platform Connect`                                                                           |
| vdcprocardsapy         | Procard S.A. on `Platform Connect`                                                                                  |
| vdcizipaype            | Procesos de Medios de Pago S.A. on `Platform Connect`                                                               |
| vdcpromerica           | Promerica in Honduras and Nicaragua on `Platform Connect`                                                           |
| vdcbkctrlasiaid        | PT Bank Central Asia on `Platform Connect`                                                                          |
| vdccimbniagaid         | PT Bank CIMB Niaga Tbk in Indonesia on `Platform Connect`                                                           |
| vdcbkdanamonid         | PT Bank Danamon on `Platform Connect`                                                                               |
| vdcbankmegaid          | PT Bank Mega Tbk on `Platform Connect`                                                                              |
| vdcbni                 | PT Bank Negara Indonesia on `Platform Connect`                                                                      |
| vdcbkrakyatid          | PT Bank Rakyat Indonesia on `Platform Connect`                                                                      |
| vdcbkmandiri           | PT Mitra Transaki Indonesia - Bk Mandiri on `Platform Connect`                                                      |
| vdcpbbma               | Public Bank Berhad on `Platform Connect`                                                                            |
| vdcqnbqa               | Qatar National Bank (QNB Group) on `Platform Connect`                                                               |
| vdcraiffeisenua        | Raiffeisen Bank Aval on `Platform Connect`                                                                          |
| vdcraiffeisenbh        | Raiffeisen Bank dd Bosnia and Herzegovina on `Platform Connect`                                                     |
| vdcraiffeisenat        | Raiffeisen Bank on `Platform Connect`                                                                               |
| vdcrakbankuae          | RAKBANK on `Platform Connect`                                                                                       |
| vdcredebanco           | Redeban - Davivienda on `Platform Connect`                                                                          |
| vdcrbmredebanco        | Redeban - Multicolor on `Platform Connect`                                                                          |
| vdcacprepublictt       | Republic Bank hybrid on `Platform Connect` and Relay Accelerated Connection Platform (ACP)                           |
| vdcrhbbankberhadmy     | RHB Bank Berhad on `Platform Connect`                                                                               |
| vdcacprbc              | Royal Bank of Canada in Caribbean on `Platform Connect`                                                             |
| vdcsacomb              | Sacombank on `Platform Connect`                                                                                     |
| vdcsafaricomke         | Safaricom PLC on `Platform Connect`                                                                                 |
| vdcsafepaypk           | Safepay on `Platform Connect`                                                                                       |
| vdcacpscotiabk         | Scotia Bank in Caribbean hybrid on `Platform Connect` and Relay Accelerated Connection Platform (ACP)                |
| vdcscotiabkca          | Scotia Bank on `Platform Connect`                                                                                   |
| vdcsiamth              | Siam Commercial Bank on `Platform Connect`                                                                          |
| vdcsocgeneralgh        | Societe General Ghana on `Platform Connect`                                                                         |
| vdcsoutheastbkbd       | Southeast Bank Ltd. on `Platform Connect`                                                                           |
| vdcsmcc                | Sumitomo Mitsui Card Co. on `Platform Connect`                                                                      |
| vdctaishintw           | Taishin Bank Ltd. on `Platform Connect`                                                                             |
| vdctbcge               | TBC Bank on `Platform Connect`                                                                                      |
| vdctcmshk              | TCM Solutions Ltd. on `Platform Connect`                                                                            |
| vdcterrapaymu          | TerraPay Mauritius on `Platform Connect`                                                                            |
| vdcsaudibritishbksa    | The Saudi British Bank on `Platform Connect`                                                                        |
| vdcstandrdbkza         | The Standard Bank of South Africa on `Platform Connect`                                                             |
| vdctillau              | Till Payments on `Platform Connect`                                                                                 |
| vdcunicreptgl          | UNICRE on `Platform Connect`                                                                                        |
| vdcunionbkph           | Union Bank in Philippines on `Platform Connect`                                                                     |
| vdcuntdbkafricang      | United Bank for Africa on `Platform Connect`                                                                        |
| vdcacpuba              | United Bank of Africa, PLC on `Platform Connect`                                                                    |
| vdcuob                 | United Overseas Bank (UOB) in Singapore and Vietnam on `Platform Connect`                                           |
| vdcuobth               | United Overseas Bank (UOB) in Thailand on `Platform Connect`                                                        |
| vdcuob                 | United Overseas Bank (UOB) on `Platform Connect`                                                                    |
| vdcvantiv              | Vantiv on `Platform Connect`                                                                                        |
| vdcvietcombk           | Vietcombank on `Platform Connect`                                                                                   |
| vdcvietin              | VietinBank on `Platform Connect`                                                                                    |
| vdcvpbankvn            | Vietnam Prosperity Joint-Stock Commercial Bank on `Platform Connect`                                                |
| vdctechcomvn           | Vietnam Technological and Commercial Joint Stock Bank (Techcombank) on `Platform Connect`                           |
| vdcguatemala           | Relay Guatemala on `Platform Connect`                                                                                |
| vdccardnetdo           | CardNet Dominicana on `Platform Connect`                                                                            |
| vdcvnperu              | CardNet Peru on `Platform Connect`                                                                                  |
| vdccardnetuy           | CardNet Uruguay on `Platform Connect`                                                                               |
| vdcuruguay             | Relay Uruguay on `Platform Connect`                                                                                  |
| vdcacpwfb              | Wells Fargo Bank on `Platform Connect`                                                                              |
| vdcwestpacnz           | Westpac New Zealand on `Platform Connect`                                                                           |
| vdcwestpac             | Westpac on `Platform Connect`                                                                                       |
| vdcwhb                 | Wing Hang Bank on `Platform Connect`                                                                                |
| vdcwinglung            | Wing Lung Bank on `Platform Connect`                                                                                |
| vdcwirecardhk          | Wirecard in Hong Kong on `Platform Connect`                                                                         |
| vdcwirecardde          | Wirecard in Munich on `Platform Connect`                                                                            |
| vdcwirecardsg          | Wirecard in Singapore on `Platform Connect`                                                                         |
| vdcwoodforestus        | Woodforest National Bank on `Platform Connect`                                                                      |
| vdcwpayau              | Wpay in Australia on `Platform Connect`                                                                             |
| vdcwpayltdnz           | Wpay Ltd. in New Zealand on `Platform Connect`                                                                      |
| vdcyesbank             | YES BANK Ltd. in Mumbai on `Platform Connect`                                                                       |
| vdcyspcn               | Yinsheng E-Pay Services (Holding) Ltd. on `Platform Connect`                                                        |
| vdczanacozam           | Zanaco on `Platform Connect`                                                                                        |
| vdcacpzenithbank       | Zenith Bank on `Platform Connect`                                                                                   |

Mapped Payment Processor Names
------------------------------

* Bank of America ACH---this processor is part of the `Cybersource ACH Service`.
* Barclays UK
* Citibank Meerbusch---this processor is now called *Elavon*.
* FDC Compass
* FDMS Nashville
* PayEase
* Paymentech---this processor is now called *`Chase Paymentech Solutions`*.
* Paymentech Tampa---this processor is now called *`Chase Paymentech Tandem`*.
* Streamline UK
* TeleCheck
* Vital---this processor is now called *`TSYS Acquiring Solutions`*.
* Wells Fargo ACH---this processor is part of the `Cybersource ACH Service`.
  {#processor-names_ul_tkx_4jb_rpb}

CARD Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Relay/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER CARD NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Platform Connect ACQUIRER.
