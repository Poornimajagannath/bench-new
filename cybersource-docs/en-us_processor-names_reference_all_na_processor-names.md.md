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
| vantivcnp              | `Worldpay VAP`                                                                                                           |
| vero                   | `Vero`                                                                                                                   |
| wellsfargoach          | `Wells Fargo ACH`. This processor is part of the `Cybersource ACH Service`.                                              |
| vital                  | `TSYS Acquiring Solutions`. This processor was formerly called *Vital*.                                                  |
| vdcabsa                | Absa Bank on `Visa Platform Connect`                                                                                     |
| vdcdhofar              | Abu Dhabi Commercial Bank (ADCB) in UAE on BankDhofar's Gateway                                                          |
| vdcadcbae              | Abu Dhabi Commercial Bank on `Visa Platform Connect`                                                                     |
| vdcaccessbk            | Access Bank PLC on `Visa Platform Connect`                                                                               |
| vdcabakh               | Advanced Bank of Asia Cambodia (ABA Bank) on `Visa Platform Connect`                                                     |
| vdcaffinbkmy           | Affin Bank on `Visa Platform Connect`                                                                                    |
| vdcagbkchina           | Agricultural Bank of China (ABC) on `Visa Platform Connect`                                                              |
| networkintluae         | Ahli United Bank in Bahrain, BLOM Bank, Network International                                                            |
| vdcacpalinma           | Alinma Bank on `Visa Platform Connect`                                                                                   |
| vdcalipaycn            | Alipay on `Visa Platform Connect`                                                                                        |
| vdcalliancemy          | Alliance Bank Malaysia Berhad on `Visa Platform Connect`                                                                 |
| vdcallinpayhk          | AllinPay Merchant Services Company Ltd. on `Visa Platform Connect`                                                       |
| vdcallinpaynsclcn      | AllinPay Network Services China on `Visa Platform Connect`                                                               |
| vdcalrajhisa           | Al-Rajhi Bank on `Visa Platform Connect`                                                                                 |
| vdcaaib                | Arab African International Bank (AAIB) on `Visa Platform Connect`                                                        |
| vdcarabbankjo          | Arab Bank on `Visa Platform Connect`                                                                                     |
| vdcacbvietnam          | Asia Commercial Bank (ACB) on `Visa Platform Connect`                                                                    |
| vdcatcsablv            | ATC Bank on `Visa Platform Connect`                                                                                      |
| vdcasb                 | Auckland Savings Bank (ASB) on `Visa Platform Connect`                                                                   |
| vdcanzbank             | Australia and New Zealand Banking Group Ltd. (ANZ) on `Visa Platform Connect`                                            |
| vdcaxis                | Axis Bank Ltd. of India on `Visa Platform Connect`                                                                       |
| vdcayabankmm           | AYA Bank on `Visa Platform Connect`                                                                                      |
| vdcayeyarswadymm       | Ayeyarwady Bank Ltd. on `Visa Platform Connect`                                                                          |
| vdcazuldo              | Azul Bank on `Visa Platform Connect`                                                                                     |
| vdcbaccredcr           | BAC Credomatic Cost Rica and BAC Credomatic Panama on `Visa Platform Connect`                                            |
| vdcbaccredsv           | BAC Credomatic El Salvador on `Visa Platform Connect`                                                                    |
| vdcbaccredgt           | BAC Credomatic Guatemala on `Visa Platform Connect`                                                                      |
| vdcbaccredhn           | BAC Credomatic Honduras on `Visa Platform Connect`                                                                       |
| vdcbaccredni           | BAC Credomatic Nicaragua on `Visa Platform Connect`                                                                      |
| vdcbaiduribn           | Baiduri Bank on `Visa Platform Connect`                                                                                  |
| vdcbancocuscatlansv    | Banco Cuscatlan on `Visa Platform Connect`                                                                               |
| vdcbanpaishn           | Banco del País on `Visa Platform Connect`                                                                                |
| vdcbancocaribecw       | Banco di Caribe on `Visa Platform Connect`                                                                               |
| vdcbancogenpa          | Banco General on `Visa Platform Connect`                                                                                 |
| vdcbkguayaquilec       | Banco Guayaquil S.A. on `Visa Platform Connect`                                                                          |
| vdcbancomer            | Bancomer (via eGLobal) on `Visa Platform Connect`                                                                        |
| vdcbanconacionalcr     | Banco Nacional de Costa Rica (BNCR) on `Visa Platform Connect`                                                           |
| vdcbanamex             | Banco Nacional de México (Banamex) on `Visa Platform Connect`                                                            |
| vdcbcosafrabr          | Banco Safra on `Visa Platform Connect`                                                                                   |
| vdcbncsantanderbzl     | Banco Santander on `Visa Platform Connect`                                                                               |
| vdcbanescopn           | Banesco on `Visa Platform Connect`                                                                                       |
| vdcbbl                 | Bangkok Bank Ltd. on `Visa Platform Connect`                                                                             |
| vdcacpbkalbilad        | Bank Albilad on `Visa Platform Connect`                                                                                  |
| vdcacpbaljazira        | Bank AlJazira on `Visa Platform Connect`                                                                                 |
| vdcdhofar              | BankDhofar in Oman                                                                                                       |
| vdcbidvvn              | Bank for Investment and Development in Vietnam (BIDV) on `Visa Platform Connect`                                         |
| vdcbankmuscat          | Bank Muscat of Oman on `Visa Platform Connect`                                                                           |
| vdcabyssiniaet         | Bank of Abyssinia on `Visa Platform Connect`                                                                             |
| vdccostcopay           | Bank of America - CostcoPay on `Visa Platform Connect`                                                                   |
| vdcbay                 | Bank of Ayudhya (BAY) on `Visa Platform Connect`                                                                         |
| vdcbocmacau            | Bank of China in Macau on `Visa Platform Connect`                                                                        |
| vdcbankcommcn          | Bank of Communication on `Visa Platform Connect`                                                                         |
| vdcbocom               | Bank of Communications on `Visa Platform Connect`                                                                        |
| vdcbkeastasiahk        | Bank of East Asia Ltd. on `Visa Platform Connect`                                                                        |
| vdcbanknznz            | Bank of New Zealand on `Visa Platform Connect`                                                                           |
| vdcacpbsn              | Bank Simpanan Nasional (BSN) on `Visa Platform Connect`                                                                  |
| vdcbksinarmasid        | Bank Sinarmas (Omise Ltd.) on `Visa Platform Connect`                                                                    |
| vdcmisreg              | Banque Misr on `Visa Platform Connect`                                                                                   |
| vdcbcellao             | Banque Pour Le Commerce Exterieur Lao (BCEL) on `Visa Platform Connect`                                                  |
| vdcbarclaysbw          | Barclays Bank Botswana on `Visa Platform Connect`                                                                        |
| vdcbarclaysgh          | Barclays Bank Ghana on `Visa Platform Connect`                                                                           |
| vdcbarclaysmu          | Barclays Bank Mauritius Ltd. on `Visa Platform Connect`                                                                  |
| vdcbarclaysghtzug      | Barclays Bank of Ghana Ltd., Barclays Bank of Tanzania Ltd., and Barclays Bank of Uganda Ltd. on `Visa Platform Connect` |
| vdcbarclayske          | Barclays Bank of Kenya on `Visa Platform Connect`                                                                        |
| vdcbarclayszm          | Barclays Bank of Zambia on `Visa Platform Connect`                                                                       |
| vdcbarclayssc          | Barclays Bank Seychelles on `Visa Platform Connect`                                                                      |
| vdcbarclaystz          | Barclays Bank Tanzania on `Visa Platform Connect`                                                                        |
| vdcbarclaysug          | Barclays Bank Uganda on `Visa Platform Connect`                                                                          |
| vdcbccardkr            | BC Card Co., Ltd. on `Visa Platform Connect`                                                                             |
| vdcbdounibkph          | BDO Unibank, Inc. in Philippines on `Visa Platform Connect`                                                              |
| vdcbfvsgsn             | BFV Société Générale on `Visa Platform Connect`                                                                          |
| vdcbocihk              | BOC International Holdings Ltd. (BOCI) on `Visa Platform Connect`                                                        |
| vdcbracbkltdbd         | BRAC Bank Ltd. on `Visa Platform Connect`                                                                                |
| vdcburganbkkw          | Burgan Bank on `Visa Platform Connect`                                                                                   |
| vdccampubkkh           | Cambodian Public Bank on `Visa Platform Connect`                                                                         |
| vdccapitalbkjo         | Capital Bank of Jordan on `Visa Platform Connect`                                                                        |
| vdcplcapone            | Capital One on `Visa Platform Connect`                                                                                   |
| opdcardnet             | Cardnet International on OmniPay Direct                                                                                  |
| vdccaribbeancckn       | Caribbean Credit Card Corporation Ltd. on `Visa Platform Connect`                                                        |
| vdccubtw               | Cathay United Bank (CUB) on `Visa Platform Connect`                                                                      |
| vdcacpcaymannb         | Cayman National Bank Ltd. on `Visa Platform Connect`                                                                     |
| vdcccbhk               | CCBC in Hong Kong on `Visa Platform Connect`                                                                             |
| vdcciticbankcn         | China CITIC Bank Credit Card Center on `Visa Platform Connect`                                                           |
| vdccimbbkmy            | CIMB Bank Berhad on `Visa Platform Connect`                                                                              |
| vdccitihkmo            | Citibank Hongkong and Macau on `Visa Platform Connect`                                                                   |
| vdccitiau              | Citibank in Australia on `Visa Platform Connect`                                                                         |
| vdccitimy              | Citibank Malaysia on `Visa Platform Connect`                                                                             |
| vdccitisg              | Citibank Singapore Ltd. on `Visa Platform Connect`                                                                       |
| vdcacpdominicana       | CMP SA Dominicana on `Visa Platform Connect`                                                                             |
| vdccbocsl              | Commercial Bank of Ceylon on `Visa Platform Connect`                                                                     |
| vdccbduae              | Commercial Bank of Dubai on `Visa Platform Connect`                                                                      |
| vdccommbket            | Commercial Bank of Ethiopia on `Visa Platform Connect`                                                                   |
| vdccbq                 | Commercial Bank of Qatar on `Visa Platform Connect`                                                                      |
| vdccbadxcau            | Commonwealth Bank of Australia DXC on `Visa Platform Connect`                                                            |
| vdccbafisau            | Commonweatlh Bank of Australia FIS on `Visa Platform Connect`                                                            |
| vdcvnperumc            | Compañía Peruana de Medios de Pago on `Visa Platform Connect`                                                            |
| vdccardnetdo           | Consorcio De Tarjetas Dominicanas, S.A. (Cardnet) on `Visa Platform Connect`                                             |
| vdccoopbkke            | Cooperative Bank in Kenya on `Visa Platform Connect`                                                                     |
| vdccrdbbktz            | CRDB Bank PLC on `Visa Platform Connect`                                                                                 |
| vdccredibanco          | Credibanco on `Visa Platform Connect`                                                                                    |
| vdccredicorppn         | Credicorp Bank on `Visa Platform Connect`                                                                                |
| vdccredimax            | CrediMax (Bahrain) on `Visa Platform Connect`                                                                            |
| vdcctbc                | CTBC Bank Ltd. on `Visa Platform Connect`                                                                                |
| vdcdashenbanket        | Dashen Bank Ethiopia (Amole) on `Visa Platform Connect`                                                                  |
| vdcdeltaair            | Delta AIR on `Visa Platform Connect`                                                                                     |
| vdcdohabkqa            | Doha Bank on `Visa Platform Connect`                                                                                     |
| vdcdubaiislamicbankuae | Dubai Islamic Bank on `Visa Platform Connect`                                                                            |
| vdceblbankbd           | Eastern Bank Ltd. on `Visa Platform Connect`                                                                             |
| vdcecobankgh           | Ecobank in Ghana on `Visa Platform Connect`                                                                              |
| vdcelavonie            | Elavon Ireland on `Visa Platform Connect`                                                                                |
| vdcacpelavon           | Elavon on `Visa Platform Connect`                                                                                        |
| vdcequitybkke          | Equity Bank on `Visa Platform Connect`                                                                                   |
| vdcevertecpr           | Evertec, Inc. hybrid on `Visa Platform Connect` and Visa Accelerated Connection Platform (ACP)                           |
| vdcfarelogix           | Farelogix on `Visa Platform Connect` (authorization only)                                                                |
| vdcfdmsau              | FDMS Australia on `Visa Platform Connect`                                                                                |
| vdcficohsahn           | Ficohsa on `Visa Platform Connect`                                                                                       |
| vdcacpcibc             | FirstCaribbean International Bank (FCIB) in Barbados on `Visa Platform Connect`                                          |
| vdcfcbtt               | First Citizens Bank on `Visa Platform Connect`                                                                           |
| vdcfdmsbn              | First Data Merchant Solutions in Brunei on `Visa Platform Connect`                                                       |
| vdcfdmshk              | First Data Merchant Solutions in Hong Kong on `Visa Platform Connect`                                                    |
| vdcfdmsmy              | First Data Merchant Solutions in Malaysia on `Visa Platform Connect`                                                     |
| vdcfdmssg              | First Data Merchant Solutions in Singapore on `Visa Platform Connect`                                                    |
| vdcfnbza               | First National Bank (FNB) on `Visa Platform Connect`                                                                     |
| vdcfnb                 | FirstRand Bank on `Visa Platform Connect`                                                                                |
| vdcftbkh               | Foreign Trade Bank on `Visa Platform Connect`                                                                            |
| vdcfresnous            | Fresno - EPX/NAB on `Visa Platform Connect`                                                                              |
| vdchsbcbank            | Global Payments Asia Pacific on `Visa Platform Connect`                                                                  |
| vdcgpsbh               | Global Payment Services on `Visa Platform Connect`                                                                       |
| vdcgblpayau            | Global Payments in Australia on `Visa Platform Connect`                                                                  |
| omnipaydirect          | Global Payments International Acquiring on `OmniPay Direct`                                                              |
| vdcgpindia             | Global Payments Ltd. in India on `Visa Platform Connect`                                                                 |
| vdcglobalprocar        | Global Processing S.A on `Visa Platform Connect`                                                                         |
| vdcgtbankng            | Guaranty Trust (GT) Bank on `Visa Platform Connect`                                                                      |
| vdcgulfbkkw            | Gulf Bank on `Visa Platform Connect`                                                                                     |
| vdchabibltd            | Habib Bank Ltd. (HBL) on `Visa Platform Connect`                                                                         |
| vdchangsenghk          | Hang Seng Bank Ltd. on `Visa Platform Connect`                                                                           |
| vdchattonlk            | Hatton National Bank on `Visa Platform Connect`                                                                          |
| vdchdfc                | HDFC Bank Ltd. of India on `Visa Platform Connect`                                                                       |
| rupayhdfc              | HDFC Bank on `RuPay`                                                                                                     |
| vdcimbank              | I\&M Bank on `Visa Platform Connect`                                                                                     |
| vdcicepaybvnl          | ICEPAY B.V. Ireland on `Visa Platform Connect`                                                                           |
| vdcicici               | ICICI of India on `Visa Platform Connect`                                                                                |
| vdcindozambiabkzm      | Indo Zambia Bank on `Visa Platform Connect`                                                                              |
| vdcicbcasisahk         | Industrial and Commercial Bank of China (Asia) on `Visa Platform Connect`                                                |
| vdcicbc                | Industrial and Commercial Bank of China (ICBC) on `Visa Platform Connect`                                                |
| vdcinterswitchng       | Interswitch Ltd. on `Visa Platform Connect`                                                                              |
| vdcishtariq            | Ishtar Gate for e-Payment Systems and Services                                                                           |
| vdcmulticajacl         | Iswitch - Multicaja on `Visa Platform Connect`                                                                           |
| vdcconcordprocarduk    | JSCB Concord on `Visa Platform Connect`                                                                                  |
| vdckapitalbkuz         | Kapital Bank on `Visa Platform Connect`                                                                                  |
| vdckbankvn             | Kasikornbank (Kbank) in Vietnam on `Visa Platform Connect`                                                               |
| vdckbank               | Kasikornbank (Kbank) on `Visa Platform Connect`                                                                          |
| vdckbzmm               | KBZ Bank on `Visa Platform Connect`                                                                                      |
| vdckcbank              | Kenya Commercial Bank on `Visa Platform Connect`                                                                         |
| vdckeb                 | Korea Exchange Bank (KEB) on `Visa Platform Connect`                                                                     |
| vdcktbth               | Krungthai Bank Public Company Ltd. on `Visa Platform Connect`                                                            |
| vdckibkw               | Kuwait International Bank on `Visa Platform Connect`                                                                     |
| vdcledgerpayus         | Ledgerpay - Westamerica Bank on `Visa Platform Connect`                                                                  |
| vdclinkserbo           | Linkser Empresa Administradora de Tarjetas on `Visa Platform Connect`                                                    |
| vdclivepymtau          | Live Payments on `Visa Platform Connect`                                                                                 |
| vdcmadfooatjo          | MadfooatCom on `Visa Platform Connect`                                                                                   |
| vdcmashreqbk           | Mashreq on `Visa Platform Connect`                                                                                       |
| vdcmaybankmy           | Maybank on `Visa Platform Connect`                                                                                       |
| vdcmetrobkpa           | MetroBank S.A on `Visa Platform Connect`                                                                                 |
| vdcmetropolitan        | Metropolitan Bank on `Visa Platform Connect`                                                                             |
| vdcmepsjo              | Middle East Payment Services (MEPS) on `Visa Platform Connect`                                                           |
| vdcacpnabau            | National Australia Bank on `Visa Platform Connect`                                                                       |
| vdcnbad                | National Bank of Abu Dhabi (NBAD) on `Visa Platform Connect`                                                             |
| vdcnabdinau            | National Bank of Australia (Diners or Discover) on `Visa Platform Connect`                                               |
| vdcnabau               | National Bank of Australia on `Visa Platform Connect`                                                                    |
| vdcacpnatlcalif        | National Bank of California on `Visa Platform Connect`                                                                   |
| vdcnbctz               | National Bank of Commerce in Tanzania on `Visa Platform Connect`                                                         |
| vdcnationalbkgr        | National Bank of Greece (NBG) on `Visa Platform Connect`                                                                 |
| vdcnbk                 | National Bank of Kuwait (NBK) on `Visa Platform Connect`                                                                 |
| vdcnboom               | National Bank of Oman on `Visa Platform Connect`                                                                         |
| vdcacpncbj             | National Commercial Bank (NCB) Jamaica hybrid on `Visa Platform Connect` and Visa Accelerated Connection Platform (ACP)  |
| vdcnacombk             | National Commercial Bank on `Visa Platform Connect`                                                                      |
| vdcndblk               | National Development Bank on `Visa Platform Connect`                                                                     |
| vdcnayapaypk           | NayaPay on `Visa Platform Connect`                                                                                       |
| vdcncbabkke            | NCBA Bank Kenya on `Visa Platform Connect`                                                                               |
| vdcnijo                | Network International (NI) Jordan on `Visa Platform Connect`                                                             |
| vdcnicnepal            | NIC Asia Bank Ltd. on `Visa Platform Connect`                                                                            |
| vdcnovattiau           | Novatti Australia on `Visa Platform Connect`                                                                             |
| vdcjscoschadbkua       | Oschadbank on `Visa Platform Connect`                                                                                    |
| vdcocbc                | Overseas Chinese Banking Corp (OCBC) on `Visa Platform Connect`                                                          |
| vdcappspk              | PayFast (APPS) on `Visa Platform Connect`                                                                                |
| vdcpayglocalin         | PayGlocal Technologies on `Visa Platform Connect`                                                                        |
| vdcpaymayaph           | PayMaya on `Visa Platform Connect`                                                                                       |
| vdcpymtsnsltdgb        | Paymentsense on `Visa Platform Connect`                                                                                  |
| vdcpayzlius            | Payzli on `Visa Platform Connect`                                                                                        |
| vdcpeoplesbksl         | Peoples Bank on `Visa Platform Connect`                                                                                  |
| vdcpinganbkch          | Ping An Bank in China on `Visa Platform Connect`                                                                         |
| vdcplanetmrchntservuk  | Planet Merchant Services on `Visa Platform Connect`                                                                      |
| vdcprismampar          | Prisma de Pago S.A. on `Visa Platform Connect`                                                                           |
| vdcprocardsapy         | Procard S.A. on `Visa Platform Connect`                                                                                  |
| vdcizipaype            | Procesos de Medios de Pago S.A. on `Visa Platform Connect`                                                               |
| vdcpromerica           | Promerica in Honduras and Nicaragua on `Visa Platform Connect`                                                           |
| vdcbkctrlasiaid        | PT Bank Central Asia on `Visa Platform Connect`                                                                          |
| vdccimbniagaid         | PT Bank CIMB Niaga Tbk in Indonesia on `Visa Platform Connect`                                                           |
| vdcbkdanamonid         | PT Bank Danamon on `Visa Platform Connect`                                                                               |
| vdcbankmegaid          | PT Bank Mega Tbk on `Visa Platform Connect`                                                                              |
| vdcbni                 | PT Bank Negara Indonesia on `Visa Platform Connect`                                                                      |
| vdcbkrakyatid          | PT Bank Rakyat Indonesia on `Visa Platform Connect`                                                                      |
| vdcbkmandiri           | PT Mitra Transaki Indonesia - Bk Mandiri on `Visa Platform Connect`                                                      |
| vdcpbbma               | Public Bank Berhad on `Visa Platform Connect`                                                                            |
| vdcqnbqa               | Qatar National Bank (QNB Group) on `Visa Platform Connect`                                                               |
| vdcraiffeisenua        | Raiffeisen Bank Aval on `Visa Platform Connect`                                                                          |
| vdcraiffeisenbh        | Raiffeisen Bank dd Bosnia and Herzegovina on `Visa Platform Connect`                                                     |
| vdcraiffeisenat        | Raiffeisen Bank on `Visa Platform Connect`                                                                               |
| vdcrakbankuae          | RAKBANK on `Visa Platform Connect`                                                                                       |
| vdcredebanco           | Redeban - Davivienda on `Visa Platform Connect`                                                                          |
| vdcrbmredebanco        | Redeban - Multicolor on `Visa Platform Connect`                                                                          |
| vdcacprepublictt       | Republic Bank hybrid on `Visa Platform Connect` and Visa Accelerated Connection Platform (ACP)                           |
| vdcrhbbankberhadmy     | RHB Bank Berhad on `Visa Platform Connect`                                                                               |
| vdcacprbc              | Royal Bank of Canada in Caribbean on `Visa Platform Connect`                                                             |
| vdcsacomb              | Sacombank on `Visa Platform Connect`                                                                                     |
| vdcsafaricomke         | Safaricom PLC on `Visa Platform Connect`                                                                                 |
| vdcsafepaypk           | Safepay on `Visa Platform Connect`                                                                                       |
| vdcacpscotiabk         | Scotia Bank in Caribbean hybrid on `Visa Platform Connect` and Visa Accelerated Connection Platform (ACP)                |
| vdcscotiabkca          | Scotia Bank on `Visa Platform Connect`                                                                                   |
| vdcsiamth              | Siam Commercial Bank on `Visa Platform Connect`                                                                          |
| vdcsocgeneralgh        | Societe General Ghana on `Visa Platform Connect`                                                                         |
| vdcsoutheastbkbd       | Southeast Bank Ltd. on `Visa Platform Connect`                                                                           |
| vdcsmcc                | Sumitomo Mitsui Card Co. on `Visa Platform Connect`                                                                      |
| vdctaishintw           | Taishin Bank Ltd. on `Visa Platform Connect`                                                                             |
| vdctbcge               | TBC Bank on `Visa Platform Connect`                                                                                      |
| vdctcmshk              | TCM Solutions Ltd. on `Visa Platform Connect`                                                                            |
| vdcterrapaymu          | TerraPay Mauritius on `Visa Platform Connect`                                                                            |
| vdcsaudibritishbksa    | The Saudi British Bank on `Visa Platform Connect`                                                                        |
| vdcstandrdbkza         | The Standard Bank of South Africa on `Visa Platform Connect`                                                             |
| vdctillau              | Till Payments on `Visa Platform Connect`                                                                                 |
| vdcunicreptgl          | UNICRE on `Visa Platform Connect`                                                                                        |
| vdcunionbkph           | Union Bank in Philippines on `Visa Platform Connect`                                                                     |
| vdcuntdbkafricang      | United Bank for Africa on `Visa Platform Connect`                                                                        |
| vdcacpuba              | United Bank of Africa, PLC on `Visa Platform Connect`                                                                    |
| vdcuob                 | United Overseas Bank (UOB) in Singapore and Vietnam on `Visa Platform Connect`                                           |
| vdcuobth               | United Overseas Bank (UOB) in Thailand on `Visa Platform Connect`                                                        |
| vdcuob                 | United Overseas Bank (UOB) on `Visa Platform Connect`                                                                    |
| vdcvantiv              | Vantiv on `Visa Platform Connect`                                                                                        |
| vdcvietcombk           | Vietcombank on `Visa Platform Connect`                                                                                   |
| vdcvietin              | VietinBank on `Visa Platform Connect`                                                                                    |
| vdcvpbankvn            | Vietnam Prosperity Joint-Stock Commercial Bank on `Visa Platform Connect`                                                |
| vdctechcomvn           | Vietnam Technological and Commercial Joint Stock Bank (Techcombank) on `Visa Platform Connect`                           |
| vdcguatemala           | Visa Guatemala on `Visa Platform Connect`                                                                                |
| vdcvisanetdo           | VisaNet Dominicana on `Visa Platform Connect`                                                                            |
| vdcvnperu              | VisaNet Peru on `Visa Platform Connect`                                                                                  |
| vdcvisanetuy           | VisaNet Uruguay on `Visa Platform Connect`                                                                               |
| vdcuruguay             | Visa Uruguay on `Visa Platform Connect`                                                                                  |
| vdcacpwfb              | Wells Fargo Bank on `Visa Platform Connect`                                                                              |
| vdcwestpacnz           | Westpac New Zealand on `Visa Platform Connect`                                                                           |
| vdcwestpac             | Westpac on `Visa Platform Connect`                                                                                       |
| vdcwhb                 | Wing Hang Bank on `Visa Platform Connect`                                                                                |
| vdcwinglung            | Wing Lung Bank on `Visa Platform Connect`                                                                                |
| vdcwirecardhk          | Wirecard in Hong Kong on `Visa Platform Connect`                                                                         |
| vdcwirecardde          | Wirecard in Munich on `Visa Platform Connect`                                                                            |
| vdcwirecardsg          | Wirecard in Singapore on `Visa Platform Connect`                                                                         |
| vdcwoodforestus        | Woodforest National Bank on `Visa Platform Connect`                                                                      |
| vdcwpayau              | Wpay in Australia on `Visa Platform Connect`                                                                             |
| vdcwpayltdnz           | Wpay Ltd. in New Zealand on `Visa Platform Connect`                                                                      |
| vdcyesbank             | YES BANK Ltd. in Mumbai on `Visa Platform Connect`                                                                       |
| vdcyspcn               | Yinsheng E-Pay Services (Holding) Ltd. on `Visa Platform Connect`                                                        |
| vdczanacozam           | Zanaco on `Visa Platform Connect`                                                                                        |
| vdcacpzenithbank       | Zenith Bank on `Visa Platform Connect`                                                                                   |

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

