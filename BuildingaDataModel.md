# Building a Data Model

## Intro To Data Modeling

The first step in every Django project is figuring out the pieces of data we want to store.

What concepts and entities do we have in an E-commerce app:

for starters we need:

Product:

1. title
2. description
3. price
4. inventory

Quite often our products are divide into different categories like: shoes, beauty-products, fruits and so on.

so we need another entity called `collection` or `category`

Collection:

- title

so now we need to make a relation or association between these entities so we can start from one end and move to the other end. for example we can take a collection and find all the products in that collection.

![product-collection-relationship](./product-collection-relation.png)

```txt

Product                       collection
          *___one to many__1
title                         title
description
price
inventory


```

relationships cab be

![relations](relations.png)
![featured product](featured-product.png)

Great question! Let’s break down this diagram step by step so you fully understand the **relationships** and how they fit into data modeling.

---

### 1️⃣ **Entities in the Diagram**

We have two entities (tables/models):

- **Product**

  - Fields: `title`, `description`, `price`, `inventory`

- **Collection**

  - Fields: `title`

These represent **real-world objects**:

- A **Product** is something you sell (e.g., "iPhone 14").
- A **Collection** is a group/category of products (e.g., "Smartphones").

---

### 2️⃣ **Relationships Between Them**

There are **two relationships** shown:

#### 🔹 (A) `products` (One-to-Many: 1 ↔ \*)

- A **Collection** can contain **many Products**.
- But **each Product belongs to exactly ONE Collection**.
  Example:

  - Collection: "Laptops"

    - Product 1: MacBook Pro
    - Product 2: Dell XPS
    - Product 3: Lenovo ThinkPad

✅ In Django:

- `Product` will have a `ForeignKey` pointing to `Collection`.

---

#### 🔹 (B) `featured_product` (Optional 0..1)

This is the **special (0..1) relationship** you asked about:

- A **Collection** can have **zero or one featured product**.

  - 0 means: It’s optional (not all collections need a featured product).
  - 1 means: At most one product can be "featured" in a collection.

Example:

- Collection: "Smartphones" → Featured Product: iPhone 14
- Collection: "Laptops" → Featured Product: (none)

✅ In Django:

- `Collection` will have a `featured_product` field, which is a `ForeignKey` to `Product` but marked as `null=True` (optional).

---

### 3️⃣ **Why Both Relationships Exist?**

Even though **`products`** already connects products to collections,
the **`featured_product`** is a **special pointer** to highlight ONE product within that collection.

Think of it like:

- `products`: all items in the collection (general list).
- `featured_product`: one special "spotlight" product in that collection.

---

### 4️⃣ **How it Looks in Django Models**

```python
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')
```

---

### ✅ **Key Takeaways**

- **One-to-many** (`products`): One collection → many products.
- **Optional one-to-one-ish** (`featured_product`): One collection → zero or one highlighted product.
- The **0..1 notation** means it’s an **optional relationship**, unlike `*` (many) or `1` (required).

---

Good morning! 🌞 Great question — this diagram introduces a very **important concept in database design: association classes** (or junction tables in databases). Let’s break it down step-by-step so it’s crystal clear for you as a beginner.

---

## 1️⃣ **What's Happening in This Diagram?**

We have 3 entities:

- **Product** → Items you sell (e.g., "iPhone 14").
- **Cart** → The shopping cart where customers put items.
- **CartItem** → The "bridge" that connects a cart and its products.

---

## 2️⃣ **Many-to-Many Relationship**

- A **Cart** can contain many **Products**.
- A **Product** can be in many **Carts** (e.g., multiple customers can add "iPhone 14" to their carts).

This is a **many-to-many** (M\:N) relationship.

➡️ But **relational databases** (and Django models) can't directly store many-to-many with extra info (like quantity).
➡️ So, we **break it down using an intermediate table/class**.

---

## 3️⃣ **Association Class (CartItem)**

- **Definition:** An **association class** is a table/model that **sits between two entities in a many-to-many relationship** and also **holds extra attributes** for that relationship.

In this case:

- `CartItem` connects `Cart` and `Product`.
- It adds **`quantity`** (because we need to track how many of each product is in the cart).

