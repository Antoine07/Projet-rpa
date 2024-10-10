import { useState } from 'react'; // Importation du hook useState pour gérer l'état local
import { useGetInvoicesDetailsQuery } from '../features/invoice'; // Importation des hooks générés par RTK Query pour obtenir et supprimer des utilisateurs


import './Invoice.css'

// Composant Invoice qui affiche la liste des utilisateurs et permet d'en supprimer
function Invoice() {
    const { data: invoices, error, isLoading } = useGetInvoicesDetailsQuery()

    if (isLoading) return <div>Loading Invoice...</div>

    if (error) return <div>Error fetching Invoice.</div>

    console.log(invoices)

    return (
        <>
            <div className="invoice-container">
                {/* Parcours des utilisateurs récupérés et affichage de chaque utilisateur avec un bouton de suppression */}
                <h1>Liste des Factures</h1>
                <table className="invoice-table" >
                    <thead>
                        <tr>
                            <th># Facture</th>
                            <th>Date Créa.</th>
                            <th>Intitulé</th>
                            <th>Jrs, hrs</th>
                            <th>Prix Unitaire</th>
                            <th>Montant TTC</th>
                            <th>Date d'interventions</th>
                            <th>Nb étudiants</th>
                            <th>École</th>
                            <th>Formateur</th>
                            <th>Cours</th>
                        </tr>
                    </thead>
                    <tbody>
                        {invoices.length > 0 && invoices.map((invoice, i) =>
                            <tr>
                                <td>{invoice.invoice_number}</td>
                                <td>{invoice.creation_date}</td>
                                <td>{invoice.invoice_wording}</td>
                                <td>days: {invoice.days_count} hours: {invoice.hours_count}</td>
                                <td>{invoice.unit_price}</td>
                                <td>{invoice.amount_ht}</td>
                                <td>{invoice.intervention_dates.map((d, i) =>
                                    <>
                                        <span>{d.start_date}</span>
                                        <span>{d.end_date}</span>
                                    </>
                                )}
                                </td>
                                <td>{invoice.student_count}</td>
                                <td>{invoice.school_name}</td>
                                <td>{invoice.trainer_name}</td>
                                <td>{invoice.course_name}</td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </>
    );
}

export default Invoice; // Exportation du composant pour l'utiliser dans d'autres parties de l'application