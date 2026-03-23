-- 코드를 입력하세요

SELECT product_code, price*A.SALES as SALES
FROM PRODUCT
JOIN (
    SELECT product_id,sum(sales_amount) as SALES
    FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
    ) A
ON A.product_id =PRODUCT.product_id
ORDER BY SALES DESC, product_code ASC

    # SELECT product_id, sum(sales_amount)
    # FROM OFFLINE_SALE
    # GROUP BY PRODUCT_ID
    
    
    
#     id = 5 -> 3