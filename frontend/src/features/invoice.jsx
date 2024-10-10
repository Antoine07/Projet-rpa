import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

// Nous créons une API avec `createApi` qui permet de gérer les requêtes vers un serveur et la gestion du cache.
export const invoicesApi = createApi({
  // `reducerPath` est le nom que nous donnons à cette API dans notre store Redux.
  reducerPath: 'invoiceApi',

  // `baseQuery` permet de définir la base des requêtes, ici l'URL de l'API à interroger.
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8002/api' }),

  tagTypes: ['Invoice'],

  // `endpoints` est une fonction qui permet de définir toutes les requêtes (endpoints) que notre API peut effectuer.
  endpoints: (builder) => ({
    
    // Première requête : obtenir la liste de tous les factures.
    getInvoicesDetails: builder.query({
      query: () => '/invoices/details',
      providesTags: ['Invoice'],
    }),

    // Deuxième requête : obtenir les détails d'une facture spécifique par son ID.
    getInvoice: builder.query({
      query: (id) => `/invoices/${id}`,
      
      providesTags: ['Invoice'],
    }),

    // Troisième requête : ajouter un nouvelle facture.
    addInvoice: builder.mutation({
      query: (newInvoice) => ({
        url: '/Invoice',
        method: 'POST',
        body: newInvoice, // `body` est le contenu de la requête, ici les informations du nouvele facture.
      }),

      invalidatesTags: ['Invoice'],
    }),

    updateInvoice: builder.mutation({
      query: ({ id, ...Invoice }) => ({
        url: `/invoice/${id}`,
        method: 'PUT',
        body: invoice, // `body` contient les nouvelles données de le'facture.
      }),

      invalidatesTags: ['Invoice'],
    }),

    // Cinquième requête : supprimer une facture.
    deleteInvoice: builder.mutation({
      query: (id) => ({
        url: `/invoice/${id}`,
        method: 'DELETE',
      }),

      // Après la suppression d'une facture, le cache est également invalidé pour rafraîchir la liste des factures.
      invalidatesTags: ['Invoice'],
    }),
  }),
});

export const {
  useGetInvoicesDetailsQuery,    
  useGetInvoiceQuery,    
  useAddInvoiceMutation, 
  useUpdateInvoiceMutation, 
  useDeleteInvoiceMutation,
} = invoicesApi;