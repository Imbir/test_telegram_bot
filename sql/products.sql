-- Table: public.products

-- DROP TABLE public.products;

CREATE TABLE public.products
(
    id integer NOT NULL DEFAULT nextval('table_2_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    price money NOT NULL,
    shipped date,
    CONSTRAINT table_2_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.products
    OWNER to postgres;