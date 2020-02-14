-- Table: public.people

-- DROP TABLE public.people;

CREATE TABLE public.people
(
    id integer NOT NULL DEFAULT nextval('table_1_id_seq'::regclass),
    name character varying(30) COLLATE pg_catalog."default" NOT NULL,
    age integer NOT NULL,
    CONSTRAINT table_1_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.people
    OWNER to postgres;