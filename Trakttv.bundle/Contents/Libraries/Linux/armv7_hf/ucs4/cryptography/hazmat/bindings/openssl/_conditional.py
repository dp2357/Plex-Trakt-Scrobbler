# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

# This is a temporary copy of all the CONDITIONAL_NAMES from _cffi_src so
# we can loop over them and delete them at runtime. It will be removed when
# cffi supports #if in cdef

CONDITIONAL_NAMES = {
    "Cryptography_HAS_AES_WRAP": [
        "AES_wrap_key",
        "AES_unwrap_key",
    ],
    "Cryptography_HAS_CMAC": [
        "CMAC_CTX_new",
        "CMAC_Init",
        "CMAC_Update",
        "CMAC_Final",
        "CMAC_CTX_copy",
        "CMAC_CTX_free",
    ],
    "Cryptography_HAS_CMS": [
        "BIO_new_CMS",
        "i2d_CMS_bio_stream",
        "PEM_write_bio_CMS_stream",
        "CMS_final",
        "CMS_sign",
        "CMS_verify",
        "CMS_encrypt",
        "CMS_decrypt",
        "CMS_add1_signer",
        "CMS_TEXT",
        "CMS_NOCERTS",
        "CMS_NO_CONTENT_VERIFY",
        "CMS_NO_ATTR_VERIFY",
        "CMS_NOSIGS",
        "CMS_NOINTERN",
        "CMS_NO_SIGNER_CERT_VERIFY",
        "CMS_NOVERIFY",
        "CMS_DETACHED",
        "CMS_BINARY",
        "CMS_NOATTR",
        "CMS_NOSMIMECAP",
        "CMS_NOOLDMIMETYPE",
        "CMS_CRLFEOL",
        "CMS_STREAM",
        "CMS_NOCRL",
        "CMS_PARTIAL",
        "CMS_REUSE_DIGEST",
        "CMS_USE_KEYID",
        "CMS_DEBUG_DECRYPT",
    ],
    "Cryptography_HAS_CMS_BIO_FUNCTIONS": [
        "BIO_new_CMS",
        "i2d_CMS_bio_stream",
        "PEM_write_bio_CMS_stream",
    ],
    "Cryptography_HAS_EC": [
        "OPENSSL_EC_NAMED_CURVE",
        "EC_GROUP_new",
        "EC_GROUP_free",
        "EC_GROUP_clear_free",
        "EC_GROUP_new_curve_GFp",
        "EC_GROUP_new_by_curve_name",
        "EC_GROUP_set_curve_GFp",
        "EC_GROUP_get_curve_GFp",
        "EC_GROUP_method_of",
        "EC_GROUP_get0_generator",
        "EC_GROUP_get_curve_name",
        "EC_GROUP_get_degree",
        "EC_GROUP_set_asn1_flag",
        "EC_GROUP_set_point_conversion_form",
        "EC_KEY_new",
        "EC_KEY_free",
        "EC_get_builtin_curves",
        "EC_KEY_new_by_curve_name",
        "EC_KEY_copy",
        "EC_KEY_dup",
        "EC_KEY_up_ref",
        "EC_KEY_set_group",
        "EC_KEY_get0_private_key",
        "EC_KEY_set_private_key",
        "EC_KEY_set_public_key",
        "EC_KEY_get_enc_flags",
        "EC_KEY_set_enc_flags",
        "EC_KEY_set_conv_form",
        "EC_KEY_get_key_method_data",
        "EC_KEY_insert_key_method_data",
        "EC_KEY_set_asn1_flag",
        "EC_KEY_precompute_mult",
        "EC_KEY_generate_key",
        "EC_KEY_check_key",
        "EC_POINT_new",
        "EC_POINT_free",
        "EC_POINT_clear_free",
        "EC_POINT_copy",
        "EC_POINT_dup",
        "EC_POINT_method_of",
        "EC_POINT_set_to_infinity",
        "EC_POINT_set_Jprojective_coordinates_GFp",
        "EC_POINT_get_Jprojective_coordinates_GFp",
        "EC_POINT_set_affine_coordinates_GFp",
        "EC_POINT_get_affine_coordinates_GFp",
        "EC_POINT_set_compressed_coordinates_GFp",
        "EC_POINT_point2oct",
        "EC_POINT_oct2point",
        "EC_POINT_point2bn",
        "EC_POINT_bn2point",
        "EC_POINT_point2hex",
        "EC_POINT_hex2point",
        "EC_POINT_add",
        "EC_POINT_dbl",
        "EC_POINT_invert",
        "EC_POINT_is_at_infinity",
        "EC_POINT_is_on_curve",
        "EC_POINT_cmp",
        "EC_POINT_make_affine",
        "EC_POINTs_make_affine",
        "EC_POINTs_mul",
        "EC_POINT_mul",
        "EC_GROUP_precompute_mult",
        "EC_GROUP_have_precompute_mult",
        "EC_GFp_simple_method",
        "EC_GFp_mont_method",
        "EC_GFp_nist_method",
        "EC_METHOD_get_field_type",
        "EVP_PKEY_assign_EC_KEY",
        "EVP_PKEY_get1_EC_KEY",
        "EVP_PKEY_set1_EC_KEY",
        "PEM_write_bio_ECPrivateKey",
        "i2d_EC_PUBKEY",
        "d2i_EC_PUBKEY",
        "d2i_EC_PUBKEY_bio",
        "i2d_EC_PUBKEY_bio",
        "d2i_ECPrivateKey",
        "d2i_ECPrivateKey_bio",
        "i2d_ECPrivateKey",
        "i2d_ECPrivateKey_bio",
        "i2o_ECPublicKey",
        "o2i_ECPublicKey",
        "SSL_CTX_set_tmp_ecdh",
        "POINT_CONVERSION_COMPRESSED",
        "POINT_CONVERSION_UNCOMPRESSED",
        "POINT_CONVERSION_HYBRID",
    ],

    "Cryptography_HAS_EC_1_0_1": [
        "EC_KEY_get_flags",
        "EC_KEY_set_flags",
        "EC_KEY_clear_flags",
        "EC_KEY_set_public_key_affine_coordinates",
    ],

    "Cryptography_HAS_EC2M": [
        "EC_GF2m_simple_method",
        "EC_POINT_set_affine_coordinates_GF2m",
        "EC_POINT_get_affine_coordinates_GF2m",
        "EC_POINT_set_compressed_coordinates_GF2m",
        "EC_GROUP_set_curve_GF2m",
        "EC_GROUP_get_curve_GF2m",
        "EC_GROUP_new_curve_GF2m",
    ],

    "Cryptography_HAS_EC_1_0_2": [
        "EC_curve_nid2nist",
    ],
    "Cryptography_HAS_ECDH": [
        "ECDH_compute_key",
        "ECDH_get_ex_new_index",
        "ECDH_set_ex_data",
        "ECDH_get_ex_data",
    ],
    "Cryptography_HAS_ECDSA": [
        "ECDSA_SIG_new",
        "ECDSA_SIG_free",
        "i2d_ECDSA_SIG",
        "d2i_ECDSA_SIG",
        "ECDSA_do_sign",
        "ECDSA_do_sign_ex",
        "ECDSA_do_verify",
        "ECDSA_sign_setup",
        "ECDSA_sign",
        "ECDSA_sign_ex",
        "ECDSA_verify",
        "ECDSA_size",
        "ECDSA_OpenSSL",
        "ECDSA_set_default_method",
        "ECDSA_get_default_method",
        "ECDSA_set_method",
        "ECDSA_get_ex_new_index",
        "ECDSA_set_ex_data",
        "ECDSA_get_ex_data",
    ],
    "Cryptography_HAS_ENGINE_CRYPTODEV": [
        "ENGINE_load_cryptodev"
    ],
    "Cryptography_HAS_REMOVE_THREAD_STATE": [
        "ERR_remove_thread_state"
    ],
    "Cryptography_HAS_098H_ERROR_CODES": [
        "ASN1_F_B64_READ_ASN1",
        "ASN1_F_B64_WRITE_ASN1",
        "ASN1_F_SMIME_READ_ASN1",
        "ASN1_F_SMIME_TEXT",
        "ASN1_R_NO_CONTENT_TYPE",
        "ASN1_R_NO_MULTIPART_BODY_FAILURE",
        "ASN1_R_NO_MULTIPART_BOUNDARY",
    ],
    "Cryptography_HAS_098C_CAMELLIA_CODES": [
        "EVP_F_CAMELLIA_INIT_KEY",
        "EVP_R_CAMELLIA_KEY_SETUP_FAILED"
    ],
    "Cryptography_HAS_EC_CODES": [
        "EC_R_UNKNOWN_GROUP",
        "EC_F_EC_GROUP_NEW_BY_CURVE_NAME"
    ],
    "Cryptography_HAS_RSA_R_PKCS_DECODING_ERROR": [
        "RSA_R_PKCS_DECODING_ERROR"
    ],
    "Cryptography_HAS_GCM": [
        "EVP_CTRL_GCM_GET_TAG",
        "EVP_CTRL_GCM_SET_TAG",
        "EVP_CTRL_GCM_SET_IVLEN",
    ],
    "Cryptography_HAS_PBKDF2_HMAC": [
        "PKCS5_PBKDF2_HMAC"
    ],
    "Cryptography_HAS_PKEY_CTX": [
        "EVP_PKEY_CTX_new",
        "EVP_PKEY_CTX_new_id",
        "EVP_PKEY_CTX_dup",
        "EVP_PKEY_CTX_free",
        "EVP_PKEY_sign",
        "EVP_PKEY_sign_init",
        "EVP_PKEY_verify",
        "EVP_PKEY_verify_init",
        "Cryptography_EVP_PKEY_encrypt",
        "EVP_PKEY_encrypt_init",
        "Cryptography_EVP_PKEY_decrypt",
        "EVP_PKEY_decrypt_init",
        "EVP_PKEY_CTX_set_signature_md",
        "EVP_PKEY_id",
        "EVP_PKEY_CTX_set_rsa_padding",
        "EVP_PKEY_CTX_set_rsa_pss_saltlen",
    ],
    "Cryptography_HAS_ECDSA_SHA2_NIDS": [
        "NID_ecdsa_with_SHA224",
        "NID_ecdsa_with_SHA256",
        "NID_ecdsa_with_SHA384",
        "NID_ecdsa_with_SHA512",
    ],
    "Cryptography_HAS_EGD": [
        "RAND_egd",
        "RAND_egd_bytes",
        "RAND_query_egd_bytes",
    ],
    "Cryptography_HAS_PSS_PADDING": [
        "RSA_PKCS1_PSS_PADDING",
    ],
    "Cryptography_HAS_MGF1_MD": [
        "EVP_PKEY_CTX_set_rsa_mgf1_md",
    ],
    "Cryptography_HAS_TLSv1_1": [
        "SSL_OP_NO_TLSv1_1",
        "TLSv1_1_method",
        "TLSv1_1_server_method",
        "TLSv1_1_client_method",
    ],

    "Cryptography_HAS_TLSv1_2": [
        "SSL_OP_NO_TLSv1_2",
        "TLSv1_2_method",
        "TLSv1_2_server_method",
        "TLSv1_2_client_method",
    ],

    "Cryptography_HAS_SSL3_METHOD": [
        "SSLv3_method",
        "SSLv3_client_method",
        "SSLv3_server_method",
    ],

    "Cryptography_HAS_TLSEXT_HOSTNAME": [
        "SSL_set_tlsext_host_name",
        "SSL_get_servername",
        "SSL_CTX_set_tlsext_servername_callback",
    ],

    "Cryptography_HAS_TLSEXT_STATUS_REQ_CB": [
        "SSL_CTX_set_tlsext_status_cb",
        "SSL_CTX_set_tlsext_status_arg"
    ],

    "Cryptography_HAS_STATUS_REQ_OCSP_RESP": [
        "SSL_set_tlsext_status_ocsp_resp",
        "SSL_get_tlsext_status_ocsp_resp",
    ],

    "Cryptography_HAS_TLSEXT_STATUS_REQ_TYPE": [
        "SSL_set_tlsext_status_type",
    ],

    "Cryptography_HAS_RELEASE_BUFFERS": [
        "SSL_MODE_RELEASE_BUFFERS",
    ],

    "Cryptography_HAS_OP_NO_COMPRESSION": [
        "SSL_OP_NO_COMPRESSION",
    ],

    "Cryptography_HAS_SSL_OP_MSIE_SSLV2_RSA_PADDING": [
        "SSL_OP_MSIE_SSLV2_RSA_PADDING",
    ],

    "Cryptography_HAS_SSL_OP_NO_TICKET": [
        "SSL_OP_NO_TICKET",
    ],

    "Cryptography_HAS_SSL_SET_SSL_CTX": [
        "SSL_set_SSL_CTX",
        "TLSEXT_NAMETYPE_host_name",
    ],

    "Cryptography_HAS_NETBSD_D1_METH": [
        "DTLSv1_method",
    ],

    "Cryptography_HAS_NEXTPROTONEG": [
        "SSL_CTX_set_next_protos_advertised_cb",
        "SSL_CTX_set_next_proto_select_cb",
        "SSL_select_next_proto",
        "SSL_get0_next_proto_negotiated",
    ],

    "Cryptography_HAS_SECURE_RENEGOTIATION": [
        "SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION",
        "SSL_OP_LEGACY_SERVER_CONNECT",
        "SSL_get_secure_renegotiation_support",
    ],

    "Cryptography_HAS_ALPN": [
        "SSL_CTX_set_alpn_protos",
        "SSL_set_alpn_protos",
        "SSL_CTX_set_alpn_select_cb",
        "SSL_get0_alpn_selected",
    ],

    "Cryptography_HAS_COMPRESSION": [
        "SSL_get_current_compression",
        "SSL_get_current_expansion",
        "SSL_COMP_get_name",
    ],

    "Cryptography_HAS_GET_SERVER_TMP_KEY": [
        "SSL_get_server_tmp_key",
    ],

    "Cryptography_HAS_SSL_CTX_SET_CLIENT_CERT_ENGINE": [
        "SSL_CTX_set_client_cert_engine",
    ],
    "Cryptography_HAS_102_VERIFICATION_ERROR_CODES": [
        'X509_V_ERR_SUITE_B_INVALID_VERSION',
        'X509_V_ERR_SUITE_B_INVALID_ALGORITHM',
        'X509_V_ERR_SUITE_B_INVALID_CURVE',
        'X509_V_ERR_SUITE_B_INVALID_SIGNATURE_ALGORITHM',
        'X509_V_ERR_SUITE_B_LOS_NOT_ALLOWED',
        'X509_V_ERR_SUITE_B_CANNOT_SIGN_P_384_WITH_P_256',
        'X509_V_ERR_HOSTNAME_MISMATCH',
        'X509_V_ERR_EMAIL_MISMATCH',
        'X509_V_ERR_IP_ADDRESS_MISMATCH'
    ],
    "Cryptography_HAS_102_VERIFICATION_PARAMS": [
        "X509_V_FLAG_SUITEB_128_LOS_ONLY",
        "X509_V_FLAG_SUITEB_192_LOS",
        "X509_V_FLAG_SUITEB_128_LOS",
        "X509_VERIFY_PARAM_set1_host",
        "X509_VERIFY_PARAM_set1_email",
        "X509_VERIFY_PARAM_set1_ip",
        "X509_VERIFY_PARAM_set1_ip_asc",
        "X509_VERIFY_PARAM_set_hostflags",
    ],
    "Cryptography_HAS_X509_V_FLAG_TRUSTED_FIRST": [
        "X509_V_FLAG_TRUSTED_FIRST",
    ],
    "Cryptography_HAS_X509_V_FLAG_PARTIAL_CHAIN": [
        "X509_V_FLAG_PARTIAL_CHAIN",
    ],
    "Cryptography_HAS_100_VERIFICATION_ERROR_CODES": [
        'X509_V_ERR_DIFFERENT_CRL_SCOPE',
        'X509_V_ERR_UNSUPPORTED_EXTENSION_FEATURE',
        'X509_V_ERR_UNNESTED_RESOURCE',
        'X509_V_ERR_PERMITTED_VIOLATION',
        'X509_V_ERR_EXCLUDED_VIOLATION',
        'X509_V_ERR_SUBTREE_MINMAX',
        'X509_V_ERR_UNSUPPORTED_CONSTRAINT_TYPE',
        'X509_V_ERR_UNSUPPORTED_CONSTRAINT_SYNTAX',
        'X509_V_ERR_UNSUPPORTED_NAME_SYNTAX',
        'X509_V_ERR_CRL_PATH_VALIDATION_ERROR',
    ],
    "Cryptography_HAS_100_VERIFICATION_PARAMS": [
        "Cryptography_HAS_100_VERIFICATION_PARAMS",
        "X509_V_FLAG_EXTENDED_CRL_SUPPORT",
        "X509_V_FLAG_USE_DELTAS",
    ],
    "Cryptography_HAS_X509_V_FLAG_CHECK_SS_SIGNATURE": [
        "X509_V_FLAG_CHECK_SS_SIGNATURE",
    ],
    "Cryptography_HAS_SET_CERT_CB": [
        "SSL_CTX_set_cert_cb",
        "SSL_set_cert_cb",
    ],
}