VISA Platform Connect: Specifications and Conditions for Resellers/Partners {#vpc-partner-reseller-disclaimer}
==============================================================================================================

The following are specifications and conditions that apply to a Reseller/Partner enabling its merchants through Cybersource for Visa Platform Connect ("VPC") processing. Failure to meet any of the specifications and conditions below is subject to the liability provisions and indemnification obligations under Reseller/Partner's contract with Visa/Cybersource.

1. Before boarding merchants for payment processing on a VPC acquirer's connection, Reseller/Partner and the VPC acquirer must have a contract or other legal agreement that permits Reseller/Partner to enable its merchants to process payments with the acquirer through the dedicated VPC connection and/or traditional connection with such VPC acquirer.
2. Reseller/Partner is responsible for boarding and enabling its merchants in accordance with the terms of the contract or other legal agreement with the relevant VPC acquirer.
3. Reseller/Partner acknowledges and agrees that all considerations and fees associated with chargebacks, interchange downgrades, settlement issues, funding delays, and other processing related activities are strictly between Reseller and the relevant VPC acquirer.
4. Reseller/Partner acknowledges and agrees that the relevant VPC acquirer is responsible for payment processing issues, including but not limited to, transaction declines by network/issuer, decline rates, and interchange qualification, as may be agreed to or outlined in the contract or other legal agreement between Reseller/Partner and such VPC acquirer.

DISCLAIMER: NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR ANY ERRORS OR OMISSIONS BY THE Visa Platform Connect ACQUIRER IN PROCESSING TRANSACTIONS. NEITHER VISA NOR CYBERSOURCE WILL BE RESPONSIBLE OR LIABLE FOR RESELLER/PARTNER BOARDING MERCHANTS OR ENABLING MERCHANT PROCESSING IN VIOLATION OF THE TERMS AND CONDITIONS IMPOSED BY THE RELEVANT Visa Platform Connect ACQUIRER.
