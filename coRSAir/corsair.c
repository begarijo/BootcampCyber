/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   corsair.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: begarijo <begarijo@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/15 15:08:08 by begarijo          #+#    #+#             */
/*   Updated: 2023/05/17 12:31:25 by begarijo         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "openssl/rsa.h"
#include "openssl/bn.h"
#include "openssl/pem.h"
#include "openssl/bio.h"
#include "openssl/x509.h"
#include "openssl/evp.h"

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>

#ifndef BUFFER_SIZE
# define BUFFER_SIZE 1024
#endif

int	parse_args(char *av1, char *av2, char *av3)
{
	if ((!strrchr(av1, '.') || strrchr(av1, '.') == av1)
		|| (!strrchr(av2, '.') || strrchr(av2, '.') == av2)
		|| (!strrchr(av3, '.') || strrchr(av3, '.') == av3))
	{
		printf("Some files could not be read.");
		return (0);
	}
	if (strcmp(strrchr(av1, '.'), ".pem") != 0
		|| strcmp(strrchr(av2, '.'), ".pem") != 0
		|| strcmp(strrchr(av3, '.'), ".enc") != 0)
	{
		printf("%s\n", strrchr(av1, '.'));
		printf("%s\n", strrchr(av2, '.'));
		printf("%s\n", strrchr(av3, '.'));
		printf("Some files extensions are wrong.");
		return (0);
	}
	else
		return (1);
}

RSA	*get_rsa(char *file)
{
	BIO			*bio_cert;
	X509		*cert;
	EVP_PKEY	*pub_key;
	RSA			*rsa;

	bio_cert = BIO_new(BIO_s_file());
	if ((BIO_read_filename(bio_cert, file)) != 1)
	{
		printf("Error");
		exit (0);
	}
	cert = PEM_read_bio_X509(bio_cert, NULL, 0, NULL);
	pub_key = X509_get_pubkey(cert);
	rsa = EVP_PKEY_get1_RSA(pub_key);
	X509_free(cert);
	EVP_PKEY_free(pub_key);
	BIO_free(bio_cert);
	return (rsa);
}

BIGNUM	*calculate_phi_n(BIGNUM *q1, BIGNUM *p, BIGNUM *one, BN_CTX *ctx)
{
	BIGNUM			*phi_q1;
	BIGNUM			*phi_p;
	BIGNUM			*phi_n;

	phi_q1 = BN_new();
	phi_p = BN_new();
	phi_n = BN_new();
	BN_sub(phi_q1, q1, one);
	BN_sub(phi_p, p, one);
	BN_mul(phi_n, phi_q1, phi_p, ctx);
	BN_free(phi_q1);
	BN_free(phi_p);
	return (phi_n);
}

BIGNUM	*calculate_d(BIGNUM *n1, BIGNUM *n2, BIGNUM *e, BN_CTX *ctx)
{
	BIGNUM			*d;
	BIGNUM			*one;
	BIGNUM			*q1;
	BIGNUM			*phi_n;
	BIGNUM			*p;

	q1 = BN_new();
	p = BN_new();
	d = BN_new();
	one = BN_new();

	BN_dec2bn(&one, "1");
	BN_gcd(p, n1, n2, ctx);
	BN_div(q1, NULL, n1, p, ctx);
	phi_n = calculate_phi_n(q1, p, one, ctx);
	BN_mod_inverse(d, e, phi_n, ctx);

	BN_free(p);
	BN_free(q1);
	BN_free(phi_n);
	return (d);
}

void	encrypt_decrypt(RSA *private, char *passwd)
{
	int				len;
	unsigned char	*buf_input;
	unsigned char	*buf_output;

	buf_input = (unsigned char *)malloc(sizeof(char) * BUFFER_SIZE);
	buf_output = (unsigned char *)malloc(sizeof(char) * BUFFER_SIZE);
	len = read(open(passwd, O_RDONLY), buf_input, BUFFER_SIZE);
	RSA_private_decrypt(len, buf_input, buf_output, private, RSA_PKCS1_PADDING);

	printf("\nEncrypt: %s\n", buf_input);
	printf("\nDecrypted: %s\n", buf_output);

	free(buf_input);
	free(buf_output);
	buf_input = NULL;
	buf_output = NULL;
}

int	main(int argc, char **av)
{
	RSA		*private;
	BIGNUM	*n1;
	BIGNUM	*n2;
	BIGNUM	*e;
	BIGNUM	*d;
	BN_CTX	*ctx;

	if (argc != 4 || parse_args(av[1], av[2], av[3]) == 0)
		return (0);
	private = RSA_new();
	ctx = BN_CTX_new();
	n1 = (BIGNUM *)RSA_get0_n(get_rsa(av[1]));
	n2 = (BIGNUM *)RSA_get0_n(get_rsa(av[2]));
	e = (BIGNUM *)RSA_get0_e(get_rsa(av[1]));
	d = calculate_d(n1, n2, e, ctx);

	RSA_set0_key(private, n1, e, d);
	encrypt_decrypt(private, av[3]);
	BN_free(n1);
	BN_free(n2);
	BN_free(e);
	BN_free(d);
	BN_CTX_free(ctx);
}
