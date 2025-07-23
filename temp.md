# [ID][Length][Value]

1. Payload Format Indicator
`00 02 01`

2. Point of Initiation Method
`01 02 12`

3. Merchant Account Information
`38 <length>  00 10 A000000727  01 [length] 0006970422 0112040204020694 0208QRIBFTTA`


<!-- 4. Merchant Category Code
`52 04 5999` -->

5. Transaction Currency 
`53 03 704`

6. Transaction Amount
`54 04 1000`

7. Country Code
`58 02 VN`

8. Merchant Name
`59 13 DAU VAN GIANG`

`62080804TEST`

<!-- 9. Merchant City
`60 05 HANOI` -->

10. CRC
`63 04 [crc tinh tu dau den 6304 => chuoi hex 4 ky tu]`