💡 Without `CartItem`, we couldn’t store **how many units** of each product the user added.

---

## 4️⃣ **Dashed Line Meaning**

The **dashed line** from `CartItem` to the middle of the Cart–Product line means:

- `CartItem` is an **association (or link) class**.
- It’s **not independent**; it **only exists because of the relationship** between `Cart` and `Product`.

So, you **can’t have a CartItem** that isn’t linked to both a Cart and a Product.

---

## 5️⃣ **When Does a Relationship Need Attributes?**

Normally, a relationship just connects two tables (like a foreign key). But if you need to store **extra data about that connection**, you turn it into an **association class**.

Examples:

- Cart ↔ Product → needs **quantity**.
- Student ↔ Course → needs **enrollment_date** and **grade**.
- Event ↔ Attendee → needs **ticket_type** or **seat_number**.

✅ If a relationship **doesn’t need extra attributes**, you can use a simple **ForeignKey** or **ManyToManyField** in Django.
✅ If it **does need attributes**, you create an **association model** (like CartItem).

---

## 6️⃣ **Why No User Link Yet?**

Mosh didn’t connect **User ↔ Cart** because:

- He wants **anonymous carts** (guests can add items without logging in).
- When the user eventually logs in or signs up, the cart can be linked to their account.

This is common in e-commerce:

- You can browse and add items **without logging in**.
- You’re only forced to log in at **checkout**.

---

## 7️⃣ **Django Implementation**

Here’s how this looks in Django:

```python
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
```

Here, `CartItem` is the **association class** that connects `Cart` and `Product` while holding `quantity`.

---

### ✅ Key Points to Remember

- **Dashed line** = Association class (dependent on two tables).
- Use it when you need **extra data on a relationship** (like `quantity`).
- Guest carts don’t require users until checkout.

---

Would you like me to **draw a real-world example** with sample data (showing tables and rows for Cart, Product, and CartItem) so you see how these connect in practice?

## Creating Models

Here’s a **comprehensive, easy-to-review set of notes** based on your Django models so far. I’ll break it down into **sections**, so you can quickly revisit concepts like fields, choices, and relationships. Let’s go step by step.

---

## ✅ **1. Django Models Overview**

- **Models** represent tables in the database.
- Each **class attribute** in a model corresponds to a **column** in the table.
- Django automatically creates an **ID primary key** for each model (unless overridden).

---

## ✅ **2. Common Field Types in Your Models**

### 🔹 **CharField**

- Stores **short text** (e.g., names, titles).
- Requires `max_length` (for DB schema & validation).

```python
title = models.CharField(max_length=255)
```

### 🔹 **TextField**

- Stores **long text** (e.g., product descriptions).
- No `max_length` needed.

```python
description = models.TextField()
```

### 🔹 **EmailField**

- Special `CharField` that validates emails.
- Often combined with `unique=True` for unique emails.

```python
email = models.EmailField(unique=True)
```

### 🔹 **IntegerField**

- Stores integer values (e.g., quantity, inventory).

```python
inventory = models.IntegerField()
```

### 🔹 **DecimalField**

- Stores **decimal numbers** (useful for money).
- Requires:

  - `max_digits` → total number of digits (including decimals).
  - `decimal_places` → digits after the decimal point.

```python
price = models.DecimalField(max_digits=6, decimal_places=2)
# Example: max 9999.99
```

### 🔹 **DateField**

- Stores **date** only.
- `null=True` means it can be empty in DB.

```python
birth_date = models.DateField(null=True)
```

### 🔹 **DateTimeField**

- Stores **date + time**.
- Common options:

  - `auto_now=True` → updates timestamp **every time** the object is saved (good for "last updated").
  - `auto_now_add=True` → sets timestamp **only when created** (good for "created at").

```python
last_update = models.DateTimeField(auto_now=True)
```

---

## ✅ **3. Choices Field (Enums in Django)**

### Why use `choices`?

- To restrict the value of a field to **predefined options** (like enums in other languages).
- Improves **data integrity** and **code readability**.

Example from your code:

