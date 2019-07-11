CREATE TABLE `aisles`
(
  `aisle_id` int PRIMARY KEY,
  `aisle` varchar(255)
);

CREATE TABLE `departments`
(
  `department_id` int PRIMARY KEY,
  `department` varchar(255)
);

CREATE TABLE `products`
(
  `product_id` int PRIMARY KEY,
  `product_name` varchar(255),
  `aisle_id` int,
  `department_id` int
);

CREATE TABLE `orders`
(
  `order_id` int PRIMARY KEY,
  `user_id` int,
  `eval_set` ENUM ('prior', 'train', 'test'),
  `order_number` int,
  `order_dow` int,
  `order_hour_of_day` int,
  `days_since_prior_order` float
);

CREATE TABLE `order_products__prior`
(
  `order_id` int,
  `product_id` int,
  `add_to_cart_order` int,
  `reordered` int
);

CREATE TABLE `order_products__train`
(
  `order_id` int,
  `product_id` int,
  `add_to_cart_order` int,
  `reordered` int
);

ALTER TABLE `products` ADD FOREIGN KEY (`aisle_id`) REFERENCES `aisles` (`aisle_id`);

ALTER TABLE `products` ADD FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`);

ALTER TABLE `order_products__prior` ADD FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`);

ALTER TABLE `order_products__prior` ADD FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);

ALTER TABLE `order_products__train` ADD FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`);

ALTER TABLE `order_products__train` ADD FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`);

