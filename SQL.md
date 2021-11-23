
Assume you have a table T with the following structure:


<table>
<tr>
<td><B>LABEL</B> </td>
<td><B>CPTY</B></td>
<td><B>VALUE</B></td>
</tr>

<tr>
<td>BASE</td>
<td>A</td>
<td>123.45</td>
</tr>  

<tr>
<td>STRESS</td>
<td>A</td>
<td>234.56</td>
</tr>  

<tr>
<td>BASE</td>
<td>B</td>
<td>345.67</td>
</tr>  

<tr>
<td>STRESS</td>
<td>B</td>
<td>456.78</td>
</tr> 

<tr>
<td>BASE</td>
<td>C</td>
<td>567.89</td>
</tr>  

<tr>
<td>STRESS</td>
<td>C</td>
<td>678.90</td>
</tr> 

<tr>
<td>...</td>
<td>...</td>
<td>...</td>
</tr> 

</table>
 

The columns (LABEL, CPTY) form a primary key of table T.

We want to get a table with IMPACT for each counterparty (CPTY), where IMPACT is defined as the difference of values between STRESS and BASE. 

The expected structure of the table is:

<table>
<tr>
<td><B>CPTY </B></td>
<td><B>IMPACT</B></td>
</tr>
<tr>
<td>A</td>
<td>...</td>
</tr>    
<tr>
<td>B</td>
<td>...</td>
</tr>
</table>
 