```python
MEMBERSHIP_BRONZE = "B"
MEMBERSHIP_SILVER = "S"
MEMBERSHIP_GOLD = "G"

MEMBERSHIP_CHOICES = [
    (MEMBERSHIP_BRONZE, "Bronze"),
    (MEMBERSHIP_SILVER, "Silver"),
    (MEMBERSHIP_GOLD, "Gold"),
]

membership = models.CharField(
    max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
)
```

✅ **Key Points**:

- First element in each tuple = stored value in DB.
- Second element = human-readable label for admin/forms.
- Good for statuses, categories, etc.

**Other example:**

```python
payment_status = models.CharField(
    max_length=1,
    choices=[("P", "Pending"), ("C", "Completed"), ("F", "Failed")],
    default="P"
)
```

---

## ✅ **4. Relationships in Django**

There are 3 main relationships:

- **One-to-One** (`OneToOneField`)
- **One-to-Many** (`ForeignKey`)
- **Many-to-Many** (`ManyToManyField`)

### 🔹 **One-to-One**

- Each record in **Model A** is linked to **exactly one** record in **Model B**, and vice versa.
- Similar to a **unique foreign key**.
- Example from your `Address` model:

```python
customer = models.OneToOneField(
    Customer,
    on_delete=models.SET_DEFAULT,
    primary_key=True
)
```

✅ **Key Points**:

- `on_delete` → what happens when the related object is deleted.

  - `CASCADE` → delete the related object too.
  - `SET_NULL` → set field to `NULL` (requires `null=True`).
  - `SET_DEFAULT` → set field to default value (requires a default).

- `primary_key=True` → this makes the `customer` field the primary key of `Address`.

### **Reverse Relationship**

- Django automatically creates a **reverse relationship**.
- For One-to-One:

  - From `Address` → `customer` (as defined).
  - From `Customer` → `address` (Django auto-creates this unless `related_name` is set).

Example usage in code:

```python
# Access address from customer
customer.address

# Access customer from address
address.customer
```

✅ You **don’t need to define reverse relationship manually** unless:

- You want a custom name (`related_name="my_address"`).
- Or you want to disable it (`related_name="+"`).

---

## ✅ **5. `on_delete` Behavior**

- Important for **referential integrity**.
- Options:

  - **CASCADE** → delete related rows.
  - **PROTECT** → prevent deletion (raises error).
  - **SET_NULL** → set to NULL.
  - **SET_DEFAULT** → set to default value.
  - **DO_NOTHING** → does nothing (risky!).

---

## ✅ **6. Auto-generated Primary Key**

- If you don’t define `primary_key=True`, Django adds `id` automatically.
- In `Address`, you defined `primary_key=True` on `customer` → so no extra `id`.

---

## ✅ **Quick Summary Table**

| Concept           | Example                                                       | Key Notes                         |
| ----------------- | ------------------------------------------------------------- | --------------------------------- |
| **CharField**     | `title = models.CharField(max_length=255)`                    | Short text, `max_length` required |
| **TextField**     | `description = models.TextField()`                            | Long text                         |
| **DecimalField**  | `price = models.DecimalField(max_digits=6, decimal_places=2)` | For money                         |
| **EmailField**    | `email = models.EmailField(unique=True)`                      | Validates email                   |
| **DateField**     | `birth_date = models.DateField(null=True)`                    | Date only                         |
| **DateTimeField** | `last_update = models.DateTimeField(auto_now=True)`           | Date + time                       |
| **choices**       | `membership = models.CharField(choices=...)`                  | Enum-like options                 |
| **OneToOneField** | `customer = models.OneToOneField(Customer, on_delete=...)`    | Unique relation                   |

---

## ✅ **7. Do We Need Reverse Relationships?**

- No, Django automatically creates them.
- But you can customize them with:

```python
related_name="custom_name"
```

Example:

```python
customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="home_address")
```

Now access via:

```python
customer.home_address
```

---

### 🔥 **Extra Tips for You**

- For real projects:

  - Add `__str__()` in models for better admin display.
  - Use `validators` for fields like price, phone.
  - Use `Meta` class for ordering, verbose names.

---

Would you like me to **add visual diagrams** showing how these tables relate to each other (ERD style) and include some **sample queries** for forward & reverse lookups?
That would make this review even more practical for you.
