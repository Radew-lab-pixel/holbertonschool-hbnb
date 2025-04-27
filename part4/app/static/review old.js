document.addEventListener('DOMContentLoaded', async () => {
    const reviewForm = document.getElementById('review-form');
    const token = checkAuthentication();
    const placeId = getPlaceIdFromURL();

    if (!placeId) {
        alert('No place specified. Redirecting...');
        // window.location.href = 'index.html';
        window.location.href = '/';
        return;
    }

    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            const reviewText = document.getElementById('review-text').value.trim();
            
            if (!reviewText) {
                alert('Please enter your review text');
                return;
            }

            try {
                await submitReview(token, placeId, reviewText);
                
                // Show success message
                const successMessage = document.createElement('div');
                successMessage.className = 'alert alert-success';
                successMessage.textContent = 'Review submitted successfully!';
                reviewForm.prepend(successMessage);
                
                // Clear the form
                document.getElementById('review-text').value = '';
                
                // Remove success message after 3 seconds
                
                setTimeout(() => {
                    successMessage.remove();
                }, 3000);
                
            } catch (error) {
                // Show error message
                const errorMessage = document.createElement('div');
                errorMessage.className = 'alert alert-danger';
                errorMessage.textContent = 'Failed to submit review. Please try again.';
                reviewForm.prepend(errorMessage);
                
                // Remove error message after 3 seconds
                setTimeout(() => {
                    errorMessage.remove();
                }, 3000);
            }
        });
    }
});

async function submitReview(token, placeId, reviewText) {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/add_review', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({
                place_id: placeId,
                text: reviewText
            })
        });

        if (!response.ok) {
            throw new Error('Failed to submit review');
        }

        return await response.json();
    } catch (error) {
        console.error('Error submitting review:', error);
        throw error;
    }
}

